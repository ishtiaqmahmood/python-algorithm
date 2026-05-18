import cmath


def fft(a, invert):
    """
    Performs Fast Fourier Transform.

    Args:
        a (list): List of complex numbers.
        invert (bool): If True, performs Inverse FFT.
    """
    n = len(a)
    if n == 1:
        return a

    a0 = a[0::2]
    a1 = a[1::2]
    fft(a0, invert)
    fft(a1, invert)

    angle = 2 * cmath.pi / n * (1 if invert else -1)
    w = complex(1)
    wn = cmath.exp(complex(0, angle))
    for i in range(n // 2):
        a[i] = a0[i] + w * a1[i]
        a[i + n // 2] = a0[i] - w * a1[i]
        if invert:
            a[i] /= 2
            a[i + n // 2] /= 2
        w *= wn
    return a


if __name__ == "__main__":
    a = [1, 2, 3, 4]
    print(f"FFT of {a}: {fft(a, False)}")
