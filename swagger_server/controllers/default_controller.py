from typing import Optional

import connexion

from swagger_server.models.student import Student
from swagger_server.service.student_service import add, delete, get_by_id


def add_student(body: Optional[Student]=None):  # noqa: E501
    """Add a new student

    Adds an item to the system # noqa: E501

    :param body: Student item to add
    :type body: dict | bytes

    :rtype: str
    """
    try:
        if connexion.request.is_json:
            body = Student.from_dict(connexion.request.get_json())  # noqa: E501
            return add(body)
    except ValueError as e:
        return str(e), 400


def delete_student(student_id: Optional[int]=None):  # noqa: E501
    """Delete student

    Deletes a single student # noqa: E501

    :param student_id: the integer
    :type student_id: Optional[int]

    :rtype: Student
    """
    try:
        if student_id is None:
            return 'invalid input', 400

        return delete(student_id)
    except ValueError as e:
        return str(e), 400


def get_student_by_id(student_id: Optional[int]=None):  # noqa: E501
    """gets student

    Returns a single student # noqa: E501

    :param student_id: the integer
    :type student_id: Optional[int]

    :rtype: Student
    """
    try:
        if student_id is None:
            return 'invalid input', 400

        return get_by_id(student_id)
    except ValueError as e:
        return str(e), 400
