from dataclasses import dataclass
from typing import TypedDict
from enum import StrEnum

from ...utils.models import POS
from ....config import CONFIG

class _EntryTyping(TypedDict):
    word: str
    pos: str
    description: str
    translation: str

class _EntryEnum(StrEnum):
    WORD = "word"
    POS = "pos"
    DESCRIPTION = "description"
    TRANSLATION = "translation"

class EntryFactory:
    def from_dict(data: dict) -> _EntryTyping:
        entry: _EntryTyping = {
            "word": data["word"],
            "pos": data.get("pos"),
            "description": data.get("description"),
            "translation": data.get("translation"),      
        }
        return entry
    
    def from_dict_strict(data: dict) -> _EntryTyping:
        entry: _EntryTyping = {
            "word": data["word"],
            "pos": data["pos"],
            "description": data["description"],
            "translation": data["translation"],
        }
        return entry
    

class EntryValidator:

    def is_dict(data) -> dict[str,str]:
        response = dict()
        if not isinstance(data, dict):
            response["error"] = "PayloadError: Payload is not JSON."
        return response
    
    def contains_word_field(data) -> dict[str,str]:
        response = dict()
        if _EntryEnum.WORD not in data.keys():
            response["error"] = "PayloadError: Missing required field [word]."
        return response
    
    def valid_pos_value(data) -> dict[str,str]:
        response = dict()
        if _EntryEnum.POS in data.keys() and data.get("pos") not in POS:
            response["error"] = f"PayloadError: Field [pos] contains invalid value '{data.get("pos")}'." 
        return response
    
    def contains_all_fields(data) -> dict[str,str]:
        response = dict()
        missing_fields = [e.value for e in _EntryEnum if e not in data.keys()]
        if missing_fields:
            response["error"] = f"PayloadError: Missing required fields {missing_fields}."
        return response
    