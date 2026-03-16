import numpy as np


def create_ofdm_symbol(data_symbols: np.ndarray) -> np.ndarray:
    """
    Convert frequency-domain QPSK/QAM symbols into a time-domain OFDM symbol
    using the IFFT.
    """
    return np.fft.ifft(data_symbols)


def add_cyclic_prefix(ofdm_time_signal: np.ndarray, cp_len: int) -> np.ndarray:
    """
    Add a cyclic prefix by copying the last cp_len samples
    to the beginning of the OFDM symbol.
    """
    cyclic_prefix = ofdm_time_signal[-cp_len:]
    return np.concatenate([cyclic_prefix, ofdm_time_signal])
