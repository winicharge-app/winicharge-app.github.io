# Site juridique statique WiniCharge

> **Mise à jour finale — 11 août 2026.** Les états historiques `BLOCKED` consignés ci-dessous décrivent la construction initiale du 7 août. La finalisation autorisée le 11 août a remplacé les 11 valeurs, renforcé le release gate, validé le rendu local bureau/mobile et publié le site via le remote `brand`. L’état courant de référence est `.agent/AUTONOMOUS_STATUS.md`.

## Objectif

Construire un site statique bilingue français/anglais, accessible et sans dépendance pour publier la politique de confidentialité et les instructions de suppression de compte de WiniCharge sur GitHub Pages.

## État initial vérifié

Le 7 août 2026, le dossier `C:\Users\yghrab\Documents\winicharge-legal` a été vérifié absent avant sa création. Les exigences produit et sécurité ont été fournies par le dépôt WiniCharge. Aucun actif public de marque n'est validé et aucune identité juridique ou durée de traitement/conservation n'est confirmée.

## Périmètre

- Page d'accueil, politique de confidentialité et page de suppression de compte.
- Feuille de styles locale, responsive, accessible et conforme à la charte fournie.
- Documentation de publication manuelle et inventaire des champs à valider.
- Tests Python standard library des contraintes structurelles, de sécurité et de publication.
- Fichiers de suivi autonomes dans `.agent`.

## Hors périmètre

- Modification du code ou des données de WiniCharge.
- Conseil juridique, validation des mentions ou remplacement des placeholders.
- Hébergement, activation de GitHub Pages, push, commit ou publication Play Store.
- JavaScript, formulaire, analytics, cookies, ressources réseau ou dépendances tierces.

## Décisions métier

- Le contenu décrit uniquement les traitements confirmés par le code et la documentation existants.
- Les informations non validées restent des placeholders explicites et empêchent le mode de test `--release` de réussir.
- Le site juridique ne charge aucune ressource distante et ne dépose aucun cookie ; les journaux techniques éventuels de l'hébergeur public ne sont pas niés.
- La suppression de compte distingue les éléments supprimés ou neutralisés des historiques et preuves pouvant être conservés en accès restreint.

## Étapes

1. **DONE** — Créer le squelette documentaire et consigner l'état initial.
2. **DONE** — Construire les trois pages HTML et la feuille de styles locale.
3. **DONE** — Ajouter le README, `.nojekyll` et la suite de tests autonome.
4. **DONE** — Exécuter les contrôles fonctionnels et syntaxiques demandés.
5. **DONE** — Mettre à jour les documents de suivi et remettre le candidat technique sans publication.

La construction et la QA statique sont terminées. La publication reste **BLOCKED** jusqu'au remplacement et à la validation humaine des 11 placeholders.

## Fichiers concernés

- `index.html`
- `styles.css`
- `privacy/index.html`
- `delete-account/index.html`
- `README.md`
- `.nojekyll`
- `.gitignore`
- `test_site.py`
- `.agent/EXECPLAN.md`
- `.agent/AUTONOMOUS_STATUS.md`
- `.agent/TASKS.md`

## Migrations

Aucune migration de base de données n'est prévue ni autorisée. Le site est entièrement statique.

## Tests

- `python test_site.py`
- `python -m py_compile test_site.py`
- `python -m compileall -q test_site.py`
- Contrôle de whitespace équivalent à `git diff --no-index --check` si le chemin Windows `NUL` ne produit pas un résultat exploitable.
- `python test_site.py --release` doit échouer tant que les placeholders existent.

## Smoke Android

Non applicable : aucun fichier Flutter/Android n'est modifié. Le responsive CSS et sa structure sont couverts statiquement ; la revue visuelle mobile et bureau reste **BLOCKED**, car aucun navigateur n'est disponible dans cette session.

## Risques

- Publication prématurée avec des placeholders juridiques ou opérationnels.
- Promesse excessive sur la conservation, les transferts, les prestataires ou les journaux techniques.
- Rupture du CTA `mailto:` lors de l'encodage du sujet ou du corps.
- Régression d'accessibilité ou chargement involontaire d'une ressource externe.

