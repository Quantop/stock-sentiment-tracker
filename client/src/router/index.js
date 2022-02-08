import Vue from 'vue';
import Router from 'vue-router';
import StockSentiment from '@/views/StockSentiment.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/sentiment',
      name: 'Sentiment',
      component: StockSentiment,
    },
  ],
});
