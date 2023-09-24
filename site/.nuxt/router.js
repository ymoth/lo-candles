import Vue from 'vue'
import Router from 'vue-router'
import { normalizeURL, decode } from 'ufo'
import { interopDefault } from './utils'
import scrollBehavior from './router.scrollBehavior.js'

const _fbdbe9ea = () => interopDefault(import('../pages/about.vue' /* webpackChunkName: "pages/about" */))
const _09bfe017 = () => interopDefault(import('../pages/catalog.vue' /* webpackChunkName: "pages/catalog" */))
const _8cbc570e = () => interopDefault(import('../pages/personalCabinet/index.vue' /* webpackChunkName: "pages/personalCabinet/index" */))
const _ab5aba82 = () => interopDefault(import('../pages/verificationEmail.vue' /* webpackChunkName: "pages/verificationEmail" */))
const _8513a26c = () => interopDefault(import('../pages/personalCabinet/makingOrder.vue' /* webpackChunkName: "pages/personalCabinet/makingOrder" */))
const _bc6c3460 = () => interopDefault(import('../pages/index.vue' /* webpackChunkName: "pages/index" */))
const _57776c5e = () => interopDefault(import('../pages/personalCabinet/orderDetail/_id.vue' /* webpackChunkName: "pages/personalCabinet/orderDetail/_id" */))

const emptyFn = () => {}

Vue.use(Router)

export const routerOptions = {
  mode: 'history',
  base: '/',
  linkActiveClass: 'nuxt-link-active',
  linkExactActiveClass: 'nuxt-link-exact-active',
  scrollBehavior,

  routes: [{
    path: "/about",
    component: _fbdbe9ea,
    name: "about"
  }, {
    path: "/catalog",
    component: _09bfe017,
    name: "catalog"
  }, {
    path: "/personalCabinet",
    component: _8cbc570e,
    name: "personalCabinet"
  }, {
    path: "/verificationEmail",
    component: _ab5aba82,
    name: "verificationEmail"
  }, {
    path: "/personalCabinet/makingOrder",
    component: _8513a26c,
    name: "personalCabinet-makingOrder"
  }, {
    path: "/",
    component: _bc6c3460,
    name: "index"
  }, {
    path: "/personalCabinet/orderDetail/:id?",
    component: _57776c5e,
    name: "personalCabinet-orderDetail-id"
  }],

  fallback: false
}

export function createRouter (ssrContext, config) {
  const base = (config._app && config._app.basePath) || routerOptions.base
  const router = new Router({ ...routerOptions, base  })

  // TODO: remove in Nuxt 3
  const originalPush = router.push
  router.push = function push (location, onComplete = emptyFn, onAbort) {
    return originalPush.call(this, location, onComplete, onAbort)
  }

  const resolve = router.resolve.bind(router)
  router.resolve = (to, current, append) => {
    if (typeof to === 'string') {
      to = normalizeURL(to)
    }
    return resolve(to, current, append)
  }

  return router
}
