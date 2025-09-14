import { writable } from "svelte/store";

export let emptyEntry = {
    word: "",
    pos: "",
    description: "",
    translation: "",
    // add tags, examples, synonyms, antonyms etc...
}

export let selectedEntry = writable(emptyEntry)
