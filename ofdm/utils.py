import numpy as np
import matplotlib.pyplot as plt


def generate_random_bits(n_bits: int) -> np.ndarray:
    """
    Generate random bits (0 or 1).
    """
    return np.random.randint(0, 2, n_bits)


def calculate_ber(tx_bits: np.ndarray, rx_bits: np.ndarray) -> float:
    """
    Calculate the Bit Error Rate (BER).
    """
    if len(tx_bits) != len(rx_bits):
        raise ValueError("Transmitted and received bit arrays must have the same length.")

    bit_errors = np.sum(tx_bits != rx_bits)
    return bit_errors / len(tx_bits)


def plot_constellation(symbols: np.ndarray, title: str = "Constellation Diagram") -> None:
    """
    Plot the constellation diagram of received symbols.
    """
    plt.figure(figsize=(6, 6))
    plt.scatter(symbols.real, symbols.imag, alpha=0.7)
    plt.axhline(0)
    plt.axvline(0)
    plt.grid(True)
    plt.title(title)
    plt.xlabel("In-Phase")
    plt.ylabel("Quadrature")
    plt.tight_layout()
    plt.show()


def plot_time_signal(signal: np.ndarray, title: str = "Time Domain Signal") -> None:
    """
    Plot the real and imaginary parts of a time-domain signal.
    """
    plt.figure(figsize=(10, 4))
    plt.plot(signal.real, label="Real")
    plt.plot(signal.imag, label="Imaginary")
    plt.title(title)
    plt.xlabel("Sample Index")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
