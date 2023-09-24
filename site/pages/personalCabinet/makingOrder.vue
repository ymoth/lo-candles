<template>
  <div>
    <makingOrder />
  </div>
</template>

<script>
import makingOrder from "~/components/makingOrder/MakingOrder";
export default {
  name: "MakingOrderPage",
  middleware: "personalCabinet",
  components: {
    makingOrder
  },
  methods: {
    scrollToTop() {
      if (process.client) {
        window.scrollTo(0, 0);
      }
    }
  },
  mounted() {
    this.scrollToTop();
  }
}
</script>

<style scoped>

</style>
