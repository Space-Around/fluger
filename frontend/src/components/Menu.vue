<template>
    <div class="d-flex menu">
        <div class="d-flex pa-4 menu-left">
            <v-icon large class="menu-left-icon">
                mdi-account-multiple
            </v-icon>
            <v-icon large class="menu-left-icon">
                mdi-account-question
            </v-icon>
            <v-icon @click="clickIcon" large class="menu-left-icon">
                mdi-currency-usd 
            </v-icon>
        </div>
        <div v-if="showMenu" class="d-flex menu-right pa-4">
            <h3>Header</h3>
            <ul class="d-flex list">
                <li><router-link to="/company" class="link">One</router-link></li>
                <li><router-link to="/company" class="link">Two</router-link></li>
                <li><router-link to="/company" class="link">Three</router-link></li>
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
            }
        }
    }
</script>

<style lang="scss" scoped>
    .menu {
        position: absolute;
        flex-direction: columns;
        height: 100%;
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