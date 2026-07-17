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

- [x] Relire le diff et l'état Git de `feat/-base-layout-and-auth-views` pour
      vérifier qu'aucun travail incomplet ou changement étranger n'est embarqué.
- [x] Vérifier manuellement le rendu, les interactions et la navigation de
      `WelcomeView` sur mobile et desktop.
- [x] Finaliser des commits ciblés et pousser la branche.
- [x] Merger la branche dans `dev`, puis vérifier la CI et l'état final de `dev`.

### Objectif 2 — Concevoir l'authentification sécurisée

- [x] Créer une branche dédiée après le merge.
- [x] Définir le contrat de cookies entre Django/DRF et Vue avant de coder.
- [x] Traiter explicitement `HttpOnly`, `Secure`, `SameSite`, CSRF, refresh,
      rotation, expiration et logout.
- [ ] Remplacer le stockage persistant du refresh token dans `localStorage` par
      la stratégie validée.
- [ ] Adapter et tester le back-end, le client Axios et le store auth.
- [ ] Vérifier le fonctionnement de bout en bout avant merge.

**Avancement au point intermédiaire :**

- ✅ Partie back réalisée sur `feat/secure-authentication` : refresh token en
  cookie `HttpOnly`, access token en JSON, refresh/logout via cookie, blacklist
  Simple JWT, expiration du cookie alignée sur le refresh token.
- ✅ Tests auth back ciblés verts : `users/tests/test_api_auth.py` — 22 tests.
- ✅ Documentation du contrat et du choix CSRF mise à jour.
- ⏳ Merge back dans `dev` en cours/à confirmer par la développeuse.
- ⏳ Partie front restante dans le repo `pause_empathique_front` : adapter Axios,
  Pinia et le parcours auth pour ne plus utiliser `localStorage` pour le refresh
  token.

### Limites de cette session

- Ne pas commencer la migration vers les cookies avant le merge de la branche
  actuelle et la création d'une branche dédiée.
- Ne pas reprendre le Dashboard ni les pages du parcours avant la session dédiée.
- Ne pas considérer tous les layouts applicatifs comme terminés : seuls ceux liés
  à l'authentification sont validés à ce stade.
- Ne pas marquer l'objectif 2 comme terminé tant que l'intégration front et la
  vérification end-to-end entre les deux repos ne sont pas réalisées.

---

## Objectif suivant — Dashboard et parcours de pratique

Après sécurisation de l'authentification, créer une branche commune pour :

- reprendre et finaliser le Dashboard ;
- finaliser le layout des pages applicatives ;
- construire le parcours « vide ton sac » → observation → sentiments → besoins ;
- définir les données et transitions entre les étapes ;
- intégrer progressivement les endpoints API correspondants.
