<script>
import { onMount } from "svelte";
import MovieItem from "$lib/MovieItem.svelte";
let results = $state(null);
let debug = $state(false);
async function getMovies() {
       let endpoint = `http://localhost:8000/movies/top`;
       const res = await fetch(endpoint);
       const data = await res.json();
       if (res.ok) {
           return data;
       } else {throw new Error(data); }
}
onMount(() => {
   getMovies().then((data)=>{
       results = data["results"]; 
   });
});
</script>

<main>
    <h1>top 20 popular movies</h1>
    
    {#if results}
        <input type="checkbox" bind:checked={debug}>
        {#if debug}
            <pre>{JSON.stringify(results[0], null, 2)}</pre>
        {/if}
        <div class="results">
            {#each results as movie }
                <MovieItem {movie}/>
            {/each}
        </div>
    {/if}
</main>
    
<style>
main{
    padding: 10px;
}
pre{
    white-space: pre-wrap;
}
.results{
    display: flex;
    gap: 10px;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: flex-start;
}
</style>