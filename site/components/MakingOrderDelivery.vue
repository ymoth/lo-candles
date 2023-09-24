<template>
  <section class="delivery">
    <div class="container">
      <div class="row">
        <div class="col-lg-4">
          <div class="delivery__content">
            <div class="row">
              <div class="col-lg-12">
                <div class="delivery__content-pickup delivery-method">
                  <label for="pickup" class="radio">
                    <input
                      type="radio"
                      name="deliveryMethod"
                      id="pickup"
                      class="radio__input"
                      @input="updateDelivery('Самовывоз')"
                    >
                    <div class="radio__radio"></div>
                  </label>
                  <div class="delivery-method-content">
                    <div class="delivery-method-img">
                      <img src="/delivery/pickup.svg" alt="">
                    </div>
                    <div class="delivery-method-title">
                      <p>Самовывоз</p>
                    </div>
                  </div>

                </div>
              </div>
              <div class="col-lg-12">
                <div class="delivery__content-yandex delivery-method">
                  <label for="yandex" class="radio">
                    <input
                      type="radio"
                      name="deliveryMethod"
                      id="yandex"
                      class="radio__input"
                      @input="updateDelivery('Яндекс')"
                    >
                    <div class="radio__radio"></div>
                  </label>
                  <div class="delivery-method-content">
                    <div class="delivery-method-img">
                      <img src="/delivery/yandex.svg" alt="">
                    </div>
                    <div class="delivery-method-title">
                      <p>Яндекс доставка</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="col-lg-8">
          <div class="delivery__description">
            <div class="delivery__description-pickup delivery__description-method" v-if="delivery === 'Самовывоз'">
              <div class="delivery__description-method-title">
                <p>Самовывоз</p>
                <hr>
              </div>
              <div class="delivery__description-method-text">
                <p>Забрать можно по адресу: </p>
                <p>ул. Рихарда Зорге 18/1 (ТРЦ Mart Village) магазин “Микс Прайс”</p>
              </div>
            </div>
            <div class="delivery__description-yandex delivery__description-method" v-else-if="delivery === 'Яндекс'">
              <div class="delivery__description-method-title">
                <p>Яндекс</p>
                <hr>
              </div>
              <div class="delivery__description-method-text">
                <p>Вызываем доставкой на ваш адрес услугами Яндекс Доставкой, за вашу оплату.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="order-button">
        <button class="order-button-back" @click="nextStep('first')">
          Назад
        </button>
        <button
          :disabled="selectDelivery === false"
          class="order-button-next"
          @click="nextStep('third')"
          title="Выберите метод доставки"
        >
          Продолжить
        </button>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "MakingOrderDelivery",
  data() {
    return {
      delivery: "",
      selectDelivery: false
    }
  },
  methods: {
    updateDelivery(delivery) {
      this.delivery = delivery
      this.selectDelivery = true
      this.$emit('update-delivery', this.delivery)
    },
    nextStep(step) {
      this.$emit('nextStep', step)
    }
  }
}
</script>

<style lang="scss">
.delivery {
  &__content {
    .delivery-method {
      display: flex;
      column-gap: 15px;
      &-content {
        display: flex;
        flex-direction: column;
        .delivery-method-title {
          color: #F44575;
          font-size: 24px;
          font-weight: 600;
        }
        .delivery-method-img {
          height: 110px;
        }
      }
    }
  }
  &__description {
    margin-bottom: 30px;
    .delivery__description-method {
      border: 1px solid #FF6F95;
      border-radius: 10px;
      padding: 15px;
      height: 300px;
      &-title {
        p {
          font-size: 24px;
          color: #FF6F95;
          font-weight: 500;
        }
        hr {
          color: #ef96ae;
        }
      }
      &-text {
        p {
          font-size: 20px;
        }
      }
    }
  }
}
@media(max-width: 1023px) {
  .delivery {
    &__content {
      .row {
        .col-lg-12 {
          max-width: 50%;
          width: 50%;
        }
      }
    }
  }
}
@media(max-width: 330px) {
  .delivery {
    &__content {
      .row {
        .col-lg-12 {
          max-width: 100%;
          width: 100%;
        }
      }
    }
  }
}
</style>
