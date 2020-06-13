<template>
  <v-row>
    <v-col cols="12" sm="6" offset-sm="3">
      <v-card color="white">
        <v-tabs light background-color="white" color="grey darken-4" centered>
          <v-tab>현재상영작</v-tab>
          <v-tab>평점순</v-tab>
          <v-tab>관객순</v-tab>

          <v-tab-item v-for="n in 3" :key="n">
            <v-card light>
              <v-container fluid>
                <v-row>
                  <v-col
                    v-for="n in 9"
                    :key="n"
                    class="d-flex child-flex pa-1"
                    cols="4"
                  >
                    <v-card flat tile class="d-flex">
                      <v-img
                        :src="
                          `https://picsum.photos/500/300?image=${n * 5 + 10}`
                        "
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
                  </v-col>
                </v-row>
              </v-container>
            </v-card>
          </v-tab-item>
        </v-tabs>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
export default {
  name: 'ImageGallery',
};
</script>

<style>
.v-tab--active {
  color: black !important;
}
</style>
