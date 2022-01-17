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
                <td>{{ stock.text }}</td>
                <td>{{ stock.price }}</td>
                </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <div id="dynamic-tabs" hidden>
      <b-tabs v-model="tabIndex" class="scrollable-tabs" card>
          <b-tab class="test" v-for="i in tabs" :key="'dyn-tab-' + i">
          <template #title>
            Tab {{ i }}
            <b-tab-item @click="closeTab(i)">
              <b-icon icon="x-circle-fill" font-scale="0.75" aria-hidden="true"></b-icon>
            </b-tab-item>
          </template>
          ContentContentContentContentContentContentContentContentCo
          ntentContentContentContentContentContentContentContentCo
          ntentContentContentContentContentContentCon
          tentContentContentContentContentContentContentContentContentContentContent
          </b-tab>

          <!-- New Tab Button (Using tabs-end slot) -->
          <template #tabs-end>
            <b-nav-item role="presentation" @click.prevent="newTab" href="#"><b>+</b></b-nav-item>
          </template>
        </b-tabs>

        <b-button-group>
          <b-button @click="tabIndex -= 1">
            <b-icon icon="chevron-left" font-scale="0.75"></b-icon>
          </b-button>
          <b-button @click="tabIndex += 1">
            <b-icon icon="chevron-right" font-scale="0.75"></b-icon>
          </b-button>
        </b-button-group>
    </div>

    <div id="dynamic-navbar" hidden>
      <b-row class="justify-content-sm-center g-0">
        <b-col class="bg-primary col-sm-1">
          <b-button squared class="flex h-100 w-100" @click="scroll_left">
            <b-icon icon="chevron-left" font-scale="0.75"></b-icon>
          </b-button>
        </b-col>

        <b-col class="col-sm-10">
          <b-navbar type="dark">
            <b-navbar-nav>
              <b-navbar-item href="#">Test 1</b-navbar-item>
              <b-navbar-item href="#">Test 2</b-navbar-item>
              <b-navbar-item href="#">Test 1</b-navbar-item>
              <b-navbar-item href="#">Test 2</b-navbar-item>
              <b-navbar-item href="#">Test 1</b-navbar-item>
              <b-navbar-item href="#">Test 2</b-navbar-item>
              <b-navbar-item href="#">Test 1</b-navbar-item>
              <b-navbar-item href="#">Test 2</b-navbar-item>
              <b-navbar-item href="#">Test 1</b-navbar-item>
              <b-navbar-item href="#">Test 2</b-navbar-item>
              <b-navbar-item href="#">Test 1</b-navbar-item>
              <b-navbar-item href="#">Test 2</b-navbar-item>
              <b-navbar-item href="#">Test 1</b-navbar-item>
              <b-navbar-item href="#">Test 2</b-navbar-item>
              <b-navbar-item href="#">Test 1</b-navbar-item>
              <b-navbar-item href="#">Test 2</b-navbar-item>
              <b-navbar-item href="#">Test 1</b-navbar-item>
              <b-navbar-item href="#">Test 2</b-navbar-item>
              <b-navbar-item href="#">Test 1</b-navbar-item>
              <b-navbar-item href="#">Test 2</b-navbar-item>
              <b-navbar-item href="#">Test 1</b-navbar-item>
              <b-navbar-item href="#">Test 2</b-navbar-item>
              <b-navbar-item href="#">Test 1</b-navbar-item>
              <b-navbar-item href="#">Test 2</b-navbar-item>
              <b-navbar-item href="#">Test 2</b-navbar-item>
              <b-navbar-item href="#">Test 1</b-navbar-item>
            </b-navbar-nav>
          </b-navbar>
        </b-col>

        <b-col class="bg-primary col-sm-1">
          <b-button squared class="flex h-100 w-100" @click="scroll_right">
            <b-icon icon="chevron-right" font-scale="0.75"></b-icon>
          </b-button>
        </b-col>
      </b-row>
    </div>

    <div class="overflow-auto">
      <!-- Use text in props -->
      <b-pagination-nav use-router
      hide-goto-end-buttons
      :pages="stocks"
      :number-of-pages="stocks.length"
      align="fill"
      ></b-pagination-nav>
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
      tabIndex: 0,
      rows: 100,
      perPage: 10,
      currentPage: 1,
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
    scroll_left() {
      const content = document.querySelector('.navbar');
      content.scrollLeft -= 200;
    },
    scroll_right() {
      const content = document.querySelector('.navbar');
      content.scrollLeft += 200;
    },
  },
  created() {
    this.getStocks();
  },
};
</script>

<style>

.navbar {
  color: black;
  background-color: grey;
  display: inline-flex;
  overflow: hidden;
  overflow-x: auto;
  white-space: nowrap;
  -ms-overflow-style: none;
  scrollbar-width: none;
}

.left-scroll {
  background-color: green;
  text-align: right;
}

.right-scroll {
  background-color: blue;
  text-align: left;
}

.navbar-col.col {
  background-color: red;
  max-width: 100%;
  padding: 0px;
  flex-grow: 1;
}

#dynamic-tabs {
  margin-top: 60px;
}

</style>
