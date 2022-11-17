<script lang="ts">
	import Router from "svelte-spa-router";
	import Home from "./routes/Home.svelte";
	import NotFound from "./routes/NotFound.svelte";
	import Team from "./routes/Team.svelte";

	let routes = {
		"/": Home,
		"/team/:id": Team,

		"*": NotFound
	}

</script>

<style>	
</style>


<div id="wrapper">
	<Router {routes} />
</div>


