# Prochaine session — Objectifs

> Ce fichier est lu en priorité par Copilot au démarrage de chaque session.
> Mis à jour en fin de session avec les objectifs suivants.

## Session #17 — prochaine session

### Contexte

Session #16 (12 juin 2026) : Vue Router, Pinia, axios client posés. Connexion front ↔ back validée.

- Vue Router 4 installé, routes `/`, `/login`, `/register` configurées ✅
- Architecture `AuthView` + `LoginForm` / `RegisterForm` décidée (une page, deux composants) ✅
- `App.vue` coquille vide avec `<RouterView />` ✅
- Pinia installé, `useAuthStore` créé (`isAuthenticated`, `user: User | null`) ✅
- `src/api/client.ts` : instance axios avec `VITE_API_URL` ✅
- Connexion front ↔ back validée (`GET /api/v1/health/` → `{ status: "ok" }`) ✅
- Merge `feat/vue-router-pinia` → `dev` front

---

### Objectifs de la session

#### Objectif 1 — Layouts de base (début de session, ~20 min)

Avant de construire les vues, poser le squelette commun à toutes les pages.

- [ ] Créer `src/layouts/AuthLayout.vue` : layout épuré pour login/register (logo centré, pas de navigation)
- [ ] Créer `src/layouts/AppLayout.vue` : layout complet avec `<AppHeader />`, `<main><RouterView /></main>`, `<AppFooter />`
- [ ] Créer `src/components/AppHeader.vue` et `src/components/AppFooter.vue` (squelettes vides pour l'instant)
- [ ] Brancher `AuthLayout` dans `AuthView` et `AppLayout` dans `HomeView`

#### Objectif 2 — Vues auth : LoginForm et RegisterForm

Construire les deux formulaires d'authentification selon la maquette.

- [ ] `LoginForm.vue` : champ email, champ mot de passe, bouton "Me connecter", lien "Mot de passe oublié ?"
- [ ] `RegisterForm.vue` : champ prénom, email, mot de passe, confirmation, toggle genre, bouton "M'inscrire"
- [ ] `AuthView.vue` : toggle "j'ai déjà un compte" / "je n'ai pas de compte" fonctionnel avec `useRoute` + `useRouter`
- [ ] Valider le rendu visuel avec `npm run dev`

#### Objectif 2 — Branchement auth store + appels API

Connecter les formulaires au back via `useAuthStore` et `apiClient`.

- [ ] Ajouter action `login(email, password)` dans `useAuthStore` : appel `POST /api/v1/auth/token/`, stockage access + refresh token
- [ ] Ajouter action `register(data)` dans `useAuthStore` : appel `POST /api/v1/users/`
- [ ] Décider du stockage des tokens : `localStorage` vs `httpOnly cookie` (à trancher)
- [ ] Après login réussi : rediriger vers `/` via `router.push`

#### Objectif 3 — Guards de navigation (si le temps le permet)

Protéger les routes qui nécessitent d'être connectée.

- [ ] Ajouter `meta: { requiresAuth: true }` sur les routes protégées
- [ ] Créer un `router.beforeEach` qui redirige vers `/login` si non authentifiée

---

### Rappels du chef de projet

- CI verte obligatoire avant merge vers `dev`
- Décision stockage JWT (localStorage vs httpOnly cookie) à prendre **avant** d'implémenter — ça impacte la sécurité
- Ne pas implémenter les guards avant que le login soit fonctionnel
