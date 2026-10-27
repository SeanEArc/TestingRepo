"""Temperature conversion helpers."""

ABSOLUTE_ZERO_C = -273.15
ABSOLUTE_ZERO_F = -459.67


def _check_celsius(c):
    if c < ABSOLUTE_ZERO_C:
        raise ValueError(f"{c} °C is below absolute zero ({ABSOLUTE_ZERO_C} °C)")


def c_to_f(c):
    """Convert Celsius to Fahrenheit."""
    _check_celsius(c)
    return c * 9 / 5 + 32


def f_to_c(f):
    """Convert Fahrenheit to Celsius."""
    if f < ABSOLUTE_ZERO_F:
        raise ValueError(f"{f} °F is below absolute zero ({ABSOLUTE_ZERO_F} °F)")
    return (f - 32) * 5 / 9


def c_to_k(c):
    """Convert Celsius to Kelvin."""
    _check_celsius(c)
    return c - ABSOLUTE_ZERO_C
