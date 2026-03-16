import numpy as np


def bits_to_qpsk(bits: np.ndarray) -> np.ndarray:
    """
    Map bits to QPSK symbols.
    Uses 2 bits per symbol.

    Mapping:
    00 -> (1 + 1j) / sqrt(2)
    01 -> (-1 + 1j) / sqrt(2)
    11 -> (-1 - 1j) / sqrt(2)
    10 -> (1 - 1j) / sqrt(2)
    """
    if len(bits) % 2 != 0:
        raise ValueError("Number of bits must be even for QPSK modulation.")

    bit_pairs = bits.reshape(-1, 2)
    symbols = []

    for b1, b2 in bit_pairs:
        if b1 == 0 and b2 == 0:
            symbol = 1 + 1j
        elif b1 == 0 and b2 == 1:
            symbol = -1 + 1j
        elif b1 == 1 and b2 == 1:
            symbol = -1 - 1j
        elif b1 == 1 and b2 == 0:
            symbol = 1 - 1j
        symbols.append(symbol)

    return np.array(symbols, dtype=complex) / np.sqrt(2)


def qpsk_to_bits(symbols: np.ndarray) -> np.ndarray:
    """
    Demap QPSK symbols back to bits using decision boundaries
    based on real and imaginary parts.
    """
    bits = []

    for symbol in symbols:
        real = symbol.real
        imag = symbol.imag

        if real >= 0 and imag >= 0:
            bits.extend([0, 0])
        elif real < 0 and imag >= 0:
            bits.extend([0, 1])
        elif real < 0 and imag < 0:
            bits.extend([1, 1])
        else:
            bits.extend([1, 0])

    return np.array(bits, dtype=int)
