import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    companyName: ''
  },
  mutations: {
    setCompanyName(state, payload) {
      state.companyName = payload
    }
  },
  actions: {
  },
  modules: {
  }
})
