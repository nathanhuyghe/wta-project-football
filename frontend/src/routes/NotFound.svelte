<script lang="ts">
    import {push, pop, replace } from "svelte-spa-router";

    const go_home = () => {
        push("/");
    }

    const go_back = () => {
        pop();
    }

</script>


<style lang="scss">
    $color-white: #eef5f7;
    $color-lightblue: #2E9CCA;
    $color-darkblue: #00385b;
    $color-background-opacity: rgba(20, 71, 104, 0.8);

    .container {
        color: $color-white;
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;

        .title {
            background: $color-background-opacity;
            margin: 2em;
            padding: 2em;
            border: $color-background-opacity solid 1px;
            border-radius: 1em;

            h1 {
                font-size: 7em;
            }

            h2 {
                font-size: 5em;
                margin: 0;
            }

            p {
                font-size: 2em;
            }

            button {
                cursor: pointer;
                color: $color-white;
                background: $color-darkblue;
                border: $color-darkblue solid 1px;
                border-radius: 0.5em;
                padding: 1em;
            }

            button:hover {
                background: $color-lightblue;
            }
        }

    }

</style>

<section class="container">
    <div class="title">
        <h1>404</h1>
        <h2>Page not found!</h2>
        <p>The requested page is not valid.</p>
        <button on:click={(go_home)}>Go back to home</button>
    </div>
</section>