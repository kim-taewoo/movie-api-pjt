<template>
  <div>
    <v-row justify="center" align="center">
      <v-col cols="12" sm="5">
        <v-card>
          <v-card-title>
            <span class="headline">SIGNUP</span>
          </v-card-title>
          <v-card-text>
            <v-container>
              <v-row>
                <v-col cols="12" class="pa-0">
                  <v-text-field
                    v-model="signupData.username"
                    color="pink lighten-3"
                    shaped
                    outlined
                    label="ID*"
                    required
                  ></v-text-field>
                </v-col>
                <v-col cols="12" class="pa-0">
                  <v-text-field
                    v-model="signupData.password1"
                    color="pink lighten-3"
                    shaped
                    outlined
                    label="Password*"
                    type="password"
                    required
                  ></v-text-field>
                </v-col>
                <v-col cols="12" class="pa-0">
                  <v-text-field
                    v-model="signupData.password2"
                    color="pink lighten-3"
                    shaped
                    outlined
                    label="Password Check*"
                    type="password"
                    required
                    @keypress.enter="signup(signupData)"
                  ></v-text-field>
                </v-col>
              </v-row>
            </v-container>
          </v-card-text>
          <v-card-actions>
            <v-btn color="pink lighten-1" text to="/login">로그인</v-btn>
            <v-spacer></v-spacer>
            <v-btn color="pink lighten-3" text>취소</v-btn>
            <v-btn color="pink lighten-3" text @click="signup(signupData)"
              >확인</v-btn
            >
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  name: 'Signup',
  data() {
    return {
      signupData: {
        username: null,
        password1: null,
        password2: null,
      },
    };
  },
  methods: {
    ...mapActions(['signup']),
  },
};
</script>

<style></style>
