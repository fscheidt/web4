<script>
import { onMount } from 'svelte';
import MovieItem from "$lib/MovieItem.svelte";
let results = $state(null);
let debug = $state(false);

async function getMovies() {
    const endpoint = `http://localhost:8000/find`;
    const response = await fetch(endpoint);
    const data = response.json();
    if (response.ok) {
        return data;
    } else {throw new Error(data); }
  }

// condição de disparo da consulta 
// (quando o componente termina de ser carregado)
onMount(() => {
    getMovies().then((data)=>{
        results = data["movies"]; 
    });
});
</script>

<main>

    <h1>Filmes favoritos</h1>
    
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