from ofdm.modulation import bits_to_qpsk, qpsk_to_bits
from ofdm.transmitter import create_ofdm_symbol, add_cyclic_prefix
from ofdm.receiver import remove_cyclic_prefix, recover_ofdm_symbol
from ofdm.channel import add_awgn
from ofdm.utils import generate_random_bits, calculate_ber

N_SUBCARRIERS = 64
CP_LEN = 16
SNR_DB = 15


def run_example():
    tx_bits = generate_random_bits(N_SUBCARRIERS * 2)
    tx_symbols = bits_to_qpsk(tx_bits)

    tx_ofdm = create_ofdm_symbol(tx_symbols)
    tx_with_cp = add_cyclic_prefix(tx_ofdm, CP_LEN)

    rx_signal = add_awgn(tx_with_cp, SNR_DB)
    rx_no_cp = remove_cyclic_prefix(rx_signal, CP_LEN)
    rx_symbols = recover_ofdm_symbol(rx_no_cp)
    rx_bits = qpsk_to_bits(rx_symbols)

    ber = calculate_ber(tx_bits, rx_bits)

    print("Basic OFDM Example")
    print(f"Subcarriers: {N_SUBCARRIERS}")
    print(f"Cyclic Prefix Length: {CP_LEN}")
    print(f"SNR: {SNR_DB} dB")
    print(f"BER: {ber:.6f}")


if __name__ == "__main__":
    run_example()
