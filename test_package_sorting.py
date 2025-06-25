from main import sort, isBulky, isHeavy, STANDARD_PACKAGE, SPECIAL_PACKAGE, REJECTED_PACKAGE, ERROR_DIMENSIONS, ERROR_INPUT_TYPE
from pytest import raises

def test_standard_package():
    assert sort(50.0, 50.0, 50.0, 10.0) == STANDARD_PACKAGE
    assert sort(50.0, 50.0, 50.0, 19.0) == STANDARD_PACKAGE

def test_special_package():
    assert sort(50.0, 50.0, 50.0, 20.0) == SPECIAL_PACKAGE
    assert sort(200.0, 50.0, 50.0, 19.0) == SPECIAL_PACKAGE
    assert sort(50.0, 200.0, 50.0, 10.0) == SPECIAL_PACKAGE
    assert sort(50.0, 50.0, 200.0, 10.0) == SPECIAL_PACKAGE

def test_rejected_package():
    assert sort(200.0, 200.0, 200.0, 20.0) == REJECTED_PACKAGE
    assert sort(200.0, 50.0, 50.0, 20.0) == REJECTED_PACKAGE
    assert sort(50.0, 200.0, 50.0, 20.0) == REJECTED_PACKAGE
    assert sort(50.0, 50.0, 200.0, 20.0) == REJECTED_PACKAGE
    assert sort(float("inf"), float("inf"), float("inf"), float("inf")) == REJECTED_PACKAGE
    assert sort(1.0, 1.0, float("inf"), float("inf")) == REJECTED_PACKAGE

def test_value_error():
    with raises(ValueError, match=ERROR_DIMENSIONS):
        sort(0.0, 50.0, 50.0, 10.0)
    with raises(ValueError, match=ERROR_DIMENSIONS):
        sort(50.0, 0.0, 50.0, 10.0)
    with raises(ValueError, match=ERROR_DIMENSIONS):
        sort(50.0, 50.0, 0.0, 10.0)
    with raises(ValueError, match=ERROR_DIMENSIONS):
        sort(-1.0, -1.0, -1.0, 10.0)
    with raises(ValueError, match=ERROR_INPUT_TYPE):
        sort("50.0", 50.0, 50.0, -1.0)

def test_is_bulky():
    assert isBulky(50.0, 50.0, 50.0) == False
    assert isBulky(200.0, 50.0, 50.0) == True
    assert isBulky(50.0, 200.0, 50.0) == True
    assert isBulky(50.0, 50.0, 200.0) == True

def test_is_heavy():
    assert isHeavy(10.0) == False
    assert isHeavy(20.0) == True
    assert isHeavy(19.99) == False