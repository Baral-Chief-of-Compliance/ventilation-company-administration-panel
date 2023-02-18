<template>
    <div class="map">
            <!-- <yandex-map  :coords='[68.970360, 33.074172]' :zoom="11" >
                <ymap-marker v-for="event in events" :key="event.id"
                    :marker-id="event.id" 
                    :coords="[event.latitude, event.longitude]" 
                    marker-type="placemark"
                    :balloon="{header: event.name}"
                    :icon="{ color: 'red' }"                    
                    ></ymap-marker>
            </yandex-map> -->
            <yandex-map
                :coords="center_coords"
                :zoom="zoom"
                :cluster-options="clusterOptions"
            >   
            
                <ymap-marker v-for="event in events" :key="event.id" 
                :marker-id="event.id"
                :coords="[event.latitude, event.longitude]"
                :balloon="{header: event.name }"
                cluster-name="1"

                :icon = "{ color: 'red'}"
                
                />

                <!-- <ymap-marker
                marker-id="1"
                :coords="coords"
                :balloon="{header: 'First'}"
                cluster-name="1"
                />
                <ymap-marker
                marker-id="2"
                :coords="coords"
                :balloon="{header: 'Second'}"
                cluster-name="1"
                />
                <ymap-marker
                marker-id="3"
                :coords="[54, 40]"
                :balloon="{header: 'Second'}"
                cluster-name="1"
                /> -->
            </yandex-map>
        </div>
        <!-- <div v-for="event in events" :key="event.id">
            {{ event.name }}
        </div> -->
</template>

<script>

export default {
    props: ['events'],
    data: () => ({
        center_coords: [68.970360, 33.074172],
        zoom: 11,
        clusterOptions: {
        1: {
            clusterDisableClickZoom: true,
            clusterOpenBalloonOnClick: true,
            preset: 'islands#redClusterIcons',
            clusterBalloonLayout: [
            '<ul class=list>',
            '{% for geoObject in properties.geoObjects %}',
            '<li><a href=# class="list_item">{{ geoObject.properties.balloonContentHeader|raw }}</a></li>',
            '{% endfor %}',
            '</ul>',
            ].join(''),
        },
        },
  }),
};
</script>

<style scoped>
.ymap-container {
    width: 858px;
    height: 600px;
}
</style>