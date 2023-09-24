export const state = () => ({
  cartData: [],
  loadingCart: false
})

export const actions = {
  cartFromApi({ commit, state }) {
    if (!state.loadingCart) {
      this.$axios.get('https://dev.aromatic.kz/api/v1/user')
        .then(res => {
          commit('UPDATE_CART', res.data.user.cart_data);
          commit('SET_CART_DATA_LOADED', true);
        })
    }
  },
  countingQuantityAndCalculatingPrice({commit}, {index, action}) {
    commit('COUNTING_QUANTITY_AND_CALCULATING_PRICE', {index, action})
  },
}

export const mutations = {
  UPDATE_CART(state, payload) { // получение корзины с api
    for (let key in payload) {
      state.cartData.push(payload[key])
    }
    state.cartData = state.cartData.filter((product, index, self) =>
      index === self.findIndex((p) => p.id === product.id)
    );
  },
  SET_CART_DATA_LOADED(state, payload) { // флаг для api
    state.loadingCart = payload
  },
  SET_PRODUCTS_TO_CART(state, payload) { // получение товаров для корзины
    payload.count = 1 // добавление количества товаров
    payload.finalPrice = payload.price // добавление конечной цены
    payload.inCart = true
    state.cartData.push(payload)
  },
  SAVE_CART_USER(state, payload) { // сохранение корзины пользователя
    const dataToSend = {}

    payload.forEach(item => {
      const {id, count, finalPrice, inCart, photo, price, title, category} = item
      dataToSend[id] = { id, count, finalPrice, inCart, photo, price, title, category }
    })

    this.$axios.post('https://dev.aromatic.kz/api/v1/cart-system/edit/', dataToSend)
  },
  COUNTING_QUANTITY_AND_CALCULATING_PRICE(state, {index, action}) { // калькулятор количества товара и подсчет цены
    const initialPrice = state.cartData[index].price

    if(action === 'plus' && state.cartData[index].count < 100) {
      state.cartData[index].count++;
      state.cartData[index].finalPrice += initialPrice

    } else if(action === 'minus' && state.cartData[index].count > 1) {
      state.cartData[index].count--;
      state.cartData[index].finalPrice -= initialPrice
    }

    this._vm.$set(state.cartData, index, state.cartData[index])
  },
  DELETE_PRODUCT(state, item) { // удаление товара
    const index = state.cartData.findIndex(product => product.id === item.id);

    if (index !== -1) {
      state.cartData[index].inCart = false
      state.cartData.splice(index, 1)
    }
  },
}

export const getters = {
  cart: state => state.cartData
}
