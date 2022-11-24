<template>
  <div class="flex items-center justify-center h-screen w-full">
    <div
      class="bg-white p-10 rounded-xl shadow-xl border-solid border-2 border-gray-100"
    >
      <div>
        <p class="text-2xl">Garbage Classification</p>
        <div>
          <div
            class="needToUpload"
            @click="chooseFile"
            :style="{ 'background-image': `url(${preview})` }"
          ></div>
          <div>
            <input
              class="form-control block w-full px-2 py-1 text-sm font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
              ref="image"
              v-on:change="handleFileUpload()"
              type="file"
            />
          </div>
          <div v-if="toSend">
            <button @click="uploadFile()">Upload</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import axios from "axios";
import { ref } from "vue";

const image = ref(null);

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

const uploadFile = () => {
  let formData = new FormData();
  formData.append("file", toSend.value);
  console.log("sending");
  // axios
  //   .get("http://localhost:5000")
  //   .then(function (response) {
  //     console.log(response);
  //   })
  //   .catch(function (error) {
  //     console.log(error);
  //   });
  // console.log("got");
  axios
    .post("http://3.89.138.240:5000/upload", formData, {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    })
    .then(function (response) {
      console.log(response);
    })
    .catch(function (error) {
      console.log(error);
    });
};
</script>

<style scoped lang="css">
* {
  @apply transition-all
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

.needToUpload {
  @apply block cursor-pointer h-96 w-96 bg-gray-100 hover:bg-gray-200 m-0 my-2 border-dashed border-4 border-gray-600 bg-contain bg-no-repeat bg-center;
}

.input {
}
</style>
