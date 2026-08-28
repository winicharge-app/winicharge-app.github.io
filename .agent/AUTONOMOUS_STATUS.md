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
- Candidat canonique `ugc-2026-08-04-v1` et commit local ciblé : **DONE — ready to push**; alignement strict sur les libellés Flutter, QA normale/release, compilations Python, diff-check et test négatif réel du verrou v1 **PASS**.
- Revue navigateur locale du 28 août pour `/terms/` et la copie v1 : **PASS** sur bureau et viewport mobile `390×844`; aucun overflow du document, sections FR/EN visibles, zéro ressource externe et zéro erreur console. Le lien relatif unique vers v1 charge directement sa cible en HTTP 200 local. La navigation du header mobile est volontairement scrollable; l'absence historique de favicon est non bloquante. Ce contrôle local ne constitue pas une preuve publique.
- Autorisation explicite de push : **BLOCKED**.
- Push du présent commit vers `brand/main` : **NOT RUN / BLOCKED** jusqu'à cette autorisation.
- Preuve publique HTTPS+contenu de la copie v1 : **NOT RUN**.
- Approbation humaine de la copie v1 : **NOT RUN**, uniquement après la preuve publique.
- Validation juridique de la copie v1 : **NON REVENDIQUÉE**.
- Révision `ugc-2026-08-27-v2` : **IMMUTABLE PASS**, SHA-256 avant/après `BCDBC5BD62402B29A6ECC34C645866DD0893FD5FE5C447EAB8116BBEA767BEF5`.

## Références publiques

- Privacy : `https://winicharge-app.github.io/privacy/`
- Delete Account : `https://winicharge-app.github.io/delete-account/`
- Bundle UGC v1 : `https://winicharge-app.github.io/terms/revisions/ugc-2026-08-04-v1/` — vérification publique **NOT RUN**.
- Support : `winichargedev@gmail.com`

## Prochaine action exacte

Attendre une autorisation explicite de push. Après cette autorisation seulement,
pousser le présent commit vers `brand/main`, attendre GitHub Pages, puis vérifier
publiquement en HTTPS l'URL canonique, son identifiant et son contenu. Demander
l'approbation humaine uniquement après cette preuve publique. Ne pas modifier
la copie v2 ni revendiquer de validation juridique.

## Contraintes de reprise

- Ne modifier aucun fichier dans `C:\Users\yghrab\Documents\WiniCharge` depuis ce dépôt.
- Ne publier que vers le remote GitHub Pages `brand` après réussite du release gate.
- Ne jamais ajouter de secret, donnée privée ou affirmation de certification non établie.
- Ne jamais modifier une copie versionnée publiée; toute future policy reçoit un nouvel identifiant et une nouvelle URL.
