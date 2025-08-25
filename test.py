import typing
from enum import StrEnum
from typing import TypedDict

from server.src.verbum.api.utils.errors import PayloadError, ParameterError

x = 2
response = dict()

try:
    if x == 0:
        raise PayloadError("HELLO")
    if x > 0:
        raise ParameterError("HELLO 2")
    
    assert x == -2
except PayloadError or ParameterError as e:
    response["error"] = str(e)
except Exception as e:
    response["error"] = str(e)
finally:
    print("END")

print(response)