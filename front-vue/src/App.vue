<template>
  <v-app id="inspire">
    <v-navigation-drawer v-model="drawer" app width="200">
      <v-list shaped>
        <!-- <v-subheader>Menu</v-subheader> -->
        <h2 class="text-center my-3">
          <v-icon style="margin-top:-10px;">mdi-movie-open-outline</v-icon><span class="red--text ml-1">무비</span>모아
        </h2>
        <v-divider></v-divider>
        <v-list-item-group v-model="item" color="white">
          <v-list-item link v-for="(item, i) in drawerItems" :key="i">
            <v-list-item-action>
              <v-icon>{{item.icon}}</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <router-link :to="item.link" >
                <v-list-item-title>{{item.name}}</v-list-item-title>
              </router-link>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar app clipped-left dense flat>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <v-spacer></v-spacer>
      <v-spacer></v-spacer>
      <v-spacer></v-spacer>
      <v-text-field
        solo
        hide-details
        dense
        label="영화검색"
        prepend-icon="mdi-magnify"
        color="red"
      ></v-text-field>
    </v-app-bar>

    <v-content>
      <v-container class="fill-height" fluid>
        <v-row align="center" justify="center">
          <v-col>
            <router-view></router-view>
          </v-col>
        </v-row>
      </v-container>
    </v-content>

    <v-footer>
      <v-row align="center" justify="center">
        <v-col class="text-right">
          <span>&copy; 2020 정형수 | 김태우</span>
        </v-col>
      </v-row>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  props: {
    source: String,
  },
  data: () => ({
    drawer: null,
    item: 0,
    drawerItems: [
      {
        name: '홈',
        icon: 'mdi-home',
        link: '/'
      },
      {
        name: '상영작·예정작',
        icon: 'mdi-movie-outline',
        link: '/movies'
      },
      {
        name: '랭킹',
        icon: 'mdi-trophy-outline',
        link: '/rankings'
      }
    ]
  }),
  created() {
    this.$vuetify.theme.dark = true;
  },
};
</script>

<style>
a {
  color: white !important;
  text-decoration: none; /* no underline */
}
</style>