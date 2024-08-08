# caesar_decrypt.py

from pathlib import Path

import numpy as np

file_name = "ciphertext2.txt"
key_shift = -154  # To reverse the decryption, take away or add to the ASC11 e(101)

file_path = Path(__file__).parent / file_name
with open(file_path, "rb") as f_in:
    f_bytes = bytearray(f_in.read())

for i in np.arange(len(f_bytes)):
    f_bytes[i] = (f_bytes[i] + key_shift) % 256

print(f_bytes.decode("utf-8", "ignore"))  # Ignore the characters
