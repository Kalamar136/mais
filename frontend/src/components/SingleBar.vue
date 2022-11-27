<template>
  <div
    class="px-2 w-full h-8 text-xs bottom-0 absolute"
    :style="{ height: scaledValue + 'vh' }"
  >
  <div :class="color" class="w-full h-full">

  </div>  
  <!-- {{ props.max }} -->
    <!-- {{ scaledValue.toFixed(0) }} -->
  </div>
</template>
<script setup>
import { defineProps, computed } from "vue";

const props = defineProps(["max", "value", "color"]);

const scaleFactor = computed(() => {
  return 25 / props.max;
});

const scaledValue = computed(() => {
  return scaleFactor.value * (props.value + props.max);
});
</script>
