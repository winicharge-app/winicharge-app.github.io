# WiniCharge Legal

Site statique bilingue destiné à héberger la politique de confidentialité et la procédure de suppression de compte de WiniCharge.

> **Publication bloquée.** Ce dossier est un candidat technique, pas une version publiable. Tous les placeholders doivent être remplacés par des informations approuvées, puis le contenu doit être validé par les responsables produit, sécurité et juridique avant tout push, activation GitHub Pages ou utilisation dans Play Console.

## Contenu

- `index.html` : accueil bilingue et accès aux documents.
- `privacy/index.html` : politique de confidentialité FR/EN.
- `delete-account/index.html` : procédure de suppression FR/EN et modèle d’e-mail.
- `styles.css` : styles locaux, responsive et accessibles.
- `.nojekyll` : désactive le traitement Jekyll sur GitHub Pages.
- `.gitignore` : exclut les caches et bytecodes Python générés localement.
- `test_site.py` : contrôles structurels, liens, sécurité et garde de publication.
- `.agent/` : plan d’exécution et état de reprise du lot.

Aucune page ne charge de police, image, script, feuille de styles ou autre ressource distante. Le site n’intègre ni formulaire, ni cookie, ni analytics, ni tracker.

## Placeholders bloquants

Les valeurs suivantes doivent être remplacées exclusivement à partir d’informations humaines approuvées :

- `[[NOM_DU_DEVELOPPEUR_PLAY_CONSOLE]]`
- `[[EMAIL_SUPPORT_APPROUVE]]`
- `[[RESPONSABLE_DU_TRAITEMENT]]`
- `[[DATE_D_EFFET]]`
- `[[DELAI_DE_TRAITEMENT_SUPPRESSION]]`
- `[[DUREES_DE_CONSERVATION]]`
- `[[FOURNISSEUR_DE_TUILES]]`
- `[[FOURNISSEUR_SMTP]]`
- `[[REGION_ET_TRANSFERTS_SUPABASE]]`
- `[[BASES_JURIDIQUES_ET_AUTORITE_DE_RECOURS]]`
- `[[PROCESSUS_VERIFICATION_WEB]]`

Ne pas transformer un placeholder en affirmation tant que la valeur, sa formulation bilingue et sa portée n’ont pas été validées. Vérifier aussi que l’adresse de support approuvée est identique dans le texte visible et dans les deux liens `mailto:`.

## Tests locaux

Depuis la racine de ce dossier :

```powershell
python test_site.py
python -m py_compile test_site.py
python -m compileall -q test_site.py
```

Le test normal valide le candidat et recense les placeholders attendus. Le contrôle de release doit échouer dans l’état actuel :

```powershell
python test_site.py --release
```

Après remplacement de tous les placeholders, `python test_site.py --release` doit réussir avant toute publication. Pour contrôler les espaces finaux sous Windows, essayer :

```powershell
git diff --no-index --check NUL .
```

Si Git ne traite pas `NUL` comme un fichier vide dans l’environnement utilisé, le test Python applique un contrôle de whitespace aux actifs du site et à la documentation.

## Publication manuelle — ne pas exécuter avant validation

Ces commandes sont fournies comme aide opératoire uniquement. Elles ne doivent être lancées qu’après validation humaine du contenu et de l’identité du dépôt :

```powershell
git init
git add .
git commit -m "Add WiniCharge legal pages"
git branch -M main
git remote add origin https://github.com/<GITHUB_USERNAME>/winicharge-legal.git
git push -u origin main
```

Dans les paramètres du dépôt GitHub :

1. Ouvrir **Settings → Pages**.
2. Choisir **Deploy from a branch**.
3. Sélectionner la branche **main** et le dossier **/ (root)**.
4. Enregistrer, attendre la génération, puis activer **Enforce HTTPS** dès que l’option est disponible.
5. Vérifier manuellement les trois pages sur mobile et ordinateur, les ancres de langue et le bouton d’e-mail.

## URL attendues après publication approuvée

- Politique de confidentialité : `https://<GITHUB_USERNAME>.github.io/winicharge-legal/privacy/`
- Suppression de compte : `https://<GITHUB_USERNAME>.github.io/winicharge-legal/delete-account/`

Ces URL ne sont pas actives tant que le dépôt et GitHub Pages n’ont pas été créés par une personne autorisée. Ne les saisir dans Play Console qu’après ouverture publique, contrôle HTTPS et validation finale du contenu.

## Checklist humaine avant release

- Valider l’identité du développeur affichée dans Play Console et celle du responsable du traitement.
- Approuver l’adresse support, tester sa réception et confirmer le processus de vérification hors application.
- Confirmer la date d’effet, les bases juridiques, l’autorité de recours et les durées applicables.
- Confirmer la région et les transferts Supabase, ainsi que les fournisseurs SMTP et de tuiles.
- Relire les versions française et anglaise et obtenir l’accord juridique approprié.
- Exécuter le mode `--release`, puis vérifier visuellement le rendu publié avant utilisation dans Play Console.
