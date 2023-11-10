<template>
  <div>
    <p>{{ detail.snippet.title }}</p>
    <p>{{ detail.publishTime }} {{ detail.channelTitle }}</p>
    <iframe :src="" frameborder="0"></iframe>
    <p>{{ detail.snippet.description }}</p>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import axios from 'axios'

const router = useRouter()
const route = useRoute()
const detailVideo = ref('')

const APIKEY = 'AIzaSyAhQztu33_AxIlDPQAijbEWZbVW4AziO0c'
const youtubeURL = ref(`https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=20&q=${searchKeyword.value}&key=${APIKEY}`)

defineProps({
  detail: Object,
})

axios.get(youtubeURL.value)
  .then((res) => {
    videos.value = res.data.items
  })
  .catch((err) => {
    console.error(err)
  })
</script>

<style scoped>

</style>