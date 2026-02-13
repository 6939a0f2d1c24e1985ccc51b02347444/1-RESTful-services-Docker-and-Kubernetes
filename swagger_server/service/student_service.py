import os
import tempfile
from functools import reduce

from tinydb import Query, TinyDB

from swagger_server.models import Student

db_dir_path = tempfile.gettempdir()
db_file_path = os.path.join(db_dir_path, "students.json")
student_db = TinyDB(db_file_path)


def add(student: Student):
    if not student:
        return 'invalid input', 400

    doc_id = student_db.insert(student.to_dict())
    student.student_id = doc_id
    return student.student_id


def get_by_id(student_id: int):
    student = student_db.get(doc_id=int(student_id))
    if not student:
        return 'not found', 404
    student_dict = dict(student[0]) if isinstance(student, list) else dict(student)
    student_dict['student_id'] = student_id
    return student_dict


def delete(student_id: int):
    student = student_db.get(doc_id=int(student_id))
    if not student:
        return 'not found', 404
    student_db.remove(doc_ids=[int(student_id)])
    return student_id
