<template>
  <v-radio-group class="mt-0 pb-1 justify-end" hide-details v-model="row" row>
    <v-radio
      color="red"
      v-for="option in options"
      :key="option.label"
      :label="option.label"
      :value="option.value"
    ></v-radio>
  </v-radio-group>
</template>

<script>
import {mapActions} from 'vuex'
export default {
  data() {
    return {
      row: '-rating',
      options: [
        {
          label: '높은 평점순',
          value: '-rating',
        },
        {
          label: '낮은 평점순',
          value: 'rating',
        },
        {
          label: '최근 영화순',
          value: '-pub_date',
        },
        {
          label: '관객수순',
          value: '-audi_cnt',
        },
      ],
    };
  },
  methods: {
    ...mapActions(['fetchMovies'])
  },
  created() {
    this.fetchMovies({
      params: {
        page: 1,
        order_by: '-rating',
      },
    });
  },
  watch: {
    row(type) {
      this.$emit('onTypeSelect', type)
    }
  }
};
</script>

<style></style>
