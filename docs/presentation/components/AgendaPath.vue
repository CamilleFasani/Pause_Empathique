<script setup lang="ts">
import { computed } from 'vue'
import { useIsSlideActive, useNav } from '@slidev/client'

const { tocTree, isPrintMode } = useNav()
const active = useIsSlideActive()
const parts = computed(() => tocTree.value.filter(item => item.titleLevel === 1))

function wrapTitle(title: string, maxLength = 22) {
  const lines: string[] = []
  for (const word of title.split(/\s+/)) {
    const last = lines.length - 1
    if (last < 0 || `${lines[last]} ${word}`.length > maxLength)
      lines.push(word)
    else
      lines[last] += ` ${word}`
  }
  return lines
}

// The entry is 140 px above the bottom, aligned with slide 2's timeline.
const anchors = [
  { x: 65, y: 350, side: 'above', maxLength: 14 },
  { x: 170, y: 425, side: 'below', gap: 40 },
  { x: 280, y: 435, side: 'below', maxLength: 16 },
  { x: 275, y: 310, side: 'right' },
  { x: 220, y: 210, side: 'left' },
  { x: 320, y: 175, side: 'above' },
  { x: 420, y: 270, side: 'right' },
  { x: 535, y: 365, side: 'below' },
  { x: 670, y: 310, side: 'right' },
  { x: 700, y: 245, side: 'left' },
  { x: 760, y: 160, side: 'right' },
  { x: 850, y: 110, side: 'left' },
  { x: 900, y: 35, side: 'right' },
]
const stops = computed(() => parts.value.map((item, index) => {
  const anchor = anchors[index % anchors.length]
  const lines = wrapTitle(item.title || '', anchor.maxLength)
  const beside = anchor.side === 'left' || anchor.side === 'right'
  const tx = anchor.x + (anchor.side === 'left' ? -25 : anchor.side === 'right' ? 25 : 0)
  const ty = beside
    ? anchor.y - (lines.length - 1) * 10
    : anchor.side === 'above'
      ? anchor.y - 28 - (lines.length - 1) * 20
      : anchor.y + (anchor.gap ?? 28)
  return {
    ...item,
    ...anchor,
    tx,
    ty,
    align: anchor.side === 'left' ? 'end' : anchor.side === 'right' ? 'start' : 'middle',
    lines,
  }
}))
</script>

<template>
  <nav class="agenda-path" aria-label="Sommaire des parties">
    <svg viewBox="0 0 980 552" preserveAspectRatio="none" :class="{ active, printed: isPrintMode }" aria-labelledby="agenda-title">
      <title id="agenda-title">Parcours de la présentation</title>
      <path class="agenda-line" d="M0 412 C45 430 35 355 65 350 C105 330 135 405 170 425 C205 450 245 465 280 435 C345 390 310 350 275 310 C240 270 205 250 220 210 C230 165 280 170 320 175 C400 170 398 235 420 270 C445 335 490 365 535 365 C600 370 665 350 670 310 C675 285 690 270 700 245 C705 210 720 185 760 160 C800 140 830 140 850 110 C880 75 890 70 900 35 C905 15 905 0 905 -10" pathLength="1" />
      <a v-for="stop in stops" :key="stop.no" :href="stop.path" class="agenda-stop" :aria-label="`${stop.title}, diapositive ${stop.no}`">
        <circle class="agenda-hit" :cx="stop.x" :cy="stop.y" r="21" />
        <circle class="agenda-dot" :cx="stop.x" :cy="stop.y" r="9" />
        <text dominant-baseline="central" :x="stop.tx" :y="stop.ty" :style="{ textAnchor: stop.align }">
          <tspan v-for="(line, index) in stop.lines" :key="index" :x="stop.tx" :dy="index === 0 ? 0 : 20">{{ line }}</tspan>
        </text>
      </a>
    </svg>
  </nav>
</template>

<style scoped>
.agenda-path { position: absolute; inset: 0; pointer-events: none; }
svg { display: block; width: 100%; height: 100%; overflow: visible; }
.agenda-line { fill: none; stroke: var(--color-brand-primary); stroke-width: 5; stroke-linecap: round; stroke-dasharray: 1; stroke-dashoffset: 1; }
.agenda-stop { opacity: 0; cursor: pointer; pointer-events: auto; }
.agenda-hit { fill: transparent; }
.agenda-dot { fill: var(--color-bg-card); stroke: var(--color-brand-primary); stroke-width: 5; }
text { fill: var(--color-black); font-family: var(--font-body); font-size: 15px; paint-order: stroke; stroke: var(--color-bg-page); stroke-width: 5px; stroke-linejoin: round; font-weight: 600; text-anchor: middle; }
.active .agenda-line { animation: agenda-draw 0.4s linear both; }
.active .agenda-stop { animation: agenda-reveal 0.18s ease-out 0.45s both; }
.agenda-stop:hover .agenda-dot, .agenda-stop:focus-visible .agenda-dot { fill: var(--color-brand-primary); }
.agenda-stop:focus-visible { outline: none; }
.agenda-stop:focus-visible text { text-decoration: underline; }
@keyframes agenda-draw { to { stroke-dashoffset: 0; } }
@keyframes agenda-reveal { from { opacity: 0; } to { opacity: 1; } }
.printed .agenda-line { animation: none; stroke-dashoffset: 0; }
.printed .agenda-stop { animation: none; opacity: 1; }
@media (prefers-reduced-motion: reduce), print {
  .agenda-line { animation: none !important; stroke-dashoffset: 0; }
  .agenda-stop { animation: none !important; opacity: 1; }
}
</style>
