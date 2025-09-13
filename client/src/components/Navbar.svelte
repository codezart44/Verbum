<script lang="ts">
    import { 
        activeMenuOption, 
        activeSortOption, 
        sortOrderReversed, 
        activeFilterInputs,
        hideDesc,
        hidePOS,
    } from "../stores/menu";
    import { menuOption, sortOption } from "../typing/menu";

    function handleMenuOptionChoice(option: number): void {
        activeMenuOption.set((option === $activeMenuOption) ? menuOption.NONE : option);
    }
    function handleSortOptionChoice(option: number): void {
        activeSortOption.set((option === $activeSortOption) ? sortOption.NONE : option);
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
        class:navbar-menu-item-selected={$activeMenuOption===menuOption.HIDE}
        onclick={() => handleMenuOptionChoice(menuOption.HIDE)}>
            <span>HIDE</span>
    </button>
    <!-- <button class="navbar-menu-item">
        <span>ADD</span>
    </button> -->

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

    <!-- HIDE -->
    <div 
    class="navbar-menu-settings"
    class:navbar-settings-lowered={$activeMenuOption === menuOption.HIDE}>
        <button 
            class="navbar-menu-hide-item"
            class:navbar-menu-item-selected={$hidePOS === true}
            onclick={() => hidePOS.set(!$hidePOS)}>
                <span>POS</span>
        </button>
        <button 
            class="navbar-menu-hide-item"
            class:navbar-menu-item-selected={$hideDesc === true}
            onclick={() => hideDesc.set(!$hideDesc)}>
                <span>DESC</span>
        </button>
    </div>

</div>

<style>
    .navbar-base-container {
        display: flex;
        flex-direction: column;
        align-items: baseline;
        justify-content: center;
        position: relative;
        height: 100px;

        font-weight: bold;
        color: #343434;

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
        transform: translateY(-103px);

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

    .navbar-menu-hide-item {
        margin-left: 3px;
        margin-right: 3px;
        color: #343434;
        border: none;
        font-family: monospace;
        background-color: inherit;
    }
    .navbar-menu-hide-item:hover {
        text-decoration: underline;
    }
    
</style>
