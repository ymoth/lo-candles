<template>
  <div>
    <customHeader />
    <main>
      <PageTransition>
        <Nuxt />
      </PageTransition>
    </main>
    <customFooter />
  </div>
</template>

<script>
import customHeader from "~/components/CustomHeader";
import customFooter from "~/components/CustomFooter";
import pageTransition from "~/components/pageTransition"
export default {
  name: "default",
  components: {customHeader, customFooter, pageTransition},
  mounted() {
    this.$nextTick(() => {
      window.scrollTo(0, 0);
    });
  }
}
</script>
