<script>
let { children } = $props();
</script>

<nav>
    <a href="/">home</a>
    <a href="/movies">filmes</a>
    <a href="/favoritos">favoritos</a>
</nav>

{@render children()}

