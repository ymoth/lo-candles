<template>
  <aside class="history__order">
    <div class="history__order-title">
      <h2>История моих заказов</h2>
    </div>
    <div class="history__order__content">
      <div class="row">
        <div class="col-md-6">
          <div class="history__order__content-title">
            <h2>Заказы в ожидании: </h2>
          </div>
          <div class="col-12">
            <div
              v-for="order in pendingOrders"
              :key="order.order"
              class="history__order__content-item"
            >
              <div class="row" v-if="pendingOrders && pendingOrders.length">
                <div class="col-8">
                  <div class="history__order__content-item-number-order">
                    <p>Номер заказа: {{ order.order }}</p>
                  </div>
                  <div class="history__order__content-item-status">
                    <p>Статус: {{ order.status }}</p>
                  </div>
                  <div class="history__order__content-item-detailed">
                    <nuxt-link :to="'/personalCabinet/orderDetail/' + order.order">Подробнее</nuxt-link>
                  </div>
                </div>
                <div class="col-4">
                  <watcher :arrowClass="'rotate-animation-' + order.order" :showArrow="true" />
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="col-md-6">
          <div class="history__order__content-title">
            <h2>Выданные заказы: </h2>
          </div>
          <div class="col-12">
            <div
              v-for="order in deliveredOrders"
              :key="order.order"
              class="history__order__content-item"
            >
              <div class="row" v-if="deliveredOrders && deliveredOrders.length"></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </aside>
</template>

<script>
import watcher from "~/components/watcher/watcher.vue";
export default {
  name: "myHistoryOrder",
  components: {
    watcher
  },
  mounted() {
    this.$store.dispatch('historyOrder/getHistoryOrderFromApi')
  },
  computed: {
    historyOrder() {
      return this.$store.getters['historyOrder/history']
    },
    pendingOrders() {
      return this.historyOrder && this.historyOrder.items
        ? this.historyOrder.items.filter(order => order.status === "На проверке")
        : [];
    },
    deliveredOrders() {
      return this.historyOrder && this.historyOrder.items
        ? this.historyOrder.items.filter(order => order.status === "Выдан")
        : [];
    }
  }
}
</script>

<style lang="scss">
.history__order {
  &-title {
    h2 {
      color: #FFB8B8;
      font-size: 32px;
      font-weight: 600;
    }
  }
  &__content {
    &-title {
      h2 {
        color: #FFF;
        font-size: 28px;
        font-weight: 600;
      }
    }
    &-item {
      box-shadow: 0 4px 8px rgba(255, 52, 108, 0.5);
      background: #F16D91;
      border-radius: 5px;
      margin-bottom: 1em;
      width: 100%;
      max-width: 350px;
      padding: 10px;
      &-number-order {
        p {
          color: #FFF;
          font-size: 20px;
        }
      }
      &-status {
        p {
          color: #FFF;
        }
      }
      &-detailed {
        a {
          color: #5252f3;
        }
      }
    }
  }
}
</style>
