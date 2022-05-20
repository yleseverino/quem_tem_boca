// 1. Define route components.
// These can be imported from other files



// 2. Define some routes
// Each route should map to a component.
// We'll talk about nested routes later.
const routes = [
    { path: '/', component: Home }, 
    { path: '/restaurante/:id', component: RestauranteDetails },
]

// 3. Create the router instance and pass the `routes` option
// You can pass in additional options here, but let's
// keep it simple for now.
const router = VueRouter.createRouter({
  // 4. Provide the history implementation to use. We are using the hash history for simplicity here.
  history: VueRouter.createWebHashHistory(),
  routes, // short for `routes: routes`
})

const app = Vue.createApp({

    data() {
        return {
            user: {},
            restaurantes: []
        }
    },
    methods: {
        checkUser(form_data){
            
            fetch('/api/login', {
                method: 'POST', // or 'PUT'
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(form_data),
                })
                .then(response => response.json())
                .then(data => {
                    if (data['authenticated'] == true){

                        window.localStorage.setItem('jwt_quem_tem_boca', data['JWT']);
                        
                    }
                console.log('Success:', data);
                
                
                })
                .catch((error) => {
                console.error('Error:', error);
                });

        },

        getRestaurantes(){

            fetch('/api').then(response => response.json()).then(data => {        

                this.restaurantes = data['restaurantes']
                
                })
                .catch((error) => {
                console.error('Error:', error);
                });

        },

        search(query_string){

            fetch(`/api/consulta/${query_string}`).then(response => response.json()).then(data => {        

                this.restaurantes = data['restaurantes']
                
                })
                .catch((error) => {
                console.error('Error:', error);
                });

        }
    },

    computed: {

    },

    beforeMount(){
        this.getRestaurantes()
    },
    
})

app.use(router)