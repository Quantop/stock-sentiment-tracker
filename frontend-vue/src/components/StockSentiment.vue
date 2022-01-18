<template>
  <div class="container">
     <b-container>
        <b-row align-h="center">
            <b-col cols="4">
               Overall Market Sentiment
               <div align="center">
                  <b-progress :max="100" height="20px" class="w-75">
                     <b-progress-bar
                     :value="overallsentiment"
                     :label="`${((overallsentiment / 100) * 100).toFixed(0)}%`"
                     show-progress>
                     </b-progress-bar>
                  </b-progress>
               </div>
            </b-col>
        </b-row>

        <b-row align-h="center" class="mt-5">
         <b-col>
            Twitter Sentiment
            <div align="center">
               <b-progress :max="100" height="20px" class="w-75">
                  <b-progress-bar
                  :value="twittersentiment"
                  :label="`${((twittersentiment / 100) * 100).toFixed(0)}%`"
                  show-progress>
                  </b-progress-bar>
               </b-progress>
            </div>
         </b-col>

         <b-col>
            Reddit Sentiment
            <div align="center">
               <b-progress :max="100" height="20px" class="w-75">
                  <b-progress-bar
                  :value="redditsentiment"
                  :label="`${((redditsentiment / 100) * 100).toFixed(0)}%`"
                  show-progress>
                  </b-progress-bar>
               </b-progress>
            </div>
         </b-col>

         <b-col>
            Media Sentiment
            <div align="center">
               <b-progress :max="100" height="20px" class="w-75">
                  <b-progress-bar
                  :value="mediasentiment"
                  :label="`${((mediasentiment / 100) * 100).toFixed(0)}%`"
                  show-progress>
                  </b-progress-bar>
               </b-progress>
            </div>
         </b-col>
        </b-row>
     </b-container>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      stocks: [],
      overallsentiment: 59,
      twittersentiment: 66,
      redditsentiment: 72,
      mediasentiment: 41,
    };
  },

  methods: {
    getStocks() {
      const path = 'http://localhost:5000/stocks';
      axios.get(path)
        .then((res) => {
          this.stocks = res.data.stocks;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getStocks();
  },
};
</script>

<style>
</style>
