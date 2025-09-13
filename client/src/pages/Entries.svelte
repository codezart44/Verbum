<script lang="ts">
    import EntriesList from "../components/EntriesList.svelte";

    const sampleEntries = [
        { word: "this is some really long word wow this word is sooooooooo loooooooong", pos: "hah", description: "oh you thought the word itself was long, just wait until you actaully see this description of the word... hahahah this is gonna be soooooo loooooong that if even breaks the ui and will overflow the container it is supposed to be contained within. What do you think about that for a description of a word. Ye, thought so.", translation: "bye"},
        { word: "run", pos: "verb", description: "walking but faster", translation: "springa"},
        { word: "car", pos: "noun", description: "metal box with four wheels", translation: "bil"},
        { word: "snow", pos: "noun", description: "fluffy ice", translation: "snö"},
        { word: "pen", pos: "noun", description: "thing to write with", translation: "penna"},
    ]

    let entries = $state(sampleEntries);
    let loading = $state(false);

    function editEntry(word: string) { // add entry type
        console.log(word);
        // entries = entries.map(($entry) => $entry.word === entry.word ? entry : $entry);
    }

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

<div>
    <div>
        <EntriesList
            entries={entries}
            editEntry={editEntry}
            deleteEntry={deleteEntry}
        ></EntriesList>
    </div>
    
</div>

<style>
</style>