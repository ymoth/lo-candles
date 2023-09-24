export { default as About } from '../../components/About.vue'
export { default as Accordion } from '../../components/Accordion.vue'
export { default as AdvantagesCandles } from '../../components/AdvantagesCandles.vue'
export { default as CustomFooter } from '../../components/CustomFooter.vue'
export { default as CustomHeader } from '../../components/CustomHeader.vue'
export { default as EmailConfirmation } from '../../components/EmailConfirmation.vue'
export { default as Login } from '../../components/Login.vue'
export { default as MakingOrder } from '../../components/MakingOrder.vue'
export { default as MakingOrderCart } from '../../components/MakingOrderCart.vue'
export { default as MakingOrderCompletion } from '../../components/MakingOrderCompletion.vue'
export { default as MakingOrderConfirm } from '../../components/MakingOrderConfirm.vue'
export { default as MakingOrderDelivery } from '../../components/MakingOrderDelivery.vue'
export { default as Notifications } from '../../components/Notifications.vue'
export { default as Products } from '../../components/Products.vue'
export { default as Register } from '../../components/Register.vue'
export { default as Spinner } from '../../components/Spinner.vue'
export { default as TopProducts } from '../../components/TopProducts.vue'
export { default as UserData } from '../../components/UserData.vue'
export { default as MyHistoryOrder } from '../../components/myHistoryOrder.vue'
export { default as MyOrder } from '../../components/myOrder.vue'
export { default as PageTransition } from '../../components/pageTransition.vue'
export { default as Watcher } from '../../components/watcher/watcher.vue'

// nuxt/nuxt.js#8607
function wrapFunctional(options) {
  if (!options || !options.functional) {
    return options
  }

  const propKeys = Array.isArray(options.props) ? options.props : Object.keys(options.props || {})

  return {
    render(h) {
      const attrs = {}
      const props = {}

      for (const key in this.$attrs) {
        if (propKeys.includes(key)) {
          props[key] = this.$attrs[key]
        } else {
          attrs[key] = this.$attrs[key]
        }
      }

      return h(options, {
        on: this.$listeners,
        attrs,
        props,
        scopedSlots: this.$scopedSlots,
      }, this.$slots.default)
    }
  }
}
