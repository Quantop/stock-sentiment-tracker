import Vue from 'vue';
import Router from 'vue-router';
import StockSentiment from '@/views/StockSentiment.vue';
import Test from '../components/Test.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/test',
      name: 'Testing',
      component: Test,
    },
    {
      path: '/sentiment',
      name: 'Sentiment',
      component: StockSentiment,
    },
  ],
});
