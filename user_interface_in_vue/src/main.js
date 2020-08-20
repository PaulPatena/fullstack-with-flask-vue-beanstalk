import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify';
import axiosCfg from './plugins/axiosConfig'

Vue.config.productionTip = false

// The following binding will allow use to use axios in components using the syntax this.$axios
Vue.prototype.$axios = axiosCfg

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
