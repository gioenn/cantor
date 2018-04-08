A Python library to encode pairs or integers with natural numbers. Unlike other available implementations it supports pairs with negative values.

It uses a slighty modified version of the [pairing function](https://en.wikipedia.org/wiki/Pairing_function)
that Georg Cantor used in 1873 to prove that the sets of natural, integer and rational numbers have the same cardinality.


#### PREREQUISITES

- Python 2 or 3
- pip

#### INSTALL

```
pip install cantor
```

#### USAGE

```
from cantor import *

# use function q_encode to map a value in Q (a pair) to one in N
q_encode(-12, 34) # returns 4255

# use function q_decode for the inverse transformation
q_decode(4255)    # returns (-12, 34)

# use function z_encode to map a value in Z to one in N
z_encode(0)       # returns 1
z_encode(-1234)   # returns 2648

# use function z_decode for the inverse transformation
z_decode(1)       # returns 0
z_decode(2648)    # returns -1234
```

#### TEST

```
python test.py
```
