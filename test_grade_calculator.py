from grade_calculator import calculate_total
from grade_calculator import calculate_average
from grade_calculator import calculate_grade


def test_total():
    assert calculate_total(80, 90, 70) == 240


def test_average():
    assert calculate_average(80, 90, 70) == 80


def test_grade_a():
    assert calculate_grade(95) == "A"


def test_grade_b():
    assert calculate_grade(80) == "B"


def test_grade_c():
    assert calculate_grade(65) == "C"


def test_grade_fail():
    assert calculate_grade(30) == "Fail"