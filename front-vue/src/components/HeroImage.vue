<template>
  <v-parallax
    height="300"
    dark
    :src="movie.poster"
  >
    <v-row align="center" justify="center">
      <v-col class="text-center" cols="12">
        <h1 class="display-2 font-weight-thin mb-4">{{movie.title}}</h1>
        <h4 class="subheading">{{movie.sub_title}}</h4>
      </v-col>
    </v-row>
  </v-parallax>
</template>

<script>
export default {
  props: ['movie']
};
</script>

<style></style>
