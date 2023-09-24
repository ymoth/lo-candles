<template>
  <div>
    <main>
      <products />
    </main>
  </div>
</template>

<script>
import products from "~/components/Products";
export default {
  name: "catalog",
  components: {
    products
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
