---
theme: default
hideInToc: true
background: /cover.jpg
title: Pause Empathique
info: |
  ## Slidev Starter Template
  Presentation slides for developers.

  Learn more at [Sli.dev](https://sli.dev)
# apply UnoCSS classes to the current slide
class: text-center
# https://sli.dev/features/drawing
drawings:
  persist: false
# slide transition: https://sli.dev/guide/animations.html#slide-transitions
transition: slide-left
# enable Comark Syntax: https://comark.dev/syntax/markdown
comark: true
# duration of the presentation
duration: 40min
---
<!-- Photo de <a href="https://unsplash.com/fr/@mrkarlphoto?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Mr Karl</a>sur <a href="https://unsplash.com/fr/photos/photographie-de-vue-aerienne-du-desert-yFmh736pYsg?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a> -->

# Pause Empathique
<p class="title">Présentation au titre : Concepteur Développeur d'Applications</p>
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
    <!-- <span class="intro-eyebrow">FAISONS CONNAISSANCE</span> -->
    <h1>Bonjour,<br>je suis <span>Camille Fasani.</span></h1>
    <p>J’apprends le développement web depuis janvier 2025.</p>
  </div>
  <ol class="intro-timeline">
    <li>
      <span class="intro-date">JANVIER 2025</span>
      <h2>Premiers pas</h2>
      <p>Apprentissage du développement web</p>
    </li>
    <li>
      <span class="intro-date">JANVIER 2026</span>
      <h2>Titre DWWM</h2>
      <p>Une première étape validée</p>
    </li>
    <li>
      <span class="intro-date">DEPUIS OCTOBRE 2025</span>
      <h2>Alternance</h2>
      <p>Développeuse Full-Stack<br>chez <strong>cogito</strong></p>
    </li>
  </ol>
</div>

<style scoped>
.intro {
  display: flex;
  flex-direction: column;
  justify-content: center;
  height: 100%;
  gap: 2.5rem;
}
.intro-eyebrow {
  display: inline-block;
  padding: 0.35rem 0.8rem;
  border-radius: var(--radius-btn);
  background: var(--color-brand-primary);
  font-size: 0.7rem;
  font-weight: 700;
  letter-spacing: 0.12em;
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
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 1.25rem;
  margin: 0;
  padding: 0;
  list-style: none;
}
.intro-timeline li {
  position: relative;
  margin: 0;
  padding: 1.2rem;
  border-radius: var(--radius-card);
  background: var(--color-bg-card);
}
.intro-date {
  font-size: 0.7rem;
  font-weight: 700;
  letter-spacing: 0.07em;
}
.intro-timeline h2 {
  margin: 0.65rem 0 0.5rem;
  font-size: 1.4rem;
}
.intro-timeline p {
  margin: 0;
  font-size: 0.9rem;
  line-height: 1.5;
}
</style>


---
hideInToc: true
---

<div class="pe-heading">
  <img src="/logo.png" alt="" />
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
  width: 85%;
  margin: 1.5rem auto 0;
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
  <img src="/persona1.png" alt ="" class="persona"/>
  <img src="/persona2.png" alt ="" class="persona"/>
  <img src="/persona3.png" alt ="" class="persona"/>
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
  margin: 0;
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

# V1 vers la V2


<!-- Souhait de partir de l'existant pour me rapprocher du travail en entreprise où l'on part rarement de zéro, donc travailler avec une code base,  et organiser une migration -->
---
class: pe-section-content
title: Objectifs
level: 2
---

# V1 vers la V2

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
  margin: 2rem 0 0;
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

<div class="pe-heading">
  <img src="/logo.png" alt="" />
  <h1>Gestion de projet</h1>
</div>


---

<div class="pe-heading">
  <img src="/logo.png" alt="" />
  <h1>Road Map - Diagramme de Gant</h1>
</div>


---

## Kanban

---

## AI Management project

---

<div class="pe-heading">
  <img src="/logo.png" alt="" />
  <h1>Conception</h1>
</div>

## Base de Données
### RGPD
### Merise

---

## Parcours utilisateur - User flow


---

## Identité visuelle - Charte graphique

---

## Wireframes
---

## Maquettes Hautes Fidélité

---

## Accessibilité ( & Ecoconception ?)

---

<div class="pe-heading">
  <img src="/logo.png" alt="" />
  <h1>Spécifications techniques</h1>
</div>

## Stack


---

## Environnement de travail

### Git / GitHub
---

### CI/CD

---

### Docker

---

### Architecture

---

### ORM

---

<div class="pe-heading">
  <img src="/logo.png" alt="" />
  <h1>Migration V1 vers V2</h1>
</div>

---

<div class="pe-heading">
  <img src="/logo.png" alt="" />
  <h1>Démo 🍿</h1>
</div>


---

<div class="pe-heading">
  <img src="/logo.png" alt="" />
  <h1>Zoom sur : pratiquer sans compte</h1>
</div>


---

<div class="pe-heading">
  <img src="/logo.png" alt="" />
  <h1>Tests</h1>
</div>


---

<div class="pe-heading">
  <img src="/logo.png" alt="" />
  <h1>Déploiement</h1>
</div>


---

<div class="pe-heading">
  <img src="/logo.png" alt="" />
  <h1>Difficultés & Défis</h1>
</div>

---

<div class="pe-heading">
  <img src="/logo.png" alt="" />
  <h1>Evolutions à venir</h1>
</div>


---
hideInToc: true
---

<div class="pe-heading">
  <img src="/logo.png" alt="" />
  <h1>Merci</h1>
</div>

<PoweredBySlidev mt-10 />
