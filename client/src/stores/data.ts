import { writable } from "svelte/store";
import type { Entry } from "../typing/data";

const sampleEntries: Entry[] = [
    // { word: "", pos: "", description: "", translation: ""}, // +ADD to add new empty element to list, then edit and add a word to it?
    { word: "Pneumonoultramicroscopicsilicovolcanoconosis", pos: "hah", description: "oh you thought the word itself was long, just wait until you actaully see this description of the word... hahahah this is gonna be soooooo loooooong that if even breaks the ui and will overflow the container it is supposed to be contained within. What do you think about that for a description of a word. Ye, thought so.", translation: "bye"},
    { word: "run", pos: "verb", description: "walking but faster", translation: "springa"},
    { word: "car", pos: "noun", description: "metal box with four wheels", translation: "bil"},
    { word: "snow", pos: "noun", description: "fluffy ice", translation: "snö"},
    { word: "pen", pos: "noun", description: "thing to write with", translation: "penna"},
]

export let entries = writable(sampleEntries);

export let emptyEntry: Entry = {
    word: "",
    pos: "",
    description: "",
    translation: "",
    synonyms: [],
    antonyms: [],
    examples: [],
    tags: [],
}
export let selectedEntry = writable({ ...emptyEntry });
