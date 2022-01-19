<template>
  <div class="container">
     <b-container>
        <b-row align-h="center" cols="1" cols-sm="2">
            <b-col>
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
                        <b-col class="pt-2">
                           <h6>+7%</h6>
                        </b-col>
                     </b-col>

                     <b-col h-align="center">
                        30-Day Change
                        <b-col class="pt-2">
                           <h6>+27%</h6>
                        </b-col>
                     </b-col>
                  </b-row>
               </b-card>
            </b-col>
        </b-row>

        <b-row align-h="center" cols="1" cols-sm="3" class="mt-5">
         <b-col class="mt-2">
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
                     <h3>73%</h3>
                  </div>
               </div>

               <b-row>
                  <b-col h-align="center">
                     7-Day Change
                     <b-col class="pt-2">
                        <h6>-5%</h6>
                     </b-col>
                  </b-col>

                  <b-col h-align="center">
                     30-Day Change
                     <b-col class="pt-2">
                        <h6>+14%</h6>
                     </b-col>
                  </b-col>
               </b-row>
            </b-card>
         </b-col>

         <b-col class="mt-2">
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
                     <b-col class="pt-2">
                        <h6>+4%</h6>
                     </b-col>
                  </b-col>

                  <b-col h-align="center">
                     30-Day Change
                     <b-col class="pt-2">
                        <h6>-3%</h6>
                     </b-col>
                  </b-col>
               </b-row>
            </b-card>
         </b-col>

         <b-col class="mt-2 mb-2">
            <b-card
               border-variant="primary"
               header="Media Sentiment"
               header-bg-variant="primary"
               header-text-variant="white"
            >
               Today's Sentiment
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
                     <b-col class="pt-2">
                        <h6>+8%</h6>
                     </b-col>
                  </b-col>

                  <b-col h-align="center">
                     30-Day Change
                     <b-col class="pt-2">
                        <h6>+31%</h6>
                     </b-col>
                  </b-col>
               </b-row>
            </b-card>
         </b-col>
        </b-row>
     </b-container>

     <b-container>
        <b-row class="mt-5">
           <b-col class="mt-1">
            <h4>Top Gainers</h4>
            <b-table
               striped
               hover
               :items="stocks"
               :fields="gainfields"
               label-sort-asc=''
               label-sort-desc=''
               label-sort-clear=''
            ></b-table>
           </b-col>

           <b-col class="mt-1">
            <h4>Top Losers</h4>
            <b-table
               striped
               hover
               :items="stocks"
               :fields="gainfields"
               label-sort-asc=''
               label-sort-desc=''
               label-sort-clear=''
            ></b-table>
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
      gainfields: [
        {
          key: 'company',
          sortable: false,
        },
        {
          key: 'price',
          sortable: true,
        },
        {
          key: 'sentiment',
          sortable: true,
        },
      ],
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
