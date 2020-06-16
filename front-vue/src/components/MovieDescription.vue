<template>
  <v-card class="pa-4" light>
    <v-row>
      <v-col
        v-for="(chip, idx) in chips"
        :key="idx"
        class="py-0"
        cols="12"
        sm="6"
      >
        <v-chip
          v-if="typeof chip.values !== 'object'"
          label
          class="ma-1"
          color="indigo"
          text-color="white"
        >
          <!-- <v-avatar left>
            <v-icon>mdi-account-circle</v-icon>
          </v-avatar> -->
          {{ chip.key }}: {{ chip.values }}
        </v-chip>

        <v-menu
          v-else
          v-model="chip.menu"
          bottom
          right
          transition="scale-transition"
          origin="top left"
        >
          <template v-slot:activator="{ on }">
            <v-chip class="ma-1" label color="indigo" text-color="white" v-on="on">
              {{chip.key}} (전체보기)
            </v-chip>
          </template>
          <v-card width="300">
            <v-list dark>
              <v-list-item>
                <v-list-item-content>
                  <v-list-item-title>{{chip.key}}</v-list-item-title>
                </v-list-item-content>
                <v-list-item-action>
                  <v-btn icon @click="menu = false">
                    <v-icon>mdi-close-circle</v-icon>
                  </v-btn>
                </v-list-item-action>
              </v-list-item>
            </v-list>
            <v-list class="d-flex justify-center">
                <v-row justify="center" align="center">
                  <v-col cols="10" class="pa-2">
                    <v-chip class="ma-1" small v-for="(value,index) in chip.values" :key="index">{{value.name}}</v-chip>
                  </v-col>
                </v-row>

            </v-list>
          </v-card>
        </v-menu>
      </v-col>
    </v-row>

    <v-row class="">
      <v-col cols="12">
        <p>{{ movie.overview }}</p>
      </v-col>
    </v-row>
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
          key: '국가',
          color: 'indigo',
          values: this.movie.nations[0].name,
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
        {
          key: '감독',
          color: 'indigo',
          values: this.movie.directors[0].name,
        },
        {
          key: '배우진',
          color: 'indigo',
          values: this.movie.actors,
        },
      ]
    }
  },
  data() {
    return {
    };
  },
};
</script>

<style></style>
