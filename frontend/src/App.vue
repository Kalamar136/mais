<template>
  <div class="flex items-center justify-center h-screen w-full">
    <div
      class="bg-white p-10 rounded-xl shadow-xl border-solid border-2 border-gray-100"
    >
      <div>
        <div v-if="state == 0">
          <p class="text-2xl mb-2">Garbage Classification</p>
          <p>Select an image to upload:</p>
          <div
            class="uploadedBox"
            :class="toSend ? 'uploaded' : 'needToUpload'"
            @click="chooseFile"
            :style="{ 'background-image': `url(${preview})` }"
          >
            <p :class="toSend ? 'hidden' : ''">Click to upload an image</p>
            <p :class="toSend ? '' : 'hidden'">Click to upload a new image</p>
          </div>
          <div class="">
            <input
              class="hidden form-control block w-full px-2 py-1 text-sm font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
              ref="image"
              v-on:change="handleFileUpload()"
              type="file"
            />
          </div>
          <div class="w-full text-right flex justify-end">
            <button
              :class="!toSend ? 'disabled' : 'blue'"
              :disabled="!toSend"
              class="btn"
              @click="uploadFile()"
            >
              Upload &rarr;
            </button>
          </div>
        </div>
        <div v-if="state == 1">
          <LoadingPage />
        </div>
        <div v-if="state == 2">
          <div v-if="results">
            <ResultsDisplay :results="results" />
          </div>
          <div class="w-full text-center md:text-left">
            <button class="btn blue" @click="reset()">&larr; Retry</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import LoadingPage from "./components/LoadingPage.vue";
import ResultsDisplay from "./components/ResultsDisplay.vue";
import axios from "axios";
import { ref } from "vue";

const state = ref(0);

const image = ref(null);

const results = ref(null);

const toSend = ref(null);
const preview = ref(null);

const handleFileUpload = async () => {
  // debugger;
  console.log(image.value.files.length);
  console.log("selected file", image.value.files[0]);
  toSend.value = image.value.files[0];
  preview.value = URL.createObjectURL(toSend.value);
  //Upload to server
};

const chooseFile = () => {
  image.value.click();
};

const reset = () => {
  results.value = null;
  preview.value = null;
  toSend.value = null;
  state.value = 0;
};

const uploadFile = () => {
  let formData = new FormData();
  formData.append("file", toSend.value);
  state.value = 1;
  console.log("sending");
  axios
    .post("http://20.121.50.123:5000/upload", formData, {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    })
    .then(function (response) {
      state.value = 2;
      results.value = response.data;
      console.log(response);
    })
    .catch(function (error) {
      console.log(error);
    });
};
</script>

<style scoped lang="css">
* {
  @apply transition-all;
}
.previewBlock {
  display: block;
  cursor: pointer;
  width: 300px;
  height: 280px;
  margin: 0 auto 20px;
  background-position: center center;
  background-size: cover;
}

.btn {
  @apply py-3 px-5 rounded-full mt-2;
}

.blue {
  @apply bg-blue-400 hover:bg-blue-600 text-white;
}

.disabled {
  @apply bg-gray-300 text-black;
}

.uploadedBox {
  @apply flex items-center justify-center cursor-pointer h-48 md:h-96 w-full md:w-96 m-0 my-2 rounded-xl bg-contain bg-no-repeat bg-center border-2 border-solid border-gray-200;
}

.needToUpload {
  @apply flex text-gray-400 hover:text-gray-500 bg-gray-100 hover:bg-gray-200 m-0 my-2 border-dashed border-4 border-gray-300;
}

.uploaded {
  @apply text-transparent hover:text-white hover:bg-red-400 hover:!bg-none hover:border-dashed hover:border-4 hover:border-red-500;
}

.input {
}
</style>
