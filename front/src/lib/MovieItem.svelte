<script>
import { onMount } from "svelte";
// variavel passada como parametro
let {movie} = $props();
let savedMovie = $state(null);

async function remove() {
    // TODO ...
}
async function save() {
    const endpoint = `http://localhost:8000/save`;
    const settings = {
        method: 'POST',
        headers: {
            Accept: 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(movie)
    };
    const res = await fetch(endpoint, settings);
    const data = res.json();
    if (res.ok) {
        savedMovie = data;
        return data;
    } else {throw new Error(data); }
  }
</script>

<main>
    {#if movie?.poster_path }
        <p><img src="https://image.tmdb.org/t/p/w185/{movie.poster_path}" alt="{movie.title}"></p>
    {/if}
    <div>
        {#if !movie?.is_fav }
            <button onclick={save}>save</button>
        {/if}
        {#if movie.is_fav }
            <button onclick={remove}>remove</button>
        {/if}
        {#if savedMovie }
            <span>Movie saved</span>
        {/if}
        <h2>{ movie?.title }</h2>
        <p>{ movie.release_date}</p>
        <p>{ movie._id}</p>
    </div>
</main>

<style>
main{
    border: 1px solid #ccc;
    width: 250px;
}
span{
    color: blue;
}
</style>
