import numpy as np


def remove_cyclic_prefix(received_signal: np.ndarray, cp_len: int) -> np.ndarray:
    """
    Remove the cyclic prefix from the received OFDM signal.
    """
    return received_signal[cp_len:]


def recover_ofdm_symbol(received_time_signal: np.ndarray) -> np.ndarray:
    """
    Convert the received OFDM time-domain symbol back to
    the frequency domain using the FFT.
    """
    return np.fft.fft(received_time_signal)
