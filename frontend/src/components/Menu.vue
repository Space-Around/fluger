<template>
    <div class="d-flex menu">
        <div class="d-flex pa-4 menu-left">
            <v-icon @click="clickIcon" large class="menu-left-icon">
                mdi-account-multiple
            </v-icon>
            <v-icon @click="clickIcon" large class="menu-left-icon">
                mdi-account-question
            </v-icon>
            <v-icon @click="clickIcon" large class="menu-left-icon">
                mdi-currency-usd 
            </v-icon>
        </div>
        <div v-if="showMenu" class="d-flex menu-right pa-4">
            <h3>Акции компаний</h3>
            <ul class="d-flex list">
                <li @click="goTo('company')" class="link">Татнефть</li>
                <li @click="goTo('company')" class="link">Газпромнефть</li>
            </ul>
        </div>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                showMenu: false,
            }
        },
        methods: {
            clickIcon() {
                this.showMenu = !this.showMenu;
            },
            goTo(link) {
                this.showMenu = false;
                this.$router.push('/' + link)
            }
        }
    }
</script>

<style lang="scss" scoped>
    .menu {
        position: fixed;
        top: 0;
        left: 0;
        z-index: 1000;
        flex-direction: columns;
        height: 100vh;
    }
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
    .link {
        display: flex;
        align-items: center;
        color: black;
        text-decoration: none;
        width: 100%;
        height: 35px;
        margin-bottom: 10px;
    }
</style>