<script>
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

// condição de disparo da consulta (button onclick)
function handleClick() {
   getMovies().then((data)=>{
       // gatilho para o mecanismo de reatividade
       results = data["results"]; 
   });
}
</script>
<h1>top 20 popular movies</h1>
<button onclick={handleClick}>list</button>

{#if results}
    <input type="checkbox" bind:checked={debug}>
    {#if debug}
        <pre>
            {@html JSON.stringify(results[0], null, 2)}
        </pre>
    {/if}
     <div class="results">
         {#each results as movie }
            <p><img src="https://image.tmdb.org/t/p/w185/{movie.poster_path}" alt="{movie.title}"></p>
            <div>
                <h2>{ movie.title }</h2>
                <p>{ movie.release_date}</p>
            </div>
         {/each}
    </div>
{/if}

<style>
pre{
    white-space: pre-line;
}
.results{
    display:grid;
    gap: 10px;
    grid-template-columns: max-content max-content;
}
</style>