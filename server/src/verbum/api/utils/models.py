from enum import StrEnum, IntEnum
from typing import TypedDict

class POS(StrEnum):
    NOUN = "noun"
    PRONOUN = "pronoun"
    VERB = "verb"
    ADJECTIVE = "adjective"
    ADVERB = "adverb"
    PREPOSITION = "preposition"
    CONJUNCTION = "conjunction"
    DETERMINER = "determiner"
    INTERJECTION = "interjection"


class StatusCode(IntEnum):
    # 1XX - Information

    # 2XX - Successful
    OK = 200
    CREATED = 201

    # 3XX - Redirection

    # 4XX - Client Error
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    CONFLICT = 409

    # 5XX - Server Error
    INTERNAL_SERVER_ERROR = 500
    NOT_IMPLEMENTED = 501
    SERVICE_UNAVAILABLE = 503
    

# class LexicalAggregate:
#     def __init__(
#             self,
#             word: str,
#             description: str = None,
#             translation: str = None,
#             tags: set[str] = None,
#             examples: set[str] = None,
#             synonymns: set[str] = None,
#             antonymns: set[str] = None,
#             ):
#         self.word = word
#         self.description = description
#         self.tags = tags
#         self.translation = translation
#         self.examples = examples
#         self.synonymns = synonymns
#         self.antonymns = antonymns
    
#         self.__id = word

#     def __str__(self) -> str:
#         return f"{self.word} \n" + \
#             (f" : (desc) {self.description} \n" if self.description else "") + \
#             (f" : (tags) {sorted(self.tags)} \n" if self.tags else "")
    
#     @property
#     def id(self) -> str:
#         return self.__id

# def main():
#     test = LexicalAggregate(
#         "test", 
#         description="this is just a test", 
#         tags={"t", "e", "s", "t", "a"}
#         )
#     print(test)

# if __name__=="__main__":
#     main()
