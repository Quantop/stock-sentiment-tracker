<template>
  <div class="container">
     <b-container>
        <b-row align-h="center" cols="1" cols-sm="2">
            <overall-sentiment-card
               header="Overall Market Sentiment"
               todaysentiment="63%"
               sevendaysentiment="+6%"
               thirtydaysentiment="+27%"
               tooltip="Overall market sentiment tooltip"
            ></overall-sentiment-card>
        </b-row>

        <b-row align-h="center" cols="1" cols-sm="3" class="mt-5">
            <b-col class="mt-2">
               <sentiment-card
                  header="Twitter Sentiment"
                  todaysentiment="73%"
                  sevendaysentiment="-5%"
                  thirtydaysentiment="+14%"
               ></sentiment-card>
            </b-col>

            <b-col class="mt-2">
               <sentiment-card
                  header="Reddit Sentiment"
                  todaysentiment="59%"
                  sevendaysentiment="+4%"
                  thirtydaysentiment="-3%"
               ></sentiment-card>
            </b-col>

            <b-col class="mt-2">
               <sentiment-card
                  header="Media Sentiment"
                  todaysentiment="61%"
                  sevendaysentiment="+8%"
                  thirtydaysentiment="+31%"
               ></sentiment-card>
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
import OverallSentimentCard from '../components/OverallSentimentCard.vue';
import SentimentCard from '../components/SentimentCard.vue';

export default {
  components: {
    'sentiment-card': SentimentCard,
    'overall-sentiment-card': OverallSentimentCard,
  },
  name: 'Sentiment',
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
          key: 'current_sentiment',
          sortable: true,
        },
        {
          key: '7_day_change',
          label: '7-Day Change',
          sortable: true,
        },
        {
          key: '30_day_change',
          label: '30-Day Change',
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
