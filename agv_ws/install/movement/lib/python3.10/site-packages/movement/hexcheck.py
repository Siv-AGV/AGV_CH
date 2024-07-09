def decimal_to_hex(decimal_value, bit_length=32):
    if decimal_value >= 0:
        # Positive decimal
        return hex(decimal_value)
    else:
        # Negative decimal, use two's complement
        two_complement_value = (1 << bit_length) + decimal_value
        return hex(two_complement_value)

# Example usage
positive_decimal = 383372
negative_decimal = -383372

positive_hex = decimal_to_hex(positive_decimal)
negative_hex = decimal_to_hex(negative_decimal)

print(f"Positive Decimal: {positive_decimal} -> Hex: {positive_hex}")
print(f"Negative Decimal: {negative_decimal} -> Hex: {negative_hex}")
