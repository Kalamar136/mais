<template>
  <div class="w-[70vw]">
    <div class="w-full text-center">
      <p>We think that is a:</p>
      <p class="text-xl">{{maxKey}}</p>
    </div>
    <div class="flex">
      <div class="w-1/12 h-full" :key="key" v-for="key in keys">
        <div>
          <div class="h-[50vh] relative">
            <SingleBar
              :color="colors[key]"
              :max="max"
              :value="Number(props.results[key])"
            />
          </div>
          <div class="h-12 text-center">
            {{ key }}
          </div>
        </div>
      </div>
    </div>
    <div class="w-full text-center">Probability of each classification</div>
  </div>
</template>
<script setup>
import SingleBar from "./SingleBar.vue";
import { defineProps, computed } from "vue";

const props = defineProps(["results"]);

const colors = {
  Battery: "bg-red-600",
  Biological: "bg-orange-500",
  "Brown Glass": "bg-yellow-500",
  Cardboard: "bg-lime-400",
  Clothes: "bg-green-400",
  "Green Glass": "bg-teal-400",
  Metal: "bg-cyan-400",
  Paper: "bg-blue-400",
  Plastic: "bg-violet-400",
  Shoes: "bg-fuchsia-400",
  Trash: "bg-pink-700",
  "White Glass": "bg-rose-500",
};

const keys = computed(() => Object.keys(props.results));

const values = computed(() => Object.values(props.results).map(Number));

const max = computed(() => Math.max.apply(false, values.value));

const maxKey = computed(() => keys.value[values.value.indexOf(max.value)])
</script>
