<template>
  <section class="products">
    <div class="container">
      <div class="row">
        <div class="col-lg-3">
          <div class="products-title">
            <p>Фильтры</p>
          </div>
          <div class="products__filters">
            <div class="products__filters-search">
              <div class="products__filters-title">
                <p>ПОИСК</p>
              </div>
              <div class="products__filters-search-input-container">
                <input type="text" placeholder="Название свечей" v-model="searchQuery" @input="performSearch">
                <img width="20px" src="/footer/search.svg" />
              </div>
            </div>
            <div class="products__filters-sorted">
              <div class="products__filters-title">
                <p>Сортировка</p>
              </div>
              <div class="products__filters-sorted-item">
                <label for="Ascending" class="radio">
                  <input
                    type="radio"
                    name="sorting"
                    id="Ascending"
                    class="radio__input"
                    v-model="ascending"
                    @input="ascendingAndDescendingProducts('возрастание')"
                  />
                  <div class="radio__radio"></div>
                  По возрастанию (цена)
                </label>
              </div>
              <div class="products__filters-sorted-item">
                <label for="Descending" class="radio">
                  <input
                    type="radio"
                    name="sorting"
                    id="Descending"
                    class="radio__input"
                    @input="ascendingAndDescendingProducts('убывание')"
                  />
                  <div class="radio__radio"></div>
                  По убыванию (цена)
                </label>
              </div>
              <div class="products__filters-sorted-item">
                <label for="popularity" class="radio">
                  <input
                    type="radio"
                    name="sorting"
                    id="popularity"
                    class="radio__input"
                    v-model="popularSorted"
                    @input="popularProducts"
                  >
                  <div class="radio__radio"></div>
                  По популярности
                </label>
              </div>
              <div class="products__filters-sorted-item">
                <label for="reset" class="radio">
                  <input
                    type="radio"
                    name="sorting"
                    id="reset"
                    class="radio__input"
                    v-model="reset"
                    @input="resetProducts"
                  >
                  <div class="radio__radio"></div>
                  Сбросить все
                </label>
              </div>
            </div>
          </div>
        </div>
        <div class="col-lg-9">
          <div class="products-title">
            <p>Товары</p>
          </div>
          <transition-group name="product-animated" tag="div" class="row">
            <div
                class="col-sm-3"
                v-for="(product, index) in products"
                :key="product.id"
              >
                <div class="products-item">
                  <div class="products-item-img">
                    <img :src="'https://dev.aromatic.kz/' + product.photo" alt="" />
                  </div>
                  <div class="products-item-title">
                    <p>{{ product.title }}</p>
                  </div>
                  <div v-show="product.description" class="products-item-description">
                    <p>{{ product.description }}</p>
                  </div>
                  <div class="products-item-category">
                    <p>{{ product.category }}</p>
                  </div>
                  <div class="products-item-price">
                    <p>{{ formatNumber(product.price) }} тг</p><span>/шт</span>
                  </div>
                  <button v-if="product.inCart === false" @click="sendingProductsToCart(product, index)">
                    <p>Добавить</p>
                    <img src="/products/cart.svg" alt="" />
                  </button>
                  <button v-else @click="sendingProductsToCart(product, index)">
                    <p>Удалить</p>
                    <img src="/products/cart.svg" alt="" />
                  </button>
                </div>
              </div>
          </transition-group>
        </div>
      </div>
    </div>
    <notifications :messages="messages"/>
    <Login
      v-if="openLogin === true"
      :open-login="openLogin"
      :open-register="openRegister"
      @closeLoginPopup="controlPopup"
      @openRegisterPopup="controlPopup"
    />
    <Register
      v-if="openRegister === true"
      :open-register="openRegister"
      @closeRegisterPopup="controlPopup"
      @openLoginPopup="controlPopup"
    />
  </section>
</template>

<script>
import formatNumber from "~/plugins/formatNumber";
import notifications from "~/components/Notifications";
import login from "~/components/Login";
export default {
  name: "Products",
  data() {
    return {
      messages: [],
      openLogin: false,
      openRegister: false,
      searchQuery: "",
      ascending: "",
      popularSorted: "",
      reset: "",
      openDropDown: false
    }
  },
  components: {
    notifications
  },
  mounted() {
    this.$store.dispatch('ProductStore/getProduct')
  },
  methods: {
    formatNumber,
    sendingProductsToCart(data, index) {
      let isCheckedCart;
      let alert;
      if(!this.$auth.loggedIn) {
        this.openLogin = true
      } else {
        if (data.inCart === true) {
          isCheckedCart = false
          alert = 'delete'
          this.$store.commit('Cart/DELETE_PRODUCT', data);
          this.$store.dispatch('ProductStore/updatedProduct', {index, isCheckedCart})
        } else {
          isCheckedCart = true
          alert = 'add'
          this.$store.commit('Cart/SET_PRODUCTS_TO_CART', data);
          this.$store.dispatch('ProductStore/updatedProduct', {index, isCheckedCart})
        }
        this.callingNotification(alert)
      }
    },
    callingNotification(notification) {
      if(notification === 'delete') {
        this.messages.unshift({
          text: 'Товар удален из корзины',
          status: 'warning',
          icon: 'warning.svg',
          id: Date.now().toLocaleString(),
        });
      } else {
        this.messages.unshift({
          text: 'Товар добавлен в корзину',
          status: 'check',
          icon: 'checkMark.svg',
          id: Date.now().toLocaleString(),
        });
      }
    },
    controlPopup(data) {
      if(data.popup === 'login') {
        this.openLogin = data.status
        this.openRegister = false
      } else {
        this.openLogin = false
        this.openRegister = data.status
      }
    },
    performSearch() {
      this.$store.dispatch("ProductStore/searchProducts", this.searchQuery);
    },
    ascendingAndDescendingProducts(data) {
      const ascending = this.ascending
      this.$store.commit('ProductStore/ASCENDING_AND_DESCENDING_PRODUCTS', {data, ascending})
    },
    popularProducts() {
      this.$store.commit('ProductStore/POPULAR_PRODUCTS', this.popularSorted)
    },
    resetProducts() {
      this.$store.commit('ProductStore/RESET_PRODUCTS', this.reset)
    },
  },
  computed: {
    products() {
      const productFromCart = this.$store.getters['Cart/cart'];
      let products = this.$store.getters['ProductStore/Products'];

      if (products) {
        products = products.map(product => {
          const cartProduct = productFromCart.find(item => item.id === product.id);
          if (cartProduct) {
            this.$store.commit('ProductStore/UPDATE_PRODUCT_IN_CART', {id: product.id, inCart: true});
          } else {
            this.$store.commit('ProductStore/UPDATE_PRODUCT_IN_CART', {id: product.id, inCart: false});
          }
          return product;
        });
      }

      return products || [];
    }
  }
}
</script>

