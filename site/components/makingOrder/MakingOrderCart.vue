<template>
  <section class="cart">
    <table class="cart-table" v-if="setProductsFromCart.length">
      <thead class="cart-table-head">
      <tr>
        <th scope="col">#</th>
        <th scope="col">Наименование</th>
        <th scope="col">Количество</th>
        <th scope="col">Цена</th>
        <th scope="col"></th>
      </tr>
      </thead>
      <tbody
        class="cart-table-body"
        v-for="(products, index) in setProductsFromCart"
        :key="products.id"
      >
      <tr>
        <th scope="row">{{ index + 1}}</th>
        <td>
          <img :src="'https://dev.aromatic.kz' + products.photo" alt="" />
          {{products.title}}
        </td>
        <td>
          <button @click="iterationCount(index, 'minus')">
            <img src="/cart/minus.svg" alt="" />
          </button>
          <input type="number" v-model="products.count" readonly>
          <button @click="iterationCount(index, 'plus')">
            <img src="/cart/plus.svg" alt="" />
          </button>
        </td>
        <td>{{formatNumber(products.finalPrice)}} тг.</td>
        <td>
          <button @click="deleteProduct(products)">
            <img src="/cart/close.svg" alt="" style="filter: brightness(0) saturate(100%) invert(18%) sepia(51%) saturate(7487%) hue-rotate(355deg) brightness(76%) contrast(85%);">
          </button>
        </td>
      </tr>
      </tbody>
    </table>
    <div class="cart-mobile" v-if="setProductsFromCart.length">
      <div class="row">
        <div
          class="col-12"
          v-for="(products, index) in setProductsFromCart"
          :key="products.id"
        >
          <div class="cart-mobile-delete">
            <button @click="deleteProduct(products)">
              <img src="/cart/closeMobile.svg" alt="" style="filter: brightness(0) saturate(100%) invert(18%) sepia(51%) saturate(7487%) hue-rotate(355deg) brightness(76%) contrast(85%);">
            </button>
          </div>
          <div class="cart-mobile-top">
            <div class="row">
              <div class="col-6">
                <div class="cart-mobile-top-img">
                  <img :src="'https://dev.aromatic.kz' + products.photo" alt="" />
                </div>
              </div>
              <div class="col-6">
                <div class="cart-mobile-top-title">
                  <div>
                    <span>Название:</span> <span>{{products.title}}</span>
                  </div>
                  <div>
                    <span>Категория:</span> <span>{{products.category}}</span>
                  </div>
                  <div class="cart-mobile-top-counter">
                    <p>Подсчитать количество: </p>
                    <button @click="iterationCount(index, 'minus')">
                      <img src="/cart/minus.svg" alt="" />
                    </button>
                    <input type="number" v-model="products.count" readonly>
                    <button @click="iterationCount(index, 'plus')">
                      <img src="/cart/plus.svg" alt="" />
                    </button>
                  </div>
                  <div>
                    <span>Цена:</span> <span>{{formatNumber(products.finalPrice)}} тг.</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="not-data-in-cart" v-else>
      <p>Добавьте товары в корзину</p>
    </div>
    <div class="cart-bottom" v-if="setProductsFromCart.length">
      <div class="cart-bottom-price">
        <span>Всего: {{formatNumber(totalPrice)}} тг.</span>
      </div>
      <div class="cart-bottom-button">
        <button @click="saveCartUser(setProductsFromCart)">
          Сохранить
        </button>
        <button :disabled="saveCart === false" title="нажмите на сохранить" @click="nextStep('second')">
          Продолжить
        </button>
      </div>
    </div>
  </section>
</template>

