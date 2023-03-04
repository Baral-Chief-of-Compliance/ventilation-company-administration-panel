<template>
    <yandex-map
        :coords="[68.970360, 33.074172]"
        zoom="11"
    >
        <ymap-marker
            :coords = "[odr_latitude, odr_longitude]"
            :icon = "{color: 'red'}"
        >
        </ymap-marker>

        <ymap-marker
            :coords = "[st_latitude, st_longitude]"
            :icon = "{color: 'blue'}"
        >
        </ymap-marker>
        
        <ymap-route></ymap-route>

    </yandex-map>
</template>

<script>
export default {
    props: ['odr_latitude', 'odr_longitude', 'st_latitude', 'st_longitude']
}
</script>

<style>
.ymap-container {
    width: 1600px;
    height: 800px;
}
</style>