<style lang="scss">
.products {
  margin-bottom: 70px;
  &-title {
    font-size: 24px;
    font-weight: 700;
  }
  &__filters {
    border: 1px solid #FF6F95;
    border-radius: 15px;
    padding: 20px 0;
    margin-bottom: 30px;
    &-title {
      p {
        text-align: center;
        font-size: 20px;
      }
    }
    &-search {
      border-bottom: 1px solid #FF6F95;
      &-input-container {
        position: relative;
        margin: 15px;
        input {
          width: 100%;
          height: 50px;
          border: 2px solid #FF6F95;
          border-radius: 10px;
          padding: 5px 35px 5px 10px;
        }
        img {
          position: absolute;
          top: 15px;
          right: 10px;
        }
      }

    }
    &-sorted {
      margin: 15px 0;
      &-item {
        margin: 0 15px 15px 15px;
        label {
          display: flex;
          align-items: center;
          column-gap: 10px;
        }
        p {
          margin-bottom: 0;
        }
      }
    }
    &-categories {
      &-dropdown {
        display: flex;
        justify-content: center;
        .dropdown {
          .btn {
            background: #FF6F95;
            border-color: #fff;
          }
          &-menu {
            display: block;
          }
        }
      }

    }
  }
  &-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-bottom: 30px;
    &-img {
      margin-bottom: 2em;
      img {
        width: 100%;
        height: 250px;
        border-radius: 5px;
      }
    }
    &-title {
      p {
        color: #FF6F95;
        font-size: 20px;
        font-weight: 700;
      }
    }
    &-description {
      p {
        font-size: 18px;
        font-weight: 500;
      }
    }
    &-category {
      p {
        color: #FF6F95;
        font-size: 18px;
      }
    }
    &-price {
      display: flex;
      p, span {
        font-size: 18px;
        font-weight: 500;
      }
      span {
        color: gray;
      }
    }
    button {
      border-radius: 8px;
      background: #FF6F95;
      display: flex;
      align-items: center;
      column-gap: 10px;
      padding: 10px 10px 10px 22px;
      p {
        margin-bottom: 0;
        color: #FFF;
        font-size: 20px;
        font-weight: 700;
      }
      img {
        width: 30px;
      }
    }
  }
  .product-animated-enter {
    transform: translateX(120px);
    opacity: 0;
  }

  .product-animated-enter-active {
    transition: all .6s ease;
  }

  .product-animated-enter-to {
    opacity: 1;
  }

  .product-animated-leave {
    height: 50px;
    opacity: 1;
  }

  .product-animated-leave-active {
    transition: translate .3s ease, opacity .3s, height .3s .2s;
  }

  .product-animated-leave-to {
    height: 0;
    transform: translateX(0px);
    opacity: 0;
  }

  .product-animated-move {
    transition: transform .3s;
  }
}

.radio__input {
  display: none;
}

.radio__radio {
  width: 1.25em;
  height: 1.25em;
  border: 2px solid #FF6F95;
  border-radius: 50%;
  box-sizing: border-box;
  padding: 2px;
  cursor: pointer;
  &::after {
    content: "";
    width: 100%;
    height: 100%;
    display: block;
    background: #FF6F95;
    border-radius: 50%;
    transform: scale(0);

    transition: transform .15s;
  }
}

.radio__input:checked + .radio__radio::after {
  transform: scale(1);
}

.product-animated-enter {
  transform: translateX(120px);
  opacity: 0;
}
.product-animated-enter-active {
  transition: all .6s ease;
}
.product-animated-enter-to {
  opacity: 1;
}
.product-animated-leave {
  height: 50px;
  opacity: 1;
}
.product-animated-leave-active {
  transition: translate .6s ease, opacity .6s, height .6s .2s;
}
.product-animated-leave-to {
  height: 0;
  transform: translateX(0px);
  opacity: 0;
}
.product-animated-move {
  transition: transform .6s;
}
@media (max-width: 767px) {
  .products {
    &-item-img {
      img {
        height: 200px;
      }
    }
    .col-sm-3 {
      width: 50%;
    }
  }
}
@media (max-width: 290px) {
  .products {
    .col-sm-3 {
      width: 100%;
    }
  }
}
</style>
