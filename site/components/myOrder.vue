<template>
  <section class="my__order">
    <div class="container">
      <div class="my__order-title">
        <h1>Заказ №{{ order.order }}</h1>
      </div>
      <div class="my__order__content">
        <div class="my__order__content-status">
          <h2>Статус заказа: {{ order.status }}</h2>
        </div>
        <div class="row">
          <div
            class="col-md-4"
            v-for="item in order.data"
            :key="item.product.id"
          >
            <div class="my__order__content-item">
              <div class="my__order__content-item-img" >
                <img :src="'https://dev.aromatic.kz/' + item.product.photo" alt="" style="width: 200px; height: 250px"/>
              </div>
              <div>
                <div class="my__order__content-item-title">
                  <p>Название: {{item.product.title}}</p>
                </div>
                <div class="my__order__content-item-price">
                  <p>Цена: {{item.product.price}} тг.</p>
                </div>
                <div class="my__order__content-item-count">
                  <p>Количество: {{item.count}}</p>
                </div>
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
  name: "myOrder",
  props: {
    order: {
      type: Object,
      default: () => {}
    }
  }
}
</script>

<style lang="scss">
.my__order {
  &-title {
    h1 {
      font-size: 28px;
    }
  }
  &__content {
    &-status {
      margin-bottom: 30px;
      h2 {
        font-size: 24px;
      }
    }
    &-item {
      display: flex;
      column-gap: 20px;
      margin-bottom: 30px;
      background: #ede8e9d6;
      img {
        border-radius: 5px;
      }
      &-title {
        margin-top: 10px;
      }
      p {
        color: #000;
      }
    }
  }
}
</style>
