import Vue from 'vue';
import Router from 'vue-router';
import Ping from '../components/Ping.vue';
import Test from '../components/Test.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Index',
      component: Ping,
    },
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
    {
      path: '/test',
      name: 'Testing',
      component: Test,
    },
  ],
});
