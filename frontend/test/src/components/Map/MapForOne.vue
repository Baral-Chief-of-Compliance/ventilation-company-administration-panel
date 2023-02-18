<template>
    <yandex-map
        :coords="[latitude, longitude]"
        zoom="18"
    >
        <ymap-marker
            :coords = "[latitude, longitude]"
            :icon = "{color: 'red'}"
        >
        </ymap-marker>

    </yandex-map>
</template>

<script>
export default {
    props: ['latitude', 'longitude']
}
</script>

<style>
.ymap-container {
    width: 1600px;
    height: 400px;
}
</style>