<script>
import formatNumber from "~/plugins/formatNumber.js";
export default {
  name: "MakingOrderCart",
  props: {
    totalPrice: {
      type: Number,
      default: () => 0
    }
  },
  data() {
    return {
      saveCart: false
    }
  },
  created() {
    this.$store.dispatch('Cart/cartFromApi')
  },
  methods: {
    formatNumber,
    iterationCount(index, action) {
      this.$store.dispatch('Cart/countingQuantityAndCalculatingPrice', {index, action})
    },
    deleteProduct(item) {
      this.$store.commit('Cart/DELETE_PRODUCT', item)
    },
    saveCartUser(data) {
      this.saveCart = true
      this.$store.commit('Cart/SAVE_CART_USER', data)
    },
    nextStep(step) {
      this.$emit('nextStep', step)
    }
  },
  computed: {
    setProductsFromCart() {
      return this.$store.state.Cart.cartData
    },
    cartDataFromUser() {
      return this.$auth.user.cart_data
    }
  },
  watch: {
    setProductsFromCart: {
      handler(products) {
        let cart = this.cartDataFromUser;
        const uniqueProducts = [...new Set(products)];

        if (cart.length !== uniqueProducts.length) {
          this.saveCart = false;
        }

      },
      deep: true,
    },
  }
}
</script>

<style lang="scss">
.cart {
  &-table {
    display: table;
    width: 100%;
    border-collapse: collapse;
    &-head {
      background: #bd4968;
      height: 40px;
      th {
        color: #fff;
        padding: 0px 0 0 15px;
        font-size: 18px;
      }
      tr {
        th:nth-child(1) {
          width: 40px;
        }
      }
    }
    &-body {
      tr {
        border-bottom: 1px solid #e3d3d3;
        th {
          text-align: center;
        }
        td:nth-child(2) {
          padding: 10px 0;
          img {
            width: 100px;
          }
        }
        td:nth-child(3) {
          vertical-align: center;
          img {
            width: 19px;
          }
          input {
            padding: 7px 18px 7px 18px;
            border: 1px solid #DCD9D9;
            background: #FFF;
            max-width: 63px;
            text-align: center;
          }
        }
        td {
          font-size: 18px;
        }
      }
    }
  }
  &-mobile {
    display: none;
  }
  .not-data-in-cart {
    p {
      font-size: 32px;
      color: #B71C1C;
    }
  }
  &-bottom {
    margin-top: 30px;
    display: flex;
    justify-content: flex-end;
    align-items: center;
    column-gap: 30px;
    &-price {
      span {
        font-size: 20px;
        font-weight: 500;
      }
    }
    &-button {
      display: flex;
      column-gap: 20px;
      button {
        border-radius: 50px;
        padding: 10px 30px;
        font-size: 18px;
      }
      button:nth-child(2) {
        background: #FF6F95;
        color: #fff;
        &:disabled {
          background: #ef96ae;
        }
      }
      button:nth-child(1) {
        border: 1px solid gray;
      }
    }
  }
}
@media(max-width: 767px) {
  .cart {
    .cart-table {
      display: none;
    }
    .cart-mobile {
      display: block;
      &-delete {
        display: flex;
        justify-content: flex-end;
      }
      .col-12 {
        padding: 10px;
        box-shadow: 0 0 10px 0 #FF6F95;
        border-radius: 10px;
        margin-bottom: 1em;
      }
      &-top {
        margin-bottom: 1em;
        &-img {
          display: flex;
          justify-content: center;
          img {
            height: 170px;
            width: 170px;
            border-radius: 5px;
          }
        }
        div {
          margin-bottom: 1em;
          span:first-child {
            font-weight: 700;
            color: #A6A6A6;
          }
        }
        &-counter {
          margin-bottom: 1em;
          p {
            font-weight: 700;
            color: #A6A6A6;
          }
          input {
            width: 70px;
            height: 40px;
            text-align: center;
            border: 1px solid #dbdeeb;
          }
          button {
            img {
            }
          }
        }
      }
    }
  }
}
@media(max-width: 520px) {
  .cart {
    &-bottom {
      display: flex;
      flex-direction: column;
    }
  }
}
</style>
