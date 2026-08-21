# Prochaine session — Objectifs

> Source de vérité pour la prochaine étape de travail. À mettre à jour à la fin de
> chaque session.

## Session #22 — Date à planifier — Finalisation du parcours de pratique

### Contexte

La session #21 du 21 août 2026 a intégré les premières étapes du parcours de
pratique :

- `EmptyYourBagView` et `ObservationView` sont reliées au brouillon Pinia ;
- `FeelingsView` et `NeedsView` chargent leurs catalogues via l'API front ;
- les sentiments et besoins utilisent une sélection multiple par familles ;
- seules les listes d'identifiants `feelingIds` et `needIds` sont stockées dans
  Pinia ;
- les états de chargement, d'erreur et d'absence de données sont affichés ;
- la progression est bloquée tant qu'aucune sélection n'a été faite dans l'étape
  courante ;
- un changement local non committé dans `pauses/api/serializers.py` expose les
  familles sous le champ `family`, attendu par le front.

La prochaine session doit d'abord isoler et committer proprement le changement
back Feelings/Needs dans une branche back dédiée, puis reprendre la fin du
parcours front. Le Dashboard et l'adaptation desktop restent volontairement en
dehors du périmètre immédiat.

### Objectif 1 — Stabiliser le contrat Feelings/Needs côté back

- [ ] Créer une branche back dédiée pour le changement de serializers
      Feelings/Needs.
- [ ] Vérifier que `FeelingSerializer` expose `id`, `family`, `names`.
- [ ] Vérifier que `NeedSerializer` expose `id`, `family`, `name`.
- [ ] Ajouter ou adapter les tests back du contrat Feelings/Needs si nécessaire.
- [ ] Lancer les tests back ciblés sur les endpoints Feelings/Needs.
- [ ] Committer le changement back dans cette branche dédiée.

### Objectif 2 — Terminer Sentiments et Besoins côté front

- [ ] Brancher `useGender()` pour choisir le label genré des sentiments.
- [ ] Vérifier que le retour en arrière conserve les textes et les sélections.
- [ ] Définir le comportement d'une arrivée directe sur une étape sans parcours
      démarré.
- [ ] Vérifier le comportement d'erreur lorsque les catalogues ne chargent pas.

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
- [ ] Ajouter des tests ciblés pour les comportements directs de vues si un outil
      de test front adapté est déjà en place.
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
