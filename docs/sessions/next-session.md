# Prochaine session — Objectifs

> Source de vérité pour la prochaine étape de travail. À mettre à jour à la fin de
> chaque session.

## Session #19 — 24 juillet 2026 — Relecture auth sécurisée, tests et merges

### Contexte

La session #18 du 17 juillet 2026 a finalisé l'objectif 1 du jour et avancé
fortement l'objectif 2 d'authentification sécurisée.

Côté back, la branche `feat/secure-authentication` implémente le refresh token en
cookie `HttpOnly` : login avec `Set-Cookie`, refresh/logout via cookie, blacklist
Simple JWT, expiration du cookie alignée sur le refresh token, configuration CORS
avec credentials, documentation OpenAPI ajustée et tests auth ciblés verts.

Côté front, la branche `feat/secure-authentication` a été adaptée au nouveau
contrat : Axios utilise `withCredentials`, les fonctions API auth ne manipulent
plus de refresh token dans le body, le store Pinia ne stocke plus le refresh token
dans `localStorage`, l'intercepteur Axios tente un refresh automatique sur `401`,
le logout appelle le back sans body, et la garde de route attend
l'initialisation auth avant de rediriger.

La prochaine session doit commencer par une relecture pédagogique du travail front
réalisé, puis par les arbitrages de review Copilot remontés sur la branche back.
Les merges ne doivent venir qu'après cette relecture, les décisions de review et
les tests manuels/end-to-end.

### Objectif 1 prioritaire — Comprendre le travail front réalisé

- [ ] Relire le diff front de `feat/secure-authentication`.
- [ ] Comprendre le rôle de `src/api/client.ts` :
  - `withCredentials`;
  - intercepteur request pour `Authorization`;
  - intercepteur response sur `401`;
  - `refreshPromise` pour éviter les refresh concurrents ;
  - `skipAuthRefresh` pour éviter les boucles sur login/refresh/logout.
- [ ] Comprendre le rôle de `src/api/auth.ts` :
  - login/register/refresh/logout alignés avec le contrat back ;
  - refresh/logout sans body ;
  - réponse auth limitée à `{ access: string }`.
- [ ] Comprendre le rôle de `src/stores/auth.ts` :
  - access token en mémoire ;
  - suppression du refresh token côté front ;
  - restauration de session via cookie ;
  - `isAuthReady` ;
  - logout et nettoyage de session.
- [ ] Comprendre le rôle de la garde Vue Router :
  - attendre l'initialisation auth ;
  - protéger les routes privées ;
  - rediriger une utilisatrice déjà connectée hors de login/register.

### Objectif 2 — Arbitrer la review Copilot côté back

- [ ] Relire les commentaires Copilot sur la branche back
  `feat/secure-authentication`.
- [ ] Classer chaque remarque :
  - à corriger avant merge ;
  - à documenter/assumer ;
  - à reporter dans une étape dédiée.
- [ ] Appliquer les corrections retenues côté back.
- [ ] Relancer les vérifications back utiles :
  - `poetry run ruff check ...` ;
  - `pytest users/tests/test_api_auth.py` ;
  - suite plus large si les corrections dépassent l'auth.

### Objectif 3 — Tests front et end-to-end

- [ ] Lancer le back et le front localement.
- [ ] Vérifier au navigateur :
  - login réussi ;
  - cookie `refresh_token` présent, `HttpOnly`, limité au chemin `/api/v1/auth/` ;
  - aucun refresh token dans `localStorage` ;
  - access token non persistant côté navigateur ;
  - rechargement de page avec restauration de session ;
  - route protégée accessible après restauration ;
  - refresh automatique après `401` ou expiration simulée de l'access token ;
  - logout avec suppression du cookie ;
  - route protégée inaccessible après logout ;
  - mauvais identifiants sans boucle de refresh.
- [ ] Relancer côté front :
  - `npm run type-check` ;
  - `npm run lint` ;
  - `npm run build`.

### Objectif 4 — Merges dans le bon ordre

- [ ] Merger la branche back `feat/secure-authentication` dans `dev`.
- [ ] Vérifier la CI back sur `dev`.
- [ ] Rebaser la branche back docs `docs/project-management-and-read-me` sur
  `dev`, résoudre les conflits éventuels, puis la merger dans `dev`.
- [ ] Vérifier que les docs de session et de projet reflètent l'état réel.
- [ ] Une fois back + docs verts, merger la branche front `feat/secure-authentication`.
- [ ] Vérifier la CI front.

### Objectif suivant — Dashboard et parcours de pratique

Après sécurisation complète de l'authentification et merges validés, créer une
branche front dédiée pour :

- reprendre et finaliser le Dashboard ;
- finaliser le layout des pages applicatives ;
- construire le parcours « vide ton sac » → observation → sentiments → besoins ;
- définir les données et transitions entre les étapes ;
- intégrer progressivement les endpoints API correspondants.

### Limites de la prochaine session

- Ne pas merger la branche front avant validation du back, des docs et des tests
  end-to-end.
- Ne pas reprendre le Dashboard ni le parcours de pratique avant la fin de
  l'authentification sécurisée.
- Ne pas considérer l'objectif 2 comme terminé sans vérification navigateur.
