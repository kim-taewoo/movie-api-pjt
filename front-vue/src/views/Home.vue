<template>
  <div class="home">
    <ImageGallery />
    <Trailers />
  </div>
</template>

<script>
import ImageGallery from '@/components/ImageGallery.vue'
import Trailers from '@/components/Trailers.vue'

export default {
  name: 'Home',
  components: {
    ImageGallery,
    Trailers
  }
}
</script>
