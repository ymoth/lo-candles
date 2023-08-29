export default {
  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: 'site',
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
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
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
  ],

  // Axios module configuration: https://go.nuxtjs.dev/config-axios
  axios: {
    // Workaround to avoid enforcing hard-coded localhost:3000: https://github.com/nuxt-community/axios-module/issues/308
    baseURL: 'http://87.249.50.115:8000/api/v1',
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
          property: 'access_token',
          maxAge: 84000,
          type: 'Bearer'
        },
        refreshToken: {
          prefix: 'refresh_token.',
          property: 'refresh_token',
          data: 'refresh_token',
          maxAge: 60 * 60 * 24 * 15,
        },
        user: {
          property: 'user',
          autoFetch: true,
        },
        endpoints: {
          registration: { url: '/register', method: 'post'},
          login: { url: '/login', method: 'post' },
          refresh: {url: '/token/refresh', method: 'post' },
          logout: { url: '/', method: 'post' },
          user: { url: '/user', method: 'get' }
        },

      },
    }
  }
}
