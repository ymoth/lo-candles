const middleware = {}

middleware['emailConfirm'] = require('../middleware/emailConfirm.js')
middleware['emailConfirm'] = middleware['emailConfirm'].default || middleware['emailConfirm']

middleware['personalCabinet'] = require('../middleware/personalCabinet.js')
middleware['personalCabinet'] = middleware['personalCabinet'].default || middleware['personalCabinet']

export default middleware
