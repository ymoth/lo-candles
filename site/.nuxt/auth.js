import Middleware from './middleware'
import { Auth, authMiddleware, ExpiredAuthSessionError } from '~auth/runtime'

// Active schemes
import { RefreshScheme } from '~auth/runtime'

Middleware.auth = authMiddleware

export default function (ctx, inject) {
  // Options
  const options = {
  "resetOnError": false,
  "ignoreExceptions": false,
  "scopeKey": "scope",
  "rewriteRedirects": true,
  "fullPathRedirect": false,
  "watchLoggedIn": true,
  "redirect": {
    "login": "/login",
    "logout": "/",
    "home": "/",
    "callback": "/login"
  },
  "vuex": {
    "namespace": "auth"
  },
  "cookie": {
    "prefix": "auth.",
    "options": {
      "path": "/"
    }
  },
  "localStorage": {
    "prefix": "auth."
  },
  "defaultStrategy": "local"
}

  // Create a new Auth instance
  const $auth = new Auth(ctx, options)

  // Register strategies
  // local
  $auth.registerStrategy('local', new RefreshScheme($auth, {
  "localStorage": {
    "prefix": "auth."
  },
  "token": {
    "prefix": "access_token.",
    "property": "access_token",
    "maxAge": 84000,
    "type": "Bearer"
  },
  "refreshToken": {
    "prefix": "refresh_token.",
    "property": "refresh_token",
    "data": "refresh_token",
    "maxAge": 1296000
  },
  "user": {
    "property": "user",
    "autoFetch": true
  },
  "endpoints": {
    "registration": {
      "url": "/register",
      "method": "post"
    },
    "login": {
      "url": "/login",
      "method": "post"
    },
    "refresh": {
      "url": "/token/refresh",
      "method": "post"
    },
    "logout": {
      "url": "/",
      "method": "post"
    },
    "user": {
      "url": "/user",
      "method": "get"
    }
  },
  "name": "local"
}))

  // Inject it to nuxt context as $auth
  inject('auth', $auth)
  ctx.$auth = $auth

  // Initialize auth
  return $auth.init().catch(error => {
    if (process.client) {
      // Don't console log expired auth session errors. This error is common, and expected to happen.
      // The error happens whenever the user does an ssr request (reload/initial navigation) with an expired refresh
      // token. We don't want to log this as an error.
      if (error instanceof ExpiredAuthSessionError) {
        return
      }

      console.error('[ERROR] [AUTH]', error)
    }
  })
}
