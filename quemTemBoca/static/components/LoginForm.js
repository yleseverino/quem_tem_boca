app.component('login-form',{
    template:
    /*html*/
    `<form action="" @submit.prevent="onSubmit">
    <input type="text" name="email" v-model="email">
    <input type="password" name="password" v-model="password">
    <input type="submit" name="submit">
  </form>`,

  data(){
    return {
        email:'',
        password:''
    }
  },

  methods:{
      onSubmit() {
          this.$emit( 'review-login', { 'email': this.email, 'password': this.password} )
      }
  }
})