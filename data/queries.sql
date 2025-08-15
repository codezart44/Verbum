CREATE TABLE IF NOT EXISTS en_entries (
    [entry_id] TEXT PRIMARY KEY,
    [word] TEXT NOT NULL,
    [pos] TEXT,
    [description] TEXT,
    [translation] TEXT
);

CREATE TABLE IF NOT EXISTS en_tags (
    [tag_id] PRIMARY KEY,
    [entry_id] TEXT,
    [word] TEXT,
    [tag] TEXT,
    FOREIGN KEY (entry_id) REFERENCES en_entries(entry_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS en_examples (
    [example_id] PRIMARY KEY,
    [entry_id] TEXT,
    [example] TEXT,
    FOREIGN KEY (entry_id) REFERENCES en_entries(entry_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS en_synonyms (
    [synonym_id] PRIMARY KEY,
    [entry_id] TEXT,
    [synonym] TEXT,
    FOREIGN KEY (entry_id) REFERENCES en_entries(entry_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS en_antonyms (
    [antonym_id] PRIMARY KEY,
    [entry_id] TEXT,
    [antonym] TEXT,
    FOREIGN KEY (entry_id) REFERENCES en_entries(entry_id) ON DELETE CASCADE
);


-- DROP TABLE en_entries;
-- DROP TABLE en_tags;
-- DROP TABLE en_examples;
-- DROP TABLE en_synonyms;
-- DROP TABLE en_antonyms;

