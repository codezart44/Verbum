from typing import Collection

from verbum.api.utils.errors import PayloadError, ParameterError


class PayloadValidator:
    @staticmethod
    def is_dict(data):
        print(data, type(data))
        if not isinstance(data, dict):
            raise PayloadError("PayloadError: Payload is not JSON.")
    
    @staticmethod
    def contain_field(data: dict, field: str):
        if field not in data.keys():
            raise PayloadError(f"PayloadError: Missing required field [{field}].")
    
    @staticmethod
    def contains_fields(data: dict, fields: list[str]):
        missing_fields = [e.value for e in fields if e not in data.keys()]
        if missing_fields:
            raise PayloadError(f"PayloadError: Missing required fields {missing_fields}.")
    
class ParameterValidator:
    @staticmethod
    def _is_int(n):
        if not isinstance(n, int):
            raise ParameterError("ParameterError: Parameter is not int.")
    
    @staticmethod
    def _is_string(s):
        if not isinstance(s, str):
            raise ParameterError("ParameterError: Parameter is not string.")
    
    @staticmethod
    def _positive_int(n: int):
        match n:
            case 0: 
                raise ParameterError("ParameterError: Parameter n should be positive, not zero.")
            case x if x < 0: 
                raise ParameterError("ParameterError: Parameter n should be positive, not negative.")

    @staticmethod
    def _allowed_value(value: str, allowed: Collection[str]):
        if value not in allowed:
            raise ParameterError(f"ParameterError: Field contains invalid value '{value}'.")

    @staticmethod
    def _max_characters(s: str, nmax: int, field: str):
        assert nmax > 0
        if len(s) > nmax:
            raise ParameterError(f"ParameterError: Field [{field}] exceeded max characters allowed, {nmax}.")

    @staticmethod
    def _min_characters(s: str, nmin: int, field: str):
        assert nmin >= 0
        if len(s) < nmin:
            raise ParameterError(f"ParameterError: Field [{field}] did not meet min characters needed, {nmin}.")
