<script lang="ts">
    import { fade } from "svelte/transition";
    import { flip } from "svelte/animate";

    import { selectedEntry } from "../stores/data";
    import { activeShowOption, activeFindInputs } from "../stores/menu";
    import type { Entry } from "../typing/data";

    const tempExamples = [
        "This is one example sentence that includes the word.",
        "Here we can express another sentence that includes the word. This is even a double sentence.",
        "This is the final sentence showcasing the word!",
    ]

    const tempSynonyms = [
        "these", "words", "are", "temporary", "placeholders"
    ]

    type InputProps = {
        entries: Entry[];
        deleteEntry: (word: string) => void
    };

    let { entries, deleteEntry }: InputProps = $props();

    let renderList: string[] = $state([]);
    let expandList: string[] = $state([]);
    let processingAnimation = $state(false);

    const renderDuration = 400;
    const expandDuration = 400;

    function handleExpandRender(word: string) {
        processingAnimation = true;
        if (expandList.includes(word)) {
            setTimeout(() => expandList = [], expandDuration);
        } else {
            expandList = [...expandList, word];
            setTimeout(() => expandList = [word], expandDuration);
        }
        if (renderList.includes(word)) {
            renderList = [];
        } else {
            renderList = [];
            setTimeout(() => renderList = [word], renderDuration);
        }
        setTimeout(() => processingAnimation = false, Math.max(renderDuration, expandDuration));
    }
</script>