## Checkpoints

- CP1 : structure et documents de suivi créés, sans contenu publié.
- CP2 : pages et styles ajoutés ; retour possible en supprimant uniquement le dossier candidat non publié, avec autorisation humaine.
- CP3 : tests ajoutés et exécutés ; aucune mutation externe.
- CP4 : construction et QA technique terminées, publication toujours bloquée.
- Revue visuelle : **BLOCKED** jusqu'à la disponibilité d'un navigateur pour le contrôle manuel mobile et bureau.

## Critères de fin

- Les fichiers demandés existent et les trois pages sont bilingues, sémantiques, navigables et responsives.
- Les tests normaux réussissent sans réseau ni dépendance externe.
- Le mode `--release` recense tous les placeholders et échoue tant qu'ils ne sont pas remplacés.
- Aucun secret, donnée réelle, ressource réseau, script, formulaire ou chaîne `localhost` n'est publié.
- La publication reste `BLOCKED` jusqu'au remplacement et à la validation humaine de tous les placeholders.

## Journal des progrès

- 2026-08-07 — État initial et absence du dossier cible vérifiés ; CP1 en cours.
- 2026-08-07 — Arborescence minimale et documents de reprise créés ; construction des pages à démarrer.
- 2026-08-07 — Accueil, politique, suppression et styles bilingues ajoutés ; CP2 atteint. Les placeholders restent visibles et la publication demeure bloquée.
- 2026-08-07 — `test_site.py` ajouté : structure, liens/fragments, ressources, secrets et CTA `mailto:` contrôlés. Test normal et compilation réussis ; mode `--release` en échec attendu sur 11 placeholders. CP3 et CP4 atteints, sans publication.
- 2026-08-07 — `.gitignore` ajouté ; l'unique bytecode `test_site` a été vérifié puis son dossier `__pycache__` supprimé. QA statique toujours réussie. Revue visuelle navigateur **BLOCKED** faute de navigateur disponible ; publication inchangée à **BLOCKED**.
- 2026-08-11 — Identité, support, délais et prestataires confirmés intégrés ; cadre tunisien formulé prudemment à partir de la loi organique n° 2004-63 et de l’INPDP. Les deux gates passent sans placeholder, la revue locale bureau/mobile ne détecte aucun débordement, et la publication cible exclusivement `winicharge-app/winicharge-app.github.io`.

## Décisions prises

- Utiliser un monogramme texte/CSS `W` avec libellé accessible, faute d'actif public validé.
- Présenter le français avant l'anglais et fournir des liens d'ancre de langue sur les pages longues.
- Réserver le vert foncé `#0F713B` aux actions sur fond plein afin de garantir le contraste avec le blanc.

## Problèmes rencontrés

Aucun navigateur n'est disponible dans cette session. La revue visuelle manuelle mobile et bureau ne peut donc pas être déclarée terminée.

## Procédure de reprise

1. Vérifier que le travail reste limité à `C:\Users\yghrab\Documents\winicharge-legal` ; la revue visuelle et la publication sont actuellement `BLOCKED`.
2. Lire `.agent/AUTONOMOUS_STATUS.md`, `.agent/TASKS.md` puis ce journal.
3. Dès qu'un navigateur est disponible, contrôler manuellement les trois pages en affichage mobile et bureau, puis exécuter les validations listées dans `## Tests`.
4. Ne renseigner aucun placeholder sans source humaine approuvée ; aucune donnée DEV temporaire n'est connue ou requise.
5. Demander une autorisation humaine avant tout push, activation GitHub Pages, utilisation de secret, publication Play Store ou autre opération externe.

## Phase bundle UGC canonique v1 — 28 août 2026

### Objectif et statut

