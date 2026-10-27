import pytest

from convert import c_to_f, c_to_k, f_to_c


@pytest.mark.parametrize(
    "c, expected",
    [(0, 32), (100, 212), (-40, -40), (37, 98.6), (-273.15, -459.67)],
)
def test_c_to_f(c, expected):
    assert c_to_f(c) == pytest.approx(expected)


@pytest.mark.parametrize(
    "f, expected",
    [(32, 0), (212, 100), (-40, -40), (98.6, 37), (-459.67, -273.15)],
)
def test_f_to_c(f, expected):
    assert f_to_c(f) == pytest.approx(expected)


@pytest.mark.parametrize(
    "c, expected",
    [(0, 273.15), (100, 373.15), (-273.15, 0)],
)
def test_c_to_k(c, expected):
    assert c_to_k(c) == pytest.approx(expected)


def test_c_to_f_below_absolute_zero():
    with pytest.raises(ValueError):
        c_to_f(-273.16)


def test_f_to_c_below_absolute_zero():
    with pytest.raises(ValueError):
        f_to_c(-459.68)


def test_c_to_k_below_absolute_zero():
    with pytest.raises(ValueError):
        c_to_k(-300)
