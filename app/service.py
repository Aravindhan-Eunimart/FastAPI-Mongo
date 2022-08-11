from pymongo.collection import Collection
from fastapi import Response


def get_single_record(id, db: Collection):
    result = db.find_one({"id": id})
    del result['_id']
    return result


def get_all_record(db: Collection):
    result = db.find({})
    modified_result = []
    for res in result:
        del res['_id']
        modified_result.append(res)
    return modified_result


def insert_single_record(student, db: Collection):
    db.insert_one(student.dict())
    return None


def insert_multiple_record(students, db: Collection):
    db.insert_many(students)
    return None


def delete_single_record(id: int, db: Collection):
    result = db.delete_one({"id": id})
    if result.deleted_count == 1:
        return Response(status_code=204)
    return Response(status_code=404)


def delete_all_record(db: Collection):
    db.delete_many({})
    return Response(status_code=204)

