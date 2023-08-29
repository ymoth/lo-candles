<template>
  <div>
    <main>
      <AdvantagesCandles />
      <Products />
    </main>
  </div>
</template>

<script>
import AdvantagesCandles from "~/components/AdvantagesCandles";
import Products from "~/components/Products";
export default {
  components: {
   AdvantagesCandles, Products,
  }
}
</script>
