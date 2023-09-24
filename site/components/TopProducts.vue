<template>
  <section class="top__products">
    <hr>
    <div class="container">
      <div class="top__products-title">
        <h2>Популярные товары</h2>
      </div>
      <div class="row">
        <div
          class="col-lg-4"
          v-for="(item, index) in topProducts"
          :key="item.id"
        >
          <div class="top__products-item">
            <div class="top__products-item-img">
              <img :src="'https://dev.aromatic.kz/' + item.photo" alt="" />
            </div>
            <div class="top__products-item-title">
              <p>{{item.title}}</p>
            </div>
            <div class="top__products-item-price">
              <span>{{formatNumber(item.price)}} тг </span><span>/ шт</span>
            </div>
          </div>
        </div>
      </div>
      <div class="top__products-button">
        <button @click="goToCatalog">
          <p>Перейти к остальным товарам</p>
          <img src="/products/arrow.svg" alt="" />
        </button>
      </div>
    </div>
  </section>
</template>

<script>
import formatNumber from "~/plugins/formatNumber";
export default {
  name: "Products",
  created() {
    this.$store.dispatch('ProductStore/getProduct')
  },
  methods: {
    formatNumber,
    goToCatalog() {
      this.$router.push('/catalog');
    }
  },
  computed: {
    topProducts() {
      return this.$store.getters['ProductStore/topProducts'];
    }
  }
}
</script>

<style lang="scss">
.top__products {
  margin-bottom: 70px;
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
        height: 231px;
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
        margin-bottom: 0;
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
  }
  &-button {
    display: flex;
    justify-content: center;
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
        transform: rotate(90deg);
        filter: invert(100%) sepia(0%) saturate(7500%) hue-rotate(48deg) brightness(110%) contrast(113%);
      }
    }

  }
  .col-lg-4 {
    position: relative;
    button {
      display: none;
    }
  }
  .col-lg-4:nth-child(2) {
    button {
      display: flex;
    }
  }
}
@media(max-width: 425px) {
  .top__products {
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
}
</style>
