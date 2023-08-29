<template>
  <section class="products">
    <hr>
    <div class="container">
      <div class="products-title">
        <h2>Популярные товары</h2>
      </div>
      <div class="row">
        <div
          class="col-lg-4"
          v-for="item in topProducts"
          :key="item.id"
        >
          <div class="products-item">
            <div class="products-item-img">
              <img :src="item.photo" alt="" />
            </div>
            <div class="products-item-title">
              <p>{{item.title}}</p>
            </div>
            <div class="products-item-price">
              <span>{{item.string_price}} тг </span><span>/ шт</span>
            </div>
            <button>
              <p>Корзина</p>
              <img src="/products/cart.svg" alt="" />
            </button>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "Products",
  data() {
    return {
    }
  },
  created() {
    this.$store.dispatch('TopProductStore/getTopProduct')
  },
  computed: {
    topProducts() {
      return this.$store.state.TopProductStore.topProducts
    }
  }
}
</script>

<style lang="scss">
.products {
  hr {
    color: #FFA3BB;
    height: 2px;
    opacity: 1;
  }
  &-title {
    margin-bottom: 90px;
    position: relative;
    h2 {
      color: #FF6F95;
      text-align: center;
      font-size: 36px;
      font-weight: 700;
    }
  }
  &-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-bottom: 40px;
    &-img {
      margin-bottom: 25px;
      position: relative;
      z-index: 3;
      img {
        width: 233px;
        height: 300px;
        border-radius: 8px;
      }
    }
    &-title {
      margin-bottom: 15px;
      p {
        color: #FF6F95;
        text-align: center;
        font-size: 36px;
        font-weight: 700;
      }
    }
    &-price {
      span {
        color: #FF6F95;
        text-align: center;
        font-size: 36px;
        font-weight: 400;
        &:nth-child(2) {
          color: gray;
          font-size: 24px;
        }
      }
    }
    button {
      border-radius: 8px;
      background: #FF6F95;
      display: flex;
      align-items: center;
      padding: 10px 10px 10px 22px;
      p {
        margin-bottom: 0;
        color: #FFF;
        font-size: 32px;
        font-weight: 700;
      }
    }
  }
  .col-lg-4 {
    position: relative;
  }
  .col-lg-4:last-child {
    &:before {
      content: "";
      background: url("/products/candle.png") no-repeat;
      position: absolute;
      width: 280px;
      height: 204px;
      left: -125px;
      bottom: -80px;
      z-index: 2;
    }
    &:after {
      content: "";
      position: absolute;
      background: url("/products/smoke.png") no-repeat;
      top: 115px;
      left: -160px;
      width: 260px;
      height: 355px;
      z-index: 1;
    }
  }
}
@media(max-width: 425px) {
  .products {
    &-title {
      margin-bottom: 30px;
      h2 {
        font-size: 24px;
      }
    }
    &-item {
      &-title {
        margin-bottom: 0;
        p {
          font-size: 20px;
        }
      }
      &-price {
        p {
          font-size: 20px;
        }
      }
      button {
        padding: 10px 10px 10px 16px;
        p {
          font-size: 18px;
        }
        img {
          width: 25px;
        }
      }
    }
  }
  .col-lg-4:last-child {
    &:before {
      display: none;
    }
    &:after {
      display: none;
    }
  }
}
</style>
