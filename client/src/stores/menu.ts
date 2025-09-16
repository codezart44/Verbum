import { writable } from "svelte/store";
import { menuOption, sortOption } from "../typing/menu";

export let activeMenuOption = writable(menuOption.NONE);

export let activeSortOption = writable(sortOption.NONE);
export let sortOrderReversed = writable(false);

export let activeFilterInputs = writable({
    word: "",
    pos: "",
    description: "",
    translation: "",
})

export let activeFindInputs = writable({
    word: "",
})

export let activeShowOption = writable({
    word: false,
    pos: false,
    description: false,
    synonyms: false,
    antonyms: false,
    examples: false,
    translation: false,
    tags: false,
});

// export let addWord = writable(undefined);
