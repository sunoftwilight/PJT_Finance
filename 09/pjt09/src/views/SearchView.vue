<template>
  <div>
    <p>뒤로가기</p>

    <h1>비디오 검색</h1>

    <div>
      <input type="text" v-model="searchKeyword" placeholder="검색어를 입력해 주세요.">
      <button @click="search">찾기</button>
    </div>

    <div v-for="video in videos">
      <SearchResult
        :video="video"
      />
    </div>

  </div>
</template>

<script setup>
import SearchResult from '@/components/SearchResult.vue'
import { ref, computed } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import axios from 'axios'

const router = useRouter()
const route = useRoute()
const videos = ref([])
const searchKeyword = ref('')

const search = function () {
  const APIKEY = 'AIzaSyAhQztu33_AxIlDPQAijbEWZbVW4AziO0c'
  const youtubeURL = ref(`https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=20&q=${searchKeyword.value}&key=${APIKEY}`)

  axios.get(youtubeURL.value)
    .then((res) => {
      videos.value = res.data.items
    })
    .catch((err) => {
      console.error(err)
    })
}
</script>

<style scoped>
</style>