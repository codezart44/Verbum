<script lang="ts">
    import EntriesList from "../components/EntriesList.svelte";
    import EntryInfo from "../components/EntryEditor.svelte";
    import type { Entry } from "../typing/data";
    
    import { sortOption } from "../typing/menu";
    import { selectedEntry } from "../stores/data";
    import { 
        activeFilterInputs,
        activeHideOption,
        activeSortOption,
        sortOrderReversed,
    } from "../stores/menu";

    const sampleEntries: Entry[] = [
        { word: "Pneumonoultramicroscopicsilicovolcanoconosis", pos: "hah", description: "oh you thought the word itself was long, just wait until you actaully see this description of the word... hahahah this is gonna be soooooo loooooong that if even breaks the ui and will overflow the container it is supposed to be contained within. What do you think about that for a description of a word. Ye, thought so.", translation: "bye"},
        { word: "run", pos: "verb", description: "walking but faster", translation: "springa"},
        { word: "car", pos: "noun", description: "metal box with four wheels", translation: "bil"},
        { word: "snow", pos: "noun", description: "fluffy ice", translation: "snö"},
        { word: "pen", pos: "noun", description: "thing to write with", translation: "penna"},
    ]

    let entries = $state(sampleEntries);
    let loading = $state(false);

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

    function deleteEntry(word: string) {
        entries = entries.filter((entry) => entry.word !== word);
        console.log(entries);
    }

    async function fetchEntries() {
        loading = true;
        try {
            // blocked by CORS policy - see how to allow CORS
            const response = await fetch("http://127.0.0.1:5000/api/entries/select-all");
            if (!response.ok) throw new Error(`HTTP ${response.status}`);
            entries = await response.json();
            console.log(entries);
        } catch (e: any) {
            alert(`Error: ${e.message}`);
        } finally {
            loading = false;
        }
    }
</script>

<div class="page-layout">
    {#if $selectedEntry.word !== ""}
        <EntryInfo/>
    {/if}
    <EntriesList
        entries={displayEntries}
        hidePOS={$activeHideOption.pos}
        hideDesc={$activeHideOption.description}
        deleteEntry={deleteEntry}
    />
</div>

<style>
    .page-layout {
        margin-top: 100px;
    }
</style>