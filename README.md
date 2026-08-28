# WiniCharge Legal

Site statique bilingue destiné à héberger la politique de confidentialité, les conditions d’utilisation et la procédure de suppression de compte de WiniCharge.

> **État au 28 août 2026.** Les pages Privacy et Delete Account sont publiées depuis le 11 août 2026. La révision des Conditions publiques `ugc-2026-08-27-v2` est datée du 27 août 2026. Le bundle `ugc-2026-08-04-v1` a été publié par le commit public `1399ecf`, puis vérifié à son URL canonique en HTTPS et approuvé en interne. Cette décision produit et de publication n’est ni une signature ni une revue, validation, certification ou avis juridique externe.

## Contenu

- `index.html` : accueil bilingue et accès aux documents.
- `privacy/index.html` : politique de confidentialité FR/EN.
- `terms/index.html` : conditions d’utilisation FR/EN.
- `terms/revisions/ugc-2026-08-27-v2/index.html` : copie immuable de la révision des Conditions publiques.
- `terms/revisions/ugc-2026-08-04-v1/index.html` : copie canonique du bundle technique enregistré par l’application.
- `delete-account/index.html` : procédure de suppression FR/EN et modèle d’e-mail.
- `styles.css` : styles locaux, responsive et accessibles.
- `.nojekyll` : désactive le traitement Jekyll sur GitHub Pages.
- `.gitignore` : exclut les caches et bytecodes Python générés localement.
- `test_site.py` : contrôles structurels, liens, sécurité et garde de publication.
- `.agent/` : plan d’exécution et état de reprise du lot.

Aucune page ne charge de police, image, script, feuille de styles ou autre ressource distante. Le site n’intègre ni formulaire, ni cookie, ni analytics, ni tracker.

## Informations confirmées

- responsable du traitement et développeur public : Yassine Gh ;
- responsable de la décision produit et de la publication du bundle `ugc-2026-08-04-v1` : Yassine Gh, décision interne du 28 août 2026 ; ce rôle ne le désigne pas comme responsable de modération ;
- support : `winichargedev@gmail.com` ;
- cadre de lancement : Tunisie et loi organique n° 2004-63 du 27 juillet 2004 ;
- autorité de recours : Instance nationale de protection des données personnelles (INPDP) ;
- backend : Supabase, hébergé dans l’Union européenne avec accès à distance depuis Tunis ;
- e-mail : Google ;
- cartographie : serveur raster standard OpenStreetMap via HTTPS ;
- demande Web de suppression traitée sous une semaine au maximum ;
- données restant en accès restreint après suppression supprimées ou anonymisées sous trois jours au maximum.

## Versions des Conditions et bundle UGC

La révision `ugc-2026-08-27-v2` est la copie versionnée des Conditions
publiques courantes. Le bundle `ugc-2026-08-04-v1` est la politique technique
enregistrée par l’application avant une opération UGC; il est distinct des
Conditions publiques courantes.

La publication du bundle v1 correspond au commit public `1399ecf`. Son push,
sa preuve publique HTTPS et son approbation interne sont terminés. L’URL
canonique est celle documentée dans la section « URL finales » ci-dessous.

Chaque copie canonique publiée est immuable. Une future politique doit recevoir
un nouvel identifiant de version et une nouvelle URL : elle ne doit jamais
remplacer ni modifier le contenu d’une URL versionnée existante. Cette
documentation technique et la décision interne du 28 août 2026 ne constituent
ni une signature ni une revue, validation, certification ou avis juridique
externe. Elles ne désignent pas le responsable de modération.

## Tests locaux

Depuis la racine de ce dossier :

```powershell
python -B test_site.py
python -m py_compile test_site.py
python -m compileall -q test_site.py
```

Le test normal et le contrôle de release doivent tous deux réussir :

```powershell
python -B test_site.py --release
```

Le mode `--release` vérifie notamment l’absence de placeholder, les URL finales, le support, le parcours de suppression et les garde-fous de sécurité. Pour contrôler les espaces finaux sous Windows, essayer :

```powershell
git diff --no-index --check NUL .
```

Si Git ne traite pas `NUL` comme un fichier vide dans l’environnement utilisé, le test Python applique un contrôle de whitespace aux actifs du site et à la documentation.

## Publication GitHub Pages

Le dépôt public autorisé est `winicharge-app/winicharge-app.github.io`. Depuis une branche `main` validée :

```powershell
git add README.md test_site.py terms/index.html terms/revisions/ugc-2026-08-04-v1/index.html .agent/EXECPLAN.md .agent/AUTONOMOUS_STATUS.md .agent/TASKS.md
git commit -m "legal: add canonical UGC policy bundle v1"
git push brand main
```

Dans les paramètres du dépôt GitHub :

1. Ouvrir **Settings → Pages**.
2. Choisir **Deploy from a branch**.
3. Sélectionner la branche **main** et le dossier **/ (root)**.
4. Enregistrer, attendre la génération, puis activer **Enforce HTTPS** dès que l’option est disponible.
5. Vérifier manuellement les quatre pages sur mobile et ordinateur, les ancres de langue et le bouton d’e-mail.

## URL finales

- Politique de confidentialité : `https://winicharge-app.github.io/privacy/`
- Conditions d’utilisation : `https://winicharge-app.github.io/terms/`
- Bundle UGC canonique v1 : `https://winicharge-app.github.io/terms/revisions/ugc-2026-08-04-v1/`
- Suppression de compte : `https://winicharge-app.github.io/delete-account/`

Ces URL doivent répondre publiquement en HTTPS, sans connexion, avant leur utilisation dans Play Console.

## Checklist de maintenance

- Rejouer les deux commandes de test avant chaque publication.
- Vérifier visuellement les versions française et anglaise sur mobile et ordinateur.
- Tester les deux liens `mailto:` et la réception par le support.
- Maintenir les pages alignées avec l’application, les prestataires et les durées réellement appliquées.
- Refaire une revue appropriée lors de toute évolution juridique ou fonctionnelle substantielle.
