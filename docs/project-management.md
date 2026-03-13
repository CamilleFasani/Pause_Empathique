# Gestion de projet — Pause Empathique

> Ce fichier suit l'avancement global du projet dans le cadre de la préparation au titre CDA.
> Mis à jour à chaque fin de phase ou étape significative.

---

## Vision globale

Transformer **Pause Empathique** d'une application Django full stack en une architecture découplée :

- **Back-end** : API REST Django (DRF) — repo actuel
- **Front-end** : SPA Vue.js 3 + TypeScript — repo séparé (à créer)

L'objectif est double : livrer une application de qualité production ET acquérir les compétences du titre CDA.

---

## État actuel — Mars 2026

- ✅ Application Django full stack fonctionnelle en production (`pause-empathique.fr`)
- ✅ Authentification par sessions Django (templates)
- ✅ CI/CD GitHub Actions (lint Ruff + tests Django via Docker)
- ✅ Job CI sécurité dépendances (`pip-audit`) ajouté
- ✅ Déploiement Railway (branche `main`)
- ✅ Environnement staging Railway opérationnel (`staging.pause-empathique.fr`) avec déploiement automatique sur `dev`
- ✅ Modèles : User, Pause, Feeling, Need
- ✅ CRUD complet sur les pauses
- ❌ Pas de couverture de tests mesurée
- ⚠️ Audit de sécurité des dépendances en place, remédiation CVE à suivre
- ❌ Charte graphique définitive non appliquée

---

## Phases du projet

### Phase 0 — Infrastructure & Qualité 🚧 EN COURS

> Objectif : avoir une base solide avant toute évolution fonctionnelle.
> Aucune phase suivante ne démarre sans que la phase 0 soit complète.

#### 0.1 — Environnement Staging

- [x] Créer un service Railway pour la branche `dev`
- [x] Configurer les variables d'environnement staging (`ENV_STATE=staging`, `DEBUG=False`, etc.)
- [x] Vérifier que le pipeline CI/CD fusionne correctement vers staging
- [x] Valider l'accès : `staging.pause-empathique.fr`

#### 0.2 — Couverture de tests

- [ ] Migrer les tests vers `pytest` + `pytest-django`
- [ ] Ajouter `pytest-cov` et mesurer la couverture actuelle
- [ ] Atteindre un seuil minimum de couverture : **80 %**
- [ ] Mettre à jour le job CI `test` pour utiliser pytest avec rapport de couverture

#### 0.3 — Sécurité des dépendances

- [x] Ajouter un job CI `security` : `pip-audit`
- [x] Résoudre les CVE critiques si détectées

#### 0.4 — Pre-commit hooks

- [ ] Installer et configurer `pre-commit` localement
- [ ] Hooks : `ruff check` + `ruff format` avant chaque commit

---

### Phase 1 — Nouvelle charte graphique ⏳ EN ATTENTE PHASE 0

> Objectif : appliquer la nouvelle identité visuelle sur le Django full stack existant.
> Le front reste en templates Django pendant toute cette phase.

- [ ] Définir la charte : couleurs, typographies, composants (déjà en cours ?)
- [ ] Configurer Tailwind v4 avec les variables CSS natives dans `input.css`
- [ ] Appliquer la charte vue par vue (templates Django)
- [ ] Responsive : vérifier mobile / desktop (le hook `user-agents` est déjà en place)
- [ ] Valider en staging avant merge sur `main`

**Critères de validation :**

- Toutes les vues sont stylées selon la charte
- Aucune régression fonctionnelle
- Tests visuels validés sur mobile et desktop

---

### Phase 2 — Migration vers API REST (DRF) ⏳ EN ATTENTE PHASE 1

> Objectif : transformer le back Django en API REST pure, progressivement, sans coupure.
> Stratégie : coexistence temporaire templates Django + endpoints API dans le même projet.

#### 2.1 — Mise en place DRF

