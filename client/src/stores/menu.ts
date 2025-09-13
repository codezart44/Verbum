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

export let hideDesc = writable(false);
export let hidePOS = writable(false);
