<template>
  <div class="container">
    <div class="stock-table">
        <div class="row">
        <div class="col-sm-10">
            <h1>Stocks</h1>
            <br><br>
            <table class="table table-hover">
            <thead>
                <tr>
                <th scope="col">Company</th>
                <th scope="col">Price</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(stock, index) in stocks" :key="index">
                <td>{{ stock.name }}</td>
                <td>{{ stock.price }}</td>
                </tr>
            </tbody>
            </table>
        </div>
        </div>
    </div>

    <div id="dynamic-navbar">
      <b-card no-body>
        <b-tabs card>
            <b-tab v-for="i in tabs" :key="'dyn-tab-' + i">
            <template #title>
              Tab {{ i }}
              <b-tab-item @click="closeTab(i)">
                <b-icon icon="x-circle-fill" aria-hidden="true"></b-icon>
              </b-tab-item>
            </template>
            Tab contents {{ i }}
            </b-tab>

            <!-- New Tab Button (Using tabs-end slot) -->
            <template #tabs-end>
              <b-nav-item role="presentation" @click.prevent="newTab" href="#"><b>+</b></b-nav-item>
            </template>

            <!-- Render this if no tabs -->
            <template #empty>
              <div class="text-center text-muted">
                  There are no open tabs<br>
                  Open a new tab using the <b>+</b> button above.
              </div>
            </template>
        </b-tabs>
    </b-card>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      stocks: [],
      tabs: [],
      tabCounter: 0,
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
    closeTab(x) {
      for (let i = 0; i < this.tabs.length; i += 1) {
        if (this.tabs[i] === x) {
          this.tabs.splice(i, 1);
          this.tabCounter -= 1;
        }
      }
    },
    newTab() {
      this.tabs.push(this.tabCounter += 1);
    },
  },
  created() {
    this.getStocks();
  },
};
</script>

<style>
#dynamic-navbar {
  margin-top: 60px;
}

.b-icon {
  margin-left: 2px;
  margin-bottom: 2px;
}
</style>
