print("Enter your string")
x = input()
y = ""
x = x.replace(' ', '')
for letter in reversed(x):
    y = y + letter
if x == y:
    print('true')
else:
    print('false')