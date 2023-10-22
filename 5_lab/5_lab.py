def adding_binary(a,b):
    s = []
    carry = 0
    i = len(a) - 1
    j = len(b) - 1

    while i >= 0 or j >= 0 or carry:
      if i >= 0:
        carry += int(a[i])
        i -= 1
      if j >= 0:
        carry += int(b[j])
        j -= 1
      s.append(str(carry % 2))
      carry //= 2
    return ''.join(reversed(s))

print("Enter your first binary value")
first = input()
print("Enter your second binary value")
second = input()
result = '0'
for digit2 in second:
    if int(digit2) == 1:
        result = adding_binary(first, result)
        first = first + "0" 
    else:
        first = first + "0"
print(result)

