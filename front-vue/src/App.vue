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
          <v-btn block @click.stop="loginDialog = true"
            >LOGIN<v-icon right dark>mdi-key</v-icon></v-btn
          >
        </div>
      </template>
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

    <v-dialog v-model="loginDialog" persistent max-width="450px">
      <v-card>
        <v-card-title>
          <span class="headline">LOGIN</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12" class="pa-0">
                <v-text-field
                  v-model="loginData.username"
                  color="pink lighten-3"
                  shaped
                  outlined
                  label="ID*"
                  required
                ></v-text-field>
              </v-col>
              <v-col cols="12" class="pa-0">
                <v-text-field
                  v-model="loginData.password"
                  color="pink lighten-3"
                  shaped
                  outlined
                  label="Password*"
                  type="password"
                  required
                ></v-text-field>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-btn color="pink lighten-1" text @click="loginDialog = false"
            >회원가입</v-btn
          >
          <v-spacer></v-spacer>
          <v-btn color="pink lighten-3" text @click="loginDialog = false"
            >취소</v-btn
          >
          <v-btn color="pink lighten-3" text @click="login(loginData)"
            >확인</v-btn
          >
        </v-card-actions>
      </v-card>
    </v-dialog>

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
          <v-btn @click="test">TEST</v-btn>
          <span>&copy; 2020 정형수 | 김태우</span>
        </v-col>
      </v-row>
    </v-footer>
  </v-app>
</template>

<script>
import { mapActions } from 'vuex';
export default {
  props: {
    source: String,
  },
  data: () => ({
    drawer: null,
    loginDialog: false,
    item: 0,
    loginData: {
      username: null,
      password: null,
    },
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
      // {
      //   name: '랭킹',
      //   icon: 'mdi-trophy-outline',
      //   link: '/rankings'
      // }
    ],
  }),
  methods: {
    ...mapActions(['fetchMovies', 'initiateMoviesDB', 'login']),

    test() {
      this.initiateMoviesDB()
        .then((res) => console.log(res))
        .catch(err => console.log(err))
    },
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
</style>
