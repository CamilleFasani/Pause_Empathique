# Prochaine session — Objectifs

> Source de vérité pour la prochaine étape de travail. À mettre à jour à la fin de
> chaque session.

## Session #25 — Vues du compte utilisateur et pré-déploiement front

### Contexte

La branche front du parcours de pratique est prête à être mergée par
l'utilisateur après validation manuelle :

- navigation Accueil / Journal / pratique / détail de pause clarifiée ;
- `HomeView` affiche les dernières pauses et mène au Journal ;
- `DiaryView` affiche l'historique complet avec timeline verticale, filtres par
  familles de sentiments, familles de besoins et période/date ;
- les visuels du Journal sont centralisés dans `src/config/journalVisuals.ts` :
  la couleur vient de la famille de sentiments prédominante et l'icône Iconoir de
  la famille de besoins prédominante ;
- `beforeunload` prévient la perte du brouillon uniquement quand le store Pinia
  contient des données utiles, sans persistance `localStorage` ou
  `sessionStorage` du brouillon ;
- les tests unitaires de base du store de pratique sont en place avec Vitest ;
- les vérifications front ont été lancées avec succès :
  `npm run test:unit`, `npm run type-check`, `npm run lint`, `npm run build`.

Les tests e2e sont volontairement reportés, car l'UI et le produit vont encore
évoluer.

La branche front `feat/add-account-views` contient désormais la vue du compte et
attend sa validation manuelle mobile avant merge.

### Objectif 1 — Repartir d'une base propre

- [x] Vérifier que la branche front précédente a bien été mergée.
- [x] Créer une branche dédiée aux vues du compte utilisateur.
- [x] Relire l'état de `docs/project-management.md` et confirmer le périmètre de
      la session.

### Objectif 2 — Vues du compte utilisateur

- [x] Définir les écrans nécessaires : consultation, modification et suppression
      du compte.
- [x] Vérifier le contrat API existant pour le profil utilisateur.
- [x] Implémenter les vues via le store d'authentification et la couche API
      existants.
- [x] Prévoir les états chargement, erreur, succès, compte supprimé et session
      expirée.
- [x] Vérifier que la suppression de compte nettoie correctement l'état local et
      redirige l'utilisateur.

### Objectif 3 — Prérequis avant déploiement front

- [ ] Ajouter côté back un timestamp au modèle/table `AnonymousPauseCounter`
      pour connaître la dernière pratique anonyme comptabilisée sans stocker le
      contenu de la pause.
- [ ] Prévoir migration, tests back ciblés et mise à jour éventuelle du suivi
      projet.
- [ ] Mettre à jour la CI si les nouvelles étapes de build/test le nécessitent.
- [ ] Créer la CD front pour automatiser le déploiement vers la cible retenue.
- [ ] Décider de la cible de déploiement front : Railway, Vercel ou Netlify.
- [ ] Préparer les variables d'environnement front, notamment l'URL de l'API.

### Objectif 4 — Vérifications

- [ ] Lancer les tests pertinents back si le timestamp anonyme est modifié.
- [x] Lancer `npm run test:unit`.
- [x] Lancer `npm run type-check`.
- [x] Lancer `npm run lint`.
- [x] Lancer `npm run build`.
- [ ] Vérifier manuellement les parcours compte sur mobile.

### Limites de la prochaine session

- Ne pas ajouter de tests e2e tant que les écrans produit restent fortement
  évolutifs.
- Ne pas déplacer la logique de sécurité côté front : l'API reste responsable de
  l'autorisation et de la suppression réelle du compte.
