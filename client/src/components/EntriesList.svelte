<script lang="ts">
        import { 
        sortOrderReversed,
        activeFilterInputs,
        hideDesc,
        hidePOS,
        activeSortOption,
    } from "../stores/menu";
    import { sortOption } from "../typing/menu";

    type Entry = {
        word: string;
        pos: string;
        description: string;
        translation: string;
    }
    type InputProps = {
        entries: Entry[];
        editEntry: (word: string) => void;
        deleteEntry: (word: string) => void
    };

    let { entries, editEntry, deleteEntry }: InputProps = $props();

    let displayEntries = $derived.by(() => {
        let _entries = [...entries];

        // filter
        _entries = $activeFilterInputs.word !== ""
            ? _entries.filter((e) => e.word.includes($activeFilterInputs.word))
            : _entries;
        _entries = $activeFilterInputs.pos !== ""
            ? _entries.filter((e) => e.pos.includes($activeFilterInputs.pos))
            : _entries;
        _entries = $activeFilterInputs.description !== ""
            ? _entries.filter((e) => e.description.includes($activeFilterInputs.description))
            : _entries;
        _entries = $activeFilterInputs.translation !== ""
            ? _entries.filter((e) => e.translation.includes($activeFilterInputs.translation))
            : _entries;

        // sort
        if ($activeSortOption === sortOption.ALPH) {
            _entries = _entries.sort((a, b) => a.word.localeCompare(b.word));
        } else if ($activeSortOption === sortOption.WLEN) {
            _entries = _entries.sort((a, b) => a.word.length - b.word.length);
        } else if ($activeSortOption === sortOption.RAND) {
            _entries = _entries.sort((a, b) => Math.random() - 0.5);
        }
        _entries = $sortOrderReversed ? _entries.reverse() : _entries;
        return _entries
    });
    
</script>

<div class="entries-container">
    {#each displayEntries as entry, index}
    <div class="entry-row-container">
        <div class="entry-row-main-container">
            <div class="entry-row-header-container">
                <div class="entry-index">
                    <p>{ index }</p>
                </div>
                <div class="entry-header">
                    <p>
                        { entry.word.length > 32 ? `${entry.word.slice(0, 32)}...` : entry.word } 
                        {!$hidePOS ? `(${entry.pos})` : ""}
                    </p>
                </div>
            </div>
            {#if !$hideDesc}
                <div class="entry-row-body-container">
                    <p>• { entry.description ? entry.description : "enter some explanation of the word here..." }</p>
                </div>
            {/if}
        </div>
        <div class="entry-row-side-container">
            <button class="remove-button" onclick={() => deleteEntry(entry.word)}>
                <p style="margin: 0px;">X</p>
            </button>
            <button class="edit-button" onclick={() => editEntry(entry.word)}>
                <p style="margin: 0px;">E</p>
            </button>
        </div>
    </div>
    {/each}
</div>

<style>
    /* base container */
    .entries-container {
        width: 400px;
    }

    /* base row container */
    .entry-row-container {
        position: relative;
        min-height: 20px;
        width: 100%;
        display: flex;
        flex-wrap: nowrap;
        justify-content: left;
        margin-top: 5px;
        margin-bottom: 5px;
        
        border-color: white;
        border-style: solid;
        border-top-width: 6px;
        border-bottom-left-radius: 6px;
        border-bottom-right-radius: 6px;
    }

    .entry-row-container:hover {
        background-color: #343434;
    }
    .entry-row-container:hover .entry-header {
        text-decoration: underline;
    }

    /* main container */
    .entry-row-main-container {
        width: 380px;
    }

    /* header */
    .entry-row-header-container {
        display: flex;
        flex-direction: row;
        justify-content: left;
        align-items: center;
        height: 20px;
        width: 380px;
    }

    .entry-header {
        font-size: small;
    }

    .entry-index {
        width: 15px;
        font-size: x-small;
    }

    /* body */
    .entry-row-body-container {
        display: flex;
        text-align: left;
        justify-content: flex-start;
        align-items: flex-start;
        min-height: 35px;
        padding-left: 20px;

        font-size: x-small;
    }

    /* side menu */
    .entry-row-side-container {
        position: relative;
        width: 20px;
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

    .edit-button {
        position: absolute;
        top: 1px;
        right: 17px;

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

    .edit-button:hover {
        background-color: #cc9005;
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