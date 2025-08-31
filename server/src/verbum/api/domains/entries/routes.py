from flask import Blueprint, request, jsonify

from verbum.api.utils.validate import PayloadValidator
from verbum.api.utils.connect import connect_db
from verbum.api.utils.models import StatusCode
from verbum.api.utils.errors import *

from verbum.api.domains.entries.service import EntriesService
from verbum.api.domains.entries.schema import EntryFactory, EntryEnum


blueprint = Blueprint("entries", __name__, url_prefix="/api/entries")


@blueprint.get("/select-one/<string:word>")
def select_entry(word: str):
    response = dict()

    try:
        with connect_db() as conn:
            entry = EntriesService.select_one(conn, word)

        response["data"] = entry
        response["message"] = "Record was successfully retrieved."
        return jsonify(response), StatusCode.OK
    
    except PayloadError or ParameterError as e:
        response["error"] = str(e)
        return jsonify(response), StatusCode.BAD_REQUEST
    except SelectError as e:
        response["error"] = str(e)
        return jsonify(response), StatusCode.NOT_FOUND  # Is NOT FOUND 404 reserved for api, or can it be for db resources as well? 
    except Exception as e:
        print(f"[log] : {e}")
        response["error"] = "UnexpectedError: Something unexpected happened."
        return jsonify(response), StatusCode.INTERNAL_SERVER_ERROR


@blueprint.delete("/delete-one/<string:word>")
def delete_entry(word: str):
    response = dict()

    try:
        with connect_db() as conn:
            EntriesService.delete_one(conn, word)

        response["message"] = "Record was successfully deleted."
        return jsonify(response), StatusCode.OK
    
    except PayloadError or ParameterError as e:
        response["error"] = str(e)
        return jsonify(response), StatusCode.BAD_REQUEST
    except DeleteError as e:
        response["error"] = str(e)
        return jsonify(response), StatusCode.NOT_FOUND
    except Exception as e:
        print(f"[log] : {e}")
        response["error"] = "UnexpectedError: Something unexpected happened."
        return jsonify(response), StatusCode.INTERNAL_SERVER_ERROR


@blueprint.post("/insert-one")
def insert_entry():
    data = request.get_json(silent=True)
    response = dict()

    try:
        PayloadValidator.is_dict(data)
        PayloadValidator.contains_field(data, EntryEnum.WORD)
        entry = EntryFactory.from_dict(data)

        with connect_db() as conn:
            EntriesService.insert_one(conn, entry)

        response["message"] = "Record was successfully created."
        return jsonify(response), StatusCode.CREATED
    
    except PayloadError or ParameterError as e:
        response["error"] = str(e)
        return jsonify(response), StatusCode.BAD_REQUEST
    except InsertError as e:
        response["error"] = str(e)
        return jsonify(response), StatusCode.CONFLICT
    except Exception as e:
        print(f"[log] : {e}")
        response["error"] = "UnexpectedError: Something unexpected happened."
        return jsonify(response), StatusCode.INTERNAL_SERVER_ERROR


@blueprint.put("/update-one")
def update_entry():
    data = request.get_json(silent=True)
    response = dict()

    try:
        PayloadValidator.is_dict(data)
        PayloadValidator.contains_field(data, EntryEnum.WORD)
        entry = EntryFactory.from_dict(data)

        with connect_db() as conn:
            EntriesService.update_one(conn, entry)
        
        response["message"] = "Record was successfully updated."
        return jsonify(response), StatusCode.OK
    
    except PayloadError or ParameterError as e:
        response["error"] = str(e)
        return jsonify(response), StatusCode.BAD_REQUEST
    except UpdateError as e:
        response["error"] = str(e)
        return jsonify(response), StatusCode.NOT_FOUND
    except Exception as e:
        print(f"[log] : {e}")
        response["error"] = "UnexpectedError: Something unexpected happened."
        return jsonify(response), StatusCode.INTERNAL_SERVER_ERROR

# NOTE FIXME v!
# @blueprint.get("/select-all")
# def select_entries():
#     with connect_db() as conn:
#         rows = EntriesService.select_all(conn)
#     response = { "data": rows }
#     return jsonify(response), StatusCode.OK

# @blueprint.get("/select-randn/<int:n>")
# def select_entries_randn(n: int):
#     validator_pipeline = []
#     for val_f in validator_pipeline:
#         response = val_f(n)
#         if "error" in response:
#             return jsonify(response), StatusCode.BAD_REQUEST

#     try:
#         with connect_db() as conn:
#             rows = EntriesService.select_randn(conn, n)
#     except Exception as e:
#         print(f"[log] : {e}")
#         response["error"] = "ServiceError: Failed to select randn records."
#         return jsonify(response), StatusCode.INTERNAL_SERVER_ERROR

#     response = { "data": rows }
#     return jsonify(response), StatusCode.OK

