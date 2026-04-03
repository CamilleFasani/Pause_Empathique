# Prochaine session — Objectifs

> Ce fichier est lu en priorité par Copilot au démarrage de chaque session.
> Mis à jour en fin de session avec les objectifs suivants.

---

## Session #9 — 3 avril 2026

### Contexte

Session #8 (27 mars) écourtée. Ce qui a été accompli :

- Merge `chore/drf-setup` → `dev` ✅
- Branche `feature/authentication` créée ✅
- Squelette auth API en place : routing `api/v1/auth/` + `api/v1/users/`, serializers `RegisterSerializer` + `UserSerializer` ✅
- **Mais :** `users/api/views.py` vide, placeholders `xxxx` dans les URL files, zéro test API

CVE ouverte : `CVE-2026-4539` sur `pygments` (pas de correctif upstream disponible à ce jour).

---

### Objectifs de la session

#### Objectif 1 — Vérifier la CVE pygments (rapide)

- [ ] Vérifier si un correctif a été publié pour `CVE-2026-4539` (pygments)
- [ ] Si oui : mettre à jour la dépendance, régénérer le lock, valider le job `pip-audit` en CI
- [ ] Si non : noter la date de vérification et passer à l'Objectif 2

#### Objectif 2 — Implémenter les endpoints auth JWT (priorité principale)

**Vues à implémenter dans `users/api/views.py` + brancher les URLs (remplacer les `xxxx`) :**

- [ ] `POST /api/v1/auth/register/` — inscription (RegisterView custom, utilise RegisterSerializer)
- [ ] `POST /api/v1/auth/token/` — login, obtention access + refresh token (TokenObtainPairView de Simple JWT)
- [ ] `POST /api/v1/auth/token/refresh/` — rafraîchissement du token (TokenRefreshView de Simple JWT)
- [ ] `POST /api/v1/auth/token/blacklist/` — logout, blacklist du refresh token (TokenBlacklistView de Simple JWT)
- [ ] `GET /api/v1/users/me/` — profil de l'utilisateur connecté (UserSerializer, permission IsAuthenticated)
- [ ] `PUT/PATCH /api/v1/users/me/` — mise à jour du profil
- [ ] `DELETE /api/v1/users/me/` — suppression de compte

#### Objectif 3 — Tests API auth

Pour chaque endpoint ci-dessus, écrire les tests :

- [ ] Cas passant (status codes, payload retourné)
- [ ] Cas d'erreur (payload invalide, credentials incorrects)
- [ ] Vérification des permissions (accès sans token refusé sur les routes protégées)
- [ ] Couverture maintenue ≥ 80 %

#### Objectif 4 (si le temps le permet) — Vérifications de base API

- [ ] Confirmer l'accès à `/api/v1/health/`, `/api/schema/`, `/api/docs/` en staging
- [ ] Valider l'absence de régression sur les vues Django existantes

---

### Ce qu'on ne fait PAS cette session

- Reset mot de passe (flux email à définir — reporté)
- Design system / templates Django
- Endpoints métier (Pauses, Feelings, Needs)

---

### Rappels du chef de projet

- 🔒 Sécuriser chaque endpoint dès le départ : JWT + `IsAuthenticated` + throttling déjà configuré
- 🧪 Écrire les tests en même temps que les vues, pas après
- ✅ Garder la V1 stable en production — travail sur `feature/authentication`
- 🔀 Merge vers `dev` uniquement après CI verte et tests passants
