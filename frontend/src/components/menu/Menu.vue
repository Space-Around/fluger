<template>
  <div class="d-flex menu">
    <div class="d-flex pa-4 menu-left">
      <v-tooltip right>
        <template v-slot:activator="{ on, attrs }">
          <v-icon
            color="blue"
            large
            v-bind="attrs"
            v-on="on"
            class="menu-left-icon"
            @click="clickIcon"
          >
            mdi-account-multiple
          </v-icon>
        </template>
        <span>Профиль</span>
      </v-tooltip>
      <v-tooltip right>
        <template v-slot:activator="{ on, attrs }">
          <v-icon
            color="blue"
            v-bind="attrs"
            v-on="on"
            large
            class="menu-left-icon"
            @click="clickIcon"
          >
            mdi-account-question
          </v-icon>
        </template>
        <span>Тестирование</span>
      </v-tooltip>
      <v-tooltip right>
        <template v-slot:activator="{ on, attrs }">
          <v-icon
            color="green"
            large
            v-bind="attrs"
            v-on="on"
            class="menu-left-icon"
            @click="clickIcon"
          >
            mdi-currency-usd
          </v-icon>
        </template>
        <span>Компании</span>
      </v-tooltip>
    </div>
<<<<<<< HEAD:frontend/src/components/Menu.vue
    <div v-if="showMenu" class="d-flex menu-right pt-4">
      <h3>Акции компаний</h3>
      <ul class="d-flex list pt-3">
        <li @click="goTo('company')" class="link">Татнефть</li>
        <li @click="goTo('company')" class="link">Газпромнефть</li>
      </ul>
    </div>
=======
    <transition name="fade">
      <div v-if="showMenu" class="d-flex menu-right pa-4">
        <v-icon
          color="red darken-1"
          class="close"
          @click="showMenu = false"
        >mdi-window-close</v-icon>
        <h3 class="text-center mt-3">Акции компаний</h3>
        <ul class="d-flex list">
          <li @click="goTo('company')" class="link py-1 pointer">Татнефть</li>
          <li @click="goTo('company')" class="link py-1 pointer">Газпромнефть</li>
        </ul>
      </div>
    </transition>
>>>>>>> 42383dd3285932cf100f038ee15dd237b4fdd6f6:frontend/src/components/menu/Menu.vue
  </div>
</template>

<script>
export default {
  data() {
    return {
      showMenu: false,
    };
  },
  methods: {
    clickIcon() {
      this.showMenu = !this.showMenu;
    },
    goTo(link) {
      this.showMenu = false;
      this.$router.push("/" + link);
    },
  },
};
</script>

<style lang="scss" scoped>
.menu {
  position: fixed;
  top: 0;
  left: 0;
  z-index: 1000;
  height: 100vh;
  .menu-left {
    background-color: white;
    flex-direction: column;
    width: 70px;
    gap: 15px;

    position: relative;
    z-index: 1200;
  }
  .menu-right {
    flex-direction: column;
    position: relative;
    z-index: 1100;
    background-color: #e8e8e8;
    width: 230px;
    overflow-y: auto;

    transition: transform 0.3s, opacity 0.3s;
    .close {
      position: absolute;
      top: 8px;
      right: 8px;

    }
    .list {
      padding-left: 0;
      flex-direction: column;
      list-style: none;
      width: 100%;
    }
  }
}
<<<<<<< HEAD:frontend/src/components/Menu.vue
.list {
  padding-left: 0;
}
.menu-left {
  flex-direction: column;
  width: 70px;
}
.menu-left-icon {
  margin-bottom: 15px;
}
.menu-right {
  background-color: #e8e8e8;
  flex-direction: column;
  width: 230px;
  overflow-y: auto;
}
.menu-right h3 {
  text-align: center;
}
.menu-right ul {
  flex-direction: column;
  list-style: none;
  width: 100%;
}
.list li:hover {
  cursor: pointer;
  background-color: #dedede;
}
.list li {
  padding-left: 15px;
}
.link {
  display: flex;
  align-items: center;
  color: black;
  text-decoration: none;
  width: 100%;
  height: 35px;
  margin-bottom: 10px;
=======

.fade-enter, .fade-leave-to {
  opacity: 0;
  transform: translateX(-20px);
>>>>>>> 42383dd3285932cf100f038ee15dd237b4fdd6f6:frontend/src/components/menu/Menu.vue
}
</style>