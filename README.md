# TestRepo

## Temperature conversion

`convert.py` provides simple temperature conversions. Each function raises
`ValueError` if the input is below absolute zero (-273.15 °C / -459.67 °F).

```python
from convert import c_to_f, f_to_c, c_to_k

c_to_f(100)   # 212.0
f_to_c(32)    # 0.0
c_to_k(0)     # 273.15

c_to_k(-300)  # raises ValueError
```

Run the tests with:

```sh
python -m pytest -q
```
