from app import greet, add


def test_greet():
    assert greet("Student") == "Hello, Student! Welcome to DevOps Lab 10."


def test_add():
    assert add(10, 20) == 30


def test_add_zero():
    assert add(5, 0) == 5