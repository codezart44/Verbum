export type Entry = {
    word: string;
    pos?: string | undefined;
    description?: string | undefined;
    translation?: string | undefined;
    synonyms?: string[] | undefined,
    antonyms?: string[] | undefined,
    examples?: string[] | undefined,
    tags?: string[] | undefined,
};
