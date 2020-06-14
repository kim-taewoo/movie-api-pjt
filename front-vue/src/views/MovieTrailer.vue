<template>
  <div>
    <v-row justify="center" align="center">
      <v-col cols="12" sm="8">
        <v-card v-if="videos.length">
          <v-row class="wrapper">
            <iframe
              :src="'https://www.youtube.com/embed/' + videos[0].id.videoId"
              allowfullscreen
              frameborder="0"
              class="video"
            ></iframe>
          </v-row>
          <v-card-text>
            <h4 class="mt-4">{{ videos[0].snippet.title }}</h4>
            <hr class="white" />
            <h6>
              {{ videos[0].snippet.channelTitle }} |
              {{ new Date(videos[0].snippet.publishedAt).toLocaleString() }}
            </h6>
            <p class="card-text mt-3">{{ videos[0].snippet.description }}</p>
          </v-card-text>
          <v-card-actions>
            <v-btn to="/" color="red" text>
              홈으로 돌아가기
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import axios from 'axios';

const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY; // 비활성화된 키
const API_URL = 'https://www.googleapis.com/youtube/v3/search';
export default {
  name: 'MovieTrailer',
  props: ['title'],
  data() {
    return {
      loading: false,
      videos: [],
    };
  },
  created() {
    this.onInputChange(this.title + '예고편');
  },
  methods: {
    onInputChange: async function(inputText) {
      this.loading = true;
      try {
        const response = await axios.get(API_URL, {
          params: {
            key: API_KEY,
            part: 'snippet',
            type: 'video',
            q: inputText,
            maxResults: 1,
          },
        });
        this.videos = response.data.items;
        this.loading = false;
      } catch (error) {
        console.error(error);
        this.loading = false;
      }
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
