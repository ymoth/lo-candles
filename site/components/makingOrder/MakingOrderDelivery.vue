<template>
  <section class="delivery">
    <div class="container">
      <div class="row">
        <div class="col-lg-12">
          <div class="delivery__content">
            <div class="row">
              <div class="col-lg-12" :class="{ 'selected-method': delivery === 'pickup' }">
                <div class="delivery__content-pickup delivery-method" @click="handleClick('pickup')">
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
                      <img src="/delivery/shop.svg" alt="">
                    </div>
                    <div class="delivery-method-title">
                      <span>Самовывоз</span>
                    </div>
                  </div>
                </div>
                <div class="delivery__content-pickup-info delivery-info">
                  <span>Бесплатно</span>
                  <img src="/delivery/mark.svg" alt="">
                  <div class="hint">
                    <ul>
                      <li><strong>✔</strong> На указанный Вами номер телефона Вы получите SMS-уведомление с номером заказа и адресом магазина, в котором Вы можете получить свой заказ.</li>
                      <li><strong>✔</strong> После оформления заказа, Вы можете самостоятельно забрать свой заказ в нашем магазине</li>
                    </ul>
                  </div>
                </div>
              </div>
              <div class="col-lg-12" :class="{ 'selected-method': delivery === 'yandex' }">
                <div class="delivery__content-yandex delivery-method" @click="handleClick('yandex')">
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
                      <img src="/delivery/delivery-fast.svg" alt="">
                    </div>
                    <div class="delivery-method-title">
                      <span>Яндекс доставка</span>
                    </div>
                  </div>
                </div>
                <div class="delivery__content-yandex-info delivery-info">
                  <span>Платно</span>
                  <img src="/delivery/mark.svg" alt="">
                  <div class="hint">
                    <ul>
                      <li><strong>✔</strong>Доставка курьером осуществляется на указанные Вами адрес и день с выбранным промежутком времени в заказе.</li>
                      <li><strong>✔</strong>Предварительно за час до доставки наши сотрудники с Вами свяжутся.</li>
                    </ul>
                  </div>
                </div>
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
    },
    handleClick(method) {
      const radioElement = document.getElementById(method);

      if (radioElement) {
        radioElement.checked = true;
        this.updateDelivery(method);
      }
    }
  }
}
</script>

<style lang="scss">
.delivery {
  background: rgba(220, 220, 220, 0.34);
  padding: 10px;
  border-radius: 10px;
  margin-bottom: 20px;
  &__content {
    .col-lg-12 {
      display: flex;
      justify-content: space-between;
      margin-bottom: 30px;
    }
    .selected-method {
      border: 1px solid #FF346C;
      padding: 15px;
      border-radius: 15px;
    }
    .delivery-info {
      position: relative;
      display: flex;
      align-items: center;
      column-gap: 10px;
      .hint {
        display: none;
        opacity: 0;
        transition: opacity 0.3s ease;
      }
      img {
        filter: brightness(0) saturate(100%) invert(79%) sepia(5%) saturate(185%) hue-rotate(339deg) brightness(90%) contrast(91%);
      }
      &:hover {
        cursor: pointer;
        img {
          filter: brightness(0) saturate(100%) invert(13%) sepia(84%) saturate(3355%) hue-rotate(346deg) brightness(125%) contrast(99%);
          transition: filter 0.3s ease;
        }
        .hint {
          display: block;
          position: absolute;
          width: 500px;
          top: 30px;
          right: 0;
          background: #fff;
          z-index: 2;
          padding: 10px;
          animation: fadeIn 0.3s ease forwards;
          ul {
            padding-left: 1rem;
            li {
              display: flex;
              column-gap: 5px;
              margin-bottom: 10px;
              text-align: center;

            }
          }
        }
      }
    }
    .delivery-method {
      display: flex;
      align-items: center;
      column-gap: 15px;
      cursor: pointer;
      &-content {
        display: flex;
        align-items: center;
        column-gap: 20px;
        .delivery-method-title {
          span {
          }
        }
        .delivery-method-img {
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
@keyframes fadeIn {
  to {
    opacity: 1;
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
