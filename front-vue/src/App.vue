<template>
  <v-app id="inspire">
    <v-navigation-drawer v-model="drawer" app width="200">
      <v-list shaped>
        <!-- <v-subheader>Menu</v-subheader> -->
        <h2 class="text-center my-3">
          <router-link to="/">
            <v-icon style="margin-top:-10px;">mdi-movie-open-outline</v-icon
            ><span class="red--text ml-1">무비</span>모아
          </router-link>
        </h2>
        <v-divider></v-divider>
        <v-list-item-group v-model="item" color="white">
          <v-list-item
            exact
            :to="item.link"
            link
            v-for="(item, i) in drawerItems"
            :key="i"
          >
            <v-list-item-action>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>{{ item.name }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>

      <template v-slot:append>
        <div class="pa-2 mb-5">
          <!-- <v-btn @click="initiateMoviesDB">InitiateDB(test)</v-btn> -->
          <v-btn v-if="!isLoggedIn" block to="/login">
            LOGIN<v-icon right dark>mdi-key</v-icon>
          </v-btn>
          <v-btn @click="logout" v-else block to="/login">
            LOGOUT<v-icon right dark>mdi-key</v-icon>
          </v-btn>
        </div>
      </template>
    </v-navigation-drawer>

    <v-app-bar app clipped-left dense flat>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <!-- <v-spacer></v-spacer>
      <v-spacer></v-spacer>
      <v-spacer></v-spacer>
      <v-text-field
        solo
        hide-details
        dense
        label="영화검색"
        prepend-icon="mdi-magnify"
        color="red"
      ></v-text-field> -->
    </v-app-bar>

    

    <v-content>
      <v-container class="fill-height" fluid>
        <v-row align="center" justify="center">
          <v-col>
            <transition name="fade" mode="out-in">
              <router-view></router-view>
            </transition>
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
import { mapActions, mapGetters } from 'vuex';
export default {
  props: {
    source: String,
  },
  data: () => ({
    drawer: null,
    loginDialog: false,
    item: 0,
    drawerItems: [
      {
        name: '홈',
        icon: 'mdi-home',
        link: '/',
      },
      {
        name: '모든 영화',
        icon: 'mdi-movie-outline',
        link: '/movies',
      },
    ],
  }),
  methods: {
    ...mapActions(['logout', 'initiateMoviesDB']),

  },
  computed: {
    ...mapGetters(['isLoggedIn'])
  },
  created() {
    this.$vuetify.theme.dark = true;
  },
};
</script>

<style>
.v-application a {
  text-decoration: none;
  color: white !important;
}

.fade-enter-active,
.fade-leave-active {
  transition-duration: 0.3s;
  transition-property: opacity;
  transition-timing-function: ease;
}

.fade-enter,
.fade-leave-active {
  opacity: 0
}
</style>
