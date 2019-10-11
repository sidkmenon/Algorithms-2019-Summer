from __future__ import annotations

def validUtf8(data: List[int]) -> bool:
    sig_bits_10 = lambda num: (num & 2**7 != 0) and (num & 2**6 == 0)
    i = 0
    if len(data) == 0:
        return False
    while (i < len(data)):
        x = data[i]
        if x & 2**7 == 0: # one digit
            i += 1
        else: # two - four digits
            num_in_sequence = 0
            while x & 2**(6 - num_in_sequence) != 0:
                num_in_sequence += 1
                if num_in_sequence >= 4:
                    return False
            print((x, num_in_sequence))
            if 1 <= num_in_sequence <= 3:
                while num_in_sequence > 0:
                    i += 1
                    if i >= len(data):
                        return False
                    x = data[i]
                    if not sig_bits_10(x):
                        return False
                    num_in_sequence -= 1
                i += 1
            else:
                return False

    return True

print(validUtf8([197, 130, 1]))
