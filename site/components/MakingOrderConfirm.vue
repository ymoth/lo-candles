<template>
  <section class="confirm__order">
    <div class="container">
      <div class="row">
        <div class="col-lg-6">
          <div class="confirm__order-cart">
            <div class="confirm__order-title">
              <h2>Корзина</h2>
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
        </div>
        <div class="col-lg-6">
          <div class="row">
            <div class="col-lg-12">
              <div class="confirm__order-delivery">
                <div class="confirm__order-title">
                  <h2>Способ доставки</h2>
                </div>
                <div class="confirm__order-delivery-img">
                  <img v-if="delivery === 'Яндекс'" src="/delivery/yandex.svg" alt="" />
                  <img v-else src="/delivery/pickup.svg" alt="">
                </div>
                <div class="confirm__order-delivery-text">
                  <p>{{ delivery }}</p>
                </div>
              </div>
            </div>
            <div class="col-lg-12">
              <div class="confirm__order-form">
                <div class="confirm__order-title">
                  <h2>Заполните свои данные</h2>
                </div>
                <form @submit.prevent="">
                  <div class="confirm__order-form-input">
                    <p>Номер телефона</p>
                    <input v-mask="'+7 (###) ###-##-##'" placeholder="+7 (000) 00-00-00" v-model="localPhoneUser" @input="updateDataUser()"/>
                  </div>
                  <div class="confirm__order-form-textarea">
                    <p>Комментарий к заказу</p>
                    <textarea placeholder="Комментарий к заказу" v-model="localCommentaryUser" @input="updateDataUser()">
                    </textarea>
                  </div>
                  <div class="order-button">
                    <button class="order-button-back" type="button" @click="nextStep('second')">
                      Назад
                    </button>
                    <button
                      :disabled="phoneUser.length < 18"
                      class="order-button-next"
                      type="button"
                      @click="nextStep('fourth')"
                      title="Напишите свой номер"
                    >
                      Продолжить
                    </button>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "MakingOrderConfirm",
  props: {
    delivery: {
      type: String,
      default: () => "",
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
  data() {
    return {
      localPhoneUser: this.phoneUser,
      localCommentaryUser: this.commentaryUser
    }
  },
  methods: {
    nextStep(step) {
      this.$emit('nextStep', step)
    },
    updateDataUser() {
      this.$emit('updateDataUser', { phone: this.localPhoneUser, commentary: this.localCommentaryUser })

    }
  },
  computed: {
    cartData() {
      return this.$store.getters['Cart/cart']
    }
  },
}
</script>

<style lang="scss">
.confirm__order {
  &-title {
    h2 {
      font-size: 28px;
      font-weight: 700;
    }
  }
  &-cart {
    &-item {
      margin-bottom: 20px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      border-radius: 12px;
      padding: 10px;
      &-img {
        margin-bottom: 20px;
        img {
          width: 200px;
          height: 200px;
          border-radius: 5px;
        }
      }
      &-title {
        margin-bottom: 10px;
        span {
          color: #808080;
          font-size: 18px;
          font-weight: 600;
        }
      }
      &-subtitle {
        p {
          color: #808080;
          font-size: 18px;
          font-weight: 600;
        }
      }
    }
  }
  &-delivery {
    &-text {
      p {
        color: #FF6F95;
        font-size: 24px;
      }
    }
  }
  &-form {
    form {
      border: 1px solid #FF6F95;
      border-radius: 12px;
      padding: 15px 30px;
      .confirm__order-form-input {
        p {
          font-size: 18px;
          margin-bottom: 10px;
        }
        input {
          border: 1px solid #ef96ae;
          border-radius: 10px;
          padding: 10px;
          width: 100%;
          margin-bottom: 10px;
        }

      }
      .confirm__order-form-textarea {
        p {
          font-size: 18px;
          margin-bottom: 10px;
        }
        textarea {
          border: 1px solid #ef96ae;
          border-radius: 10px;
          padding: 10px;
          width: 100%;
          margin-bottom: 10px;
          min-height: 150px;
          resize: none;
        }
      }
    }
  }
}
@media (max-width: 330px) {
  .confirm__order {
    .order-button {
      display: flex;
      flex-wrap: wrap;
      button {
        margin-bottom: 10px;
      }
    }
  }
}
</style>
