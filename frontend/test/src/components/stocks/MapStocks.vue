<template>
    <div class="text-h3 py-6 mx-10 text-left">Карта складов</div>

    <div class="py-6 mx-10 d-flex justify-center">
        <Map :events="Stocks" />
    </div>
</template>

<script>
import axios from 'axios';
import Map from '@/components/Map/Map.vue'


    export default {
        data () {
            return {
                Stocks: null
            }
        },
        components: {
            Map
        },
        mounted(){
            this.get_data()
        },
        methods: {
            get_data(){
                axios.get('http://127.0.0.1:5000/admin_panel/api/v1.0/stocks')
                .then(response => (this.Stocks = response.data))
            }
        }
    }
</script>