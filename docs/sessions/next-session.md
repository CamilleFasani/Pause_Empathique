# Prochaine session — Objectifs

> Source de vérité pour la prochaine étape de travail. À mettre à jour à la fin de
> chaque session.

## Session #18 — 17 juillet 2026 — Merge puis authentification sécurisée

### Contexte

La session #17 a été clôturée le 10 juillet 2026. Les vues d'authentification, leur
branchement au store et les choix de parcours depuis `WelcomeView` sont terminés.
Les commandes `npm run type-check`, `npm run lint` et `npm run build` ont réussi.

La branche front `feat/-base-layout-and-auth-views` doit être finalisée et mergée
au début de cette session. Elle contient une première gestion JWT fonctionnelle
avec refresh token dans `localStorage` ; cette stratégie reste strictement
transitoire et ne doit pas être prolongée dans les travaux suivants.

### Objectif 1 prioritaire — Finaliser et merger la branche actuelle

- [ ] Relire le diff et l'état Git de `feat/-base-layout-and-auth-views` pour
  vérifier qu'aucun travail incomplet ou changement étranger n'est embarqué.
- [ ] Vérifier manuellement le rendu, les interactions et la navigation de
  `WelcomeView` sur mobile et desktop.
- [ ] Finaliser des commits ciblés et pousser la branche.
- [ ] Merger la branche dans `dev`, puis vérifier la CI et l'état final de `dev`.

### Objectif 2 — Concevoir l'authentification sécurisée

- [ ] Créer une branche dédiée après le merge.
- [ ] Définir le contrat de cookies entre Django/DRF et Vue avant de coder.
- [ ] Traiter explicitement `HttpOnly`, `Secure`, `SameSite`, CSRF, refresh,
  rotation, expiration et logout.
- [ ] Remplacer le stockage persistant du refresh token dans `localStorage` par
  la stratégie validée.
- [ ] Adapter et tester le back-end, le client Axios et le store auth.
- [ ] Vérifier le fonctionnement de bout en bout avant merge.

### Limites de cette session

- Ne pas commencer la migration vers les cookies avant le merge de la branche
  actuelle et la création d'une branche dédiée.
- Ne pas reprendre le Dashboard ni les pages du parcours avant la session dédiée.
- Ne pas considérer tous les layouts applicatifs comme terminés : seuls ceux liés
  à l'authentification sont validés à ce stade.

---

## Objectif suivant — Dashboard et parcours de pratique

Après sécurisation de l'authentification, créer une branche commune pour :

- reprendre et finaliser le Dashboard ;
- finaliser le layout des pages applicatives ;
- construire le parcours « vide ton sac » → observation → sentiments → besoins ;
- définir les données et transitions entre les étapes ;
- intégrer progressivement les endpoints API correspondants.
