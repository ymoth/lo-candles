<template>
  <div class="accordion accordion-flush">
    <div class="accordion-item">
      <h2
        class="accordion-header"
        v-for="(acc_header_item, index) in acc_header"
        :key="acc_header_item.id"
      >
        <button
          class="accordion-button collapsed"
          type="button"
          @click="openAcc(index)"
        >
          {{acc_header_item.text}}
        </button>
      </h2>
      <div
        class="accordion-collapse collapse"
        v-for="acc_body_item in acc_body"
        :key="acc_body_item.id"
      >
        <button
          class="accordion-body"
          v-for="(acc_body_item_btn, index) in acc_body_item.btn"
          :key="acc_body_item_btn.id"
          :class="{ show: activeIndex === index }"
        >
          {{acc_body_item_btn.text}}
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Accordion",
  props: {
    acc_header: {
      type: Array,
      default: () => [],
    },
    acc_body: {
      type: Array,
      default: () => []
    },
  },
  data() {
    return {
      activeIndex: null
    }
  },
  methods: {
    openAcc(index) {
      if(this.activeIndex === index) {
        this.activeIndex = null
      } else {
        this.activeIndex = index
      }
    }
  }
}
</script>

<style scoped>

</style>
