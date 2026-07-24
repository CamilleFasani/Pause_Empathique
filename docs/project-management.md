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

## État actuel — Juillet 2026

- ✅ Application Django full stack fonctionnelle en production (`pause-empathique.fr`)
- ✅ Authentification par sessions Django (templates)
- ✅ CI/CD GitHub Actions (lint Ruff + tests Django via Docker)
- ✅ Job CI sécurité dépendances (`pip-audit`) ajouté
- ✅ Déploiement Railway (branche `main`)
- ✅ Environnement staging Railway opérationnel (`staging.pause-empathique.fr`) avec déploiement automatique sur `dev`
- ✅ Modèles : User, Pause, Feeling, Need
- ✅ CRUD complet sur les pauses
- ✅ Couverture de tests mesurée via `pytest-cov` (seuil 80 % à atteindre)
- ✅ CVE-2026-4539 (pygments) corrigée — mise à jour 2.20.0 mergée sur `dev`
- ✅ `pre-commit` local en place (Ruff + hooks qualité)
- ✅ Outil de documentation API validé : `drf-spectacular`
- ✅ Vérification des contrastes accessibilité (niveau AA) validée sur la palette actuelle
- ✅ Captures d'écran réalisées pour le dossier projet
- ✅ Stratégie de transition actée : V1 maintenue en production, V2 travaillée sur staging
- ✅ Endpoints auth API implémentés : register, login, refresh, logout, profil (GET/PATCH/DELETE)
- ✅ Tests API auth et login/logout écrits
- ✅ Socle du front Vue opérationnel : Router, Pinia, client Axios et connexion à
  l'API
- ✅ Vues de connexion et d'inscription réalisées et branchées au store auth
- ✅ Page Welcome et layout d'authentification réalisés
- ✅ Choix authentification/pratique anonyme intégré directement à Welcome et
  relié aux routes correspondantes
- 🚧 Layouts applicatifs seulement partiellement réalisés
- 🚧 Authentification sécurisée implémentée sur les branches dédiées : access
  token en mémoire côté front et refresh token en cookie `HttpOnly` côté back ;
  validation navigateur et merges encore requis
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
- [x] Corriger `CVE-2026-4539` (pygments) — mise à jour 2.20.0, CI verte sur `dev`
- [ ] Valider que staging/prod utilisent des images de déploiement adaptées (runtime sans dépendances dev inutiles)

#### 0.4 — Pre-commit hooks

- [x] Installer et configurer `pre-commit` localement
- [x] Hooks : `ruff check` + `ruff format` avant chaque commit

---

### Phase 1 — Nouvelle charte graphique 🚧 EN COURS

> Objectif : poser une base solide de charte graphique (tokens + direction visuelle) sans refonte complète des templates Django.
> La V1 reste en production ; la V2 est travaillée et validée sur staging.

- [x] Définir la charte : couleurs, typographies, composants (base v1.0)
- [x] Configurer Tailwind v4 avec les variables CSS natives dans `input.css`
- [x] Appliquer la charte uniquement sur des vues pilotes (pas de refonte complète des templates Django)
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
- [x] Configurer les endpoints JWT : `api/v1/auth/token/`, `api/v1/auth/token/refresh/`
- [x] Configurer CORS (`django-cors-headers`) pour le futur front Vue.js

#### 2.2 — Endpoints par ressource

Pour chaque ressource, créer serializer + viewset + URL avant de migrer le front :

