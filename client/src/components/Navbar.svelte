<script lang="ts">
    import { 
        activeMenuOption, 
        activeSortOption, 
        sortOrderReversed, 
        activeFilterInputs,
        activeFindInputs,
        activeShowOption,
    } from "../stores/menu";
    import { menuOption, sortOption } from "../typing/menu";
    import { entries } from "../stores/data";

    function handleMenuOptionChoice(option: number): void {
        activeMenuOption.set((option === $activeMenuOption) ? menuOption.NONE : option);
    }
    function handleSortOptionChoice(option: number): void {
        activeSortOption.set((option === $activeSortOption) ? sortOption.NONE : option);
    }

    let addWord = $state("");
    let disableAdd = $derived.by(() => {
        return addWord === "" 
            || addWord === undefined 
            || $entries.map((entry => entry.word)).includes(addWord);
    });

    function handleAddNewWord() {
        // CONTINUE HERE!! ASASDASDAS
        // ALSO MAKE THE "SHOW" MENU ALL INACTIVE, DISPLAY AMONG COLLAPSED CARDS WHEN TOGGLED ON
        //     USER CAN STYLE HIS CARDS HIMSELF
        //     MAKES MORE SENSE THAN CURRENT VERSION WHERE YOU CAN TOGGLE AWAY FROM EXPANDE CARD...
        //     WOULD REQUIRE THE CARD INFO ITEMS TO BE CONDITIONALLY RENDERED WITH AN OR CONDITION
        //         EITHER CARD IS EXPANDED OR TURNED ON IN SHOW MENU
        console.log(addWord);
        addWord = "";
    }
</script>

<div class="navbar-base-container">
    <!-- MENU -->
    <button 
        class="navbar-menu-item"
        class:navbar-menu-item-selected={$activeMenuOption===menuOption.SORT}
        onclick={() => handleMenuOptionChoice(menuOption.SORT)}>
            <span>SORT</span>
    </button>
    <button 
        class="navbar-menu-item"
        class:navbar-menu-item-selected={$activeMenuOption===menuOption.FILTER}
        onclick={() => handleMenuOptionChoice(menuOption.FILTER)}>
            <span>FILT</span>
    </button>
    <button
        class="navbar-menu-item"
        class:navbar-menu-item-selected={$activeMenuOption===menuOption.FIND}
        onclick={() => handleMenuOptionChoice(menuOption.FIND)}>
            <!-- Only highligh words, dont filter them away -->
            <span>FIND</span>
    </button>
    <button
        class="navbar-menu-item"
        class:navbar-menu-item-selected={$activeMenuOption===menuOption.SHOW}
        onclick={() => handleMenuOptionChoice(menuOption.SHOW)}>
            <span>SHOW</span>
    </button>
    <button
        class="navbar-menu-item"
        class:navbar-menu-item-selected={$activeMenuOption===menuOption.ADD}
        onclick={() => handleMenuOptionChoice(menuOption.ADD)}>
            <span>+ADD</span>
    </button>

    <!-- SORT -->
    <div 
    class="navbar-menu-settings"
    class:navbar-settings-lowered={$activeMenuOption === menuOption.SORT}>
        <button 
            class="navbar-menu-sort-item"
            class:navbar-menu-item-selected={$activeSortOption === sortOption.ALPH}
            onclick={() => handleSortOptionChoice(sortOption.ALPH)}>
                <span>ALPH</span>
        </button>
        <button 
            class="navbar-menu-sort-item"
            class:navbar-menu-item-selected={$activeSortOption === sortOption.WLEN}
            onclick={() => handleSortOptionChoice(sortOption.WLEN)}>
                <span>WLEN</span>
        </button>
        <button 
            class="navbar-menu-sort-item"
            class:navbar-menu-item-selected={$activeSortOption === sortOption.RAND}
            onclick={() => handleSortOptionChoice(sortOption.RAND)}>
                <span>RAND</span>
        </button>
        <button 
            class="navbar-menu-sort-item"
            class:navbar-menu-item-toggled={$sortOrderReversed === true}
            onclick={() => sortOrderReversed.set(!$sortOrderReversed)}>
                <span>R</span>
        </button>
    </div>

    <!-- FILTER -->
    <div 
    class="navbar-menu-settings"
    class:navbar-settings-lowered={$activeMenuOption === menuOption.FILTER}>
        <!-- NOTE Add incl. or excl. toggle for each filter - matching strings -->
        <input 
            type="text"
            bind:value={$activeFilterInputs.word}
            placeholder="WORD"
            class="navbar-menu-filter-item"
            class:navbar-menu-filter-item-filled={$activeFilterInputs.word !== ""}
        />
        <input 
            type="text"
            bind:value={$activeFilterInputs.pos}
            placeholder="POS"
            class="navbar-menu-filter-item"
            style="width: 24px;"
            class:navbar-menu-filter-item-filled={$activeFilterInputs.pos !== ""}
        />
        <input 
            type="text"
            bind:value={$activeFilterInputs.description}
            placeholder="DESC"
            class="navbar-menu-filter-item"
            class:navbar-menu-filter-item-filled={$activeFilterInputs.description !== ""}
        />
        <input  
            type="text"
            bind:value={$activeFilterInputs.translation}
            placeholder="TRNS"
            class="navbar-menu-filter-item"
            class:navbar-menu-filter-item-filled={$activeFilterInputs.translation !== ""}
        />
    </div>

    <!-- FIND -->
    <div 
    class="navbar-menu-settings"
    class:navbar-settings-lowered={$activeMenuOption === menuOption.FIND}>
        <input 
            type="text"
            bind:value={$activeFindInputs.word}
            placeholder="WORD"
            class="navbar-menu-filter-item"
            class:navbar-menu-filter-item-filled={$activeFindInputs.word !== ""}
        />
    </div>

    <!-- SHOW -->
    <div 
    class="navbar-menu-settings"
    class:navbar-settings-lowered={$activeMenuOption === menuOption.SHOW}>
        <button 
            class="navbar-menu-show-item"
            class:navbar-menu-item-selected={$activeShowOption.pos === true}
            onclick={() => activeShowOption.update(prev => ({ ...prev, pos: !prev.pos }))}>
                <span>POS</span>
        </button>
        <button 
            class="navbar-menu-show-item"
            class:navbar-menu-item-selected={$activeShowOption.description === true}
            onclick={() => activeShowOption.update(prev => ({ ...prev, description: !prev.description }))}>
                <span>DESC</span>
        </button>
        <button
            class="navbar-menu-show-item"
            class:navbar-menu-item-selected={$activeShowOption.synonyms === true}
            onclick={() => activeShowOption.update(prev => ({ ...prev, synonyms: !prev.synonyms }))}>
                <span>SYNS</span>
        </button>
        <button
            class="navbar-menu-show-item"
            class:navbar-menu-item-selected={$activeShowOption.examples === true}
            onclick={() => activeShowOption.update(prev => ({ ...prev, examples: !prev.examples }))}>
                <span>EXS</span>
        </button>
        <button
            class="navbar-menu-show-item"
            class:navbar-menu-item-selected={$activeShowOption.translation === true}
            onclick={() => activeShowOption.update(prev => ({ ...prev, translation: !prev.translation }))}>
                <span>TRNS</span>
        </button>
    </div>

    <!-- +ADD -->
    <div 
    class="navbar-menu-settings"
    class:navbar-settings-lowered={$activeMenuOption === menuOption.ADD}>
        <input 
            type="text"
            bind:value={addWord}
            placeholder="WORD"
            class="navbar-menu-filter-item"
            class:navbar-menu-filter-item-filled={addWord !== ""}
        />
        <button
            class="navbar-menu-add-button"
            onclick={() => handleAddNewWord()}
            disabled={disableAdd}>
            <!-- CLEAR THE INPUT FIELD UPON PRESSIGN + BUTTON -->
            <!-- DISABLE BUTTON UNLESS VALID WORD INPUT -->
                <span>+</span>
        </button>
    </div>