<div class="entries-container">
    {#each entries as entry, index (entry.word)}
    <div 
        class="entry-row-container"
        class:expanded={expandList.includes(entry.word)}
        class:disabled={processingAnimation}
        animate:flip
    >   
        <!-- buttons -->
        <button 
        class="entry-item-button info-button"
        class:info-button-highlighted={expandList.includes(entry.word)}
        disabled={processingAnimation} 
        onclick={() => handleExpandRender(entry.word)}>
            <p style="margin: 0px;">{expandList.includes(entry.word) ? "-" : "+"}</p>
        </button>
        <button class="entry-item-button edit-button" onclick={() => selectedEntry.set(entry)}>
            <p style="margin: 0px;">E</p>
        </button>
        <button class="entry-item-button remove-button" onclick={() => deleteEntry(entry.word)}>
            <p style="margin: 0px;">X</p>
        </button>

        <!-- content -->
        <div class="entry-row-main-container">
            <span 
                class="entry-word" 
                class:highlighted={$activeFindInputs.word !== "" && !entry.word.toLowerCase().includes($activeFindInputs.word.toLowerCase())}>
                    { entry.word.length > 32 ? `${entry.word.slice(0, 32)}...` : entry.word }
            </span>
            <div class="entry-expanded-content" transition:fade={{ duration: renderDuration }}>
                {#if $activeShowOption.pos || renderList.includes(entry.word)}
                    <div class="entry-expanded-content-cell" style="padding-bottom: 10px;">
                        <div class="entry-subheader" transition:fade={{ duration: renderDuration }}>
                            <span class="entry-pos">{ entry.pos }</span>
                            <span class="entry-index">({ index })</span>
                        </div>
                        <hr transition:fade={{ duration: renderDuration }}>
                    </div>
                {/if}
                {#if $activeShowOption.description || renderList.includes(entry.word)}
                    <div class="entry-expanded-content-cell">
                        <span class="entry-expanded-content-title" transition:fade={{ duration: renderDuration }}>Description</span>
                        <p class="entry-description" transition:fade={{ duration: renderDuration }}>{ entry.description }</p>
                    </div>
                {/if}
                {#if $activeShowOption.synonyms || renderList.includes(entry.word)}
                    <div class="entry-expanded-content-cell">
                        <span class="entry-expanded-content-title" transition:fade={{ duration: renderDuration }}>Synonyms</span>
                        <span style="padding-top: 10px;" transition:fade={{ duration: renderDuration }}>
                            {#each tempSynonyms as synonym}
                                <span class="entry-info-synonym-item">{ synonym }</span>
                            {/each}
                        </span>
                    </div>
                {/if}
                {#if $activeShowOption.examples || renderList.includes(entry.word)}
                    <div class="entry-expanded-content-cell">
                        <span class="entry-expanded-content-title" transition:fade={{ duration: renderDuration }}>Examples</span>
                        <div class="entry-examples-container" transition:fade={{ duration: renderDuration }}>
                            {#each tempExamples as example}
                                <span style="padding-bottom: 5px;">• { example }</span>
                            {/each}
                        </div>
                    </div>
                {/if}
                {#if $activeShowOption.translation || renderList.includes(entry.word)}
                    <div class="entry-expanded-content-cell">
                        <span class="entry-expanded-content-title" transition:fade={{ duration: renderDuration }}>Translation</span>
                        <span style="font-size: small;" transition:fade={{ duration: renderDuration }}>{ entry.translation }</span>
                    </div>
                {/if}
            </div>
        </div>

    </div>
    {/each}
</div>

<style>
    /* entries container */
    .entries-container {
        width: 400px;
    }

    /* entry container */
    .entry-row-container {
        position: relative;
        min-height: 20px;
        width: 100%;
        display: flex;
        flex-wrap: nowrap;
        justify-content: left;
        margin-top: 5px;
        
        background-color: black;
        border-color: white;
        border-style: solid;
        border-top-width: 6px;
        border-bottom-left-radius: 6px;
        border-bottom-right-radius: 6px;
        /* transition: min-height 1.2s; */
        transition: min-height 0.4s;
    }
    .expanded {
        min-height: 500px;
    }
    /* .entry-row-container:hover {
        background-color: #212121;
    } */
    hr {
        width: 100%;
        border: none;
        border-top: 1px solid white;
        margin: 0px auto;
    }

    /* main container */
    .entry-row-main-container {
        display: flex;
        flex-direction: column;
        justify-content: baseline;
        align-items: baseline;
        width: 100%;
        /* padding-left: 10px;
        padding-right: 10px;
        padding-bottom: 10px;
        padding-top: 10px; */
        padding: 10px;
    }

    /* header */
    .entry-word {
        font-size: medium;
        font-weight: bold;
    }
    .highlighted {
        color: #242424;
    }
    .entry-row-container:hover .entry-word {
        text-decoration: underline;
    }
    .entry-subheader {
        margin-top: 4px;
        width: 100%;
        display: flex;
        flex-direction: row;
        align-items: baseline;
        justify-content: space-between;
    }
    .entry-pos {
        font-size: x-small;
        font-style: italic;
    }
    .entry-index {
        font-size: x-small;
    }
    
    
    /* body */
    .entry-description {
        font-size: x-small;
        text-align: left;
        margin: 0px;
        padding: 0px;
        padding-top: 6px;
    }
    .entry-expanded-content {
        width: 100%;
        display: flex;
        flex-direction: column;
        justify-content: baseline;
        align-items: baseline;
    }
    .entry-expanded-content-cell {
        padding-bottom: 20px;
        width: 100%;
        display: flex;
        flex-direction: column;
        justify-content: baseline;
        align-items: baseline;
    }
    .entry-expanded-content-title {
        font-size: small;
        font-style: italic;
    }
    .entry-info-synonym-item {
        font-size: x-small;
        border-style: solid;
        border-color: white;
        padding: 2px 7px 2px 7px;
        margin-right: 5px;
        border-width: 1px;
        border-radius: 6px;
    }
    .entry-examples-container {
        display: flex;
        flex-direction: column;
        text-align: left;
        font-size: x-small;
    }

    /* Buttons */
    .entry-item-button {
        position: absolute;
        height: 15px;
        width: 15px;
        padding: 0%;
        font-size: 10px;
        font-weight: 500;

        font-family: monospace;
        color: white;
        background-color: black;
        border-color: white;
        transition: 1s;
    }
    .remove-button {
        top: 1px;
        right: 1px;
    }
    .remove-button:hover {
        background-color: brown;
    }
    .edit-button {
        top: 1px;
        right: 17px;
    }
    .edit-button:hover {
        background-color: #cc9005;
    }
    .info-button {
        top: 1px;
        right: 33px;
    }
    /* .info-button:hover {
        background-color: rgb(42, 63, 166);
    } */
    .info-button:disabled {
        /* background-color: white; */
        cursor: not-allowed;
    }
    .info-button-highlighted {
        background-color: white;
        color: black;
    }
</style>

<!-- 
Part of Speech

1. Adjective    Ad
2. Noun         Nn
3. Verb         Vb
4. Adverb       Av
5. Injection    Ij
6. Preposition  Pe
7. Conjunction  Cn
8. Pronouns     Po
-->