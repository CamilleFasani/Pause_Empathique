# Plan de tests — API Pauses

> Rédigé avant l'implémentation (approche TDD).
> Ce document fait partie du dossier de certification CDA (RNCP6).

---

## 1. Contexte fonctionnel

Les endpoints Pauses couvrent la fonctionnalité centrale de l'application : la **pause empathique**.

Une pause empathique est un processus guidé en 4 étapes :
1. Vide ton sac
2. Observation
3. Sentiments
4. Besoins

À l'issue du processus, un résumé de la pause est affiché à l'utilisateur.

Cette fonctionnalité est accessible de deux manières :
- **Utilisateur connecté** : la pause est sauvegardée en base de données, liée à son compte.
- **Utilisateur anonyme** : la progression est stockée côté client (sessionStorage) pendant la session ; la préférence de genre est également stockée côté client. Seul un compteur anonyme est envoyé au serveur en fin de pause.

---

## 2. Endpoints couverts

| Méthode | URL | Description | Auth JWT requise |
|---|---|---|---|
| GET | `api/v1/pauses/` | Liste de toutes les pauses de l'utilisateur | Oui |
| POST | `api/v1/pauses/` | Créer une pause | Oui |
| GET | `api/v1/pauses/<id>/` | Détail d'une pause | Oui |
| PATCH | `api/v1/pauses/<id>/` | Modifier une pause (partiel) | Oui |
| DELETE | `api/v1/pauses/<id>/` | Supprimer une pause | Oui |
| POST | `api/v1/pauses/anonymous` | Incrémenter le compteur anonyme | Non |

---

## 3. Cas de tests

### Légende

- **Nominal** : flux attendu, tout va bien
- **Limite** : données aux bornes de la validation
- **Erreur** : cas de rejet ou d'accès interdit

---

### 3.0 Tests unitaires — Serializers

#### Sérialisation (lecture — on donne une instance au serializer, on vérifie le format de sortie)

| ID | Description | Données d'entrée | Résultat attendu | Type |
|---|---|---|---|---|
| SER-01 | Structure `names` des feelings | Pause avec 1 feeling (`feminine_name: "submergée"`, `masculine_name: "submergé"`) | `feelings[0].names == {"f": "submergée", "m": "submergé"}` | Nominal |
| SER-02 | Structure `name` des needs | Pause avec 1 need (`name: "sécurité"`) | `needs[0].name == "sécurité"` | Nominal |
| SER-03 | Champ `user` absent de la réponse | Pause avec un user | La clé `user` n'apparaît pas dans `serializer.data` | Nominal |
| SER-04 | _Supprimé — feelings et needs sont désormais requis_ | — | — | — |
| SER-05 | Tous les champs attendus sont présents | Pause complète | La réponse contient exactement : `id`, `title`, `created_at`, `updated_at`, `empty_your_bag`, `observation`, `feelings`, `needs` | Nominal |

#### Validation (écriture — on donne un `data={}`, on vérifie `is_valid()`)

| ID | Description | Données d'entrée | Résultat attendu | Type |
|---|---|---|---|---|
| SER-06 | Données valides minimales | `feelings: [id]`, `needs: [id]` | `is_valid() == True` | Nominal |
| SER-07 | Titre auto-généré si absent | Pas de `title` dans `data` | `is_valid() == True`, titre au format "Pause du JJ Mois AAAA" | Nominal |
| SER-08 | Titre dépasse 200 caractères | `title` de 201 caractères | `is_valid() == False`, erreur sur `title` | Limite |
| SER-09 | Feelings et needs absents → rejet | Ni `feelings` ni `needs` | `is_valid() == False`, erreur sur `feelings` et `needs` | Erreur |

---

### 3.1 `GET /api/v1/pauses/` — Liste

| ID | Description | Préconditions | Résultat attendu | Type |
|---|---|---|---|---|
| LST-01 | Lister ses pauses | User A connecté, 3 pauses en base | 200, liste de 3 pauses avec `id`, `title`, `created_at`, `updated_at`, `empty_your_bag`, `observation`, `feelings`, `needs` | Nominal |
| LST-02 | Aucune pause | User A connecté, 0 pause en base | 200, liste vide `[]` | Limite |
| LST-03 | Isolation des données | User A connecté, user B a 10 pauses en base | 200, liste vide `[]` pour user A | Erreur |
| LST-04 | Pas de token | Requête sans header Authorization | 401 | Erreur |
| LST-05 | Token invalide/expiré | Token JWT invalide ou expiré | 401 | Erreur |

---

### 3.2 `POST /api/v1/pauses/` — Création

