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

Mise à jour session #8 (27 mars) :

- ✅ Merge de `chore/drf-setup` vers `dev` effectué
- ⚠️ CI non passante après merge : `pip-audit` a détecté `CVE-2026-4539` sur `pygments` (pas de version corrigée publiée à ce stade)
- ✅ Ajout d'un objectif complémentaire de pré-check sécurité avant prochain déploiement
- ✅ Passage sur l'Objectif 2 (auth API)

---

### Objectifs de la session

#### Objectif 1 — Finaliser le merge de setup DRF (priorité)

- [x] Merger `chore/drf-setup` vers `dev`
- [x] Vérifier CI/CD après merge sur `dev` (échec du job security : `pip-audit` / `CVE-2026-4539`)
- [ ] Vérifier le déploiement staging post-merge
- [x] Créer une nouvelle branche dédiée auth API : `feature/authentication`

#### Objectif complémentaire — Pré-check sécurité avant prochain déploiement

- [ ] Surveiller la publication d'un correctif pour `CVE-2026-4539` (pygments)
- [ ] Dès qu'un fix est disponible, mettre à jour la version dans les dépendances et régénérer le lock
- [ ] Relancer le job sécurité (`pip-audit`) en CI pour valider la remédiation
- [ ] Vérifier l'adéquation des images de déploiement staging et production (dépendances runtime uniquement, pas de dépendances dev inutiles)

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
