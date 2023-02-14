<template>
    Бригада {{ $route.params.id }}
    {{ inf  }}
</template>

<script>
import axios from 'axios';
export default{
    data(){
        return{
            inf: null
        }
    },
    mounted(){
        axios.get(`http://127.0.0.1:5000/admin_panel/api/v1.0/brigades/${this.$route.params.id}`)
        .then(response => (this.inf = response.data))
    }
}
</script>