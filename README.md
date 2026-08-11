# WiniCharge Legal

Site statique bilingue destiné à héberger la politique de confidentialité et la procédure de suppression de compte de WiniCharge.

> **Version de publication.** Le contenu décrit le fonctionnement documenté de WiniCharge au 11 août 2026. Il ne constitue ni une certification de conformité ni une validation par une autorité publique. Toute évolution du produit ou de la réglementation doit déclencher une nouvelle revue.

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

## Informations confirmées

- responsable du traitement et développeur public : Yassine Gh ;
- support : `winichargedev@gmail.com` ;
- cadre de lancement : Tunisie et loi organique n° 2004-63 du 27 juillet 2004 ;
- autorité de recours : Instance nationale de protection des données personnelles (INPDP) ;
- backend : Supabase, hébergé dans l’Union européenne avec accès à distance depuis Tunis ;
- e-mail : Google ;
- cartographie : serveur raster standard OpenStreetMap via HTTPS ;
- demande Web de suppression traitée sous une semaine au maximum ;
- données restant en accès restreint après suppression supprimées ou anonymisées sous trois jours au maximum.

## Tests locaux

Depuis la racine de ce dossier :

```powershell
python test_site.py
python -m py_compile test_site.py
python -m compileall -q test_site.py
```

Le test normal et le contrôle de release doivent tous deux réussir :

```powershell
python test_site.py --release
```

Le mode `--release` vérifie notamment l’absence de placeholder, les URL finales, le support, le parcours de suppression et les garde-fous de sécurité. Pour contrôler les espaces finaux sous Windows, essayer :

```powershell
git diff --no-index --check NUL .
```

Si Git ne traite pas `NUL` comme un fichier vide dans l’environnement utilisé, le test Python applique un contrôle de whitespace aux actifs du site et à la documentation.

## Publication GitHub Pages

Le dépôt public autorisé est `winicharge-app/winicharge-app.github.io`. Depuis une branche `main` validée :

```powershell
git add .
git commit -m "docs: finalize WiniCharge legal pages"
git push brand main
```

Dans les paramètres du dépôt GitHub :

1. Ouvrir **Settings → Pages**.
2. Choisir **Deploy from a branch**.
3. Sélectionner la branche **main** et le dossier **/ (root)**.
4. Enregistrer, attendre la génération, puis activer **Enforce HTTPS** dès que l’option est disponible.
5. Vérifier manuellement les trois pages sur mobile et ordinateur, les ancres de langue et le bouton d’e-mail.

## URL finales

- Politique de confidentialité : `https://winicharge-app.github.io/privacy/`
- Suppression de compte : `https://winicharge-app.github.io/delete-account/`

Ces URL doivent répondre publiquement en HTTPS, sans connexion, avant leur utilisation dans Play Console.

## Checklist de maintenance

- Rejouer les deux commandes de test avant chaque publication.
- Vérifier visuellement les versions française et anglaise sur mobile et ordinateur.
- Tester les deux liens `mailto:` et la réception par le support.
- Maintenir les pages alignées avec l’application, les prestataires et les durées réellement appliquées.
- Refaire une revue appropriée lors de toute évolution juridique ou fonctionnelle substantielle.
