# Prochaine session — Objectifs

> Ce fichier est lu en priorité par Copilot au démarrage de chaque session.
> Mis à jour en fin de session avec les objectifs suivants.

---

## Session #10 — 10 avril 2026 ✅ COMPLÉTÉE

### Bilan

- [x] Objectif 1 — Ruff S106 débloqué : `per-file-ignores` dans `pyproject.toml`
- [x] Objectif 2 — `UserMeAPITest` relu et validé (40 tests passent)
- [x] Objectif 3 — `LoginAPITest` + `LogoutAPITest` écrits avec vrais tokens JWT
- [x] Objectif 4 — Couverture 87% (seuil 80% atteint)
- [x] Merge `feature/authentication` → `dev` (CI verte requise)
- [x] Branche `feature/pauses-api` créée

---

## Session #11 — 10 avril 2026 ✅ COMPLÉTÉE

### Bilan

- [x] Brainstorm architecture endpoints pauses (utilisateurs anonymes + connectés)
- [x] Décision : sauvegarde en fin de pause uniquement (pas progressive)
- [x] Décision : données anonymes stockées côté client (sessionStorage) pendant la session

### Décisions prises

- **Flux anonyme :** toutes les données de la pause sont stockées dans `sessionStorage` côté front pendant la session. Aucune donnée n'est envoyée au serveur avant la décision de sauvegarder.
- **Fin de pause :** l'utilisateur voit un récap (construit depuis sessionStorage), puis choisit de sauvegarder (→ création de compte + `POST /api/v1/pauses/`) ou non (→ `POST /api/v1/pauses/anonymous` pour incrémenter le compteur uniquement).
- **Sauvegarde progressive abandonnée** pour tous les utilisateurs (anonymes et connectés) : 1 seul `POST` en fin de pause, même logique partout.
- **Fermeture navigateur en cours de pause** = données perdues, comportement voulu.

---

## Session #12 — 17 avril 2026

### Contexte

Session #11 (10 avril) : architecture endpoints pauses cadrée, décisions prises avant implémentation.

- Architecture flux anonyme + connecté définie ✅
- Sauvegarde en fin de pause (1 seul POST) retenue ✅
- Plan de tests Pauses non encore rédigé (reporté à cette session)

---

### Question ouverte à trancher en début de session

**Sentiments genrés — où filtrer ?**

Le modèle `Feeling` expose `feminine_name` et `masculine_name`. Pour le front Vue (futur), deux options :

- **Option A — filtrer côté back :** l'API retourne un seul champ `label` selon le genre de l'utilisateur
- **Option B — envoyer les deux au front :** l'API retourne `feminine_name` + `masculine_name`, le front choisit

**Cas bloquant :** l'utilisateur non connecté n'a pas de genre connu. Faut-il demander son genre en début de pause anonyme ?

→ **À trancher avant d'écrire le serializer.**

---

### Objectifs de la session

#### Objectif 0 — Trancher la question du genre pour les sentiments

- [ ] Décider : filtrage côté back ou envoi des deux formes au front
- [ ] Décider : demande du genre en début de pause anonyme, ou genre neutre par défaut

#### Objectif 1 — Rédiger le plan de tests Pauses (dossier CDA)

- [ ] Rédiger le plan de tests formalisé avant d'écrire le code
- [ ] Couvrir : cas nominaux, cas limites, cas d'erreur pour list/create/retrieve/update/delete
- [ ] Intégrer le flux anonyme dans le plan (POST sans auth + POST /pauses/anonymous)
- [ ] Valider le plan avant implémentation

#### Objectif 2 — Serializer Pause

- [ ] Créer `PauseSerializer` dans `pauses/api/serializers.py`
- [ ] Champs : `id`, `title`, `created_at`, `feelings`, `needs`
- [ ] Écrire les tests unitaires du serializer

#### Objectif 3 — Endpoints Pauses

- [ ] `GET /api/v1/pauses/` — liste des pauses de l'utilisateur connecté
- [ ] `POST /api/v1/pauses/` — créer une pause complète (fin de session)
- [ ] `POST /api/v1/pauses/anonymous` — incrémenter le compteur anonyme
- [ ] `GET /api/v1/pauses/<id>/` — détail d'une pause
- [ ] `PATCH /api/v1/pauses/<id>/` — modifier une pause
- [ ] `DELETE /api/v1/pauses/<id>/` — supprimer une pause
- [ ] Vérifier l'isolation : un utilisateur ne peut pas accéder aux pauses d'un autre

#### Objectif 4 — Tests d'intégration Pauses

- [ ] Tests CRUD complets selon le plan de tests rédigé en Objectif 1
- [ ] Couverture `pauses` maintenue ≥ 80%

---

### Rappels du chef de projet

- Le plan de tests doit être rédigé **avant** le code (pas après)
- Toujours tester l'isolation des données entre utilisateurs
- CI verte obligatoire avant merge `feature/pauses-api` → `dev`
- Trancher la question du genre **avant** d'écrire le serializer
