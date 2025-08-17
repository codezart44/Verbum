from flask import Blueprint, request, jsonify

from .service import EntriesService
from .schema import EntryFactory, EntryValidator
from ...utils.connect import connect_db
from ...utils.models import StatusCode

blueprint = Blueprint("entries", __name__, url_prefix="/api/entries")


@blueprint.post("/insert-one")
def insert_entry():
    data = request.get_json(silent=True)

    validator_pipeline = [
        EntryValidator.is_dict,
        EntryValidator.contains_word_field,
        EntryValidator.valid_pos_value,
    ]
    for val_f in validator_pipeline:
        response = val_f(data)
        if "error" in response:
            return jsonify(response), StatusCode.BAD_REQUEST

    try:
        entry = EntryFactory.from_dict(data)
        with connect_db() as conn:
            rowcount = EntriesService.insert_one(conn, entry)
    except Exception as e:
        print(f"[log] : {e}")
        response["error"] = "ServiceError: Failed to create record."
        return jsonify(response), StatusCode.INTERNAL_SERVER_ERROR

    match rowcount:
        case 0:
            response["message"] = "Record already exists."
            response["rowcount"] = rowcount
            return jsonify(response), StatusCode.CONFLICT
        case 1:
            response["message"] = "Record was successfully created."
            response["rowcount"] = rowcount
            return jsonify(response), StatusCode.CREATED
        case _:
            response["error"] = "ServiceError: Unexpected number of records were created."
            return jsonify(response), StatusCode.INTERNAL_SERVER_ERROR


@blueprint.post("/update-one")
def update_entry():
    data = request.get_json(silent=True)

    validator_pipeline = [
        EntryValidator.is_dict,
        EntryValidator.contains_all_fields,
        EntryValidator.valid_pos_value,
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

@blueprint.get("/select-randn/<int:n>")         # FIXME Validation that input is int
def select_entries_randn(n: int):
    with connect_db() as conn:
        rows = EntriesService.select_randn(conn, n)
    response = { "data": rows }
    return jsonify(response), StatusCode.OK

