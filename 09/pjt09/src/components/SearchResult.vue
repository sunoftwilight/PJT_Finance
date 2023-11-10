<template>
  <div class="video">
    <p>{{ video.snippet.title }}</p>
    <div @click="goDetail(video.id.videoId)">
      <img  
        :src="video.snippet.thumbnails.medium.url" 
        alt="썸네일"
        :detail="video"
      >
    </div>
    <p>{{ video.snippet.description }}</p>
  </div>
</template>

<script setup>
defineProps({
  video: Object,
})

const goDetail = function (videoId) {
  router.push({name: 'detail', params:{ videoId }})
}
</script>

<style scoped>
.video {
  border: 1px solid black;
  margin: 5px;
  padding: 10px;
}
</style>