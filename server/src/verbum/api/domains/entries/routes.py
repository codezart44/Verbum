from flask import Blueprint, request, jsonify

from verbum.api.utils.validate import PayloadValidator
from verbum.api.utils.connect import connect_db
from verbum.api.utils.models import StatusCode
from verbum.api.utils.errors import *

from verbum.api.domains.entries.service import EntriesService
from verbum.api.domains.entries.schema import EntryFactory, EntryEnum


blueprint = Blueprint("entries", __name__, url_prefix="/api/entries")


@blueprint.post("/insert-one")
def insert_entry():
    data = request.get_json(silent=True)
    response = dict()

    try:
        PayloadValidator.is_dict(data)
        PayloadValidator.contain_field(data, EntryEnum.WORD)
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
        response["error"] = "ServiceError: Failed to create record."
        return jsonify(response), StatusCode.INTERNAL_SERVER_ERROR


@blueprint.post("/delete-one")
def delete_entry():
    do stuff here


@blueprint.post("/update-one")
def update_entry():
    data = request.get_json(silent=True)

    validator_pipeline = [
        PayloadValidator.is_dict,
        PayloadValidator.contain_field,
    ]
    for val_f in validator_pipeline:
        response = val_f(data)
        if "error" in response:
            return jsonify(response), StatusCode.BAD_REQUEST

    try:
        entry = EntryFactory.from_dict_strict(data)
        with connect_db() as conn:
            rowcount = EntriesService.update_one(conn, entry)
    except Exception as e:
        print(f"[log] : {e}")
        response["error"] = "ServiceError: Failed to update record."
        return jsonify(response), StatusCode.INTERNAL_SERVER_ERROR
    
    match rowcount:
        case 0:
            response["message"] = f"Record does not exist."
            response["rowcount"] = rowcount
            return jsonify(response), StatusCode.CONFLICT
        case 1:
            response["message"] = "Record was successfully updated."
            response["rowcount"] = rowcount
            return jsonify(response), StatusCode.OK
        case _:
            response["error"] = "ServiceError: Unexpected number of records were updated."
            return jsonify(response), StatusCode.INTERNAL_SERVER_ERROR


@blueprint.get("/select-one/<string:word>")     # FIXME Validation that input is string
def select_entry(word: str):
    with connect_db() as conn:
        row = EntriesService.select_one(conn, word)
    response = { "data": row }
    return jsonify(response), StatusCode.OK

@blueprint.get("/select-all")
def select_entries():
    with connect_db() as conn:
        rows = EntriesService.select_all(conn)
    response = { "data": rows }
    return jsonify(response), StatusCode.OK

@blueprint.get("/select-randn/<int:n>")
def select_entries_randn(n: int):
    validator_pipeline = []
    for val_f in validator_pipeline:
        response = val_f(n)
        if "error" in response:
            return jsonify(response), StatusCode.BAD_REQUEST

    try:
        with connect_db() as conn:
            rows = EntriesService.select_randn(conn, n)
    except Exception as e:
        print(f"[log] : {e}")
        response["error"] = "ServiceError: Failed to select randn records."
        return jsonify(response), StatusCode.INTERNAL_SERVER_ERROR

    response = { "data": rows }
    return jsonify(response), StatusCode.OK

