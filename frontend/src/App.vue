<template>
  <div>
    <input ref="image" v-on:change="handleFileUpload()" type="file" />
    <div v-if="toSend">
      {{ toSend.name }}
      <!-- {{file.files[0].size}} -->
      File uploaded
    </div>
    <button @click="uploadFile()">Upload</button>
  </div>
</template>

<script setup>
import axios from "axios";
import { ref } from "vue";

const image = ref(null);

const toSend = ref(null);

const handleFileUpload = async () => {
  // debugger;
  console.log(image.value.files.length);
  console.log("selected file", image.value.files[0]);
  toSend.value = image.value.files[0];
  //Upload to server
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
    .post("http://localhost:5000/upload", formData, {
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
