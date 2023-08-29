<template>
  <section class="cabinet">
    <div class="container">
      <div class="row">
        <div class="col-lg-2">
          <Accordion :acc_header="acc_header"/>
        </div>
        <div class="col-lg-3">
        </div>
        <div class="col-lg-7"></div>
      </div>
    </div>
  </section>
</template>

<script>
import Accordion from "~/components/Accordion";
export default {
  name: "PersonalCabinet",
  components: {
    Accordion
  },
  data() {
    return {
      acc_header: [
        {
          id: 1,
          text: "Личные данные"
        }
      ],
      acc_body: [
        {
          id: 1,
          btn: [
            {
              id: 1,
              text: "Данные текущей сессии"
            },
            {
              id: 2,
              text: 'Мои заказы'
            }
          ]
        }
      ]
    }
  },
}
</script>

<style scoped>

</style>
