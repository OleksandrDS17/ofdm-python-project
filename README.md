# ofdm-python-project
Das Projekt simuliert vereinfacht ein OFDM-System:  Bitfolge erzeugen  QPSK oder QAM Modulation  OFDM-Symbol mit IFFT  Cyclic Prefix hinzufügen  Kanal simulieren, zum Beispiel Rauschen oder Mehrwegekanal  Empfang mit FFT  Demodulation  Bitfehlerquote auswerten  Plots anzeigen

# OFDM Simulation in Python

## Overview

This project implements a simple **Orthogonal Frequency Division Multiplexing (OFDM)** communication system simulation using Python.
The goal is to demonstrate the basic principles of OFDM transmission and reception, including modulation, IFFT/FFT processing, cyclic prefix handling, and channel effects.

OFDM is widely used in modern communication systems such as Wi-Fi, LTE, 5G, and digital broadcasting.

## Features

* Random bit generation
* QPSK modulation
* OFDM symbol generation using IFFT
* Cyclic Prefix (CP) insertion and removal
* Additive White Gaussian Noise (AWGN) channel simulation
* OFDM demodulation using FFT
* Bit error rate (BER) calculation
* Visualization of signals and constellation diagrams

## Project Structure

```
ofdm-python-simulation/
│
├── main.py                # Run the full simulation
├── requirements.txt       # Required Python packages
├── README.md
│
├── ofdm/
│   ├── transmitter.py     # OFDM transmitter
│   ├── receiver.py        # OFDM receiver
│   ├── modulation.py      # QPSK / QAM mapping
│   ├── channel.py         # Channel models (AWGN)
│   └── utils.py           # Helper functions
│
└── examples/
    └── basic_simulation.py
```

## Requirements

Install the required libraries:

```
pip install -r requirements.txt
```

Required packages:

* numpy
* matplotlib
* scipy

## How to Run

Run the simulation:

```
python main.py
```

The program will:

1. Generate random bits
2. Modulate them using QPSK
3. Create OFDM symbols using IFFT
4. Add a cyclic prefix
5. Send the signal through a noisy channel
6. Recover the data using FFT
7. Calculate the Bit Error Rate (BER)

## Example Output

The simulation may generate plots such as:

* OFDM time-domain signal
* Constellation diagram
* Bit Error Rate results

## OFDM System Flow

Transmitter:

```
Bits → Modulation → IFFT → Add Cyclic Prefix → Channel
```

Receiver:

```
Signal → Remove CP → FFT → Demodulation → Bits
```

## Learning Goals

This project helps understand:

* Basics of digital communication systems
* OFDM signal generation
* FFT and IFFT in communication
* Channel noise effects
* Bit Error Rate analysis

## Possible Improvements

Future extensions could include:

* QAM modulation
* Multipath channel model
* Channel estimation and equalization
* BER vs SNR analysis
* Interactive visualization
* Web interface using Streamlit

## License

This project is open-source and available under the MIT License.