</div>

<style>
    .navbar-base-container {
        height: 100px;
        width: 403px;
        position: fixed;
        top: 0;
        z-index: 8;

        /* position: relative; */
        display: flex;
        flex-direction: column;
        align-items: baseline;
        justify-content: center;

        font-weight: bold;
        color: #343434;
        background-color: black;

        border-bottom-style: solid;
        border-color: white;
        border-width: 2px;
    }
    
    .navbar-menu-item {
        width: 100%;
        display: flex;
        align-items: baseline;
        padding: 0%;
        border: none;
        
        color: inherit;
        background-color: inherit;
        font-family: inherit;
        font-weight: bold;
        cursor: pointer;
    }
    .navbar-menu-item span {
        margin-bottom: auto;
        transform: translateX(0px);
        transition: 1.2s;
    }
    .navbar-menu-item:hover span {
        /* color: white; */
        text-decoration: underline;
        transform: translateX(10px);
    }
    .navbar-menu-item-selected span {
        color: white;
        text-decoration: underline;
    }
    .navbar-menu-item-toggled span {
        text-decoration: underline;
        color: white;
        outline-color: white;
        outline-style: solid;
    }


    .navbar-menu-settings {
        height: 100px;
        width: 85%;
        position: absolute;
        top: 0px;
        right: 0px;
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
        transform: translateY(-108px);

        border-color: white;
        border-style: solid;
        transition: 1.2s;

        background-color: black;
    }
    .navbar-settings-lowered {
        transform: translateY(-3px);
    }

    .navbar-menu-sort-item {
        margin-left: 3px;
        margin-right: 3px;
        color: #343434;
        border: none;
        font-family: monospace;
        background-color: inherit;
    }
    .navbar-menu-sort-item:hover {
        text-decoration: underline;
    }

    .navbar-menu-filter-item {
        margin-left: 3px;
        margin-right: 3px;
        padding-left: 6px;
        padding-right: 6px;
        color: #343434;
        border: solid;
        border-radius: 0px;
        font-family: monospace;
        background-color: inherit;
        width: 32px;
    }
    .navbar-menu-filter-item:hover {
        text-decoration: underline;
    }
    .navbar-menu-filter-item:focus {
        outline-style: solid;
        outline-color: white;
    }
    .navbar-menu-filter-item-filled {
        color: white;
        outline-color: white;
        box-shadow: none;
    }

    .navbar-menu-show-item {
        margin-left: 3px;
        margin-right: 3px;
        color: #343434;
        border: none;
        font-family: monospace;
        background-color: inherit;
    }
    .navbar-menu-show-item:hover {
        text-decoration: underline;
    }
    .navbar-menu-add-button {
        margin-left: 3px;
        margin-right: 3px;
        color: white;
        border: solid;
        font-family: monospace;
        background-color: green;
        border-color: white;
        transition: 1.2s;
    }
    /* .navbar-menu-add-button:hover {
        background-color: ;
    } */
    .navbar-menu-add-button:disabled {
        background-color: black;
        border-color: #343434;
        color: #343434;
        cursor: not-allowed;
    }
    
</style>
