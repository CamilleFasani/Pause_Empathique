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
- ✅ Couverture de tests mesurée via `pytest-cov` (seuil 80 % à atteindre)
- ⚠️ Audit de sécurité des dépendances en place, remédiation CVE à suivre
- ✅ `pre-commit` local en place (Ruff + hooks qualité)
- ✅ Outil de documentation API validé : `drf-spectacular`
- ✅ Vérification des contrastes accessibilité (niveau AA) validée sur la palette actuelle
- ✅ Captures d'écran réalisées pour le dossier projet
- ✅ Stratégie de transition actée : V1 maintenue en production, V2 travaillée sur staging
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

- [x] Migrer les tests vers `pytest` + `pytest-django`
- [x] Ajouter `pytest-cov` et mesurer la couverture actuelle
- [ ] Atteindre un seuil minimum de couverture : **80 %**
- [x] Mettre à jour le job CI `test` pour utiliser pytest avec rapport de couverture

#### 0.3 — Sécurité des dépendances

- [x] Ajouter un job CI `security` : `pip-audit`
- [x] Résoudre les CVE critiques si détectées
- [ ] Suivre la publication du correctif pour `CVE-2026-4539` (pygments) et mettre à jour la dépendance dès disponibilité
- [ ] Après mise à jour, relancer l'audit sécurité CI et valider que staging/prod utilisent des images de déploiement adaptées (runtime sans dépendances dev inutiles)

#### 0.4 — Pre-commit hooks

- [x] Installer et configurer `pre-commit` localement
- [x] Hooks : `ruff check` + `ruff format` avant chaque commit

---

### Phase 1 — Nouvelle charte graphique 🚧 EN COURS

> Objectif : poser une base solide de charte graphique (tokens + direction visuelle) sans refonte complète des templates Django.
> La V1 reste en production ; la V2 est travaillée et validée sur staging.

- [x] Définir la charte : couleurs, typographies, composants (base v1.0)
- [x] Configurer Tailwind v4 avec les variables CSS natives dans `input.css`
- [ ] Appliquer la charte uniquement sur des vues pilotes (pas de refonte complète des templates Django)
- [ ] Responsive : vérifier mobile / desktop (le hook `user-agents` est déjà en place)
- [ ] Accessibilité : contrastes validés, navigation clavier/focus visible/labels à finaliser
- [x] Réaliser des captures d'écran pour le dossier projet
- [ ] Valider en staging avant merge sur `main`
- [ ] Approche composants hybride : composants simples "maison" (bouton, card, input) + choix ultérieur d'une librairie pour composants complexes (calendrier, etc.)

**Critères de validation :**

- Base de charte v1.0 stabilisée (tokens + direction visuelle)
- Vues pilotes validées en staging sans refonte globale des templates
- Aucune régression fonctionnelle
- Tests visuels (captures) validés sur mobile et desktop
- Contrastes conformes ; focus visible et navigation clavier validés avant généralisation

---

### Phase 2 — Migration vers API REST (DRF) 🚧 EN COURS (démarrage anticipé)

> Objectif : transformer le back Django en API REST pure, progressivement, sans coupure.
> Stratégie : coexistence temporaire templates Django + endpoints API dans le même projet.

#### 2.1 — Mise en place DRF

- [x] Installer `djangorestframework`
- [x] Configurer DRF dans `settings.py` (authentification, permissions, pagination)
- [x] Installer `drf-spectacular` et exposer les routes de documentation (`/api/schema/`, Swagger UI, Redoc)
- [x] Installer `djangorestframework-simplejwt`
- [ ] Configurer les endpoints JWT : `/api/token/`, `/api/token/refresh/`
- [x] Configurer CORS (`django-cors-headers`) pour le futur front Vue.js

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

#### 3.4 — Mise à jour sécurité

- [ ] Mettre en place HSTS côté application et/ou reverse proxy
- [ ] Lancer un test de sécurité avec OWASP ZAP sur l'environnement staging
- [ ] Refaire l'audit de sécurité du projet ( avec fiche donnée par Théo encadrant) et traiter les vulnérabilités remontées

#### 3.5 — Déploiement front

- [ ] Déployer le front (Railway, Vercel, Netlify — à décider)
- [ ] Configurer les variables d'environnement (URL de l'API)
- [ ] Valider en staging

---

### Phase 4 — Mise en conformité RGPD ⏳ EN ATTENTE PHASE 3

> Objectif : sécuriser la conformité légale et la protection des données personnelles avant la phase d'observabilité.

#### 4.1 — Cartographie et minimisation des données

- [ ] Cartographier les données personnelles collectées (profil, contenus de pauses, logs)
- [ ] Vérifier la minimisation des données et la base légale des traitements
- [ ] Formaliser les finalités de traitement dans la documentation projet

#### 4.2 — Information et consentement

- [ ] Rédiger/mettre à jour politique de confidentialité et mentions légales
- [ ] Vérifier les mécanismes de consentement si des traceurs/cookies sont utilisés
- [ ] Ajouter des informations claires sur les droits utilisateurs (accès, rectification, suppression)

#### 4.3 — Droits des personnes et sécurité

- [ ] Définir la procédure d'exercice des droits RGPD (demande d'accès/suppression)
- [ ] Vérifier la politique de conservation et suppression des données
- [ ] Vérifier les mesures techniques de sécurité (contrôle d'accès, secrets, sauvegardes)

---

### Phase 5 — Logs & Monitoring 📌 NON PRIORITAIRE (post-CDA)

> Objectif : améliorer l'observabilité et la maintenance après stabilisation fonctionnelle.
> Cette phase est volontairement positionnée en fin de roadmap.

#### 5.1 — Logs applicatifs

- [ ] Structurer les logs Django (niveau, format, contexte requête)
- [ ] Centraliser les logs (solution à décider : Railway, Grafana stack, autre)
- [ ] Définir une politique de rétention adaptée

#### 5.2 — Monitoring technique

- [ ] Mettre en place des checks de santé (app + DB)
- [ ] Suivre des métriques minimales : erreurs 5xx, latence, disponibilité
- [ ] Configurer des alertes (mail/Slack) sur incidents critiques

#### 5.3 — Monitoring produit

- [ ] Définir 2 à 3 KPI d'usage utiles (ex: pauses créées, taux de complétion)
- [ ] Ajouter un tableau de bord de suivi simple

---

## Informations à collecter

| Information                                                 | Statut                        |
| ----------------------------------------------------------- | ----------------------------- |
| Détails de la nouvelle charte graphique (couleurs, typos)   | ⚠️ En cours de définition     |
| Stratégie composants design system (maison + librairie)     | ✅ Validée (approche hybride) |
| URL du repo front Vue.js                                    | ❌ À créer                    |
| Contraintes de délai pour la formation CDA                  | ❌ À préciser                 |
| Décision stockage JWT : `httpOnly cookie` vs `localStorage` | ❌ À décider (phase 3)        |
| Stack logs/monitoring retenue                               | ❌ À décider (phase 5)        |

---

## Principes directeurs (non négociables)

- **Production continue** : jamais de coupure, toujours une version stable sur `main`
- **Tests avant tout** : on ne livre pas de fonctionnalité sans test
- **Staging obligatoire** : toute évolution passe par staging avant `main`
- **Sécurité by design** : CORS, JWT, validation des données, audit de dépendances
- **Documentation officielle** : Django, DRF, Vue.js, TypeScript — pas de tutos douteux
- **Gitflow** : `main` / `dev` / `feature/<nom>` — commits conventionnels
