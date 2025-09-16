<script lang="ts">
    import { selectedEntry, emptyEntry } from "../stores/data";

    const tempExamples = [
        "This is one example sentence that includes the word.",
        "Here we can express another sentence that includes the word. This is even a double sentence.",
        "This is the final sentence showcasing the word!",
    ]

    const tempSynonyms = [
        "these", "words", "are", "temporary", "placeholders"
    ]
</script>

<div class="entry-info-background-shader">
    

    <div class="entry-info-container">
        <button class="action-button remove-button" onclick={() => selectedEntry.set({ ...emptyEntry })}>
            <span>X</span>
        </button>
        <!-- FIXME -->
        <button class="action-button save-button" onclick={() => console.log("fart...")}>
            <span>S</span>
        </button>
        
        <div class="entry-edit-card-item">
            <span>
                {$selectedEntry.word.length > 32
                    ? `${$selectedEntry.word.slice(0, 32)}...`
                    : $selectedEntry.word}
            </span>
        </div>

        <div class="entry-edit-card-item">
            <!-- Might want to build a reusable dropdown component for this -->
            <input type="text" class="entry-editor-input" bind:value={$selectedEntry.pos} placeholder="pos">
            <hr>
        </div>

        <div class="entry-edit-card-item">
            <span>Description</span>
            <input type="text" class="entry-editor-input" bind:value={$selectedEntry.description} placeholder="description">
        </div>

        <div class="entry-edit-card-item">
            <span>Synonyms <button>+</button></span>
            <!-- MAX 5 SYNONYMS, deactivate add button if 5 synonyms -->
            <span>
                {#each tempSynonyms as synonym}
                <!-- <span class="entry-info-synonym-item">{ synonym }</span> -->
                    <input type="text" class="entry-editor-input" bind:value={synonym} placeholder="synonym">
                {/each}
            </span>
        </div>
        
        <div class="entry-edit-card-item">
            <span>Examples <button>+</button></span>
            {#each tempExamples as example}
                <!-- <span style="padding-bottom: 5px;">• { example }</span> -->
                <input type="text" class="entry-editor-input" bind:value={example} placeholder="example">
            {/each}
        </div>

        <div class="entry-edit-card-item">
            <span>Translation</span>
            <input type="text" class="entry-editor-input" bind:value={$selectedEntry.translation} placeholder="translation">
        </div>
        
    </div>
</div>

<style>
    .entry-info-background-shader {
        position: fixed;
        top: 0px;
        width: 403px;
        height: 100%;
        z-index: 10;
        background-color: rgba(0, 0, 0, 0.6);
    }
    .entry-info-container {
        position: absolute;
        top: 108px;
        height: 500px;
        background-color: black;
        position: relative;
        padding: 10px;

        display: flex;
        flex-direction: column;
        justify-content: baseline;
        align-items: baseline;

        border-bottom-left-radius: 8px;
        border-bottom-right-radius: 8px;
        border-top-width: 6px;
        border-style: solid;
        border-color: white;
    }
    .action-button {
        position: absolute;

        height: 15px;
        width: 15px;
        padding: 0%;
        font-size: x-small;
        font-weight: lighter;

        color: white;
        background-color: inherit;
        border-color: white;
        transition: 0.15s;
    }
    .remove-button {
        top: 1px;
        right: 1px;
    }
    .remove-button:hover {
        background-color: brown;
    }
    .save-button {
        top: 1px;
        right: 17px;
    }
    .save-button:hover {
        background-color: green;
    }
    .entry-edit-card-item {
        width: 100%;
        display: flex;
        flex-direction: column;
        justify-content: baseline;
        align-items: baseline;
        padding-bottom: 20px;
    }
    .entry-info-header-container {
        width: 100%;
        height: 50px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: baseline;
        font-size: large;
    }
    .entry-info-subheader-container {
        width: 100%;
        padding-top: 15px;
        font-size: x-small;
        font-weight: lighter;
    }
    hr {
        width: 100%;
        border: none;
        border-top: 1px solid white;
        margin: 0px auto;
    }

    .entry-editor-input {
        width: 100%;

        background-color: black;
        padding: 0px;
        margin: 0px;
        color: white;
        font-family: monospace;
        font-size: x-small;
        border-style: none;
        transition: 0.8s;
    }
    .entry-editor-input:hover {
        background-color: #cc9005;
    }
    .entry-editor-input:focus {
        background-color: #cc9005;
    }


</style>