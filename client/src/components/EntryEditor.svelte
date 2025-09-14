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
        <button class="remove-button" onclick={() => selectedEntry.set(emptyEntry)}>
            <span>X</span>
        </button>
        <div class="entry-info-header-container">
            <span>
                {$selectedEntry.word.length > 32
                    ? `${$selectedEntry.word.slice(0, 32)}...`
                    : $selectedEntry.word}
            </span>
            <div class="entry-info-subheader-container">
                <span><i>{ $selectedEntry.pos }</i></span>
            </div>
        </div>
        <hr>
        <div class="entry-info-body-container">
            <div class="entry-info-body-description">
                <span style="font-size: small; padding-bottom: 5px;"><i>Description</i></span>
                <span style="">{ $selectedEntry.description }</span>
                <br><br>
                <span style="font-size: small; padding-bottom: 5px;"><i>Synonyms</i></span>
                <span>
                    {#each tempSynonyms as synonym}
                        <span class="entry-info-synonym-item">{ synonym }</span>
                    {/each}
                </span>
                <br><br>
                <span style="font-size: small; padding-bottom: 5px;"><i>Examples</i></span>
                {#each tempExamples as example}
                    <span style="padding-bottom: 5px;">• { example }</span>
                {/each}
                <br><br>
                <span style="font-size: small; padding-bottom: 5px;"><i>Translation</i></span>
                <span style="font-size: small;">{ $selectedEntry.translation }</span>
            </div>
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
        width: 400px;
        height: 500px;
        background-color: black;
        position: relative;

        display: flex;
        flex-direction: column;
        justify-content: baseline;

        border-bottom-left-radius: 8px;
        border-bottom-right-radius: 8px;
        border-top-width: 6px;
        border-style: solid;
        border-color: white;
    }
    .remove-button {
        position: absolute;
        top: 1px;
        right: 1px;

        height: 15px;
        width: 15px;
        padding: 0%;
        font-size: 10px;
        font-weight: 500;

        color: white;
        background-color: inherit;
        border-color: white;
        transition: background-color 0.15s;
        transition: border-color 0.35s;
    }
    .remove-button:hover {
        background-color: brown;
    }
    .entry-info-header-container {
        height: 50px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: baseline;
        padding-left: 10px;
        padding-top: 15px;

        /* outline-style: solid;
        outline-color: white; */

        font-size: large;
    }
    .entry-info-subheader-container {
        padding-top: 15px;
        font-size: x-small;
        font-weight: lighter;
    }
    .entry-info-body-description {
        min-height: 50px;
        display: flex;
        flex-direction: column;
        align-items: baseline;
        justify-content: center;
        padding-left: 10px;
        padding-top: 15px;

        /* outline-style: solid;
        outline-color: white; */
        flex-wrap: wrap;
    }
    .entry-info-body-description span {
        text-align: left;
        white-space: normal;
        word-break: break-word;
        font-size: x-small;
    }
    .entry-info-synonym-item {
        border-style: solid;
        border-color: white;
        padding: 2px 7px 2px 7px;
        margin-right: 5px;
        border-width: 1px;
        border-radius: 6px;
    }
    hr {
        width: 95%;
        border: none;
        border-top: 1px solid white;
        margin: 0px auto;
    }


</style>