- [ ] Installer `djangorestframework`
- [ ] Configurer DRF dans `settings.py` (authentification, permissions, pagination)
- [ ] Installer `drf-spectacular` et exposer les routes de documentation (`/api/schema/`, Swagger UI, Redoc)
- [ ] Installer `djangorestframework-simplejwt`
- [ ] Configurer les endpoints JWT : `/api/token/`, `/api/token/refresh/`
- [ ] Configurer CORS (`django-cors-headers`) pour le futur front Vue.js

#### 2.2 — Endpoints par ressource

Pour chaque ressource, créer serializer + viewset + URL avant de migrer le front :

- [ ] **Auth** : register, login (JWT), logout, profil, mise à jour, suppression
- [ ] **Pauses** : list, create, retrieve, update, delete
- [ ] **Feelings** : list (lecture seule, organisée par famille)
- [ ] **Needs** : list (lecture seule)

#### 2.3 — Tests API

- [ ] Écrire les tests pour chaque endpoint (authentification, permissions, payloads)
- [ ] Couverture maintenue ≥ 80 %

#### 2.4 — Documentation API

- [ ] Stabiliser et compléter le schéma OpenAPI (serializers, exemples, erreurs)
- [ ] Valider la doc Swagger / Redoc en staging avant migration front complète

#### 2.5 — Suppression des templates Django

- [ ] Une fois le front Vue.js validé en staging, supprimer les templates
- [ ] Nettoyer les dépendances front-only (django-widget-tweaks, django-browser-reload)

---

### Phase 3 — Frontend Vue.js + TypeScript ⏳ EN ATTENTE PHASE 2

> Objectif : SPA Vue.js 3 consommant l'API DRF, déployée séparément.

#### 3.1 — Setup du repo front

- [ ] Créer un nouveau repo GitHub `pause-empathique-front`
- [ ] Initialiser avec Vite + Vue.js 3 + TypeScript
- [ ] Configurer Tailwind CSS v4
- [ ] Configurer le linter (ESLint + Prettier)
- [ ] CI/CD : lint + build check

#### 3.2 — Authentification

- [ ] Intégrer la gestion des tokens JWT (access + refresh)
- [ ] Décider du stockage : `httpOnly cookie` vs `localStorage` (à discuter)
- [ ] Guards de navigation (routes protégées)
- [ ] Store Pinia pour l'état auth

#### 3.3 — Migration vue par vue

Pour chaque vue Django existante, créer le composant Vue équivalent :

- [ ] Login / Register
- [ ] Dashboard
- [ ] Observation (étape 1)
- [ ] Feelings (étape 2)
- [ ] Needs (étape 3)
- [ ] Diary (liste des pauses)
- [ ] Détail d'une pause
- [ ] Profil utilisateur

#### 3.4 — Déploiement front

- [ ] Déployer le front (Railway, Vercel, Netlify — à décider)
- [ ] Configurer les variables d'environnement (URL de l'API)
- [ ] Valider en staging

---

## Informations à collecter

| Information                                                 | Statut                 |
| ----------------------------------------------------------- | ---------------------- |
| Détails de la nouvelle charte graphique (couleurs, typos)   | ❌ À définir           |
| URL du repo front Vue.js                                    | ❌ À créer             |
| Contraintes de délai pour la formation CDA                  | ❌ À préciser          |
| Décision stockage JWT : `httpOnly cookie` vs `localStorage` | ❌ À décider (phase 3) |

---

## Principes directeurs (non négociables)

- **Production continue** : jamais de coupure, toujours une version stable sur `main`
- **Tests avant tout** : on ne livre pas de fonctionnalité sans test
- **Staging obligatoire** : toute évolution passe par staging avant `main`
- **Sécurité by design** : CORS, JWT, validation des données, audit de dépendances
- **Documentation officielle** : Django, DRF, Vue.js, TypeScript — pas de tutos douteux
- **Gitflow** : `main` / `dev` / `feature/<nom>` — commits conventionnels
