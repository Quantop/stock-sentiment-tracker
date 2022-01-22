<template>
   <div>
      <b-col>
         <b-card
            border-variant="dark"
            :header="header"
            header-bg-variant="dark"
            header-text-variant="white"
         >
            <template #header>
               <div class="card-header">
                  <div>
                  <b-icon
                  id="overall-tt"
                  icon="info-circle-fill"
                  class="pull-right mt-2"
                  scale="1"
                  :v-show="tooltipshow"
                  >
                  </b-icon>
                  </div>
                  <b-tooltip target="overall-tt" triggers="hover">
                     {{tooltip}}
                  </b-tooltip>
                  <h5 class="text-center mt-1">{{header}}</h5>
               </div>
            </template>
            Today's Sentiment
            <div align="center">
               <div class="m-4">
                  <h2>{{todaysentiment}}</h2>
               </div>
            </div>

            <b-row>
               <b-col h-align="center">
                  7-Day Change
                  <b-col class="pt-2">
                     <h6>{{sevendaysentiment}}</h6>
                  </b-col>
               </b-col>

               <b-col h-align="center">
                  30-Day Change
                  <b-col class="pt-2">
                     <h6>{{thirtydaysentiment}}</h6>
                  </b-col>
               </b-col>
            </b-row>
         </b-card>
      </b-col>
   </div>
</template>

<script>
export default {
  props: {
    header: String,
    todaysentiment: Number,
    sevendaysentiment: Number,
    thirtydaysentiment: Number,
    tooltip: String,
    tooltipshow: Boolean,
  },
};
</script>

<style>
.card-header .pull-right {position: absolute; right: 15px;}
</style>
