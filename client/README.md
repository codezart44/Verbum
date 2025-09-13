# Svelte + Vite

## Svelte Runes vs. Store
* `$state` → I own this value here.
* `$derived` → This value comes from others.
* `$effect` → Do something when things change.
* Stores → Share values between components.

TL;DR Mental Map
Runes:
$state → local state
$derived → computed
$effect → side effects
Svelte syntax:
bind: → binding values or refs
{#if}, {#each}, {#await} → template control flow
<slot> / export let / on:event → component communication
transition: → animations with zero setup

<script>
  let count = $state(0);
</script>

<button on:click={() => count++}>Clicked {count} times</button>

<script>
  let a = $state(2);
  let b = $state(3);
  const sum = $derived(a + b);
</script>

<p>{a} + {b} = {sum}</p>



<script>
  let name = $state('Oskar');
  $effect(() => {
    console.log('Name changed:', name);
    localStorage.setItem('name', name);
  });
</script>

<input bind:value={name} />

## Bindings

<script> let text = $state(''); </script>
<input bind:value={text} placeholder="Type here" />
<p>You typed: {text}</p>

<script> let inputEl; </script>
<input bind:this={inputEl}>
<button on:click={() => inputEl.focus()}>Focus</button>


## Control Flow
<script> let loggedIn = $state(false); </script>
{#if loggedIn}
  <p>Welcome back!</p>
{:else}
  <p>Please log in</p>
{/if}

<script>
  let items = $state(['milk','bread','eggs']);
</script>
<ul>
  {#each items as item}
    <li>{item}</li>
  {/each}
</ul>

<script>
  let data = $state(fetch('/api/data').then(r => r.json()));
</script>
{#await data}
  <p>Loading…</p>
{:then value}
  <p>Got {value.message}</p>
{:catch err}
  <p>Error: {err.message}</p>
{/await}


## Components
### Props
<!-- Button.svelte -->
<script> export let label = "Click"; </script>
<button>{label}</button>
svelte
Copy code
<!-- App.svelte -->
<script> import Button from './Button.svelte'; </script>
<Button label="Save" />

### Events

<!-- Child.svelte -->
<script>
  import { createEventDispatcher } from 'svelte';
  const dispatch = createEventDispatcher();
</script>
<button on:click={() => dispatch('close')}>Close</button>
svelte
Copy code
<!-- Parent.svelte -->
<Child on:close={() => console.log("Closed!")} />

### Slots

<!-- Card.svelte -->
<div class="card">
  <slot name="header" />
  <slot />  <!-- default slot -->
</div>
svelte
Copy code
<!-- App.svelte -->
<Card>
  <h2 slot="header">Title</h2>
  <p>Some content</p>
</Card>
