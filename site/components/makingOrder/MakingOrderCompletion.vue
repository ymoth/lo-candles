<template>
  <section class="order__completion">
    <div class="container">
      <div class="order__completion-title">
        <h2>Спасибо за заказ</h2>
      </div>
      <div class="row">
        <div class="col-lg-8">
          <div class="order__completion-cart">
            <div class="order__completion-cart-title">
              <h2>Информация о заказе</h2>
            </div>
            <div class="row">
              <div
                class="col-sm-6"
                v-for="item in cartData"
                :key="item.id"
              >
                <div class="confirm__order-cart-item">
                  <div class="confirm__order-cart-item-img">
                    <img :src="'https://dev.aromatic.kz' + item.photo" alt="">
                  </div>
                  <div>
                    <div class="confirm__order-cart-item-title">
                      <span>{{ item.title }}</span>
                    </div>
                    <div class="confirm__order-cart-item-subtitle">
                      <p>{{ item.count }} штук - {{ item.price }} тг.</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="order__completion-cart-price">
              <p>Итого: {{ totalPrice }} тг.</p>
              <p>Без учёта доставки</p>
            </div>
          </div>
        </div>
        <div class="col-lg-4">
          <div class="order__completion__info">
            <div class="order__completion__info-title">
              <h2>Связь с менеджером</h2>
              <hr>
            </div>
            <div class="order__completion__info-text">
              <p>Спасибо за заказ!</p>
              <p>Ожидайте, наш менеджер с вами свяжется</p>
              <p>С уважением, команда.</p>
              <img src="/confirm/AromaticCandles.png" alt="">
              <hr>
            </div>
            <div class="order__completion__info-user">
              <p>{{this.$auth.user.first_name }} {{ this.$auth.user.last_name }}</p>
              <span>Номер телефона: {{ phoneUser }}</span>
            </div>
            <div class="order__completion__info-text">
              <span>Доставка: {{ delivery }}. </span>
              <p style="margin-bottom: 15px;">Итого: {{ totalPrice }} тг.</p>
              <span>Комментарий к заказу:</span>
              <p>{{commentaryUser}}</p>
            </div>
          </div>
          <div class="order-button" style="justify-content: center">
            <button class="order-button-next" @click="goToHome">
              Перейти к главной странице
            </button>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "MakingOrderCompletion",
  props: {
    totalPrice: {
      type: Number,
      default: () => 0
    },
    delivery: {
      type: String,
      default: () => ""
    },
    phoneUser: {
      type: String,
      default: () => ""
    },
    commentaryUser: {
      type: String,
      default: () => ""
    }
  },
  mounted() {
    this.$axios.post('orders/create', {
      contact_data: {
        "first_name": this.userData.first_name,
        "last_name": this.userData.last_name,
        "phone_number": this.phoneUser,
        "commentary": this.commentaryUser
      },
      payload_products: this.payloadProducts
    })
  },
  beforeDestroy() {
    window.location.reload();
  },
  methods: {
    goToHome() {
      this.$router.push('/')
    },
  },
  computed: {
    cartData() {
      return this.$store.getters['Cart/cart']
    },
    payloadProducts() {
      let products = []
      this.cartData.forEach(item => {
        products.push({
          "id": item.id,
          "count": item.count
        })
      })
      return products
    },
    userData() {
      return this.$auth.user
    }
  }
}
</script>

<style lang="scss">
.order__completion {
  &-title {
    margin-bottom: 35px;
    h2 {
      font-size: 32px;
      font-weight: 600;
    }
  }
  &-cart {
    padding: 34px 0px 34px 15px;
    border-radius: 14px;
    background: rgba(169, 57, 124, 0.1);
    box-shadow: 0px 15px 30px 0px rgba(0, 0, 0, 0.25);
    margin-bottom: 1em;
    &-title {
      h2 {
        text-align: center;
        color: #FF6F95;
        font-size: 24px;
        font-weight: 600;
      }
    }
    &-price {
      margin-left: 50px;
      p:nth-child(1) {
        margin-bottom: 5px;
        color: #FF6F95;
        font-size: 38px;
        font-weight: 600;
      }
      p:nth-child(2) {
        color: #FF6F95;
        font-size: 24px;
        font-weight: 600;
      }
    }
  }
  &__info {
    hr {
      color: #FF346C;
      opacity: 1;
    }
    &-text {
      margin-bottom: 3em;
      p, span {
        font-size: 18px;
        font-weight: 600;
        color: gray;
        margin-bottom: 0;
      }
      img {
        margin: 15px 0;
      }
    }
    &-user {
      margin-bottom: 15px;
      p {
        margin-bottom: 5px;
        color: #F16D91;
        font-size: 28px;
        font-weight: 600;
      }
      span {
        color: gray;
        font-size: 18px;
        font-weight: 600;
      }
    }
  }
}
@media(max-width: 575px) {
  .order__completion {
    padding: 34px 0;
    .confirm__order-cart-item {
      display: flex;
      flex-direction: row;
      column-gap: 30px;
      img {
        width: 150px;
        height: 150px;
      }
      &-subtitle {
        p {
          font-size: 16px;
        }
      }
    }
  }
}
</style>