| ID | Description | Préconditions | Données d'entrée | Résultat attendu | Type |
|---|---|---|---|---|---|
| CRE-01 | Créer une pause complète | User connecté | `title`, `empty_your_bag`, `observation`, `feelings: [ids]`, `needs: [ids]` | 201, objet pause créé (avec `id` généré) | Nominal |
| CRE-02 | Champ requis manquant | User connecté | Champ(s) requis absent(s) | 400, message d'erreur indiquant le champ manquant | Erreur |
| CRE-03 | Feeling ID inexistant | User connecté | `feelings: [9999]` | 400, message d'erreur | Erreur |
| CRE-04 | Titre dépasse 200 caractères | User connecté | `title` de 201+ caractères | 400, message d'erreur | Limite |
| CRE-05 | Pas de token | Requête sans auth | Corps valide | 401 | Erreur |
| CRE-06 | L'identité vient du token, pas du body | User A connecté | `user: <id_user_B>` dans le body | 201, pause créée pour user A (le champ `user` du body est ignoré) | Erreur |

---

### 3.3 `GET /api/v1/pauses/<id>/` — Détail

| ID | Description | Préconditions | Résultat attendu | Type |
|---|---|---|---|---|
| DET-01 | Consulter sa propre pause | User A connecté, pause appartient à user A | 200, objet complet (`id`, `title`, `created_at`, `updated_at`, `empty_your_bag`, `observation`, `feelings`, `needs`) | Nominal |
| DET-02 | ID inexistant | User A connecté, aucune pause avec cet ID | 404 | Erreur |
| DET-03 | Isolation — pause d'un autre utilisateur | User A connecté, pause appartient à user B | 404 | Erreur |
| DET-04 | Pas de token | Requête sans header Authorization | 401 | Erreur |
| DET-05 | Token invalide/expiré | Token JWT invalide ou expiré | 401 | Erreur |

---

### 3.4 `PATCH /api/v1/pauses/<id>/` — Modification partielle

| ID | Description | Préconditions | Données d'entrée | Résultat attendu | Type |
|---|---|---|---|---|---|
| UPD-01 | Modifier le titre | User A connecté, pause de user A | `title: "Nouveau titre"` | 200, objet pause mis à jour (tous les champs) | Nominal |
| UPD-02 | Modifier les feelings | User A connecté, pause de user A | `feelings: [1, 2]` | 200, M2M mis à jour | Nominal |
| UPD-03 | Titre dépasse 200 caractères | User A connecté, pause de user A | `title` de 201+ caractères | 400, message d'erreur | Limite |
| UPD-04 | Feeling ID inexistant | User A connecté, pause de user A | `feelings: [9999]` | 400, message d'erreur | Erreur |
| UPD-05 | ID de pause inexistant | User A connecté | Corps valide | 404 | Erreur |
| UPD-06 | Isolation — modifier la pause d'un autre | User A connecté, pause appartient à user B | Corps valide | 404 | Erreur |
| UPD-07 | Pas de token | Requête sans auth | Corps valide | 401 | Erreur |
| UPD-08 | Token invalide/expiré | Token JWT invalide ou expiré | Corps valide | 401 | Erreur |

---

### 3.5 `DELETE /api/v1/pauses/<id>/` — Suppression

| ID | Description | Préconditions | Résultat attendu | Type |
|---|---|---|---|---|
| DEL-01 | Supprimer sa propre pause | User A connecté, pause appartient à user A | 204, pause absente en base | Nominal |
| DEL-02 | ID inexistant | User A connecté, aucune pause avec cet ID | 404 | Erreur |
| DEL-03 | Isolation — supprimer la pause d'un autre | User A connecté, pause appartient à user B | 404 | Erreur |
| DEL-04 | Pas de token | Requête sans auth | 401 | Erreur |
| DEL-05 | Token invalide/expiré | Token JWT invalide ou expiré | 401 | Erreur |

---

### 3.6 `POST /api/v1/pauses/anonymous` — Compteur anonyme

| ID | Description | Préconditions | Résultat attendu | Type |
|---|---|---|---|---|
| ANO-01 | Incrémenter le compteur anonyme | Pas d'authentification | 200, compteur incrémenté | Nominal |
| ANO-02 | Utilisateur connecté interdit | Token JWT valide | 403, accès refusé | Erreur |

---

## 4. Critères de validation

| Critère | Seuil | Justification |
|---|---|---|
| Tests de sécurité et d'isolation (LST-03, DET-03, UPD-06, DEL-03, CRE-06, ANO-02) | 100 % passent | Une faille d'isolation = accès aux données d'un autre utilisateur. Aucune tolérance. |
| Tests nominaux | 100 % passent | Le fonctionnement de base de l'API doit être garanti. |
| Couverture de code (app `pauses`) | ≥ 80 % | Seuil défini pour le projet global. |
| CI verte sur `feature/pauses-api` | Obligatoire | Aucun merge vers `dev` sans pipeline verte (lint + audit + tests). |
