<template>
    <v-radio-group class="mt-0 pb-1 justify-end" hide-details v-model="row" row>
      <v-radio color="red" v-for="option in options" :key="option.label" :label="option.label" :value="option.value"></v-radio>
    </v-radio-group>
</template>

<script>
export default {
  data() {
    return {
      row: 'radio-1',
      options: [
        {
          label: '높은 평점순',
          value: 'ratingDesc'
        },
        {
          label: '낮은 평점순',
          value: 'ratingAsc'
        },
        {
          label: '최근 영화순',
          value: 'dateDesc'
        },
        {
          label: '관객수순',
          value: 'audienceDesc'
        },
      ]
    };
  },
};
</script>

<style></style>
