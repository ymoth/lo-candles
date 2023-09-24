<template>
  <aside class="order">
    <div class="container">
      <div class="order-title">
        <h2>Оформить заказ</h2>
      </div>
      <div class="order__content">
        <div class="row">
          <div class="col-lg-3">
            <div class="order__content__line">
              <div class="order__content__line-first order__content__line__progress">
                <div class="order__content__line-number-step">
                  <p>1</p>
                </div>
                <div class="order__content__line-name-step">
                  <p>Корзина</p>
                </div>
              </div >
              <div class="order__content__line-second order__content__line__progress">
                <div class="order__content__line-number-step">
                  <p>2</p>
                </div>
                <div class="order__content__line-name-step">
                  <p>Способы доставки</p>
                </div>
              </div>
              <div class="order__content__line-third order__content__line__progress">
                <div class="order__content__line-number-step">
                  <p>3</p>
                </div>
                <div class="order__content__line-name-step">
                  <p>Подтверждение</p>
                </div>
              </div>
              <div class="order__content__line-fourth order__content__line__progress">
                <div class="order__content__line-number-step">
                  <p>4</p>
                </div>
                <div class="order__content__line-name-step">
                  <p>Связь с менеджером</p>
                </div>
              </div>
            </div>
          </div>
          <div class="col-lg-3">
            <div class="order__content__progress">
              <div class="order__content__line-first order__content__line__progress" v-if="activeProgress === 'first'">
                <div class="order__content__line-number-step">
                  <p>1</p>
                </div>
                <div class="order__content__line-name-step">
                  <p>Корзина</p>
                </div>
              </div>
              <div class="order__content__line-second order__content__line__progress" v-if="activeProgress === 'second'">
                <div class="order__content__line-number-step">
                  <p>2</p>
                </div>
                <div class="order__content__line-name-step">
                  <p>Способы доставки</p>
                </div>
              </div>
              <div class="order__content__line-third order__content__line__progress" v-if="activeProgress === 'third'">
                <div class="order__content__line-number-step">
                  <p>3</p>
                </div>
                <div class="order__content__line-name-step">
                  <p>Подтверждение</p>
                </div>
              </div>
              <div class="order__content__line-fourth order__content__line__progress" v-if="activeProgress === 'fourth'">
                <div class="order__content__line-number-step">
                  <p>4</p>
                </div>
                <div class="order__content__line-name-step">
                  <p>Связь с менеджером</p>
                </div>
              </div>
            </div>
          </div>
          <div class="col-lg-9">
              <div class="order__content-cart">
                <transition name="fade" mode="out-in">
                  <MakingOrderCart
                    :total-price="totalPrice"
                    v-if="step === 'first'"
                    @nextStep="updateStep"
                  />
                  <MakingOrderDelivery
                    v-else-if="step === 'second'"
                    @update-delivery="updateDelivery"
                    @nextStep="updateStep"
                  />
                  <MakingOrderConfirm
                    :delivery="delivery"
                    :phoneUser="phoneUser"
                    :commentaryUser="commentaryUser"
                    v-else-if="step === 'third'"
                    @nextStep="updateStep"
                    @updateDataUser="updatePhoneAndCommentaryUser"
                  />
                  <MakingOrderCompletion
                    :total-price="totalPrice"
                    :delivery="delivery"
                    :phoneUser="phoneUser"
                    :commentaryUser="commentaryUser"
                    v-else-if="step === 'fourth'"
                  />
                </transition>

              </div>
          </div>
        </div>
      </div>
    </div>
  </aside>
</template>

<script>
import MakingOrderCart from '~/components/MakingOrderCart.vue'
import MakingOrderDelivery from "~/components/MakingOrderDelivery.vue";
import MakingOrderConfirm from "~/components/MakingOrderConfirm.vue";
import MakingOrderCompletion from "~/components/MakingOrderCompletion.vue";
export default {
  name: "MakingOrder",
  components: {
    MakingOrderCart, MakingOrderDelivery, MakingOrderConfirm, MakingOrderCompletion
  },
  data() {
    return {
      activeProgress: 'first',
      step: 'first',
      delivery: "",
      phoneUser: "",
      commentaryUser: "",
    }
  },
  methods: {
    updateDelivery(delivery) {
      this.delivery = delivery
    },
    updatePhoneAndCommentaryUser(phone) {
      this.phoneUser = phone.phone
      this.commentaryUser = phone.commentary
    },
    updateStep(step) {
      this.step = step
    }
  },
  computed: {
    setProductsFromCart() {
      return this.$store.state.Cart.cartData
    },
    totalPrice() {
      const total = this.setProductsFromCart.reduce((acc, product) => acc + product.finalPrice, 0);
      return total
    }
  }
}
</script>

<style lang="scss">
.order {
  margin-top: 20px;
  &-title {
    margin-bottom: 30px;
  }
  &__content {
    .col-lg-3:nth-child(2) {
      display: none;
    }
    &__line {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
      position: relative;
      &:before {
        content: "";
        position: absolute;
        width: 2px;
        top: 18px;
        left: 51px;
        height: 299px;
        background: #FF6F95;
        z-index: -1;
      }
      &-number-step {
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 15px;
        position: relative;
        z-index: 1;
        &:before {
          content: "";
          position: absolute;
          width: 120px;
          top: 18px;
          right: 0;
          height: 2px;
          background: #FF6F95;
          z-index: -1;
        }
        p {
          font-size: 20px;
          color: #fff;
          padding: 5px 15px;
          background: #FF6F95;
          border-radius: 50px;
        }
      }
      &__progress {
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
        margin-bottom: 20px;
      }
      p {
        margin-bottom: 0;
      }
    }
  }
  .fade-enter-active, .fade-leave-active {
    transform: translateX(20px);
    transition: opacity 0.3s, transform 0.2s;
  }
  .fade-enter, .fade-leave-to {
    transform: translateX(-20px);
    opacity: 0;
  }
}
.order-button {
  display: flex;
  justify-content: flex-end;
  column-gap: 20px;
  button {
    border-radius: 50px;
    padding: 10px 30px;
    font-size: 18px;
  }
  &-back {
    border: 1px solid gray;

    background: #fff;
    border-radius: 20px;
  }
  &-next {
    background: #FF6F95;
    color: #fff;
    &:disabled {
      background: #ef96ae;
    }
  }
}
@media(max-width: 1024px) {
  .order {
    .order__content__line:before {
      left: 33px;
    }
    .order__content__line-number-step:before {
      width: 93px;
    }
  }
}
@media(max-width: 768px) {
  .order {
    .order__content__line:before {
      display: none;
    }
    .order__content__line {
      display: flex;
      flex-direction: row;
      width: 100%;
      column-gap: 30px;
    }
    .order__content__line-number-step:before {
      left: 30px;
      width: 150px;
    }
    .order__content__line__progress:last-child {
      .order__content__line-number-step:before {
        display: none;
      }
    }
    .order__content__line-name-step {
      p {
        height: 50px;
      }
    }
  }
}
@media (max-width: 520px) {
  .order {
    &__content {
      .col-lg-3:nth-child(1) {
        display: none;
      }
      .col-lg-3:nth-child(2) {
        display: block;
      }
      .col-lg-9 {
        padding: 0;
      }
    }
    .order__content__line-number-step {
      margin-bottom: 0;
    }
    .order__content__line-number-step p {
      padding: 8px 21px;
    }
    .order__content__line-name-step p {
      height: 100%;
    }
  }
}
</style>
