from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlsplit


ROOT = Path(__file__).resolve().parent
HTML_FILES = (
    ROOT / "index.html",
    ROOT / "privacy" / "index.html",
    ROOT / "delete-account" / "index.html",
)
REQUIRED_FILES = (*HTML_FILES, ROOT / "styles.css", ROOT / ".nojekyll", ROOT / "README.md")
ACTIVE_FILES = (*HTML_FILES, ROOT / "styles.css")
PLACEHOLDER_RE = re.compile(r"\[\[([^\[\]\r\n]+)\]\]")
PUBLICATION_TEXT_SUFFIXES = {".html", ".css", ".md", ".py"}

EXPECTED_MAIL_SUBJECT = "Demande de suppression de compte WiniCharge"
EXPECTED_SUPPORT_EMAIL = "winichargedev@gmail.com"
EXPECTED_PRIVACY_URL = "https://winicharge-app.github.io/privacy/"
EXPECTED_DELETION_URL = "https://winicharge-app.github.io/delete-account/"
EXPECTED_DELETION_PATH_FR = "WiniCharge → Profil → Supprimer mon compte"
EXPECTED_DELETION_PATH_EN = "WiniCharge → Profile → Delete my account"
EXPECTED_LAW_FR = "loi organique tunisienne n° 2004-63 du 27 juillet 2004"
EXPECTED_LAW_EN = "Tunisian Organic Law No. 2004-63 of 27 July 2004"
LEGACY_HOST = "yassineghrab237-dotcom" + ".github.io"
EMAIL_RE = re.compile(r"(?<![\w.+-])[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}(?![\w.-])", re.I)
EXPECTED_MAIL_BODY = """Bonjour,

Je souhaite demander la suppression de mon compte WiniCharge.

Adresse e-mail associée au compte :
[à compléter]

Je confirme être le titulaire de ce compte."""

SENSITIVE_PATTERNS = {
    "hôte local": re.compile(r"\b(?:localhost|127\.0\.0\.1|0\.0\.0\.0)\b", re.I),
    "rôle privilégié": re.compile(r"\bservice[_-]?role\b", re.I),
    "URL Supabase": re.compile(
        r"(?:https?|postgres(?:ql)?)://[^\s\"'<>]*supabase[^\s\"'<>]*"
        r"|\b[a-z0-9-]+\.supabase\.(?:co|net)\b",
        re.I,
    ),
    "JWT": re.compile(
        r"\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\b"
    ),
    "clé à format connu": re.compile(
        r"\b(?:sb_(?:secret|publishable)_[A-Za-z0-9_-]{12,}"
        r"|sk-(?:proj-)?[A-Za-z0-9_-]{20,}"
        r"|gh[pousr]_[A-Za-z0-9_]{20,}"
        r"|AKIA[A-Z0-9]{16}|AIza[A-Za-z0-9_-]{30,})\b"
    ),
    "secret affecté": re.compile(
        r"\b(?:supabase_url|supabase_anon_key|anon_key|api[_-]?key|client[_-]?secret|"
        r"access[_-]?token|refresh[_-]?token|password)\b\s*[:=]\s*[\"']?[^\s\"'<>]{8,}",
        re.I,
    ),
}


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.tags: Counter[str] = Counter()
        self.ids: set[str] = set()
        self.duplicate_ids: set[str] = set()
        self.uris: list[tuple[str, str, str]] = []
        self.stylesheets: list[str] = []
        self.descriptions: list[str] = []
        self.viewports: list[str] = []
        self._in_title = False
        self._title_parts: list[str] = []

    @property
    def title(self) -> str:
        return "".join(self._title_parts).strip()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        self.tags[tag] += 1
        values = {name.lower(): value or "" for name, value in attrs}

        element_id = values.get("id")
        if element_id:
            if element_id in self.ids:
                self.duplicate_ids.add(element_id)
            self.ids.add(element_id)

        if tag == "title":
            self._in_title = True
        if tag == "meta":
            name = values.get("name", "").lower()
            if name == "description":
                self.descriptions.append(values.get("content", "").strip())
            elif name == "viewport":
                self.viewports.append(values.get("content", "").strip())
        if tag == "link" and "stylesheet" in values.get("rel", "").lower().split():
            self.stylesheets.append(values.get("href", ""))

        for attribute in ("href", "src", "srcset", "action", "poster", "data"):
            if attribute in values:
                self.uris.append((tag, attribute, values[attribute].strip()))

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "title":
            self._in_title = False

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self._title_parts.append(data)


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def local_target(source: Path, href: str) -> tuple[Path, str] | None:
    parts = urlsplit(href)
    if parts.scheme or parts.netloc:
        return None
    raw_path = unquote(parts.path)
    target = ROOT / raw_path.lstrip("/") if raw_path.startswith("/") else source.parent / raw_path
    target = target.resolve()
    try:
        target.relative_to(ROOT)
    except ValueError:
        return None
    if not raw_path or raw_path.endswith("/") or target.is_dir():
        target /= "index.html"
    return target, unquote(parts.fragment)


