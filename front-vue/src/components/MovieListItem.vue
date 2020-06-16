<template>
  <v-card
    :to="{ name: 'MovieDetail', params: { id: movie.id } }"
    outlined
    style="overflow:hidden"
    light
  >
    <div class="d-flex flex-no-wrap justify-start">
      <v-avatar size="130" tile>
        <v-img :src="movie.poster" :lazy-src="`https://picsum.photos/10/6`">
          <template v-slot:placeholder>
            <v-row class="fill-height ma-0" align="center" justify="center">
              <v-progress-circular
                indeterminate
                color="grey lighten-5"
              ></v-progress-circular>
            </v-row>
          </template>
        </v-img>
      </v-avatar>
      <div>
        <v-card-title class="headline black--text">{{
          movie.title
        }}</v-card-title>
        <v-card-subtitle class="pb-1" v-text="movie.directors[0].name"></v-card-subtitle>
        <div class="pa-2">
          <span v-for="(chip, i) in chips" :key="i">
            <v-chip
              v-if="typeof chip.values !== 'object'"
              class="ma-1"
              small
              color="indigo"
              text-color="white"
            >
              {{ chip.key }}: {{ chip.values }}
            </v-chip>
          </span>
        </div>
      </div>
    </div>
  </v-card>
</template>

<script>
export default {
  props: ['movie'],
  computed: {
    chips() {
      return [
        {
          key: '장르',
          color: 'indigo',
          values: this.movie.genres[0].name,
        },
        {
          key: '런타임',
          color: 'indigo',
          values: this.movie.runtime + '분',
        },
        {
          key: '개봉일',
          color: 'indigo',
          values: this.movie.pub_date,
        },
        {
          key: '연령',
          color: 'indigo',
          values: this.movie.audits,
        },
        {
          key: '누적관객',
          color: 'indigo',
          values: this.movie.audi_cnt + '명',
        },
      ];
    },
  },
};
</script>

<style></style>
