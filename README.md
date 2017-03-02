# DigitalChannelVLC
This project creates a protocol over raspbian into Raspberry pi 2 model B, in order to probe different FEC coding, such as Turbo coding, Convolutional coding and LDPC coding. In this project is used Commpy toolkit from Veeresht [1] to run and test FEC codes. The first step is create a communication protocol with FEC. The basic communication protocol invloves conversion from text to bits sequence, framing, training sequence and basic modulation OOK.

In the fist stage, it is necesary to understand FEC theory, how Commpy library can be implemented into raspberry pi 2, and then in pyboard.

[1] Veeresh Taranalli, "CommPy: Digital Communication with Python, version 0.3.0. Available at https://github.com/veeresht/CommPy", 2015.
