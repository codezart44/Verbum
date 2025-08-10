class LexicalEntry:
    def __init__(
            self,
            word: str,
            description: str = None,
            translation: str = None,
            tags: set[str] = None,
            examples: set[str] = None,
            synonymns: set[str] = None,
            antonymns: set[str] = None,
            ):
        self.word = word
        self.description = description
        self.tags = tags
        self.translation = translation
        self.examples = examples
        self.synonymns = synonymns
        self.antonymns = antonymns
    
        self.__id = word

    def __str__(self) -> str:
        return f"{self.word} \n" + \
            (f" : (desc) {self.description} \n" if self.description else "") + \
            (f" : (tags) {sorted(self.tags)} \n" if self.tags else "")
    
    @property
    def id(self) -> str:
        return self.__id

def main():
    test = LexicalEntry(
        "test", 
        description="this is just a test", 
        tags={"t", "e", "s", "t", "a"}
        )
    print(test)

if __name__=="__main__":
    main()
