import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: {
    // movieList: '',
  },
  getters: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
  }
})
