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
            @click="clickIcon('Profile', 'Профиль')"
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
            @click="goTo('risk')"
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
            @click="clickIcon('Company', 'Компании')"
          >
            mdi-currency-usd
          </v-icon>
        </template>
        <span>Компании</span>
      </v-tooltip>
    </div>
    <transition name="fade">
      <right-menu :header="menuTabHeader" :showMenu="showMenu" @close="showMenu = false">
        <ul v-if="menuTabSelection == 'Company'" class="d-flex list mt-3">
          <li @click="goTo('company')" class="link py-1 pointer">Татнефть</li>
          <li @click="goTo('company')" class="link py-1 pointer">
            Газпромнефть
          </li>
        </ul>
        <ul v-if="menuTabSelection == 'Profile'" class="d-flex list mt-3">
          <li @click="goTo('profile')" class="link py-1 pointer">Настройки профиля</li>
          <li @click="goTo('')" class="link py-1 pointer red--text text--darken-1">Выйти из аккаунта</li>
        </ul>
      </right-menu>
    </transition>
  </div>
</template>

<script>
import rightMenu from "./RightMenu.vue";

export default {
  data() {
    return {
      showMenu: false,
      menuTabSelection: "",
      menuTabHeader: "",
    };
  },
  components: {
    rightMenu,
  },
  methods: {
    clickIcon(menuTabName, menuTabHeader) {
      this.showMenu = true;
      this.menuTabSelection = menuTabName;
      this.menuTabHeader = menuTabHeader;
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
    border-right: 2px solid #2196F3;
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

.fade-enter,
.fade-leave-to {
  opacity: 0;
  transform: translateX(-20px);
}
</style>