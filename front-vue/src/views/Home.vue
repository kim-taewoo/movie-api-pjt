<template>
  <div>
    <v-row>
      <v-col cols="12" sm="6">
        <ImageGallery />
      </v-col>
      <v-col cols="12" sm="6">
        <Trailers class="mt-3 mt-sm-0" />
      </v-col>
    </v-row>
  </div>
</template>

<script>
import ImageGallery from '@/components/ImageGallery.vue';
import Trailers from '@/components/Trailers.vue';

export default {
  name: 'Home',
  components: {
    ImageGallery,
    Trailers,
  },
};
</script>
