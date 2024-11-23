<script>
let { children } = $props();
</script>

<nav>
    <a href="/">home</a>
    <a href="/movies">filmes</a>
</nav>

{@render children()}

