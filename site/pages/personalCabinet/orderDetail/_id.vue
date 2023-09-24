<template>
  <div>
    <myOrder :order="order"/>
  </div>
</template>

<script>
import myOrder from "~/components/myOrder.vue";
export default {
  name: 'orderDetail',
  components: {
    myOrder
  },
  data() {
    return {
      order: []
    }
  },
  created() {
    this.$axios.get('/orders/getList')
      .then(res => {
        let orders = res.data.items
        const orderIdFromRoute = parseInt(this.orderID, 10);
        const order = orders.find(item => item.order === orderIdFromRoute);
        this.order = order
      })
      .catch(error => {
        console.error(error);
      });
    this.scrollToTop();
  },
  methods: {
    scrollToTop() {
      if (process.client) {
        window.scrollTo(0, 0);
      }
    }
  },
  computed: {
    orderID() {
      return this.$route.params.id;
    }
  },
}
</script>
