from cantor import *

def test_q(a, b):
    assert q_decode(q_encode(a, b)) == (a, b)
    return q_encode(a, b)

def test_z(z):
    assert z_decode(z_encode(z)) == z
    return z_encode(z)

def run():
    for i in range(2**10):
        test_q(i , i)
        test_q(i, -i)
        test_q(-i, i)
        test_q(-i, -i)

        test_q(i , i//3)
        test_q(i, -i//3)
        test_q(-i, i//3)
        test_q(-i, -i//3)

        test_q(i, 0)
        test_q(0, i)
        test_q(-i, 0)
        test_q(0, -i)

        test_z(i)
        test_z(-i)

    try:
        z_decode(0)
        assert(False)
    except ValueError:
        pass

    try:
        z_decode(-1)
        assert(False)
    except ValueError:
        pass

    try:
        q_decode(0)
        assert(False)
    except ValueError:
        pass

    try:
        q_decode(-1)
        assert(False)
    except ValueError:
        pass

    return "Ok"


if __name__ == '__main__':
    print(run())
