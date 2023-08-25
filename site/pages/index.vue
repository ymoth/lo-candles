<template>
  <div>
    <CustomHeader/>
    <main>
      <AdvantagesCandles />
    </main>
  </div>
</template>

<script>
import CustomHeader from "@/components/CustomHeader.vue";
import AdvantagesCandles from "~/components/AdvantagesCandles";
export default {
  components: {
    CustomHeader,AdvantagesCandles
  }
}
</script>
