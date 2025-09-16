<script lang="ts">
    import EntriesList from "../components/EntriesList.svelte";
    import EntryEditor from "../components/EntryEditor.svelte";
    import { entries } from "../stores/data";
    
    import { selectedEntry } from "../stores/data";
    import { 
        activeFilterInputs, 
        activeSortOption, 
        sortOrderReversed,
    } from "../stores/menu";
    import { sortOption } from "../typing/menu";

    let loading = $state(false);
    let displayEntries = $derived.by(() => {
        let _entries = [...$entries];

        // filter
        _entries = $activeFilterInputs.word !== ""
            ? _entries.filter((e) => e.word.toLowerCase().includes($activeFilterInputs.word.toLowerCase()))
            : _entries;
        _entries = $activeFilterInputs.pos !== ""
            ? _entries.filter((e) => e.pos?.toLowerCase().includes($activeFilterInputs.pos.toLowerCase()))
            : _entries;
        _entries = $activeFilterInputs.description !== ""
            ? _entries.filter((e) => e.description?.toLowerCase().includes($activeFilterInputs.description.toLowerCase()))
            : _entries;
        _entries = $activeFilterInputs.translation !== ""
            ? _entries.filter((e) => e.translation?.toLowerCase().includes($activeFilterInputs.translation.toLowerCase()))
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
        entries.set($entries.filter((entry) => entry.word !== word));
    }

    async function fetchEntries() {
        loading = true;
        try {
            // blocked by CORS policy - see how to allow CORS
            const response = await fetch("http://127.0.0.1:5000/api/entries/select-all");
            if (!response.ok) throw new Error(`HTTP ${response.status}`);
            entries.set(await response.json());
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
        <EntryEditor/>
    {/if}
    <EntriesList
        entries={displayEntries}
        deleteEntry={deleteEntry}
    />
</div>

<style>
    .page-layout {
        margin-top: 100px;
    }
</style>