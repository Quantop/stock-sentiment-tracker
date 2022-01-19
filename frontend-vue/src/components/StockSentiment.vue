<template>
  <div class="container">
     <b-container>
        <b-row align-h="center">
            <b-col cols="6">
               <b-card
                  border-variant="primary"
                  header="Overall Market Sentiment"
                  header-bg-variant="primary"
                  header-text-variant="white"
               >
                  Today's Sentiment
                  <div align="center">
                     <b-progress :max="100" height="20px" class="w-75" hidden>
                        <b-progress-bar
                        :value="overallsentiment"
                        :label="`${((overallsentiment / 100) * 100).toFixed(0)}%`"
                        show-progress>
                        </b-progress-bar>
                     </b-progress>

                     <div class="m-4">
                        <h2>85%</h2>
                     </div>
                  </div>

                  <b-row>
                     <b-col h-align="center">
                        7-Day Change
                        <b-col>
                           <h6>+7%</h6>
                        </b-col>
                     </b-col>

                     <b-col h-align="center">
                        30-Day Change
                        <b-col>
                           <h6>+27%</h6>
                        </b-col>
                     </b-col>
                  </b-row>
               </b-card>
            </b-col>
        </b-row>

        <b-row align-h="center" class="mt-5">
         <b-col>
            <b-card
               border-variant="primary"
               header="Twitter Sentiment"
               header-bg-variant="primary"
               header-text-variant="white"
            >
               <div align="center">
                  Today's Sentiment
                  <b-progress :max="100" height="20px" class="w-75" hidden>
                     <b-progress-bar
                     :value="twittersentiment"
                     :label="`${((twittersentiment / 100) * 100).toFixed(0)}%`"
                     show-progress>
                     </b-progress-bar>
                  </b-progress>

                  <div class="m-4">
                     <h2>73%</h2>
                  </div>
               </div>

               <b-row>
                  <b-col h-align="center">
                     7-Day Change
                     <b-col>
                        <h6>-5%</h6>
                     </b-col>
                  </b-col>

                  <b-col h-align="center">
                     30-Day Change
                     <b-col>
                        <h6>+14%</h6>
                     </b-col>
                  </b-col>
               </b-row>
            </b-card>
         </b-col>

         <b-col>
            <b-card
               border-variant="primary"
               header="Reddit Sentiment"
               header-bg-variant="primary"
               header-text-variant="white"
            >
               Today's Sentiment
               <div align="center">
                  <b-progress :max="100" height="20px" class="w-75" hidden>
                     <b-progress-bar
                     :value="redditsentiment"
                     :label="`${((redditsentiment / 100) * 100).toFixed(0)}%`"
                     show-progress>
                     </b-progress-bar>
                  </b-progress>

                  <div class="m-4">
                     <h3>59%</h3>
                  </div>
               </div>

               <b-row>
                  <b-col h-align="center">
                     7-Day Change
                     <b-col>
                        <h6>+4%</h6>
                     </b-col>
                  </b-col>

                  <b-col h-align="center">
                     30-Day Change
                     <b-col>
                        <h6>-3%</h6>
                     </b-col>
                  </b-col>
               </b-row>
            </b-card>
         </b-col>

         <b-col>
            <b-card
               border-variant="primary"
               header="Media Sentiment"
               header-bg-variant="primary"
               header-text-variant="white"
            >
               Media Sentiment
               <div align="center">
                  <b-progress :max="100" height="20px" class="w-75" hidden>
                     <b-progress-bar
                     :value="mediasentiment"
                     :label="`${((mediasentiment / 100) * 100).toFixed(0)}%`"
                     show-progress>
                     </b-progress-bar>
                  </b-progress>

                  <div class="m-4">
                     <h3>61%</h3>
                  </div>
               </div>

               <b-row>
                  <b-col h-align="center">
                     7-Day Change
                     <b-col>
                        <h6>+8%</h6>
                     </b-col>
                  </b-col>

                  <b-col h-align="center">
                     30-Day Change
                     <b-col>
                        <h6>+31%</h6>
                     </b-col>
                  </b-col>
               </b-row>
            </b-card>
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
