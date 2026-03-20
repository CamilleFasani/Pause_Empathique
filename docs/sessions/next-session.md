# Prochaine session — Objectifs

> Ce fichier est lu en priorité par Copilot au démarrage de chaque session.
> Mis à jour en fin de session avec les objectifs suivants.

---

## Session #8 — Date prévue : 27 mars 2026

### Contexte

Session #7 (20 mars) : démarrage effectif de la phase DRF/JWT sur backend Dockerisé.

- Installation des dépendances API : DRF, Simple JWT, CORS headers, drf-spectacular
- Configuration initiale DRF dans `settings.py` (JWT, permissions, throttling, schéma OpenAPI)
- Ajout du routing API versionné et du premier endpoint `health`
- Clarification de la stratégie : auth API d'abord (JWT), endpoints métier ensuite

---

### Objectifs de la session

#### Objectif 1 — Finaliser le merge de setup DRF (priorité)

- [ ] Merger `chore/drf-setup` vers `dev`
- [ ] Vérifier CI/CD après merge sur `dev`
- [ ] Vérifier le déploiement staging post-merge
- [ ] Créer une nouvelle branche dédiée auth API (ex: `feature/auth-api-jwt`)

#### Objectif 2 — Implémenter les endpoints d'authentification JWT

- [ ] Créer les routes auth API dans l'app `users` (namespace `api/v1/auth/`)
- [ ] Implémenter : se connecter, se déconnecter, créer son compte
- [ ] Implémenter : consulter son compte, supprimer son compte
- [ ] Implémenter : reset mot de passe (forgot/reset)
- [ ] Ajouter les tests API auth (permissions, cas OK/KO)

#### Objectif 3 — Stabiliser la base API et documentation

- [ ] Vérifier l'accès à `/api/v1/health/`, `/api/schema/`, `/api/docs/`
- [ ] Documenter les endpoints auth dans le schéma OpenAPI
- [ ] Valider l'absence de régression sur les vues Django existantes

---

### Rappels du chef de projet

- 🔀 Merger d'abord `chore/drf-setup` vers `dev`, puis créer une branche feature dédiée auth
- ✅ Garder la V1 stable en production, travailler la V2/API sur staging
- 🔒 Sécuriser les endpoints auth dès le départ (JWT + permissions + throttling + tests)
- 🧩 Reporter les efforts design system front tant que le socle auth API n'est pas stabilisé
