
def binary(n, bits):
    return format(n & ((1 << bits) - 1), f'0{bits}b')


def signed_value(n, bits):
    if n & (1 << (bits - 1)):
        return n - (1 << bits)
    return n


def calculate(a, b, expression):
    print("\nExpression:", expression)

    # Display operands in 8-bit format
    print("First operand (8-bit): ", binary(a, 8))
    print("Second operand (8-bit):", binary(b, 8))

    # Convert operands to 16-bit representation
    A = a & 0xFFFF
    B = b & 0xFFFF

    # Subtraction using 2's complement:
    # A - B = A + (~B + 1)
    neg_B = (~B + 1) & 0xFFFF
    result = (A + neg_B) & 0xFFFF

    decimal_result = signed_value(result, 16)

    # Check signed 16-bit overflow
    overflow = (a >= 0 and b < 0 and decimal_result < 0) or \
               (a < 0 and b >= 0 and decimal_result >= 0)

    print("16-bit first operand: ", binary(a, 16))
    print("16-bit second operand:", binary(b, 16))
    print("2's complement of second operand:", binary(neg_B, 16))
    print("Final result (16-bit binary):", binary(result, 16))
    print("Final result (decimal):", decimal_result)
    print("Arithmetic overflow:", "Yes" if overflow else "No")


# (a) 35 - (+29)
calculate(35, 29, "35 - (+29)")

# (b) (-35) - (-12)
calculate(-35, -12, "(-35) - (-12)")
