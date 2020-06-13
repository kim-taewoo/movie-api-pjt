<template>
  <div>
    <v-row>
      <v-col cols="12" sm="6" offset-sm="3">
        <ImageGallery />
        <Trailers class="mt-4" />
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
