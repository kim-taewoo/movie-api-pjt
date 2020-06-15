<template>
  <v-card class="pa-4" light>

    <v-row>
      <v-col class="py-0" cols="12">
        <v-chip label class="ma-1" color="indigo" text-color="white">
          <v-avatar left>
            <v-icon>mdi-account-circle</v-icon>
          </v-avatar>
          평점: {{movie.rating}}
        </v-chip>
        <v-chip label class="ma-1" color="indigo" text-color="white">
          <v-avatar left>
            <v-icon>mdi-account-circle</v-icon>
          </v-avatar>
          개봉일: {{movie.pub_date}}
        </v-chip>
        <v-chip label class="ma-1" color="indigo" text-color="white">
          <v-avatar left>
            <v-icon>mdi-account-circle</v-icon>
          </v-avatar>
          {{movie.runtime}}
        </v-chip>
        <v-chip label class="ma-1" color="indigo" text-color="white">
          <v-avatar left>
            <v-icon>mdi-account-circle</v-icon>
          </v-avatar>
          {{movie.audits}}
        </v-chip>
        <v-chip label class="ma-1" color="indigo" text-color="white">
          <v-avatar left>
            <v-icon>mdi-account-circle</v-icon>
          </v-avatar>
          <!-- 장르: {{movie.genres[0].name}} -->
        </v-chip>
        <v-chip label class="ma-1" color="indigo" text-color="white">
          <v-avatar left>
            <v-icon>mdi-account-circle</v-icon>
          </v-avatar>
          <!-- 감독: {{movie.directors[0].name}} -->
        </v-chip>
        <v-chip label class="ma-1" color="indigo" text-color="white">
          <v-avatar left>
            <v-icon>mdi-account-circle</v-icon>
          </v-avatar>
          <!-- {{movie.nations[0].name}} -->
        </v-chip>
        <v-chip label class="ma-1" color="indigo" text-color="white">
          <v-avatar left>
            <v-icon>mdi-account-circle</v-icon>
          </v-avatar>
          <!-- 배우: {{movie.actors[0].name}} -->
        </v-chip>
      </v-col>
    </v-row>

    <v-row class="">
      <v-col cols="12">
        <p>{{movie.overview}}</p>
      </v-col>
    </v-row>
  </v-card>
</template>

<script>
export default {
  props: ['movie']
};
</script>

<style></style>
