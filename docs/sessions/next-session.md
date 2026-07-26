# Prochaine session — Objectifs

> Source de vérité pour la prochaine étape de travail. À mettre à jour à la fin de
> chaque session.

## Session #20 — 31 juillet 2026 — Dashboard et parcours de pratique

### Contexte

La session #19 du 24 juillet 2026, clôturée le 26 juillet, a terminé la
sécurisation de l'authentification :

- le back `feat/secure-authentication` est mergé dans `dev` ;
- le front `feat/secure-authentication` est mergé dans `dev` ;
- le refresh token est stocké en cookie `HttpOnly` côté Django ;
- l'access token reste en mémoire côté Vue/Pinia ;
- le refresh automatique, la restauration de session et le logout ont été
  vérifiés manuellement ;
- le développement local utilise `/api/v1` avec proxy Vite vers Django pour
  éviter les problèmes de transport du cookie entre origins.

La prochaine session démarre une nouvelle étape fonctionnelle : reprendre le
Dashboard et construire progressivement le parcours de pratique.

### Objectif 0 — Préparer les branches

- [ ] Créer une nouvelle branche documentation côté back depuis `dev`.
- [ ] Créer une nouvelle branche front depuis `dev` pour le Dashboard et le
  parcours de pratique.
- [ ] Vérifier que les deux dépôts sont bien à jour avec `dev` avant de coder.

### Objectif 1 — Cadrer le Dashboard

- [ ] Relire l'état actuel des vues et composants front existants.
- [ ] Définir le rôle exact du Dashboard dans la V2 :
  - accueil authentifié ;
  - accès au parcours de pratique ;
  - accès futur au journal des pauses ;
  - état vide pour une utilisatrice sans pause.
- [ ] Identifier les données nécessaires côté API et ce qui peut rester statique
  dans cette première itération.
- [ ] Définir les routes protégées attendues.

### Objectif 2 — Finaliser le layout applicatif

- [ ] Stabiliser le layout des pages connectées : header, sidebar, footer et
  contenu principal.
- [ ] Vérifier les comportements mobile et desktop.
- [ ] S'assurer que les routes protégées utilisent le bon layout.
- [ ] Garder les composants centrés sur le rendu, avec la logique partagée dans
  stores/composables si nécessaire.

### Objectif 3 — Démarrer le parcours de pratique

- [ ] Reprendre le parcours depuis l'entrée Welcome : pratique anonyme ou
  pratique avec compte.
- [ ] Construire l'étape Dashboard → début de pratique.
- [ ] Créer ou compléter les premières vues du parcours :
  - observation ;
  - sentiments ;
  - besoins.
- [ ] Préparer la circulation des données entre étapes sans dupliquer les règles
  métier du back.
- [ ] Identifier précisément quand les endpoints Feelings/Needs et Pauses sont
  consommés.

### Objectif 4 — Vérifications

- [ ] Lancer `npm run type-check`.
- [ ] Lancer `npm run lint`.
- [ ] Lancer `npm run build`.
- [ ] Vérifier manuellement les routes principales sur mobile et desktop.
- [ ] Mettre à jour les documents de session en fin de travail.

### Limites de la prochaine session

- Ne pas ajouter de nouvelle logique métier durable côté front si elle appartient
  au back.
- Ne pas démarrer le journal complet des pauses avant d'avoir stabilisé le
  Dashboard et le début du parcours.
- Ne pas créer de nouvelle abstraction générique tant que le besoin n'est pas
  visible dans au moins deux écrans.