def publication_text_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*")
        if path.is_file()
        and path.suffix.lower() in PUBLICATION_TEXT_SUFFIXES
        and ".git" not in path.parts
        and "__pycache__" not in path.parts
    )


def collect_placeholders() -> list[str]:
    found: set[str] = set()
    for path in publication_text_files():
        found.update(
            match.group(1).strip()
            for match in PLACEHOLDER_RE.finditer(path.read_text(encoding="utf-8"))
        )
    return sorted(found)


def validate_site() -> list[str]:
    errors: list[str] = []
    for path in REQUIRED_FILES:
        if not path.is_file():
            errors.append(f"Fichier requis absent : {relative(path)}")

    actual_html = {path.resolve() for path in ROOT.rglob("*.html")}
    expected_html = {path.resolve() for path in HTML_FILES}
    if actual_html != expected_html:
        actual = ", ".join(sorted(relative(path) for path in actual_html)) or "aucun"
        errors.append(f"Le site doit contenir exactement les 3 pages prévues (trouvé : {actual})")

    if any(not path.is_file() for path in HTML_FILES):
        return errors

    parsers: dict[Path, PageParser] = {}
    contents: dict[Path, str] = {}
    for path in HTML_FILES:
        content = path.read_text(encoding="utf-8")
        parser = PageParser()
        try:
            parser.feed(content)
            parser.close()
        except Exception as exc:
            errors.append(f"HTML illisible dans {relative(path)} : {type(exc).__name__}")
        parsers[path.resolve()] = parser
        contents[path] = content

        if parser.tags["title"] != 1 or not parser.title or "WiniCharge" not in parser.title:
            errors.append(f"{relative(path)} : title unique, non vide et marqué WiniCharge requis")
        if len(parser.descriptions) != 1 or not parser.descriptions[0] or "WiniCharge" not in parser.descriptions[0]:
            errors.append(f"{relative(path)} : meta description unique, non vide et marquée WiniCharge requise")
        if len(parser.viewports) != 1 or "width=device-width" not in parser.viewports[0]:
            errors.append(f"{relative(path)} : meta viewport mobile requise")
        if parser.tags["main"] != 1:
            errors.append(f"{relative(path)} : exactement un élément main requis")
        if parser.tags["h1"] != 1:
            errors.append(f"{relative(path)} : exactement un h1 requis")
        if parser.tags["script"] or parser.tags["form"]:
            errors.append(f"{relative(path)} : script et form sont interdits")
        if parser.duplicate_ids:
            errors.append(f"{relative(path)} : identifiants HTML dupliqués")
        if len(parser.stylesheets) != 1:
            errors.append(f"{relative(path)} : une seule feuille de styles est requise")
        else:
            target = local_target(path, parser.stylesheets[0])
            if target is None or target[0] != (ROOT / "styles.css").resolve():
                errors.append(f"{relative(path)} : la feuille de styles locale attendue n'est pas liée")

    for path, parser in ((path, parsers[path.resolve()]) for path in HTML_FILES):
        for tag, attribute, uri in parser.uris:
            if not uri:
                errors.append(f"{relative(path)} : attribut {attribute} vide sur <{tag}>")
                continue
            if uri.lower().startswith("mailto:"):
                if tag != "a" or attribute != "href":
                    errors.append(f"{relative(path)} : mailto autorisé uniquement sur un lien")
                continue
            target = local_target(path, uri)
            if target is None:
                errors.append(f"{relative(path)} : URI externe ou hors site interdite")
                continue
            target_path, fragment = target
            if not target_path.is_file():
                errors.append(f"{relative(path)} : cible locale absente pour un attribut {attribute}")
                continue
            if fragment:
                target_parser = parsers.get(target_path.resolve())
                if target_parser is None or fragment not in target_parser.ids:
                    errors.append(f"{relative(path)} : fragment interne introuvable #{fragment}")

    for path in ACTIVE_FILES:
        if not path.is_file():
            continue
        content = path.read_text(encoding="utf-8")
        if re.search(r"https?://|(?<!:)//", content, re.I):
            errors.append(f"{relative(path)} : URL HTTP(S) ou ressource réseau interdite")
        for label, pattern in SENSITIVE_PATTERNS.items():
            if pattern.search(content):
                errors.append(f"{relative(path)} : contenu sensible détecté ({label})")

    for path in (*ACTIVE_FILES, ROOT / "README.md"):
        if not path.is_file():
            continue
        content = path.read_text(encoding="utf-8")
        if any(line.endswith((" ", "\t")) for line in content.splitlines()):
            errors.append(f"{relative(path)} : espaces finaux interdits")
        if content and not content.endswith("\n"):
            errors.append(f"{relative(path)} : fin de fichier sans saut de ligne")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if readme.count(EXPECTED_PRIVACY_URL) != 1:
        errors.append("README.md : URL Privacy finale unique requise")
    if readme.count(EXPECTED_DELETION_URL) != 1:
        errors.append("README.md : URL Delete Account finale unique requise")

    publication_contents = {
        path: path.read_text(encoding="utf-8") for path in publication_text_files()
    }
    if any(LEGACY_HOST in content for content in publication_contents.values()):
        errors.append("Ancien hôte GitHub Pages personnel interdit")

    deletion_content = contents[ROOT / "delete-account" / "index.html"]
    if EXPECTED_DELETION_PATH_FR not in deletion_content:
        errors.append("delete-account/index.html : parcours français exact absent")
    if EXPECTED_DELETION_PATH_EN not in deletion_content:
        errors.append("delete-account/index.html : parcours anglais exact absent")

    privacy_content = contents[ROOT / "privacy" / "index.html"]
    if EXPECTED_LAW_FR not in privacy_content or EXPECTED_LAW_EN not in privacy_content:
        errors.append("privacy/index.html : cadre légal tunisien bilingue absent")
    if privacy_content.count("INPDP") < 4:
        errors.append("privacy/index.html : autorité de recours bilingue absente")

    public_html = "\n".join(contents.values()).lower()
    for forbidden_phrase in ("publication bloquée", "double brackets", "draft under review"):
        if forbidden_phrase in public_html:
            errors.append(f"Pages HTML : mention de brouillon interdite ({forbidden_phrase})")

    html_emails = {
        address.lower()
        for content in contents.values()
        for address in EMAIL_RE.findall(content)
    }
    if html_emails != {EXPECTED_SUPPORT_EMAIL}:
        errors.append("Pages HTML : adresse de support absente ou inattendue")

    css = (ROOT / "styles.css").read_text(encoding="utf-8") if (ROOT / "styles.css").is_file() else ""
    for match in re.finditer(r"url\(\s*(['\"]?)(.*?)\1\s*\)", css, re.I):
        uri = match.group(2).strip()
        target = local_target(ROOT / "styles.css", uri)
        if target is None or not target[0].is_file():
            errors.append("styles.css : ressource CSS externe ou absente")

    deletion_parser = parsers[(ROOT / "delete-account" / "index.html").resolve()]
    mailtos = [uri for tag, attribute, uri in deletion_parser.uris if tag == "a" and attribute == "href" and uri.lower().startswith("mailto:")]
    all_mailtos = [
        uri
        for parser in parsers.values()
        for tag, attribute, uri in parser.uris
        if tag == "a" and attribute == "href" and uri.lower().startswith("mailto:")
    ]
    if len(mailtos) != 2 or len(all_mailtos) != 2:
        errors.append("delete-account/index.html : exactement deux CTA mailto bilingues sont requis")
    for mailto in mailtos:
        parts = urlsplit(mailto)
        try:
            query = parse_qs(parts.query, keep_blank_values=True, strict_parsing=True)
        except ValueError:
            query = {}
        if unquote(parts.path) != EXPECTED_SUPPORT_EMAIL:
            errors.append("delete-account/index.html : destinataire mailto inattendu")
        if query != {"subject": [EXPECTED_MAIL_SUBJECT], "body": [EXPECTED_MAIL_BODY]}:
            errors.append("delete-account/index.html : sujet ou corps mailto décodé non conforme")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="QA statique locale du site juridique WiniCharge")
    parser.add_argument("--release", action="store_true", help="bloque aussi sur les placeholders")
    args = parser.parse_args()

    errors = validate_site()
    placeholders = collect_placeholders()
    if errors:
        print(f"FAIL — {len(errors)} erreur(s) de QA statique")
        for error in errors:
            print(f"- {error}")
        return 1

    if args.release and placeholders:
        print(f"FAIL — publication bloquée par {len(placeholders)} placeholder(s)")
        for placeholder in placeholders:
            print(f"- {placeholder}")
        return 1

    print("PASS — QA statique réussie pour les 3 pages")
    if placeholders:
        print(f"Placeholders à valider avant publication ({len(placeholders)}) :")
        for placeholder in placeholders:
            print(f"- {placeholder}")
    else:
        print("Aucun placeholder restant.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
