# Prochaine session — Objectifs

> Ce fichier est lu en priorité par Copilot au démarrage de chaque session.
> Mis à jour en fin de session avec les objectifs suivants.

## Session #16 — à planifier

### Contexte

Session #15 (5 juin 2026) : validation finale back + préparation init front.

- Couverture globale **84 %** (81 tests au vert) ✅
- `pauses` API : couverture **100 %** ✅
- CI verte sur `dev` (confirmé) ✅
- Merge `feat/add-pauses-endpoints` → `dev` ✅
- Endpoints Feelings + Needs : **à faire** (voir Objectif 1 ci-dessous)
- Init repo front : **à faire** (voir Objectif 2 ci-dessous)

---

### Objectifs de la session

#### Objectif 1 — Endpoints Feelings + Needs

Les serializers `FeelingSerializer` et `NeedSerializer` existent déjà et sont utilisés en sortie des endpoints pauses. Mais le front a besoin d'endpoints dédiés pour **peupler les écrans de sélection** (étapes "choisis tes sentiments" et "choisis tes besoins") : un utilisateur sans aucune pause ne peut pas obtenir le catalogue autrement.

- [ ] Créer branche `feat/feelings-needs-endpoints`
- [ ] `FeelingListView` : `ListAPIView`, permission `AllowAny`, `GET /api/v1/feelings/`
- [ ] `NeedListView` : `ListAPIView`, permission `AllowAny`, `GET /api/v1/needs/`
- [ ] Câbler les URLs dans `pause_empathique/api/urls.py`
- [ ] Écrire au moins 2 tests (structure de réponse pour chaque endpoint)
- [ ] Merge → `dev`, CI verte

#### Objectif 2 — Initialisation du repo front

- [ ] `create-vite` avec template `vue-ts` dans `pause_empathique_front/`
- [ ] Configurer Tailwind CSS v4
- [ ] Configurer ESLint + Prettier
- [ ] CI GitHub Actions : lint + build check
- [ ] `.env.example` avec `VITE_API_URL`

---

### Rappels du chef de projet

- TDD strict : ne pas modifier un test pour qu'il passe sans en comprendre la raison
- CI verte obligatoire avant merge vers `dev`
