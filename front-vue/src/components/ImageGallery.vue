<template>
  <v-card color="white">
    <v-tabs light background-color="white" color="grey darken-4" centered>
      <v-tab @click="onTabClick('-pub_date')">현재상영작</v-tab>
      <v-tab @click="onTabClick('-rating')">평점순</v-tab>
      <v-tab @click="onTabClick('-audi_cnt')">관객순</v-tab>

      <v-tab-item v-for="n in 3" :key="n">
        <v-card light class="pb-4">
          <v-container fluid>
            <v-row>
              <v-col
                v-for="movie in movies"
                :key="movie.id"
                class="d-flex child-flex pa-1"
                cols="4"
              >
                <v-hover v-slot:default="{ hover }">
                  <v-card
                    flat
                    tile
                    class="d-flex galleryItem"
                    :elevation="hover ? 12 : 2"
                    :class="{ 'on-hover': hover }"
                    :to="{ name: 'MovieDetail', params: { id: movie.id, movie: movie } }"
                  >
                    <v-img
                      :src="movie.horizontal_poster"
                      :lazy-src="
                        `https://picsum.photos/10/6?image=${n * 5 + 10}`
                      "
                      aspect-ratio="1.0"
                      class="grey lighten-2"
                    >
                      <template v-slot:placeholder>
                        <v-row
                          class="fill-height ma-0"
                          align="center"
                          justify="center"
                        >
                          <v-progress-circular
                            indeterminate
                            color="grey lighten-5"
                          ></v-progress-circular>
                        </v-row>
                      </template>
                    </v-img>
                  </v-card>
                </v-hover>
              </v-col>
            </v-row>
          </v-container>
        </v-card>
        <div style="position:absolute;bottom:0;right:0;color:black">
          <v-btn :to="{ name: 'Movies' }" color="blue" small text>더보기</v-btn>
        </div>
      </v-tab-item>
    </v-tabs>
  </v-card>
</template>

<script>
import { mapState, mapActions } from 'vuex';

export default {
  name: 'ImageGallery',
  computed: {
    ...mapState(['movies']),
  },
  methods: {
    ...mapActions(['fetchMovies']),
    onTabClick(type) {
      this.fetchMovies({
        params: {
          page: 1,
          order_by: type,
        },
      });
    },
  },
  created() {
    this.fetchMovies({
      params: {
        page: 1,
        order_by: '-pub_date',
      },
    });
  },
};
</script>

<style>
.v-tab--active {
  color: black !important;
}

.galleryItem {
  transition: opacity 0.4s ease-in-out;
  cursor: pointer;
}

.galleryItem:not(.on-hover) {
  opacity: 0.85;
}
</style>
