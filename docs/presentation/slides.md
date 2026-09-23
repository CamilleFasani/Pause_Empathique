---
theme: default
hideInToc: true
background: /cover.webp
title: Pause Empathique
info: |
  ## Pause Empathique
  Présentation du projet pour le titre de
  Concepteur Développeur d’Applications.

  Camille Fasani — Novembre 2026
class: text-center
drawings:
  persist: false
transition: slide-left
comark: true
duration: 40min
---
<!-- Photo de <a href="https://unsplash.com/fr/@mrkarlphoto?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Mr Karl</a>sur <a href="https://unsplash.com/fr/photos/photographie-de-vue-aerienne-du-desert-yFmh736pYsg?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a> -->

# Pause Empathique
<p class="title">Présentation au titre de Concepteur Développeur d'Applications</p>
<p class="signature">
  Camille Fasani - Novembre 2026
</p>


<style scoped>
  h1{
    color: var(--color-bg-page);
  }

  .signature {
  position: absolute;
  bottom: 2rem;
  left: 50%;
  transform: translateX(-50%);
  text-align: center;
  font-family: var(--font-logo);
  font-size: 1.1rem;
  color: var(--color-bg-page);
}

.title::before {
  content: "";
  display: block;
  width: 20rem;
  height: 1px;
  margin: 0 auto 0.8rem;
  background: var(--color-bg-page);
}
</style>
<!--
The last comment block of each slide will be treated as slide notes. It will be visible and editable in Presenter Mode along with the slide. [Read more in the docs](https://sli.dev/guide/syntax.html#notes)
-->

---
hideInToc: true
---

<div class="intro">
  <div class="intro-heading">
    <h1>Bonjour,<br>je suis <span>Camille Fasani.</span></h1>
    <p>J’apprends le développement web depuis janvier 2025.</p>
  </div>
  <ol class="intro-timeline" aria-label="Mon parcours de janvier 2025 à novembre 2026">
    <li style="--month: 0">
      <time class="intro-date" datetime="2025-01">Janvier 2025</time>
      <span class="intro-point" aria-hidden="true"></span>
    </li>
    <li style="--month: 9">
      <time class="intro-date" datetime="2025-10">Octobre 2025</time>
      <span class="intro-point" aria-hidden="true"></span>
      <p v-click="1" class="intro-event">Alternance <br> Développeuse full stack <br> chez <strong>cogito</strong></p>
    </li>
    <li style="--month: 12">
      <time class="intro-date" datetime="2026-01">Janvier 2026</time>
      <span class="intro-point" aria-hidden="true"></span>
      <p v-click="2" class="intro-event">Titre DWWM</p>
    </li>
    <li style="--month: 22">
      <time class="intro-date" datetime="2026-11">Novembre 2026</time>
      <span class="intro-point" aria-hidden="true"></span>
      <p v-click="3" class="intro-event">Titre CDA</p>
    </li>
  </ol>
</div>

<style scoped>
.intro {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  height: 100%;
  padding-top: 3rem;
}
.intro-heading h1 {
  margin: 1rem 0;
  font-size: 2.6rem;
  line-height: 1.2;
}
.intro-heading h1 span {
  text-decoration: underline;
  text-decoration-color: var(--color-brand-primary);
  text-decoration-thickness: 4px;
  text-underline-offset: 0.18em;
}
.intro-heading p {
  margin: 0;
  font-size: 1.05rem;
  opacity: 1;
}
.intro-timeline {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 50px;
  height: 185px;
  margin: 0;
  padding: 0;
  list-style: none;
}
.intro-timeline::before {
  content: "";
  position: absolute;
  top: 95px;
  left: 0;
  right: 0;
  height: 5px;
  background: var(--color-brand-primary);
  transform: translateY(-50%);
}
.intro-timeline li {
  position: absolute;
  top: 95px;
  left: calc(8% + var(--month) * 84% / 22);
  width: 0;
  margin: 0;
  padding: 0;
}
.intro-point {
  position: absolute;
  width: 18px;
  height: 18px;
  border: 4px solid var(--color-brand-primary);
  border-radius: 50%;
  background: var(--color-bg-card);
  transform: translate(-50%, -50%);
}
.intro-date {
  position: absolute;
  bottom: 22px;
  width: max-content;
  white-space: nowrap;
  transform: rotate(-45deg);
  transform-origin: left bottom;
  font-size: 0.8rem;
  text-align: center;
  line-height: 1.4;
  color: var(--color-black);
}
.intro-timeline .intro-event {
  position: absolute;
  top: 28px;
  width: 170px;
  margin: 0;
  transform: translateX(-30%);
  font-size: 0.9rem;
  font-weight: 600;
  line-height: 1.5;
  color: var(--color-black);
}
.intro-timeline li:nth-child(2) .intro-event {
  width: 225px;
  transform: translateX(-85%);
  text-align: right;
}
.intro-timeline li:nth-child(3) .intro-event {
  width: 140px;
  transform: translateX(-30%);
}
.intro-timeline li:last-child .intro-event {
  width: 150px;
  transform: translateX(-80%);
  text-align: right;
}
</style>


---
hideInToc: true
---

<div class="pe-heading">
  <img src="/logo.webp" alt="" />
  <h1>Sommaire</h1>
</div>

<Toc minDepth="1" maxDepth="1" />

---
layout: center
class: pe-section
---

# Pause Empathique, c'est quoi ?

<!--
Application web permet de pratiquer l'auto empathie en suivant un protocole inspiré de la Communication Non Violente, souvent appelé OSBD.
La CNV est une pratique qui permet de résoudre des conflits, de faire médiation, d'améliorer la communication dans nos relations pro, privées, citoyennes.  PE est dédiée à la pratique d'auto empathie, qui est une première étape pour aller ensuite parler à l'autre -->
---
class: pe-section-content
title: Concrètement ?
level: 2
---

# PE, c'est quoi ?

## Concrètement

<ol class="practice-steps">
  <li><span class="step-number" aria-hidden="true">01</span><span><strong>Vide ton sac</strong> : se décharger</span></li>
  <li><span class="step-number" aria-hidden="true">02</span><span><strong>Observation</strong> : décrire factuellement</span></li>
  <li><span class="step-number" aria-hidden="true">03</span><span><strong>Sentiments</strong> : déterminer ses émotions</span></li>
  <li><span class="step-number" aria-hidden="true">04</span><span><strong>Besoins</strong> : identifier ses besoins</span></li>
</ol>

<style scoped>
.practice-steps {
  display: grid;
  gap: 0.75rem;
  width: 50%;
  margin: 4rem auto 0;
  padding: 0;
  list-style: none;
}
.practice-steps li {
  display: flex;
  align-items: center;
  gap: 1.25rem;
  margin: 0;
  padding: 0.65rem 1.5rem;
  min-height: 3.4rem;
  border-radius: var(--radius-card);
  background: var(--color-bg-card);
  font-size: 1.1rem;
}
.step-number {
  flex: 0 0 2.3rem;
  color: var(--color-brand-primary);
  font-family: var(--font-logo);
  font-size: 1.65rem;
  font-weight: 700;
  line-height: 1;
}
</style>

---
class: pe-section-content
title: Concrètement ?
level: 2
---

# PE, c'est quoi ?

## Pourquoi

<!-- Quand on s'est formé à la CNV ce n'est pas facile de trouver avec qui pratiquer, et aussi de trouver une oreille attentive quand le besoin s'en fait sentir
Une application est disponible 24/24, permet de prendre le temps nécessaire à l'introspection sans enjeu relationnel -->
---
class: pe-section-content
title: Pour qui
level: 2
---

# PE, c'est quoi ?

## Pour qui

<div class="personae">
  <img src="/persona1.webp" alt ="" class="persona"/>
  <img src="/persona2.webp" alt ="" class="persona"/>
  <img src="/persona3.webp" alt ="" class="persona"/>
</div>
<style scoped>
.personae {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 2rem;
}
.persona {
  width: 130px;
  height: auto;
}
</style>

<!-- En premier lieu aux initiés à la CNV, mais on peut élargir à quiconque souhaite mieux de connaitre et gagner en discernement. Plutôt public féminin, peu technophile. -->

---
layout: default
class: pe-section
---

# Vers la V2


<!-- Souhait de partir de l'existant pour me rapprocher du travail en entreprise où l'on part rarement de zéro, donc travailler avec une code base,  et organiser une migration -->
---
class: pe-section-content
title: Objectifs
level: 2
---

# Vers la V2

## Objectifs

<div class="objectives">
  <section class="objective-card">
    <h3>PRODUIT</h3>
    <ul>
      <li>Refonte complète du design</li>
      <li>Ajout de nouvelles fonctionnalités</li>
    </ul>
  </section>
  <section class="objective-card">
    <h3>TECHNIQUE</h3>
    <ul>
      <li>Découplage front-back</li>
      <li>Maintien du service</li>
    </ul>
  </section>
</div>

<style>
.objectives {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1.25rem;
  margin: 4rem 0 0;
  padding: 0;
}

.objective-card {
  padding: 1.5rem;
  border-radius: var(--radius-card);
  background: var(--color-bg-card);
}

.objective-card h3 {
  margin: 0 0 1.25rem;
  padding-bottom: 0.75rem;
  border-bottom: 2px solid var(--color-brand-primary);
  font-size: 0.95rem;
  font-weight: 700;
  letter-spacing: 0.12em;
}

.objective-card ul {
  display: grid;
  margin: 0;
  padding: 0;
  list-style: none;
}

.objective-card li {
  display: flex;
  align-items: center;
  gap: 1rem;
  min-height: 4.5rem;
  margin: 0;
  padding: 0;
  font-size: 1.15rem;
  font-weight: 600;
}
</style>
---
class: pe-section
title: Gestion de projet
---

# Gestion de projet

<!-- Dire que j'étais seule sur le projet, à raison 1J/semaine  -->
---
class: pe-section-content
title: Diagramme de Gantt
level: 2
---

# Gestion de projet

## Diagramme de Gantt

<div class="gantt" role="group" aria-label="Planning de la roadmap Miro, regroupé en huit phases. Les dates ne représentent pas un relevé de réalisation.">
  <div class="gantt-header">
    <span class="gantt-column-label">PHASES DU PROJET</span>
    <div class="gantt-calendar">
      <div class="gantt-years"><span style="width: 15.4430%">2025</span><span>2026</span></div>
      <div class="gantt-months">
        <span style="width: 7.5949%">Nov.</span>
        <span style="width: 7.8481%">Déc.</span>
        <span style="width: 7.8481%">Jan.</span>
        <span style="width: 7.0886%">Fév.</span>
        <span style="width: 7.8481%">Mars</span>
        <span style="width: 7.5949%">Avr.</span>
        <span style="width: 7.8481%">Mai</span>
        <span style="width: 7.5949%">Juin</span>
        <span style="width: 7.8481%">Juil.</span>
        <span style="width: 7.8481%">Août</span>
        <span style="width: 7.5949%">Sept.</span>
        <span style="width: 7.8481%">Oct.</span>
        <span style="width: 7.5949%">Nov.</span>
      </div>
    </div>
  </div>
  <div class="gantt-body">
    <div class="gantt-grid" aria-hidden="true">
      <i style="left: 0.0000%"></i>
      <i style="left: 7.5949%"></i>
      <i style="left: 15.4430%"></i>
      <i style="left: 23.2911%"></i>
      <i style="left: 30.3797%"></i>
      <i style="left: 38.2278%"></i>
      <i style="left: 45.8228%"></i>
      <i style="left: 53.6709%"></i>
      <i style="left: 61.2658%"></i>
      <i style="left: 69.1139%"></i>
      <i style="left: 76.9620%"></i>
      <i style="left: 84.5570%"></i>
      <i style="left: 92.4051%"></i>
    </div>
    <div class="gantt-row">
      <span class="gantt-label">Conception produit</span>
      <div class="gantt-track"><span class="gantt-bar" style="left: 1.2658%; width: 31.1392%" role="img" aria-label="Conception produit : du 06/11/2025 au 08/03/2026" title="Conception produit : du 06/11/2025 au 08/03/2026"></span></div>
    </div>
    <div class="gantt-row">
      <span class="gantt-label">Conception technique</span>
      <div class="gantt-track"><span class="gantt-bar" style="left: 8.1013%; width: 18.9873%" role="img" aria-label="Conception technique : du 03/12/2025 au 15/02/2026" title="Conception technique : du 03/12/2025 au 15/02/2026"></span></div>
    </div>
    <div class="gantt-row">
      <span class="gantt-label">V1 · déploiement et oral</span>
      <div class="gantt-track"><span class="gantt-bar" style="left: 1.5190%; width: 16.2025%" role="img" aria-label="V1 · déploiement et oral : du 07/11/2025 au 09/01/2026" title="V1 · déploiement et oral : du 07/11/2025 au 09/01/2026"></span></div>
    </div>
    <div class="gantt-row">
      <span class="gantt-label">Set up Environnement</span>
      <div class="gantt-track"><span class="gantt-bar" style="left: 29.8734%; width: 7.8481%" role="img" aria-label="Environnement technique : du 27/02/2026 au 29/03/2026" title="Environnement technique : du 27/02/2026 au 29/03/2026"></span></div>
    </div>
    <div class="gantt-row">
      <span class="gantt-label">Migration vers la V2</span>
      <div class="gantt-track"><span class="gantt-bar" style="left: 37.7215%; width: 14.1772%" role="img" aria-label="Migration vers la V2 : du 30/03/2026 au 24/05/2026" title="Migration vers la V2 : du 30/03/2026 au 24/05/2026"></span></div>
    </div>
    <div class="gantt-row">
      <span class="gantt-label">Nouvelles fonctionnalités</span>
      <div class="gantt-track"><span class="gantt-bar" style="left: 51.8987%; width: 24.8101%" role="img" aria-label="Nouvelles fonctionnalités : du 25/05/2026 au 30/08/2026" title="Nouvelles fonctionnalités : du 25/05/2026 au 30/08/2026"></span></div>
    </div>
    <div class="gantt-row">
      <span class="gantt-label">Dossiers RNCP</span>
      <div class="gantt-track"><span class="gantt-bar" style="left: 1.2658%; width: 87.3418%" role="img" aria-label="Dossiers RNCP : du 06/11/2025 au 16/10/2026" title="Dossiers RNCP : du 06/11/2025 au 16/10/2026"></span></div>
    </div>
    <div class="gantt-row">
      <span class="gantt-label">Présentation et oral</span>
      <div class="gantt-track"><span class="gantt-bar" style="left: 81.2658%; width: 12.6582%" role="img" aria-label="Présentation et oral : du 18/09/2026 au 06/11/2026" title="Présentation et oral : du 18/09/2026 au 06/11/2026"></span></div>
    </div>
  </div>
  <div class="gantt-milestones">
    <span class="gantt-column-label">Etapes clés</span>
    <div class="gantt-track">
      <span class="gantt-milestone" style="left: 17.4684%"><b aria-hidden="true">◆</b><span>Oral V1</span></span>
      <span class="gantt-milestone" style="left: 22.7848%"><b aria-hidden="true">◆</b><span>Démo 1</span></span>
      <span class="gantt-milestone" style="left: 33.4177%"><b aria-hidden="true">◆</b><span>Démo 2</span></span>
      <span class="gantt-milestone" style="left: 81.2658%"><b aria-hidden="true">◆</b><span>Oral blanc</span></span>
      <!-- Position indicative dans la première semaine de novembre : jour exact non précisé. -->
      <span class="gantt-milestone" style="left: 93.2%" title="Examen · début novembre 2026"><b aria-hidden="true">◆</b><span>Examen</span></span>
    </div>
  </div>
</div>

<style scoped>
.gantt { --label-width: 205px; padding: 12px 14px 8px; background: var(--color-bg-card); border-radius: var(--radius-card); margin-top: 3rem; }
.gantt-header, .gantt-row, .gantt-milestones { display: grid; grid-template-columns: var(--label-width) minmax(0, 1fr); align-items: center; }
.gantt-column-label { font-size: 10px; font-weight: 700; letter-spacing: 0.08em; }
.gantt-years, .gantt-months { display: flex; }
.gantt-years { height: 20px; font-size: 12px; font-weight: 700; }
.gantt-years span { padding-left: 5px; }
.gantt-months { height: 25px; align-items: center; }
.gantt-months span { flex-shrink: 0; text-align: center; font-size: 10px; }
.gantt-body { position: relative; }
.gantt-grid { position: absolute; inset: 0 0 0 var(--label-width); border-right: 1px solid #e9e3d6; pointer-events: none; }
.gantt-grid i { position: absolute; top: 0; bottom: 0; border-left: 1px solid #e9e3d6; }
.gantt-row { position: relative; height: 28px; border-bottom: 1px solid #f2eee5; }
.gantt-label { padding-right: 8px; font-size: 13px; font-weight: 600; }
.gantt-track { position: relative; height: 100%; }
.gantt-bar { position: absolute; top: 6px; height: 16px; border-radius: 4px; background: var(--color-brand-primary); border: 1px solid #ad7300; }
.gantt-milestones { height: 54px; }
.gantt-milestone { position: absolute; top: 4px; display: flex; flex-direction: column; align-items: center; transform: translateX(-50%); white-space: nowrap; }
.gantt-milestone b { font-size: 13px; line-height: 16px; }
.gantt-milestone span { font-size: 10px; }
</style>
---
class: pe-section-content
title: Backlog
level: 2
---

# Gestion de projet

## Backlog

<div class="backlog-scroll" role="region" aria-label="Backlog complet, tableau défilant de 39 tâches" tabindex="0">
  <table class="backlog-table">
    <colgroup><col class="backlog-task-column" /><col /><col /><col /></colgroup>
    <thead><tr><th scope="col">Tâche</th><th scope="col">To Do</th><th scope="col">In progress</th><th scope="col">Done</th></tr></thead>
    <tbody class="backlog-phase" style="--phase-bg: #fff2cf">
      <tr class="backlog-phase-title"><th colspan="4" scope="rowgroup">Conception produit</th></tr>
      <tr><th scope="row">Définir les personae</th>
        <td></td>
        <td></td>
        <td><span class="backlog-status done" role="img" aria-label="Done">●</span></td>
      </tr>
      <tr><th scope="row">Cahier des charges</th>
        <td></td>
        <td></td>
        <td><span class="backlog-status done" role="img" aria-label="Done">●</span></td>
      </tr>
      <tr><th scope="row">Wireframes</th>
        <td></td>
        <td></td>
        <td><span class="backlog-status done" role="img" aria-label="Done">●</span></td>
      </tr>
      <tr><th scope="row">Charte graphique et logo</th>
        <td></td>
        <td></td>
        <td><span class="backlog-status done" role="img" aria-label="Done">●</span></td>
      </tr>
      <tr><th scope="row">Maquettes</th>
        <td></td>
        <td></td>
        <td><span class="backlog-status done" role="img" aria-label="Done">●</span></td>
      </tr>
    </tbody>
    <tbody class="backlog-phase" style="--phase-bg: #eaf0fc">
      <tr class="backlog-phase-title"><th colspan="4" scope="rowgroup">Conception technique</th></tr>
      <tr><th scope="row">Modélisation BDD</th>
        <td></td>
        <td></td>
        <td><span class="backlog-status done" role="img" aria-label="Done">●</span></td>
      </tr>
      <tr><th scope="row">Rédiger le backlog</th>
        <td></td>
        <td></td>
        <td><span class="backlog-status done" role="img" aria-label="Done">●</span></td>
      </tr>
    </tbody>
    <tbody class="backlog-phase" style="--phase-bg: #f3eafa">
      <tr class="backlog-phase-title"><th colspan="4" scope="rowgroup">V1 · déploiement et oral</th></tr>
      <tr><th scope="row">Dossier professionnel · V1</th>
        <td></td>
        <td></td>
        <td><span class="backlog-status done" role="img" aria-label="Done">●</span></td>
      </tr>
      <tr><th scope="row">Déploiement · V1</th>
        <td></td>
        <td></td>
        <td><span class="backlog-status done" role="img" aria-label="Done">●</span></td>
      </tr>
      <tr><th scope="row">Adapter le dossier projet · V1</th>
        <td></td>
        <td></td>
        <td><span class="backlog-status done" role="img" aria-label="Done">●</span></td>
      </tr>
      <tr><th scope="row">Adapter la présentation · V1</th>
        <td></td>
        <td></td>
        <td><span class="backlog-status done" role="img" aria-label="Done">●</span></td>
      </tr>
      <tr><th scope="row">Préparer l’oral · V1</th>
        <td></td>
        <td></td>
        <td><span class="backlog-status done" role="img" aria-label="Done">●</span></td>
      </tr>
      <tr><th scope="row">Oral · V1</th>
        <td></td>
        <td></td>
        <td><span class="backlog-status done" role="img" aria-label="Done">●</span></td>
      </tr>
    </tbody>
    <tbody class="backlog-phase" style="--phase-bg: #e7f3f1">
      <tr class="backlog-phase-title"><th colspan="4" scope="rowgroup">Set up Environnement</th></tr>
      <tr><th scope="row">Instructions Copilot</th>
        <td></td>
        <td></td>
        <td><span class="backlog-status done" role="img" aria-label="Done">●</span></td>
      </tr>
      <tr><th scope="row">Déployer en staging</th>
        <td></td>
        <td></td>
        <td><span class="backlog-status done" role="img" aria-label="Done">●</span></td>
      </tr>
      <tr><th scope="row">Migrer de Black à Ruff</th>
        <td></td>
        <td></td>
        <td><span class="backlog-status done" role="img" aria-label="Done">●</span></td>
      </tr>
      <tr><th scope="row">Initialiser le front, DRF et Vue</th>
        <td></td>
        <td></td>
        <td><span class="backlog-status done" role="img" aria-label="Done">●</span></td>
      </tr>
      <tr><th scope="row">Dockeriser le front</th>
        <td><span class="backlog-status todo" role="img" aria-label="To Do">●</span></td>
        <td></td>
        <td></td>
      </tr>
    </tbody>
    <tbody class="backlog-phase" style="--phase-bg: #eaf2de">
      <tr class="backlog-phase-title"><th colspan="4" scope="rowgroup">Migration vers la V2</th></tr>
      <tr><th scope="row">Appliquer la nouvelle charte</th>
        <td></td>
        <td></td>
        <td><span class="backlog-status done" role="img" aria-label="Done">●</span></td>
      </tr>
      <tr><th scope="row">Connexion</th>
        <td></td>
        <td></td>
        <td><span class="backlog-status done" role="img" aria-label="Done">●</span></td>
      </tr>
      <tr><th scope="row">Inscription</th>
        <td></td>
        <td></td>
        <td><span class="backlog-status done" role="img" aria-label="Done">●</span></td>
      </tr>
      <tr><th scope="row">Page profil</th>
        <td></td>
        <td></td>
        <td><span class="backlog-status done" role="img" aria-label="Done">●</span></td>
      </tr>
      <tr><th scope="row">Page accueil</th>
        <td></td>
        <td></td>
        <td><span class="backlog-status done" role="img" aria-label="Done">●</span></td>
      </tr>
      <tr><th scope="row">Déployer le front sur Railway</th>
        <td><span class="backlog-status todo" role="img" aria-label="To Do">●</span></td>
        <td></td>
        <td></td>
      </tr>
    </tbody>
    <tbody class="backlog-phase" style="--phase-bg: #fce9df">
      <tr class="backlog-phase-title"><th colspan="4" scope="rowgroup">Nouvelles fonctionnalités</th></tr>
      <tr><th scope="row">Mot de passe oublié</th>
        <td><span class="backlog-status todo" role="img" aria-label="To Do">●</span></td>
        <td></td>
        <td></td>
      </tr>
      <tr><th scope="row">Pratiquer sans compte</th>
        <td></td>
        <td></td>
        <td><span class="backlog-status done" role="img" aria-label="Done">●</span></td>
      </tr>
      <tr><th scope="row">Visualisation des données</th>
        <td><span class="backlog-status todo" role="img" aria-label="To Do">●</span></td>
        <td></td>
        <td></td>
      </tr>
      <tr><th scope="row">Notifications d’erreur et de succès</th>
        <td><span class="backlog-status todo" role="img" aria-label="To Do">●</span></td>
        <td></td>
        <td></td>
      </tr>
      <tr><th scope="row">Authentification MFA</th>
        <td><span class="backlog-status todo" role="img" aria-label="To Do">●</span></td>
        <td></td>
        <td></td>
      </tr>
      <tr><th scope="row">Saisie vocale · Vide ton sac</th>
        <td><span class="backlog-status todo" role="img" aria-label="To Do">●</span></td>
        <td></td>
        <td></td>
      </tr>
      <tr><th scope="row">Saisie vocale · Observation</th>
        <td><span class="backlog-status todo" role="img" aria-label="To Do">●</span></td>
        <td></td>
        <td></td>
      </tr>
    </tbody>
    <tbody class="backlog-phase" style="--phase-bg: #f8e7ef">
      <tr class="backlog-phase-title"><th colspan="4" scope="rowgroup">Dossiers RNCP</th></tr>
      <tr><th scope="row">Dossier professionnel · RNCP</th>
        <td></td>
        <td></td>
        <td><span class="backlog-status done" role="img" aria-label="Done">●</span></td>
      </tr>
      <tr><th scope="row">Dossier projet · RNCP</th>
        <td></td>
        <td><span class="backlog-status progress" role="img" aria-label="In progress">●</span></td>
        <td></td>
      </tr>
    </tbody>
    <tbody class="backlog-phase" style="--phase-bg: #e6f1f8">
      <tr class="backlog-phase-title"><th colspan="4" scope="rowgroup">Présentation et oral</th></tr>
      <tr><th scope="row">Présentation · RNCP</th>
        <td><span class="backlog-status todo" role="img" aria-label="To Do">●</span></td>
        <td></td>
        <td></td>
      </tr>
      <tr><th scope="row">Préparer l’oral · RNCP</th>
        <td><span class="backlog-status todo" role="img" aria-label="To Do">●</span></td>
        <td></td>
        <td></td>
      </tr>
      <tr><th scope="row">Démo 1</th>
        <td></td>
        <td></td>
        <td><span class="backlog-status done" role="img" aria-label="Done">●</span></td>
      </tr>
      <tr><th scope="row">Démo 2</th>
        <td></td>
        <td></td>
        <td><span class="backlog-status done" role="img" aria-label="Done">●</span></td>
      </tr>
      <tr><th scope="row">Séminaire 2</th>
        <td></td>
        <td><span class="backlog-status progress" role="img" aria-label="In progress">●</span></td>
        <td></td>
      </tr>
    </tbody>
  </table>
</div>

<style scoped>
.backlog-scroll { max-height: 380px; overflow-y: auto; border: 1px solid #d8cba9; border-radius: var(--radius-card); background: var(--color-bg-card); scrollbar-color: #ad7300 var(--color-bg-page); }
.backlog-scroll:focus-visible { outline: 3px solid #ad7300; outline-offset: 3px; }
.backlog-table { width: 100%; margin: 0; border-collapse: separate; border-spacing: 0; table-layout: fixed; font-size: 15px; line-height: 1.3; }
.backlog-task-column { width: 61%; }
.backlog-table th, .backlog-table td { padding: 8px 12px; border: 0; border-bottom: 1px solid #eee8da; }
.backlog-table thead th { position: sticky; top: 0; z-index: 1; background: var(--color-brand-primary); color: var(--color-black); font-size: 13px; font-weight: 700; white-space: nowrap; }
.backlog-table th { text-align: left; }
.backlog-table tbody th { font-weight: 500; }
.backlog-table td, .backlog-table thead th:not(:first-child) { text-align: center; }
.backlog-phase { background: var(--phase-bg); }
.backlog-table .backlog-phase-title th { padding: 10px 12px 6px; font-size: 12px; font-weight: 700; letter-spacing: 0.04em; border-top: 3px solid var(--color-bg-card); border-bottom: 1px solid #00000015; }
.backlog-table tbody tr:last-child > * { border-bottom: 0; }
.backlog-status { display: inline-block; width: 24px; height: 24px; box-sizing: border-box; border-radius: 50%; vertical-align: middle; font-size: 0; }
.backlog-status.todo { background: var(--color-white); }
.backlog-status.progress { background: var(--color-bg-observation); }
.backlog-status.done { background: var(--color-brand-primary); }
</style>
---
class: pe-section-content
title: Gestion de projet assistée par IA
level: 2
---

# Gestion de projet

## Gestion de projet assistée par IA

<div class="ai-project-files">
  <section class="ai-file-card ai-file-framework">
    <h3>AGENTS.md</h3>
    <p>Rôles &amp; bonnes pratiques</p>
  </section>
  <div class="ai-file-details">
    <section class="ai-file-card">
      <h3>project-management.md</h3>
      <p>Backlog</p>
    </section>
    <section class="ai-file-card">
      <h3>next-session.md</h3>
      <p>Objectifs</p>
    </section>
    <section class="ai-file-card">
      <h3>session-log.md</h3>
      <p>Journalisation</p>
    </section>
  </div>
</div>

<style scoped>
.ai-project-files { display: grid; gap: 1.25rem; margin-top: 3rem; }
.ai-file-details { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 1.25rem; }
.ai-file-card { display: flex; flex-direction: column; align-items: stretch; gap: 1rem; min-height: 145px; padding: 1.25rem; border-radius: var(--radius-card); background: var(--color-bg-card); }
.ai-file-framework { min-height: 115px; }
.ai-file-card h3 { align-self: flex-start; margin: 0; font-family: ui-monospace, SFMono-Regular, Consolas, "Liberation Mono", monospace; font-size: 0.85rem; font-weight: 600;text-align: left; }
.ai-file-card p {font-size: 1.5rem; text-align: center; text-decoration: underline; text-decoration-color: var(--color-brand-primary); }
.ai-file-framework h3 { font-size: 1rem; }
</style>

---
class: pe-section
title: Conception
---

# Conception


---
class: pe-section-content
title: Base de données - MCD
level: 2
---

# Conception
## Base de données - MCD

<img
  class="mcd-diagram"
  src="/mcd.svg"
  alt="MCD de l’API : un utilisateur enregistre zéro à plusieurs pauses ; chaque pause appartient à un utilisateur et contient au moins un sentiment et un besoin."
/>

<style scoped>
.mcd-diagram { display: block; width: 100%; height: 370px; object-fit: contain; margin-top: 2rem; }
</style>

---
class: pe-section-content
title: Base de données - MLD
level: 2
---

# Conception
## Base de données - MLD

<img
  class="mld-diagram"
  src="/mld.svg"
  alt="MCD de l’API : un utilisateur enregistre zéro à plusieurs pauses ; chaque pause appartient à un utilisateur et contient au moins un sentiment et un besoin."
/>

<style scoped>
.mld-diagram { display: block; width: 100%; height: 370px; object-fit: contain; margin-top: 2rem; }
</style>

---
class: pe-section-content
title: Base de données - MPD
level: 2
---

# Conception
## Base de données - MPD

<img
  class="mpd-diagram"
  src="/mpd.svg"
  alt="MPD PostgreSQL : sept tables applicatives avec leurs colonnes, types et clés. Pause référence Utilisateur ; les deux tables d’association relient Pause à Sentiment et Besoin. Le compteur anonyme est indépendant."
/>

<style scoped>
.mpd-diagram { display: block; width: 100%; height: 400px; object-fit: contain; margin: 0 auto; }
</style>
---
class: pe-section-content
title: Cas d’utilisation
level: 2
---

# Conception
## Cas d’utilisation

<img
  class="use-cases-diagram"
  src="/use-cases.svg"
  alt="Cas d’utilisation : visiteur et utilisateur connecté. La pratique avec compte inclut l’enregistrement ; la pratique anonyme n’enregistre pas le contenu."
/>

<style scoped>
.use-cases-diagram { display: block; width: 100%; height: 400px; object-fit: contain; margin: 0 auto; }
</style>

---
class: pe-section-content
title: Parcours utilisateur
level: 2
---

# Conception
## Parcours utilisateur

<div class="userflow-scroll" role="region" aria-label="Parcours utilisateur, image défilante" tabindex="0" @keydown.stop @wheel.stop>
  <img src="/userflow.svg" alt="Parcours utilisateur de Pause Empathique" />
</div>

<style scoped>
.userflow-scroll { height: 390px; overflow: auto; padding: 1rem; box-sizing: border-box; background: var(--color-bg-card); border-radius: var(--radius-card); scrollbar-color: #ad7300 var(--color-bg-card); overscroll-behavior: contain; }
.userflow-scroll:focus-visible { outline: 2px solid #ad7300; outline-offset: 3px; }
.userflow-scroll img { display: block; width: 100%; height: auto; max-height: none; }
</style>
---
class: pe-section-content
title: Wireframes
level: 2
---

# Conception

## Wireframes

<div class="wireframes-scroll" role="region" aria-label="Wireframes, image défilante" tabindex="0" @keydown.stop @wheel.stop>
  <img src="/wireframe.webp" alt="Wireframes du projet Pause Empathique 2.0" />
</div>

<style scoped>
.wireframes-scroll { height: 390px; overflow: auto; padding: 1rem; box-sizing: border-box; background: var(--color-bg-card); border-radius: var(--radius-card); scrollbar-color: #ad7300 var(--color-bg-card); overscroll-behavior: contain; }
.wireframes-scroll:focus-visible { outline: 2px solid #ad7300; outline-offset: 3px; }
.wireframes-scroll img { display: block; width: 100%; height: auto; max-height: none; }
</style>
---
class: pe-section-content
title: Charte graphique
level: 2
---

# Conception

## Charte graphique

<div class="brand-guide">
  <section class="brand-type" aria-label="Typographies">
    <h3 class="brand-section-label">TYPOGRAPHIES</h3>
    <div class="brand-font-card">
      <span class="brand-role">Logo &amp; titres</span>
      <p class="brand-fraunces">Fraunces</p>
    </div>
    <div class="brand-font-card">
      <span class="brand-role">Textes &amp; interface</span>
      <p class="brand-manrope">Manrope</p>
    </div>
    <div class="brand-logo-card">
      <img src="/logo-name.webp" alt="Logo Pause Empathique" />
    </div>
  </section>
  <section class="brand-colors" aria-label="Palette de couleurs">
    <h3 class="brand-section-label">COULEURS</h3>
    <div class="brand-palette">
      <div class="brand-color-column" role="group" aria-label="Couleurs principales">
        <div class="brand-color-card">
          <span class="brand-swatch" style="background: var(--color-brand-primary)" aria-hidden="true"></span>
          <span class="brand-color-name">Primaire</span>
          <span class="brand-hex">#FFB300</span>
        </div>
        <div class="brand-color-card">
          <span class="brand-swatch" style="background: var(--color-white)" aria-hidden="true"></span>
          <span class="brand-color-name">Cartes</span>
          <span class="brand-hex">#FFFFFF</span>
        </div>
        <div class="brand-color-card">
          <span class="brand-swatch" style="background: var(--color-black)" aria-hidden="true"></span>
          <span class="brand-color-name">Texte</span>
          <span class="brand-hex">#1A1300</span>
        </div>
      </div>
      <div class="brand-color-column" role="group" aria-label="Étapes de pratique">
        <div class="brand-color-card">
          <span class="brand-swatch" style="background: var(--color-bg-empty-your-bag)" aria-hidden="true"></span>
          <span class="brand-color-name">Vide ton sac</span>
          <span class="brand-hex">#FFD151</span>
        </div>
        <div class="brand-color-card">
          <span class="brand-swatch" style="background: var(--color-bg-observation)" aria-hidden="true"></span>
          <span class="brand-color-name">Observation</span>
          <span class="brand-hex">#FFDC7D</span>
        </div>
        <div class="brand-color-card">
          <span class="brand-swatch" style="background: var(--color-bg-feelings)" aria-hidden="true"></span>
          <span class="brand-color-name">Sentiments</span>
          <span class="brand-hex">#FFE8AA</span>
        </div>
        <div class="brand-color-card">
          <span class="brand-swatch" style="background: var(--color-bg-page)" aria-hidden="true"></span>
          <span class="brand-color-name">Besoins</span>
          <span class="brand-hex">#FFF4D5</span>
        </div>
      </div>
    </div>
  </section>
</div>

<style scoped>
.brand-guide { display: grid; grid-template-columns: 260px minmax(0, 1fr); gap: 1.5rem; }
.brand-section-label { margin: 0 0 0.75rem; font-family: var(--font-body); font-size: 0.7rem; font-weight: 700; letter-spacing: 0.12em; }
.brand-font-card { display: flex; flex-direction: column; justify-content: center; gap: 0.75rem; min-height: 108px; padding: 1.1rem 1.4rem; background: var(--color-bg-card); border-radius: var(--radius-card); }
.brand-font-card + .brand-font-card { margin-top: 0.75rem; }
.brand-logo-card { display: flex; align-items: center; justify-content: center; height: 68px; margin-top: 0.75rem; padding: 0.5rem 1rem; background: var(--color-bg-card); border-radius: var(--radius-card); }
.brand-logo-card img { display: block; width: 100%; height: 100%; object-fit: contain; }
.brand-role { font-size: 0.8rem; font-weight: 600; }
.brand-font-card p { margin: 0; font-size: 2.15rem; line-height: 1.2; }
.brand-fraunces { font-family: var(--font-logo); font-weight: 700; }
.brand-manrope { font-family: var(--font-body); font-weight: 400; }
.brand-palette { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 0.75rem; height: 308px; }
.brand-color-column { display: grid; grid-auto-rows: minmax(0, 1fr); gap: 0.75rem; min-width: 0; }
.brand-color-card { display: grid; grid-template-columns: 62px minmax(0, 1fr); grid-template-rows: 1fr 1fr; column-gap: 0.75rem; row-gap: 0.3rem; min-height: 0; padding: 0.6rem; background: var(--color-bg-card); border-radius: var(--radius-card); }
.brand-swatch { display: block; grid-row: 1 / 3; height: 100%; border-radius: 7px; box-shadow: inset 0 0 0 1px #1a130015; }
.brand-color-name { align-self: end; font-size: 0.8rem; font-weight: 600; line-height: 1.2; }
.brand-hex { font-family: ui-monospace, Consolas, monospace; font-size: 0.7rem; line-height: 1.2; }
</style>
---
class: pe-section-content
title: Identité visuelle
level: 2
---

# Conception

## Identité visuelle

<div class="visual-universe">
  <div class="visual-planets">
    <div class="visual-planet visual-planet-clarity">Cheminement</div>
    <div class="visual-planet visual-planet-world">Monde intérieur</div>
    <div class="visual-planet visual-planet-journey">Clarté</div>
  </div>
  <svg class="visual-path" viewBox="0 0 680 42" aria-hidden="true">
    <path d="M12 22 C38 -8 69 45 90 19 S125 0 132 22 S104 44 98 29 S140 4 165 23 S192 43 207 21 S243 2 267 21 S312 36 347 23 S410 18 452 21 L668 21" />
  </svg>
  <p class="visual-message">Du compliqué et sinueux, vers le <strong>simple et clair</strong></p>
</div>

<style scoped>
.visual-universe { margin-top: 1.5rem; text-align: center; }
.visual-planets { display: flex; justify-content: center; align-items: center; gap: 2rem; height: 250px; }
.visual-planet { display: flex; flex-direction: column; align-items: center; justify-content: center; flex-shrink: 0; width: 185px; height: 185px; border-radius: 50%; background: var(--color-bg-circle-white); box-shadow: 0 18px 45px rgba(26, 19, 0, 0.12); font-family: var(--font-logo); font-size: 1.45rem; }
.visual-planet-clarity { transform: translateY(12px); }
.visual-planet-world { width: 225px; height: 225px; gap: 0.65rem; }
.visual-planet-journey { transform: translateY(22px); }
.visual-path { display: block; width: 76%; height: 42px; margin: 0.75rem auto 0; overflow: visible; }
.visual-path path { fill: none; stroke: var(--color-brand-primary); stroke-width: 2.5; stroke-linecap: round; }
.visual-message { margin: 0.8rem 0 0; font-size: 1.25rem; }
.visual-message strong { font-weight: 700; }
</style>

---
class: pe-section-content
title: Maquette Haute fidélité
level: 2
---

# Conception

## Maquette Haute Fidélité

<div class="mockups-board" role="region" aria-label="Maquettes Figma mobiles puis desktop, tableau défilant" tabindex="0" @keydown.stop @wheel.stop>
  <h3>Mobile</h3>
  <div class="mockups-mobile">
    <figure>
      <figcaption>Accueil</figcaption>
      <img src="/maquettes/Home%20Page.webp" alt="Maquette mobile : Accueil" />
    </figure>
    <figure>
      <figcaption>Connexion</figcaption>
      <img src="/maquettes/Login%20Page.webp" alt="Maquette mobile : Connexion" />
    </figure>
    <figure>
      <figcaption>Inscription</figcaption>
      <img src="/maquettes/Register%20Page.webp" alt="Maquette mobile : Inscription" />
    </figure>
    <figure>
      <figcaption>Vide ton sac</figcaption>
      <img src="/maquettes/Vide%20ton%20sac%20Page.webp" alt="Maquette mobile : Vide ton sac" />
    </figure>
    <figure>
      <figcaption>Observation</figcaption>
      <img src="/maquettes/Observation%20Page.webp" alt="Maquette mobile : Observation" />
    </figure>
    <figure>
      <figcaption>Sentiments</figcaption>
      <img src="/maquettes/Feelings%20Page.webp" alt="Maquette mobile : Sentiments" />
    </figure>
    <figure>
      <figcaption>Sentiments · sélection</figcaption>
      <img src="/maquettes/Feelings%20Page-1.webp" alt="Maquette mobile : Sentiments · sélection" />
    </figure>
    <figure>
      <figcaption>Besoins</figcaption>
      <img src="/maquettes/Needs%20Page.webp" alt="Maquette mobile : Besoins" />
    </figure>
    <figure>
      <figcaption>Journal</figcaption>
      <img src="/maquettes/Journal%20Page.webp" alt="Maquette mobile : Journal" />
    </figure>
  </div>
  <h3 class="mockups-desktop-heading">Desktop</h3>
  <div class="mockups-desktop">
    <figure>
      <figcaption>Accueil · desktop</figcaption>
      <img src="/maquettes/Desktop%20-%201.webp" alt="Maquette Accueil · desktop" />
    </figure>
    <figure>
      <figcaption>Connexion · desktop</figcaption>
      <img src="/maquettes/Desktop%20-%203.webp" alt="Maquette Connexion · desktop" />
    </figure>
  </div>
</div>

<style scoped>
.mockups-board { height: 400px; overflow: auto; padding: 1.5rem; box-sizing: border-box; background: var(--color-bg-card); border-radius: var(--radius-card); scrollbar-color: #ad7300 var(--color-bg-card); overscroll-behavior: contain; }
.mockups-board:focus-visible { outline: 2px solid #ad7300; outline-offset: 3px; }
.mockups-board h3 { margin: 0 0 1rem; font-family: var(--font-body); font-size: 0.8rem; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; }
.mockups-mobile { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); align-items: start; gap: 1.5rem; }
.mockups-desktop { display: grid; gap: 1.75rem; }
.mockups-board .mockups-desktop-heading { margin-top: 2rem; }
.mockups-board figure { margin: 0; min-width: 0; }
.mockups-board figcaption { margin-bottom: 0.6rem; font-size: 0.75rem; font-weight: 600; }
.mockups-board img { display: block; width: 100%; height: auto; max-height: none; border-radius: 8px; }
.mockups-mobile img { width: auto; max-width: 100%; height: 280px; margin-inline: auto; object-fit: contain; }
</style>

---
class: pe-section-content
title: Qualité & Réglementation
level: 2
---

# Conception

## Qualité & Réglementation

<div class="quality-rules">
  <div class="rule accessibility">Accessibilité</div>
  <div class="rule rgpd">RGPD</div>
  <div class="rule ecoconception">Ecoconception</div>
</div>


<style>
.quality-rules {  margin-top: 3rem; text-align: center; display: flex; justify-content: center; align-items: center; gap: 3rem; height: 250px; }
.rule { display: flex; flex-direction: column; align-items: center; justify-content: center; flex-shrink: 0; width: 195px; height: 195px; border-radius: 50%; background: var(--color-bg-circle-white); box-shadow: 0 18px 45px rgba(26, 19, 0, 0.12); font-family: var(--font-logo); font-size: 1.45rem; }
.accessibility { transform: translateY(12px); }
.rgpd { width: 225px; height: 225px; gap: 0.65rem; }
.ecoconception { transform: translateY(22px); }
</style>

<!--
Accessibilité : Contraste, navigation au clavier, balises sémantiques html
RGPD : Réflexion sur les données, suppression et accès, attention données intimes
Ecoconception : Existe mais peu pris en compte, pas de vidéos,

Manque Mentions Légales, Consentement, Politique de Confidentialité -->

---
layout: center
class: pe-section
---

# Spécifications techniques

---
class: pe-section-content
title: Stack
level: 2
---

# Spécifications techniques


## Stack

<div class="stack-grid">
  <div class="stack-support">
  <section class="pe-card stack-card">
    <h3>Base de données</h3>
    <div class="stack-tools">
      <div class="stack-tool"><img src="/tech/postgresql.svg" alt="" /><span>PostgreSQL</span></div>
    </div>
  </section>
  <section class="pe-card stack-card stack-card-compact">
    <h3>Conteneurisation &amp; déploiement</h3>
    <div class="stack-tools">
      <div class="stack-tool"><img src="/tech/docker.svg" alt="" /><span>Docker</span></div>
      <div class="stack-tool"><img src="/tech/railway.svg" alt="" /><span>Railway</span></div>
    </div>
  </section>
  <section class="pe-card stack-card stack-card-compact">
    <h3>Versionnement</h3>
    <div class="stack-tools">
      <div class="stack-tool"><img src="/tech/git.svg" alt="" /><span>Git</span></div>
      <div class="stack-tool"><img src="/tech/github.svg" alt="" /><span>GitHub</span></div>
    </div>
  </section>
  </div>
  <section class="pe-card stack-card stack-card-main">
    <h3>Back-end</h3>
    <div class="stack-tools">
      <div class="stack-tool"><img src="/tech/drf.webp" alt="" /><span>Django REST Framework</span></div>
      <div class="stack-tool"><img src="/tech/poetry.svg" alt="" /><span>Poetry</span></div>
      <div class="stack-tool"><img src="/tech/pytest.svg" alt="" /><span>Pytest</span></div>
    </div>
  </section>
  <section class="pe-card stack-card stack-card-main">
    <h3>Front-end</h3>
    <div class="stack-tools">
      <div class="stack-tool"><img src="/tech/vuedotjs.svg" alt="" /><span>Vue</span></div>
      <div class="stack-tool"><img src="/tech/typescript.svg" alt="" /><span>TypeScript</span></div>
      <div class="stack-tool"><img src="/tech/tailwindcss.svg" alt="" /><span>Tailwind CSS</span></div>
      <div class="stack-tool"><img src="/tech/vitest.svg" alt="" /><span>Vitest</span></div>
    </div>
  </section>
</div>

<style scoped>
.stack-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 1rem; height: 380px; margin-top: 1.5rem; }
.stack-support { display: grid; grid-template-rows: 1fr 1.2fr 1fr; gap: 0.75rem; }
.stack-support .stack-card { padding: 1.1rem 1.25rem; }
.stack-card h3 { margin: 0 0 2rem; font-family: var(--font-body); font-size: 0.9rem; font-weight: 00; line-height: 1.4; border-bottom: 1px solid var(--color-brand-primary); }
.stack-tools { display: grid ;gap: 0.8rem; }
.stack-card-compact .stack-tools { display: flex; gap: 1.5rem; }
.stack-card-main .stack-tools { margin-top: 2rem; gap: 2.25rem; }
.stack-tool { display: flex; align-items: center; gap: 0.75rem; font-size: 0.95rem; line-height: 1.3; }
.stack-tool img { width: 26px; height: 26px; flex-shrink: 0; object-fit: contain; }
</style>

---
class: pe-section-content
title: Git Flow
level: 2
---

# Spécifications techniques

## Git Flow

<div class="git-flow-board">
  <svg class="git-flow" viewBox="0 0 900 390" role="img" aria-labelledby="git-flow-title git-flow-desc">
    <g class="git-labels">
      <text x="26" y="71">main</text>
      <text x="26" y="156">dev</text>
      <text x="26" y="236">feat/</text>
      <text x="26" y="316">fix/</text>
    </g>
    <g class="git-lines">
      <path class="git-main" d="M 170 65 H 845" />
      <path class="git-main" d="M 845 65 H 875" stroke-dasharray="3 12" />
      <path class="git-dev" d="M 170 65 V 110 Q 170 150 210 150 H 845" />
      <path class="git-dev" d="M 845 150 H 875" stroke-dasharray="3 12" />
      <path class="git-feature-one" d="M 280 150 V 192 Q 280 230 318 230 H 430 Q 480 230 480 190 V 165" marker-end="url(#git-flow-merge)" />
      <path class="git-feature-two" d="M 530 150 V 272 Q 530 310 568 310 H 670 Q 720 310 720 270 V 165" marker-end="url(#git-flow-merge)" />
      <path class="git-dev" d="M 755 150 Q 800 150 800 110 V 80" marker-end="url(#git-flow-merge)" />
    </g>
    <!-- Commits : cercle blanc extérieur et centre de la couleur de la branche. -->
    <g class="git-commit git-main"><circle cx="800" cy="65" r="11" /><circle class="git-commit-core" cx="800" cy="65" r="4" /></g>
    <g class="git-commit git-dev"><circle cx="480" cy="150" r="11" /><circle class="git-commit-core" cx="480" cy="150" r="4" /></g>
    <g class="git-commit git-dev"><circle cx="720" cy="150" r="11" /><circle class="git-commit-core" cx="720" cy="150" r="4" /></g>
    <g class="git-commit git-feature-one"><circle cx="345" cy="230" r="11" /><circle class="git-commit-core" cx="345" cy="230" r="4" /></g>
    <g class="git-commit git-feature-one"><circle cx="415" cy="230" r="11" /><circle class="git-commit-core" cx="415" cy="230" r="4" /></g>
    <g class="git-commit git-feature-two"><circle cx="590" cy="310" r="11" /><circle class="git-commit-core" cx="590" cy="310" r="4" /></g>
    <g class="git-commit git-feature-two"><circle cx="655" cy="310" r="11" /><circle class="git-commit-core" cx="655" cy="310" r="4" /></g>
  </svg>
</div>

<style scoped>
.git-flow-board { margin-top: 1.5rem; padding: 0.5rem; background: var(--color-bg-card); border-radius: var(--radius-card); }
.git-flow { display: block; width: 100%; height: auto; font-family: var(--font-body); }
.git-labels { font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: 18px; font-weight: 700; fill: var(--color-black); }
.git-main { color: var(--color-black); }
.git-dev { color: var(--color-brand-primary); }
.git-feature-one { color: #238799; }
.git-feature-two { color: #c65345; }
.git-lines { fill: none; stroke-width: 5; stroke-linecap: round; stroke-linejoin: round; }
.git-lines path { stroke: currentColor; }
.git-commit { fill: white; stroke: currentColor; stroke-width: 3; }
.git-commit-core { fill: currentColor; stroke: none; }
</style>

---
class: pe-section-content
title: CI
---

# Spécifications techniques

## CI

<div class="ci-diagrams">
  <figure>
    <figcaption>Back ></figcaption>
    <img src="/ci-back.webp" alt="Pipeline d’intégration continue du back-end" class="code-capture" />
  </figure>
  <figure>
    <figcaption>Front ></figcaption>
    <img src="/ci-front.webp" alt="Pipeline d’intégration continue du front-end" class="code-capture" />
  </figure>
</div>

<style scoped>
.ci-diagrams { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 1rem; height: 420px; }
.ci-diagrams figure { display: grid; grid-template-columns: 76px minmax(0, 1fr); align-items: center; margin: 0; min-width: 0; min-height: 0; }
.ci-diagrams figcaption { display: flex; align-items: center; gap: 0.4rem; font-size: 1rem; font-weight: 700; line-height: 1.3; }
.ci-diagrams img { display: block; width: 100%; height: 100%; min-height: 0; object-fit: contain; object-position: center top; }
</style>

---
class: pe-section-content
title: Docker
---

# Spécifications techniques

## Docker

<div class="ci-diagrams">
  <figure>
    <figcaption>Dockerfile</figcaption>
    <img src="/dockerfile.webp" class="code-capture"/>
  </figure>
  <figure>
    <figcaption>Docker compose</figcaption>
    <img src="/docker-compose.webp" class="code-capture"/>
  </figure>
</div>

<style scoped>
.ci-diagrams { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 1rem; height: 420px; }
.ci-diagrams figure { display: grid; grid-template-columns: 76px minmax(0, 1fr); align-items: center; margin: 0; min-width: 0; min-height: 0; }
.ci-diagrams figcaption { display: flex; align-items: center; gap: 0.4rem; font-size: 1rem; font-weight: 700; line-height: 1.3; }
.ci-diagrams img { display: block; width: 100%; height: 100%; min-height: 0; object-fit: contain; object-position: center top; }
</style>



---
class: pe-section-content
title: Architecture
---

# Spécifications techniques
## Architecture

<div class="architecture-comparison">
  <section class="architecture-version" aria-label="Architecture V1 : rendu côté serveur">
    <div class="architecture-heading"><span class="architecture-badge">V1</span><span>SSR</span></div>
    <div class="architecture-flow">
      <div class="architecture-node"><span class="architecture-role">Base de données</span><img src="/tech/postgresql.svg" alt="" /><strong>PostgreSQL</strong></div>
      <div class="architecture-link"><span>Données</span><i aria-hidden="true"></i></div>
      <div class="architecture-node"><span class="architecture-role">Back-end</span><img src="/tech/django.svg" alt="" /><strong>Django</strong></div>
      <div class="architecture-link"><span>Rendu HTML</span><i aria-hidden="true"></i></div>
      <div class="architecture-node"><span class="architecture-role">Interface</span><span class="architecture-code" aria-hidden="true">&lt;/&gt;</span><strong>Templates HTML</strong></div>
    </div>
  </section>
  <section class="architecture-version" aria-label="Architecture V2 : API Django et front-end Vue séparés">
    <div class="architecture-heading"><span class="architecture-badge architecture-badge-v2">V2</span><span>CSR</span></div>
    <div class="architecture-flow">
      <div class="architecture-node"><span class="architecture-role">Base de données</span><img src="/tech/postgresql.svg" alt="" /><strong>PostgreSQL</strong></div>
      <div class="architecture-link"><span>Données</span><i aria-hidden="true"></i></div>
      <div class="architecture-node architecture-api"><span class="architecture-role">Back-end · API REST</span><img src="/tech/drf.webp" alt="" /><strong>Django REST Framework</strong></div>
      <div class="architecture-link architecture-json"><span>JSON</span><i aria-hidden="true"></i></div>
      <div class="architecture-node"><span class="architecture-role">Front-end</span><img src="/tech/vuedotjs.svg" alt="" /><strong>Vue</strong></div>
    </div>
  </section>
</div>

<style scoped>
.architecture-comparison { display: grid; gap: 1.75rem; margin-top: 1.5rem; }
.architecture-heading { display: flex; align-items: center; gap: 0.75rem; margin-bottom: 0.75rem; font-size: 1rem; font-weight: 600; }
.architecture-badge { padding: 0.3rem 0.75rem; border-radius: var(--radius-btn); background: var(--color-black); color: var(--color-white); font-weight: 700; }
.architecture-badge-v2 { background: var(--color-brand-primary); color: var(--color-black); }
.architecture-flow { display: grid; grid-template-columns: minmax(0, 1fr) 105px minmax(0, 1fr) 105px minmax(0, 1fr); align-items: center; }
.architecture-node { display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 0.65rem; height: 125px; padding: 0.75rem; border-radius: var(--radius-card); background: var(--color-bg-card); text-align: center; }
.architecture-role { font-size: 0.8rem; opacity: 0.7; }
.architecture-node img { width: 30px; height: 30px; object-fit: contain; }
.architecture-node strong { font-size: 0.95rem; line-height: 1.25; }
.architecture-code { height: 30px; font: 700 26px/30px ui-monospace, SFMono-Regular, Consolas, monospace; }
.architecture-api { background: var(--color-bg-feelings); }
.architecture-link { display: flex; flex-direction: column; gap: 0.65rem; padding: 0 0.5rem; text-align: center; }
.architecture-link > span { font-size: 0.75rem; font-weight: 600; white-space: nowrap; }
.architecture-link i { display: block; position: relative; height: 3px; background: var(--color-black); }
.architecture-link i::after { content: ''; position: absolute; right: 0; top: -4px; width: 10px; height: 10px; border-top: 3px solid var(--color-black); border-right: 3px solid var(--color-black); transform: rotate(45deg); }
.architecture-json > span { align-self: center; padding: 0.15rem 0.6rem; border-radius: 6px; background: var(--color-brand-primary); font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-weight: 700; }
</style>


---
layout: center
class: pe-section
---

# Migration vers la V2

---
class: pe-section-content
title: Etapes de la migration
level: 2
---

# Migration vers la V2

<svg class="migration-journey" viewBox="0 0 900 430" role="img" aria-labelledby="migration-journey-title">
  <title id="migration-journey-title">Migration vers la V2 en onze étapes, révélées au clic</title>
  <g v-click="1" class="migration-step">
    <g class="migration-stop">
      <circle cx="135" cy="40" r="19" />
      <text class="migration-number" x="135" y="46">1</text>
      <text class="migration-label" x="135" y="83">
        <tspan x="135" dy="0">Environnement de</tspan>
        <tspan x="135" dy="23">préproduction</tspan>
      </text>
    </g>
  </g>
  <g v-click="2" class="migration-step">
    <path class="migration-segment" d="M157 40 H345" pathLength="1" />
    <g class="migration-stop">
      <circle cx="345" cy="40" r="19" />
      <text class="migration-number" x="345" y="46">2</text>
      <text class="migration-label" x="345" y="83">
        <tspan x="345" dy="0">Charte graphique</tspan>
      </text>
    </g>
  </g>
  <g v-click="3" class="migration-step">
    <path class="migration-segment" d="M367 40 H555" pathLength="1" />
    <g class="migration-stop">
      <circle cx="555" cy="40" r="19" />
      <text class="migration-number" x="555" y="46">3</text>
      <text class="migration-label" x="555" y="83">
        <tspan x="555" dy="0">Black → Ruff</tspan>
      </text>
    </g>
  </g>
  <g v-click="4" class="migration-step">
    <path class="migration-segment" d="M577 40 H765" pathLength="1" />
    <g class="migration-stop">
      <circle cx="765" cy="40" r="19" />
      <text class="migration-number" x="765" y="46">4</text>
      <text class="migration-label" x="765" y="83">
        <tspan x="765" dy="0">unittest → pytest</tspan>
      </text>
    </g>
  </g>
  <g v-click="5" class="migration-step">
    <path class="migration-segment" d="M787 40 H805 C890 40 890 190 805 190 H765" pathLength="1" />
    <g class="migration-stop">
      <circle cx="765" cy="190" r="19" />
      <text class="migration-number" x="765" y="196">5</text>
      <text class="migration-label" x="765" y="233">
        <tspan x="765" dy="0">Endpoints API</tspan>
      </text>
    </g>
  </g>
  <g v-click="6" class="migration-step">
    <path class="migration-segment" d="M743 190 H450" pathLength="1" />
    <g class="migration-stop">
      <circle cx="450" cy="190" r="19" />
      <text class="migration-number" x="450" y="196">6</text>
      <text class="migration-label" x="450" y="233">
        <tspan x="450" dy="0">Tests &amp; documentation</tspan>
        <tspan x="450" dy="23">API</tspan>
      </text>
    </g>
  </g>
  <g v-click="7" class="migration-step">
    <path class="migration-segment" d="M428 190 H135" pathLength="1" />
    <g class="migration-stop">
      <circle cx="135" cy="190" r="19" />
      <text class="migration-number" x="135" y="196">7</text>
      <text class="migration-label" x="135" y="233">
        <tspan x="135" dy="0">Setup </tspan>
        <tspan x="135" dy="23">repo front</tspan>
      </text>
    </g>
  </g>
  <g v-click="8" class="migration-step">
    <path class="migration-segment" d="M113 190 H95 C10 190 10 340 95 340 H135" pathLength="1" />
    <g class="migration-stop">
      <circle cx="135" cy="340" r="19" />
      <text class="migration-number" x="135" y="346">8</text>
      <text class="migration-label" x="135" y="383">
        <tspan x="135" dy="0">Authentification</tspan>
        <tspan x="135" dy="23" class="migration-detail">Vues · Logique · Tests</tspan>
      </text>
    </g>
  </g>
  <g v-click="9" class="migration-step">
    <path class="migration-segment" d="M157 340 H345" pathLength="1" />
    <g class="migration-stop">
      <circle cx="345" cy="340" r="19" />
      <text class="migration-number" x="345" y="346">9</text>
      <text class="migration-label" x="345" y="383">
        <tspan x="345" dy="0">Pratique</tspan>
        <tspan x="345" dy="23" class="migration-detail">Vues · Logique · Tests</tspan>
      </text>
    </g>
  </g>
  <g v-click="10" class="migration-step">
    <path class="migration-segment" d="M367 340 H555" pathLength="1" />
    <g class="migration-stop">
      <circle cx="555" cy="340" r="19" />
      <text class="migration-number" x="555" y="346">10</text>
      <text class="migration-label" x="555" y="383">
        <tspan x="555" dy="0">Mise en conformité</tspan>
        <tspan x="555" dy="23">RGPD</tspan>
      </text>
    </g>
  </g>
  <g v-click="11" class="migration-step">
    <path class="migration-segment" d="M577 340 H765" pathLength="1" />
    <g class="migration-stop">
      <circle cx="765" cy="340" r="19" />
      <text class="migration-number" x="765" y="346">11</text>
      <text class="migration-label" x="765" y="383">
        <tspan x="765" dy="0">Préparation du</tspan>
        <tspan x="765" dy="23">déploiement</tspan>
      </text>
    </g>
  </g>
</svg>

<style scoped>
.migration-journey { display: block; width: 100%; height: 430px; margin-top: 0.75rem; overflow: visible; font-family: var(--font-body); }
.migration-segment { fill: none; stroke: var(--color-brand-primary); stroke-width: 5; stroke-linecap: round; stroke-dasharray: 1; stroke-dashoffset: 0; transition: stroke-dashoffset 550ms ease; }
.migration-step.slidev-vclick-hidden .migration-segment { stroke-dashoffset: 1; }
.migration-stop { opacity: 1; transition: opacity 250ms ease 350ms; }
.migration-step.slidev-vclick-hidden .migration-stop { opacity: 0; transition-delay: 0ms; }
.migration-stop circle { fill: var(--color-bg-card); stroke: var(--color-brand-primary); stroke-width: 4; }
.migration-number { fill: var(--color-black); font-size: 17px; font-weight: 700; text-anchor: middle; }
.migration-label { fill: var(--color-black); font-size: 18px; font-weight: 600; text-anchor: middle; }
.migration-detail { font-size: 15px; font-weight: 400; }
@media (prefers-reduced-motion: reduce) {
  .migration-segment, .migration-stop { transition: none; }
}
</style>

---
layout: center
class: pe-section
---

# Démo 🍿

---
layout: center
class: pe-section
---

# Zoom sur : Pratiquer sans compte


---
class: pe-section-content !bg-white
title: Diagramme de séquence
preload: false
level: 2
---

# Pratiquer sans compte - Diagramme de séquence

<div class="sequence-panel" role="img" aria-label="Diagramme de séquence">

```mermaid {scale: 0.44,theme: 'base', themeVariables: {fontFamily: 'Arial, sans-serif', primaryColor: '#fff4d5', primaryTextColor: '#1a1300', primaryBorderColor: '#ad7300', lineColor: '#1a1300', actorBkg: '#fff4d5', actorBorder: '#ad7300', actorTextColor: '#1a1300', noteBkgColor: '#ffe8aa', noteTextColor: '#1a1300', noteBorderColor: '#ffb300'}, sequence: {useMaxWidth: true, actorFontSize: 16, messageFontSize: 18, noteFontSize: 12, actorMargin: 70, width: 125, height: 36, messageMargin: 7, noteMargin: 3, boxMargin: 4, boxTextMargin: 3, diagramMarginX: 12, diagramMarginY: 8, wrap: false, mirrorActors: false}}
sequenceDiagram
    actor P as Personne
    participant V as Interface Vue
    participant S as Stores Pinia
    participant C as Client API
    participant A as API DRF
    participant D as Base de données
    P->>V: EmptyYourBagView : saisir le texte
    V->>S: draft.emptyYourBag (v-model)
    P->>V: Suivant → ObservationView : décrire les faits
    V->>S: draft.observation (v-model)
    P->>V: Suivant → FeelingsView
    V->>C: getFeelings()
    C->>A: GET /api/v1/feelings/
    A->>D: Lire les sentiments
    A-->>C: 200 · sentiments
    Note over P,V: Sans sentiment : bouton « Étape suivante » désactivé
    P->>V: Sélectionner un sentiment
    V->>S: toggleFeeling(id)
    P->>V: Suivant → NeedsView
    V->>C: getNeeds()
    C->>A: GET /api/v1/needs/
    A->>D: Lire les besoins
    A-->>C: 200 · besoins
    P->>V: Sélectionner un besoin
    V->>S: toggleNeed(id)
    P->>V: Suivant → PauseView
    S-->>V: Brouillon réactif → récapitulatif
```

</div>

<style scoped>
.sequence-panel { position: absolute; inset: 80px 0 0; background: #fff; }
/* La taille du SVG est réglée par l’option scale du bloc Mermaid. */
.sequence-panel :deep(.mermaid) { display: flex; justify-content: center; align-items: flex-start; width: 100%; height: 98%; }
</style>

---
class: pe-section-content !bg-white
title: Terminer sans enregistrer
preload: false
level: 2
---

# Terminer sans enregistrer

<div class="sequence-panel" role="img" aria-label="Terminer sans enregistrer">

```mermaid {scale: 0.56, theme: 'base', themeVariables: {fontFamily: 'Arial, sans-serif', primaryColor: '#fff4d5', primaryTextColor: '#1a1300', primaryBorderColor: '#ad7300', lineColor: '#1a1300', actorBkg: '#fff4d5', actorBorder: '#ad7300', actorTextColor: '#1a1300', noteBkgColor: '#ffe8aa', noteTextColor: '#1a1300', noteBorderColor: '#ffb300'}, sequence: {useMaxWidth: true, actorFontSize: 14, messageFontSize: 14, noteFontSize: 13, actorMargin: 14, width: 125, height: 55, messageMargin: 12, noteMargin: 4, boxMargin: 4, boxTextMargin: 3, diagramMarginX: 14, diagramMarginY: 18, wrap: false, mirrorActors: true}}
sequenceDiagram
    actor P as Personne
    participant V as Interface Vue
    participant S as Store Pinia pratice
    participant C as Client API
    participant A as API DRF
    participant D as Base de données
    P->>V: Terminer sans enregistrer
    V->>S: practice.submitAnonymousPractice()
    S->>C: countAnonymousPractice()
    C->>A: POST /api/v1/pauses/anonymous/
    Note over C,A: Aucun contenu du brouillon transmis
    A->>A: Vérifier l’absence d’authentification
    A->>D: Incrémenter AnonymousPauseCounter
    D-->>A: Compteur mis à jour
    A-->>C: 204 · aucun contenu
    C-->>S: Succès
    S->>S: reset() · effacer le brouillon
    S-->>V: Finalisation terminée
    V-->>P: Retour à l’accueil (Welcome)
```

</div>

<style scoped>
.sequence-panel { position: absolute; inset: 84px 0 0; }
.sequence-panel :deep(.mermaid) { display: flex; justify-content: center; align-items: flex-start; width: 95%; height: 95%; }
</style>

---
class: pe-section-content !bg-white
title: Créer un compte pour enregistrer
preload: false
level: 2
---

# Créer un compte pour enregistrer

<div class="sequence-panel" role="img" aria-label="Créer un compte pour enregistrer">

```mermaid {scale: 0.51, theme: 'base', themeVariables: {fontFamily: 'Arial, sans-serif', primaryColor: '#fff4d5', primaryTextColor: '#1a1300', primaryBorderColor: '#ad7300', lineColor: '#1a1300', actorBkg: '#fff4d5', actorBorder: '#ad7300', actorTextColor: '#1a1300', noteBkgColor: '#ffe8aa', noteTextColor: '#1a1300', noteBorderColor: '#ffb300'}, sequence: {useMaxWidth: true, actorFontSize: 14, messageFontSize: 14, noteFontSize: 13, actorMargin: 130, width: 125, height:60 , messageMargin: 12, noteMargin: 4, boxMargin: 4, boxTextMargin: 3, diagramMarginX: 26, diagramMarginY: 16, wrap: true, mirrorActors: true}}
sequenceDiagram
    actor P as Personne
    participant V as Interface Vue
    participant S as Stores Pinia
    participant C as Client API
    participant A as API DRF
    participant D as Base de données
    P->>V: Créer un compte pour enregistrer
    V->>S: practice.prepareAuthentication()
    Note over V,S: Brouillon conservé · reprise après authentification
    V->>V: Route register · AuthView / RegisterForm
    P->>V: Renseigner et soumettre le formulaire
    V->>V: Valider les champs côté front
    V->>S: auth.register(données)
    S->>C: registerUser(données)
    C->>A: POST /api/v1/auth/register/
    A->>D: Vérifier l’unicité de l’email
    D-->>A: Email présent ou absent
    Note over A,D: Deux issues : email déjà utilisé (38) ou inscription valide (39)
```

</div>

<style scoped>
.sequence-panel { position: absolute; inset: 80px 0 0; }
.sequence-panel :deep(.mermaid) { display: flex; justify-content: center; align-items: flex-start; width: 95%; height: 95%; }
</style>

---
class: pe-section-content !bg-white
title: Cas d’erreur — email déjà utilisé
preload: false
level: 2
---

# Cas d’erreur : email déjà utilisé

<div class="sequence-panel" role="img" aria-label="Cas d’erreur — email déjà utilisé">

```mermaid {scale: 0.8, theme: 'base', themeVariables: {fontFamily: 'Arial, sans-serif', primaryColor: '#fff4d5', primaryTextColor: '#1a1300', primaryBorderColor: '#ad7300', lineColor: '#1a1300', actorBkg: '#fff4d5', actorBorder: '#ad7300', actorTextColor: '#1a1300', noteBkgColor: '#ffe8aa', noteTextColor: '#1a1300', noteBorderColor: '#ffb300'}, sequence: {useMaxWidth: true, actorFontSize: 14, messageFontSize: 14, noteFontSize: 13, actorMargin: 60, width: 125, height: 60, messageMargin: 12, noteMargin: 4, boxMargin: 4, boxTextMargin: 3, diagramMarginX: 16, diagramMarginY: 16, wrap: true, mirrorActors: true}}
sequenceDiagram
    actor P as Personne
    participant V as Interface Vue
    participant S as Stores Pinia<br/>practice / auth
    participant C as Client API<br/>src/api · Axios
    participant A as API DRF
    participant D as Base de données
    A-->>C: 400 · erreur de validation sur email
    C-->>S: Rejet de registerUser()
    S-->>V: Erreur propagée à RegisterForm
    V-->>P: Afficher l’erreur sous le champ email
    Note over V,S: Rester sur Register · brouillon conservé
    P->>V: Corriger l’email et soumettre à nouveau
```

</div>

<style scoped>
.sequence-panel { position: absolute; inset: 84px 0 0; }
.sequence-panel :deep(.mermaid) { display: flex; justify-content: center; align-items: flex-start; width: 95%; height: 95%; }
</style>

---
class: pe-section-content !bg-white
title: Inscription validée
preload: false
level: 2
---

# Inscription validée

<div class="sequence-panel" role="img" aria-label="Inscription validée">

```mermaid {scale: 0.42, theme: 'base', themeVariables: {fontFamily: 'Arial, sans-serif', primaryColor: '#fff4d5', primaryTextColor: '#1a1300', primaryBorderColor: '#ad7300', lineColor: '#1a1300', actorBkg: '#fff4d5', actorBorder: '#ad7300', actorTextColor: '#1a1300', noteBkgColor: '#ffe8aa', noteTextColor: '#1a1300', noteBorderColor: '#ffb300'}, sequence: {useMaxWidth: true, actorFontSize: 18, messageFontSize: 16, noteFontSize: 14, actorMargin: 64, width: 125, height: 55, messageMargin: 7, noteMargin: 4, boxMargin: 4, boxTextMargin: 3, diagramMarginX: 12, diagramMarginY: 20, wrap: false, mirrorActors: true}}
sequenceDiagram
    actor P as Personne
    participant V as Interface Vue
    participant S as Stores Pinia
    participant C as Client API
    participant A as API DRF
    participant D as Base de données
    Note over A,D: Données validées · mot de passe haché
    A->>D: Créer le compte
    A-->>C: 201 · compte créé
    C-->>S: Inscription réussie
    S->>C: loginUser(email, mot de passe)
    C->>A: POST /api/v1/auth/token/
    A->>D: Rechercher le compte pour vérifier le mot de passe
    A-->>C: 200 · access JWT + cookie refresh HttpOnly
    C-->>S: Access token conservé en mémoire
    Note over S,D: getCurrentUser() → GET /users/me/ authentifié → profil chargé
    S-->>V: Connexion terminée
    V-->>P: Retour à PauseView · brouillon retrouvé
    P->>V: Enregistrer ma pause
    V->>S: submitAuthenticatedPause()
    S->>C: createPause(payload)
    C->>A: POST /api/v1/pauses/ · Bearer JWT + contenu
    A->>D: Créer la pause liée à request.user et ses associations
    A-->>C: 201 · pause
    C-->>S: Succès · reset() du brouillon
    S-->>V: Enregistrement terminé
    V-->>P: Retour à l’accueil connecté (Home)
```

</div>

<style scoped>
.sequence-panel { position: absolute; inset: 70px 0 0; }
.sequence-panel :deep(.mermaid) { display: flex; justify-content: center; align-items: flex-start; width: 100%; height: 100%; }
</style>
---
class: pe-section-content
level: 2
title: Composable useGender
---
# Composable useGender

<img src="/useGender.png" class="code-capture" />

<style>
  img {
    display: block;
    width: 700px;
    height:auto;
    margin-inline: auto;
  }
</style>
---
class: pe-section-content
level: 2
title: Composable useGender
---
# Composable useGender

<img src="/PauseDetailview.png" class="code-capture" />

<style>
  img {
    display: block;
    height: 90%;
    width: auto;
    margin-inline: auto;
  }
</style>
---
layout: center
class: pe-section
---

# Tests

---
layout: center
class: pe-section
---

# Déploiement


---
layout: center
class: pe-section
---

# Difficultés & Défis


---
layout: center
class: pe-section
---

# Evolutions à venir


Suppressions des templates Django, nettoyage des dépendances
Toutes les pages légales
Page de contact,
Réinitialisation du mot de passe
Page FAQ

---

# Veille


---

# Documentation


---
hideInToc: true
class: pe-section
layout: center
---

# Merci


<PoweredBySlidev mt-10 />
