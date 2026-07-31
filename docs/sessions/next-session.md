# Prochaine session — Objectifs

> Source de vérité pour la prochaine étape de travail. À mettre à jour à la fin de
> chaque session.

## Session #21 — 21 août 2026 — Intégration du parcours de pratique

### Contexte

La session #20 du 31 juillet 2026 a préparé le socle front du parcours de
pratique :

- le parcours anonyme et le parcours authentifié ont été clarifiés ;
- le brouillon est conservé dans Pinia pendant la navigation, sans persistance
  navigateur pour le moment ;
- le module API `src/api/practice.ts` regroupe les types et appels liés aux
  catalogues Feelings/Needs, à la création de pauses et au compteur anonyme ;
- le store `src/stores/practice.ts` contient le brouillon, les sélections, le
  titre, le mode de pratique, les états d'envoi et la reprise après
  authentification ;
- `npm run type-check` et `npm run lint` sont verts ;
- la confirmation native `beforeunload` à prévoir en cas de rechargement avec un
  brouillon est documentée dans la roadmap.

La prochaine session reprend le plan d'intégration page par page. Le Dashboard
et l'adaptation desktop restent volontairement en dehors du périmètre immédiat.

### Objectif 1 — Brancher les premières étapes au store

- [ ] Relier `EmptyYourBagView` à `draft.emptyYourBag`.
- [ ] Relier `ObservationView` à `draft.observation`.
- [ ] Vérifier que le retour en arrière conserve les valeurs saisies.
- [ ] Définir le comportement d'une arrivée directe sur une étape sans parcours
      démarré.

### Objectif 2 — Implémenter Sentiments et Besoins

- [ ] Charger les catalogues via `getFeelings()` et `getNeeds()`.
- [ ] Remplacer les `textarea` provisoires par des boutons de sélection multiple.
- [ ] Stocker uniquement les identifiants sélectionnés dans Pinia.
- [ ] Afficher les états de chargement, d'erreur et d'absence de données.
- [ ] Brancher `useGender()` pour choisir le label genré des sentiments.
- [ ] Empêcher la progression sans au moins un sentiment et un besoin.

### Objectif 3 — Finaliser `PauseView`

- [ ] Transformer `PauseView` en page de résumé du brouillon.
- [ ] Ajouter le champ de titre modifiable et gérer le titre par défaut du back
      lorsqu'il est laissé vide.
- [ ] Pour un utilisateur connecté, envoyer le payload via `createPause()`.
- [ ] Pour un utilisateur anonyme, proposer la création d'un compte pour
      enregistrer la pause.
- [ ] Conserver le brouillon lors de l'inscription et de la connexion
      automatique.
- [ ] Reprendre l'envoi après authentification et empêcher les doubles envois.
- [ ] Prévoir une fin anonyme explicite avec appel du compteur sans envoyer le
      contenu de la pause.
- [ ] Conserver le brouillon en cas d'erreur API et permettre un nouvel essai.
- [ ] Vider le brouillon uniquement après succès ou fin anonyme explicite.

### Objectif 4 — Ajouter le Journal

- [ ] Ajouter les fonctions API de liste des pauses et, si nécessaire, de détail.
- [ ] Créer la route et la vue Journal protégées par authentification.
- [ ] Afficher les pauses créées avec leur titre et leur date.
- [ ] Afficher un lien vers le détail de chaque pause.
- [ ] Rediriger vers le Journal après création réussie depuis `PauseView`.

### Objectif 5 — Prévenir la perte du brouillon

- [ ] Ajouter `beforeunload` uniquement lorsqu'un brouillon contient des données.
- [ ] Vérifier le comportement sur un rechargement mobile et desktop.
- [ ] Ne pas ajouter de persistance `localStorage` ou `sessionStorage` dans cette
      étape.

### Objectif 6 — Vérifications

- [ ] Ajouter les tests ciblés du store : sélection, validation, réinitialisation,
      soumission authentifiée, soumission anonyme et conservation après erreur.
- [ ] Lancer `npm run type-check`.
- [ ] Lancer `npm run lint`.
- [ ] Lancer `npm run build`.
- [ ] Vérifier manuellement le parcours anonyme sur mobile.
- [ ] Vérifier manuellement le parcours création de compte → sauvegarde → Journal.
- [ ] Mettre à jour les documents de session en fin de travail.

### Limites de la prochaine session

- Ne pas finaliser le Dashboard avant la stabilisation du parcours de pratique.
- Ne pas ajouter de logique métier durable côté front si elle appartient au back.
- Ne pas persister le brouillon dans `localStorage` ou `sessionStorage`.
- Ne pas viser l'adaptation desktop complète au-delà de la vérification du
  parcours.
- Ne pas créer d'abstraction générique sans besoin observé dans plusieurs vues.
