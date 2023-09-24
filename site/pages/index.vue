<template>
  <div>
    <main>
      <AdvantagesCandles />
      <TopProducts />
    </main>
  </div>
</template>

<script>
import AdvantagesCandles from "~/components/AdvantagesCandles";
import TopProducts from "~/components/TopProducts";
export default {
  components: {
   AdvantagesCandles, TopProducts,
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
