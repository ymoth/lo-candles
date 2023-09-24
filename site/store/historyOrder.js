export const state = () => ({
  historyOrder: null
})

export const actions = {
  getHistoryOrderFromApi({commit}) {
    this.$axios.get('https://dev.aromatic.kz/api/v1/orders/getList')
      .then(res => commit('HISTORY_ORDER', res.data))
      .catch(e => console.log(e))
  }
}

export const mutations = {
  HISTORY_ORDER(state, payload) {
    state.historyOrder = payload
  }
}

export const getters = {
  history: state => state.historyOrder
}
