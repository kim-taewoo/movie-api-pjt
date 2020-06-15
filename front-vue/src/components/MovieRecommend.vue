<template>
  <v-card class="pa-4" light>
    <v-card-title class="pa-0">Ai 추천</v-card-title>
    <v-row dense>
      <v-col v-for="(recommend, idx) in recommends" :key="idx" cols="3">
        <v-hover v-slot:default="{ hover }">
          <v-card
            class="recommendItem"
            :elevation="hover ? 12 : 2"
            :class="{ 'on-hover': hover }"
            light
            :to="{ name: 'MovieDetail', params: { id: recommend.id } }"
          >
            <v-img
              :src="recommend.poster"
              class="white--text align-end"
              gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
              height="200px"
            >
              <v-card-title v-text="recommend.title"></v-card-title>
            </v-img>
          </v-card>
        </v-hover>
      </v-col>
    </v-row>
  </v-card>
</template>

<script>
import { mapActions, mapState } from 'vuex';
export default {
  props: ['movieId'],
  computed: {
    ...mapState(['recommends']),
  },
  methods: {
    ...mapActions(['fetchRecommends']),
  },
  created() {
    this.fetchRecommends(this.movieId);
  },
};
</script>

<style>
.v-application a {
  text-decoration: none !important;
  color: white;
}

.recommendItem {
  transition: opacity 0.4s ease-in-out;
  cursor: pointer;
}

.recommendItem:not(.on-hover) {
  opacity: 0.85;
}
</style>
