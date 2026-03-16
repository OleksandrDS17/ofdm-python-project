from ofdm.modulation import bits_to_qpsk, qpsk_to_bits
from ofdm.transmitter import create_ofdm_symbol, add_cyclic_prefix
from ofdm.receiver import remove_cyclic_prefix, recover_ofdm_symbol
from ofdm.channel import add_awgn
from ofdm.utils import (
    generate_random_bits,
    calculate_ber,
    plot_constellation,
    plot_time_signal,
)

# Simulation parameters
N_SUBCARRIERS = 64
CP_LEN = 16
SNR_DB = 20


def main():
    print("Starting OFDM simulation...")

    # QPSK carries 2 bits per symbol
    n_bits = N_SUBCARRIERS * 2

    # 1. Generate random bits
    tx_bits = generate_random_bits(n_bits)

    # 2. Modulate bits to QPSK symbols
    tx_symbols = bits_to_qpsk(tx_bits)

    # 3. Create OFDM time-domain symbol using IFFT
    tx_ofdm = create_ofdm_symbol(tx_symbols)

    # 4. Add cyclic prefix
    tx_signal = add_cyclic_prefix(tx_ofdm, CP_LEN)

    # 5. Send through AWGN channel
    rx_signal = add_awgn(tx_signal, SNR_DB)

    # 6. Remove cyclic prefix
    rx_no_cp = remove_cyclic_prefix(rx_signal, CP_LEN)

    # 7. Recover symbols using FFT
    rx_symbols = recover_ofdm_symbol(rx_no_cp)

    # 8. Demodulate symbols back to bits
    rx_bits = qpsk_to_bits(rx_symbols)

    # 9. Calculate BER
    ber = calculate_ber(tx_bits, rx_bits)

    print(f"Number of transmitted bits: {len(tx_bits)}")
    print(f"SNR: {SNR_DB} dB")
    print(f"Bit Error Rate (BER): {ber:.6f}")

    # 10. Plot results
    plot_time_signal(tx_signal, title="Transmitted OFDM Signal (Time Domain)")
    plot_constellation(rx_symbols, title="Received QPSK Constellation")


if __name__ == "__main__":
    main()
