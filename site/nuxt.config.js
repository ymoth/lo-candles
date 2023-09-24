export default {
  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: 'AromaticCandles',
    htmlAttrs: {
      lang: 'ru',
      'data-bs-theme': "light"
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
      { name: 'format-detection', content: 'telephone=no' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: './favicon.ico' },
      { rel: "preconnect", href: "https://fonts.googleapis.com"},
      { rel: "preconnect", href: "https://fonts.gstatic.com"},
      { rel: "stylesheet", href: "https://fonts.googleapis.com/css2?family=El+Messiri:wght@400;500;600;700&display=swap"},
    ]
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [
    '@/assets/css/null.css',
    '@/node_modules/bootstrap/dist/css/bootstrap.min.css'
  ],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [
    { src: '~/plugins/formatNumber.js', mode: 'client' },
    { src: '~/plugins/vMask.js', mode: 'client' },
  ],

  // Auto import components: https://go.nuxtjs.de v/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/axios
    '@nuxtjs/axios',
    '@nuxtjs/auth-next',
    'cookie-universal-nuxt',
    'vue-yandex-maps/nuxt',
  ],

  // Axios module configuration: https://go.nuxtjs.dev/config-axios
  axios: {
    // Workaround to avoid enforcing hard-coded localhost:3000: https://github.com/nuxt-community/axios-module/issues/308
    baseURL: 'https://dev.aromatic.kz/api/v1',
  },

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {
    loaders: {
      sass: {
        implementation: require('sass'),
      },
      scss: {
        implementation: require('sass'),
      },
    },
  },
  auth: {
    strategies: {
      local: {
        scheme: 'refresh',
        localStorage: {
          prefix: 'auth.'
        },
        token: {
          prefix: 'access_token.',
          property: 'access',
          maxAge: 600,
          type: 'Bearer'
        },
        refreshToken: {
          prefix: 'refresh_token',
          property: 'refresh_token',
          data: 'refresh',
          maxAge: 3600 * 24 * 3,
        },
        user: {
          property: 'user',
          autoFetch: true,
        },
        endpoints: {
          registration: { url: '/register', method: 'post'},
          login: { url: '/login', method: 'post' },
          refresh: { url: '/token/refresh/', method: 'post' },
          logout: { url: '/logout', method: 'post' },
          user: { url: '/user', method: 'get' },
        },
      },
    }
  },

  loading: '~/components/Spinner.vue',

  yandexMaps: {
    apiKey: 'd788c73c-29d9-479c-89da-856189171458',
    lang: 'ru_RU',
  },

  router: {
    middleware: 'emailConfirm',
  },
}
