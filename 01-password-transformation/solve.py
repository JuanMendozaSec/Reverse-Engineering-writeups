
expected = [
    0x49, 0x66, 0x64, 0x75,
    0x69, 0x48, 0x71, 0x70
]

password = ""

for byte in expected:
    original = (byte ^ 0x20) - 3
    password += chr(original)

print(password)
