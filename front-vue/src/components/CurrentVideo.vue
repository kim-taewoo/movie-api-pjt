<template>
  <div>
    <v-row class="wrapper">
      <iframe
        :src="'https://www.youtube.com/embed/' + video.id.videoId"
        allowfullscreen
        frameborder="0"
        class="video"
      ></iframe>
    </v-row>

    <h4 class="mt-4">{{ video.snippet.title }}</h4>
    <hr class="white">
    <h6>
      {{ video.snippet.channelTitle }} |
      {{ new Date(video.snippet.publishedAt).toLocaleString() }}
    </h6>
    <p class="card-text">{{ video.snippet.description }}</p>
  </div>
</template>

<script>
export default {
  name: 'CurrentVideo',
  props: {
    video: {
      type: Object,
      required: true,
    },
  },
};
</script>

<style>
.wrapper {
  position: relative;
  width: 100%;
  height: 0;
  padding-bottom: 56.25%;
}
.video {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
</style>