- [x] **Auth** : register, login (JWT), logout, profil (GET/PATCH), suppression de compte — mergé dans `dev`
- [x] **Pauses** : list, create, retrieve, update, delete — mergé dans `dev` (session #13)
- [x] **Feelings** : `GET /api/v1/feelings/` — `FeelingsListView`, `AllowAny`, `pagination_class = None` — session #15
- [x] **Needs** : `GET /api/v1/needs/` — `NeedsListView`, `AllowAny`, `pagination_class = None` — session #15

**Décisions d'architecture API — Feelings/Needs (session #12, 17 avril 2026) :**

- `Feeling` expose les deux formes genrées sous une structure imbriquée : `"names": {"f": "submergée", "m": "submergé"}` — le front choisit la forme à afficher selon le genre connu (connecté : profil utilisateur ; anonyme : choix en début de pause stocké en `sessionStorage`).
- `Need` n'a pas de genre : un seul champ `name` dans le serializer.
- La logique d'affichage genré est centralisée côté front dans un composable `useGender()` (voir Phase 3). Ne pas dupliquer cette logique dans les composants Vue.

#### 2.3 — Tests API

- [x] Tests auth : RegisterSerializerTest, RegisterAPITest, UserMeAPITest écrits
- [x] Tests login/logout : LoginAPITest + LogoutAPITest écrits avec vrais tokens JWT — couverture users 87%
- [x] **Plan de tests Pauses** rédigé : `docs/test-plan-pauses-api.md` (6 endpoints + SER-01..SER-09) — session #12
- [x] Tests unitaires serializer Pause : `pauses/tests/test_serializers.py` (8 tests) — session #12
- [x] Tests d'intégration Pauses (CRUD) : `pauses/tests/test_api_pauses.py` (28 tests) — session #12 (TDD, phase red) → **verts en session #13**
- [x] Tests anonymes (ANO-01, ANO-02) — après conception du compteur (session #14)
- [x] Tests Feelings, Needs — FEE-01/02 + NEE-01/02 dans `test_api_pauses.py` — session #15
- [x] Couverture `pauses` ≥ 80 % — **100 %** — session #15

#### 2.4 — Documentation API

- [ ] Stabiliser et compléter le schéma OpenAPI (serializers, exemples, erreurs)
- [ ] Valider la doc Swagger / Redoc en staging avant migration front complète

#### 2.5 — Suppression des templates Django

- [ ] Une fois le front Vue.js validé en staging, supprimer les templates
- [ ] Nettoyer les dépendances front-only (django-widget-tweaks, django-browser-reload)

---

### Phase 3 — Frontend Vue.js + TypeScript 🚧 EN COURS

> Objectif : SPA Vue.js 3 consommant l'API DRF, déployée séparément.

#### 3.1 — Setup du repo front

- [x] Créer un nouveau repo GitHub `pause-empathique-front`
- [x] Initialiser avec Vite + Vue.js 3 + TypeScript — session #15
- [x] Configurer Tailwind CSS v4 — session #15
- [x] Configurer le linter (ESLint + Prettier) — session #15
- [x] CI/CD : lint + type-check + build check — session #15

#### 3.1.1 — Composable `useGender()`

- [ ] Créer un composable `useGender()` qui centralise la résolution du genre à afficher
  - Utilisateur connecté → genre depuis le store Pinia (profil)
  - Utilisateur anonyme → genre depuis `sessionStorage` (choix en début de pause)
- [ ] Ce composable est l'unique point d'accès au genre dans toute l'application Vue
- [ ] Utilisation : `const label = feeling.names[gender]`

#### 3.2 — Authentification

- [x] Créer les vues et formulaires de connexion/inscription avec validation
- [x] Brancher connexion et inscription au store Pinia et à l'API
- [x] Mettre en place une première gestion JWT (access, refresh, restauration de
      session et logout)
- [x] Ajouter une première garde de navigation pour les routes protégées
- [ ] Remplacer le refresh token stocké dans `localStorage` par une stratégie de
      cookies sécurisés — session dédiée prévue le 17 juillet 2026
- [x] Définir et documenter le contrat complet : `HttpOnly`, `Secure`, `SameSite`,
      CSRF, rotation/expiration du refresh et logout
- [ ] Adapter et tester le back-end DRF, Axios et le store Pinia selon ce contrat

#### 3.2.1 — Entrée dans le parcours

- [x] Créer la page publique Welcome
- [x] Intégrer directement à Welcome les choix authentification ou pratique anonyme
- [x] Relier chaque choix à son parcours par un lien Vue Router
- [ ] Merger `feat/-base-layout-and-auth-views` dans `dev` après validation qualité

**Décision d'architecture auth sécurisée — 17 juillet 2026 :**

- L'`access token` JWT est court, renvoyé dans la réponse JSON au login et au
  refresh, puis conservé uniquement en mémoire côté Vue/Pinia.
- Le `refresh token` JWT est long, sensible, et ne doit jamais être stocké dans
  `localStorage` ni renvoyé au front dans le JSON après migration.
- Le `refresh token` est stocké par Django dans un cookie `HttpOnly`, afin de le
  rendre illisible par le JavaScript du navigateur et de réduire l'impact d'une
  faille XSS.
- Le cookie de refresh doit être configuré explicitement avec `HttpOnly`,
  `Secure`, `SameSite`, une expiration alignée sur la durée de vie du refresh
  token, et un `path` limité aux endpoints d'authentification si possible.
- En staging et production, le cookie doit être envoyé uniquement en HTTPS
  (`Secure=True`). En développement local, une configuration adaptée peut être
  utilisée pour permettre les tests en HTTP.
- Le choix `SameSite` dépend du déploiement front/API :
  - `Lax` si le front et l'API restent dans un contexte same-site compatible ;
  - `None; Secure` si le front et l'API sont considérés cross-site par le
    navigateur.
- Pour cette étape, la protection CSRF des endpoints refresh/logout repose sur
  `SameSite=Lax`, sur un cookie limité au chemin `/api/v1/auth/`, et sur le fait
  que les endpoints métier restent authentifiés par `Authorization: Bearer
<access token>` plutôt que par cookie. `CSRF_TRUSTED_ORIGINS` reste nécessaire
  pour les flux Django soumis à la vérification CSRF, mais ne constitue pas seul
  une protection CSRF complète pour l'API JWT.
- Un jeton CSRF dédié côté SPA n'est pas ajouté dans cette étape. Il devra être
  réévalué avant staging/production si le front et l'API imposent
  `SameSite=None; Secure`, ou si des endpoints métier deviennent authentifiés par
  cookie.
- Le refresh automatique est déclenché par le client Axios uniquement quand
  l'`access token` a expiré ou qu'une requête protégée reçoit un `401`
  récupérable.
- Le client Axios doit éviter les boucles de refresh et coordonner les requêtes
  concurrentes pour ne pas lancer plusieurs refresh simultanés.
- Le logout doit invalider le refresh token côté serveur quand la blacklist
  Simple JWT est disponible, supprimer le cookie de refresh côté navigateur, et
  vider l'état auth côté front.
- En cas de refresh expiré, absent, invalide ou blacklisté, le front doit
  considérer la session terminée, vider son état local et rediriger vers le
  parcours de connexion si la route demandée est protégée.
- Le back-end reste l'autorité de sécurité : les guards Vue améliorent
  l'expérience utilisateur mais ne remplacent jamais les permissions DRF.

#### 3.3 — Migration vue par vue

Pour chaque vue Django existante, créer le composant Vue équivalent :

- [x] Login / Register
- [ ] Dashboard
- [ ] Observation (étape 1)
- [ ] Feelings (étape 2)
- [ ] Needs (étape 3)
- [ ] Diary (liste des pauses)
- [ ] Détail d'une pause
- [ ] Profil utilisateur

**Ordre de travail retenu en juillet 2026 :**

1. effectuer la dernière validation et merger la branche auth/layout actuelle ;
2. sécuriser l'authentification par cookies sur une nouvelle branche ;
3. regrouper Dashboard, layouts applicatifs et parcours de pratique sur une même
   branche fonctionnelle.

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

| Information                                               | Statut                                                                    |
| --------------------------------------------------------- | ------------------------------------------------------------------------- |
| Détails de la nouvelle charte graphique (couleurs, typos) | ⚠️ En cours de définition                                                 |
| Stratégie composants design system (maison + librairie)   | ✅ Validée (approche hybride)                                             |
| URL du repo front Vue.js                                  | ✅ Repo créé et initialisé                                                |
| Contraintes de délai pour la formation CDA                | ❌ À préciser                                                             |
| Orientation stockage JWT                                  | 🚧 Cookies sécurisés retenus ; contrat détaillé à concevoir le 17/07/2026 |
| Stack logs/monitoring retenue                             | ❌ À décider (phase 5)                                                    |

---

## Principes directeurs (non négociables)

- **Production continue** : jamais de coupure, toujours une version stable sur `main`
- **Tests avant tout** : on ne livre pas de fonctionnalité sans test
- **Staging obligatoire** : toute évolution passe par staging avant `main`
- **Sécurité by design** : CORS, JWT, validation des données, audit de dépendances
- **Documentation officielle** : Django, DRF, Vue.js, TypeScript — pas de tutos douteux
- **Gitflow** : `main` / `dev` / `feature/<nom>` — commits conventionnels
