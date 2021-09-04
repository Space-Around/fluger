<template>
  <v-app>
    <v-main>
      <app-menu/>
      <v-container>
        <router-view/>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import appMenu from "./components/menu/Menu.vue"

export default {
  name: 'App',

  data() {
    return {
      activeTab: undefined,
    }
  },
  components: {
    appMenu
  }
};
</script>

<style>
  #app {
    min-height: 100vh;
    font-family: 'Golos-UI', sans-serif;
  }
  @font-face {
    font-family: 'Golos-UI';
    src: local('Golos UI'), local('Golos-UI'),
      url('~@/assets/fonts/Golos-UI/Golos-UI_Regular.woff') format('woff'),
      url('~@/assets/fonts/Golos-UI/Golos-UI_Regular.woff2') format('woff2');
    font-weight: 100;
    font-style: normal;
  }
  .pointer {
    cursor: pointer;
  }
</style>
