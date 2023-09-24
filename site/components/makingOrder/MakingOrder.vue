<template>
  <aside class="order">
    <div class="container">
      <div class="order-title">
        <h1>Оформление заказа</h1>
      </div>
      <div class="order__content">
        <div class="row">
          <div class="col-12">
            <div class="order__content-first order__content__progress">
              <div class="order__content-step">
                <div class="order__content-step-number">
                  <span>1</span>
                </div>
                <div class="order__content-step-text">
                  <span>Товары в корзине</span>
                </div>
              </div>
              <transition name="fade" mode="out-in" appear>
                <MakingOrderCart
                  v-if="step === 'first'"
                  :total-price="totalPrice"
                  @nextStep="updateStep"
                />
              </transition>
            </div>
          </div>
          <div class="col-12">
            <div class="order__content-second order__content__progress">
              <div class="order__content-step">
                <div class="order__content-step-number">
                  <span>2</span>
                </div>
                <div class="order__content-step-text">
                  <span>Способы доставки</span>
                </div>
              </div>
              <transition name="fade" mode="out-in" appear>
                <MakingOrderDelivery
                  v-if="step === 'second'"
                  @update-delivery="updateDelivery"
                  @nextStep="updateStep"
                />
              </transition>
            </div>
          </div>
          <div class="col-12">
            <div class="order__content-third order__content__progress">
              <div class="order__content-step">
                <div class="order__content-step-number">
                  <span>3</span>
                </div>
                <div class="order__content-step-text">
                  <span>Подтверждение</span>
                </div>
              </div>
              <transition name="fade" mode="out-in" appear>
                <MakingOrderConfirm
                  v-if="step === 'third'"
                  :delivery="delivery"
                  :phoneUser="phoneUser"
                  :commentaryUser="commentaryUser"
                  @nextStep="updateStep"
                  @updateDataUser="updatePhoneAndCommentaryUser"
                />
              </transition>
            </div>
          </div>
          <div class="col-12">
            <div class="order__content-fourth order__content__progress">
              <div class="order__content-step">
                <div class="order__content-step-number">
                  <span>4</span>
                </div>
                <div class="order__content-step-text">
                  <span>Связь с менеджером</span>
                </div>
              </div>
              <transition name="fade" mode="out-in" appear>
                <MakingOrderCompletion
                  v-if="step === 'fourth'"
                  :total-price="totalPrice"
                  :delivery="delivery"
                  :phoneUser="phoneUser"
                  :commentaryUser="commentaryUser"
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
import MakingOrderCart from '~/components/makingOrder/MakingOrderCart.vue'
import MakingOrderDelivery from "~/components/makingOrder/MakingOrderDelivery.vue";
import MakingOrderConfirm from "~/components/makingOrder/MakingOrderConfirm.vue";
import MakingOrderCompletion from "~/components/makingOrder/MakingOrderCompletion.vue";
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
    margin-bottom: 2rem;
  }
  &__content {
    &-step {
      display: flex;
      align-items: center;
      column-gap: 10px;
      margin-bottom: 20px;
      &-number {
        width: 30px;
        height: 30px;
        line-height: 26px;
        border: 3px solid #d71a21;
        border-radius: 50%;
        text-align: center;
        font-size: 15px;
        font-weight: bold;
        display: inline-block;
        vertical-align: middle;
        margin-right: 5px;
      }
      &-text {
        span {
          font-size: 18px;
          font-weight: 500;
        }
      }
    }
  }
  .fade-enter-active, .fade-leave-active {
    transition: opacity 0.2s, transform 0.3s, height .3s;
  }
  .fade-enter, .fade-leave-to {
    height: 0;
    opacity: 0;
    transform: translateY(-20px);
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

</style>