Créer localement la copie canonique bilingue du bundle technique
`ugc-2026-08-04-v1`, la relier sans modifier le texte immuable de la révision
publique `ugc-2026-08-27-v2`, puis verrouiller les deux copies par des tests de
digest distincts. Statut : **DONE local — ready to push** — candidat et commit
local ciblé terminés par le présent commit, avec validations finales vertes.
Autorisation de push **BLOCKED**; push `brand/main` **NOT RUN / BLOCKED**;
preuve publique et approbation humaine **NOT RUN**, dans cet ordre. Aucune
validation juridique n'est revendiquée.

### Périmètre de la phase

- Nouveau fichier `terms/revisions/ugc-2026-08-04-v1/index.html`.
- Notices de version dans `terms/index.html`, sans changement du texte v2.
- Contrats d'immuabilité et QA six pages dans `test_site.py`.
- Documentation de version et de publication explicite dans `README.md`.
- Reprise autonome dans les trois fichiers `.agent`.

La copie `terms/revisions/ugc-2026-08-27-v2/index.html` doit rester identique
octet pour octet. Le staging explicite et le commit local ciblé sont intégrés au
présent commit par exception au périmètre historique ci-dessus. Aucun push ni
changement externe n'est autorisé sans autorisation humaine explicite.

### Validations prévues

- `python -B test_site.py`
- `python -B test_site.py --release`
- `python -m py_compile test_site.py`
- `python -m compileall -q test_site.py`
- `git diff --check`
- SHA-256 de la copie v2 avant/après strictement identique.
- Revue navigateur locale de `/terms/` et de la copie v1 sur bureau et viewport
  mobile `390×844` : overflow document, visibilité FR/EN, ressources externes,
  console et chargement direct de la cible du lien relatif unique.

### Procédure de reprise exacte

1. **DONE** — Relire cette phase, `.agent/AUTONOMOUS_STATUS.md` et
   `.agent/TASKS.md`.
2. **DONE** — Vérifier le SHA-256 v2 et préserver ce fichier octet pour octet.
3. **DONE** — Terminer la copie v1, les notices, les digests et les cinq
   validations.
4. **DONE** — Créer le candidat et le commit local ciblé par le présent commit;
   état **ready to push**.
5. **BLOCKED** — Attendre une autorisation humaine explicite de push.
6. **NOT RUN / BLOCKED** — Après cette autorisation, pousser le présent commit
   vers `brand/main`.
7. **NOT RUN** — Attendre GitHub Pages et vérifier publiquement en HTTPS l'URL
   canonique, l'identifiant et le contenu exacts.
8. **NOT RUN** — Demander et consigner l'approbation humaine uniquement après
   cette preuve publique, sans revendiquer d'approbation juridique implicite.

### Checkpoint local

- 2026-08-28 — Correction terminée : le corps v1 reprend exactement les
  quatorze libellés Flutter, sans élargissement, et les verrous digest/SHA brut
  détectent une altération réelle avant restauration. Digest sémantique v1
  `47c2619697866edff20829db94d3f3f1d082173ac5476e485b6139755958d862`;
  SHA-256 brut v1
  `BDD182194F7B1F10AB28A2DBB28126495E7AF6403AA92BF903BA324B901CCCE2`.
  QA normale/release, `py_compile`, `compileall` et diff-check PASS. Le SHA-256
  brut v2 reste
  `BCDBC5BD62402B29A6ECC34C645866DD0893FD5FE5C447EAB8116BBEA767BEF5`
  avant/après. Candidat et commit local ciblé **DONE — ready to push** par le
  présent commit. Autorisation de push **BLOCKED**; push `brand/main`
  **NOT RUN / BLOCKED**; preuve publique et approbation humaine **NOT RUN**, dans
  cet ordre.
- 2026-08-28 — Revue navigateur locale `/terms/` et copie v1 : **PASS** sur
  bureau et viewport mobile `390×844`. Aucun overflow du document; sections
  FR/EN visibles; zéro ressource externe; zéro erreur console. Le lien relatif
  unique vers v1 charge directement sa cible en HTTP 200 local. La navigation
  du header mobile est volontairement scrollable et l'absence historique de
  favicon est non bloquante. Cette revue locale n'est pas une preuve publique;
  publication et approbation restent **NOT RUN / BLOCKED**.
