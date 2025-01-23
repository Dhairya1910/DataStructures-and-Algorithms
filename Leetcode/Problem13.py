def myAtoi(s):
    res = []
    neg = False
    num = "0123456789"
    i = 0
    n = len(s)

    # Skip leading whitespace
    while i < n and s[i] == ' ':
        i += 1

    # Check for sign
    if i < n and (s[i] == '-' or s[i] == '+'):
        neg = s[i] == '-'
        i += 1

    # Process digits and construct the number
    while i < n and s[i] in num:
        res.append(s[i])
        i += 1

    # Convert list to integer
    if res:
        ans = int(''.join(res))
        if neg:
            ans = -ans
        # Clamp to 32-bit signed integer range
        ans = max(-2**31, min(ans, 2**31 - 1))
        return ans

    # Return 0 if no valid conversion
    return 0

# Test cases
print(myAtoi("42"))  # Output: 42
print(myAtoi("   -42"))  # Output: -42
print(myAtoi("4193 with words"))  # Output: 4193
print(myAtoi("words and 987"))  # Output: 0
print(myAtoi("-91283472332"))  # Output: -2147483648 (clamped to 32-bit signed integer range)

s= " "
print(len(s))