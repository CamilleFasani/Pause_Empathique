<script setup>
import { useNav, useSlideContext } from '@slidev/client'

const { $page } = useSlideContext()
const { total } = useNav()
</script>

<template>
  <div v-if="$page > 1" class="slide-page-number" :aria-label="`Diapositive ${$page} sur ${total}`">
    {{ $page }}/{{ total }}
  </div>
</template>

<style scoped>
.slide-page-number {
  position: absolute;
  right: 20px;
  bottom: 12px;
  z-index: 10;
  font-family: var(--font-body);
  font-size: 11px;
  font-variant-numeric: tabular-nums;
  line-height: 1;
  color: var(--color-black);
  opacity: 0.45;
  pointer-events: none;
}
</style>
