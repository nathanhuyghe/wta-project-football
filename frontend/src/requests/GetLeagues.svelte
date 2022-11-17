<script lang="ts">
    import { onMount } from "svelte"
    import { leagues_store } from "../store.js"

    onMount(async () => {

        fetch("https://wta-project-football.azurewebsites.net/api/leagues/?format=json")
        .then(response => response.json()) 
        .then(data => {
            leagues_store.set(data);
        }).catch(error => {
            console.log(error);
            return [];
        });

    });
</script>