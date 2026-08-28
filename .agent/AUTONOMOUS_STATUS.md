# Statut autonome — site juridique WiniCharge

Dernière mise à jour : 28 août 2026

## État courant

- Pages bilingues Privacy et Delete Account : **DONE**.
- Informations approuvées et formulations prudentes : **DONE**.
- Placeholders : **DONE** — zéro restant dans la recherche récursive.
- QA normale et release : **DONE** — les deux commandes passent.
- Revue navigateur locale bureau/mobile : **DONE** — trois pages navigables, sans débordement horizontal.
- Publication GitHub Pages : **DONE** — remote autorisé `brand`, dépôt `winicharge-app/winicharge-app.github.io`.
- Vérification publique HTTPS sans connexion : **DONE** pour `/privacy/` et `/delete-account/`.
- Bundle canonique `ugc-2026-08-04-v1` et commit public `1399ecf` : **DONE — publié**; alignement strict sur les libellés Flutter, QA normale/release, compilations Python, diff-check et test négatif réel du verrou v1 **PASS**.
- Revue navigateur locale du 28 août pour `/terms/` et la copie v1 : **PASS** sur bureau et viewport mobile `390×844`; aucun overflow du document, sections FR/EN visibles, zéro ressource externe et zéro erreur console. Le lien relatif unique vers v1 charge directement sa cible en HTTP 200 local. La navigation du header mobile est volontairement scrollable; l'absence historique de favicon est non bloquante. Ce contrôle local ne constitue pas une preuve publique.
- Autorisation de push et push du commit `1399ecf` vers `brand/main` : **DONE**.
- Preuve publique HTTPS+contenu à l'URL canonique de la copie v1 : **DONE**.
- Décision et approbation internes du 28 août 2026 : **DONE** — responsable produit et publication : Yassine Gh. Ce rôle ne le désigne pas comme responsable de modération.
- Portée de l'approbation interne : elle n'est ni une signature ni une revue, validation, certification ou avis juridique externe.
- Révision `ugc-2026-08-27-v2` : **IMMUTABLE PASS**, SHA-256 avant/après `BCDBC5BD62402B29A6ECC34C645866DD0893FD5FE5C447EAB8116BBEA767BEF5`.

## Références publiques

- Privacy : `https://winicharge-app.github.io/privacy/`
- Delete Account : `https://winicharge-app.github.io/delete-account/`
- Bundle UGC v1 : `https://winicharge-app.github.io/terms/revisions/ugc-2026-08-04-v1/` — vérification publique HTTPS **DONE**, commit public `1399ecf`.
- Support : `winichargedev@gmail.com`

## Prochaine action exacte

Maintenir la copie `ugc-2026-08-04-v1` immuable à son URL canonique. Toute
évolution reçoit un nouvel identifiant et une nouvelle URL, avec un nouveau
cycle de décision, publication et preuve. Ne pas présenter la décision interne
comme une signature, une revue, validation, certification ou un avis juridique
externe, ni comme la désignation du responsable de modération.

## Contraintes de reprise

- Ne modifier aucun fichier dans `C:\Users\yghrab\Documents\WiniCharge` depuis ce dépôt.
- Ne publier que vers le remote GitHub Pages `brand` après réussite du release gate.
- Ne jamais ajouter de secret, donnée privée ou affirmation de certification non établie.
- Ne jamais modifier une copie versionnée publiée; toute future policy reçoit un nouvel identifiant et une nouvelle URL.
