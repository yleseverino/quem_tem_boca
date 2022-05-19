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
