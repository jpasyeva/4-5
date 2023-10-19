print("Enter your string")
string = input()
curly_unclosed = 0
square_unclosed = 0
round_unclosed = 0
for bracket in string:
    if bracket == '{':
        curly_unclosed += 1
    elif bracket == '[':
        square_unclosed += 1
    elif bracket == '(':
        round_unclosed += 1
    elif (bracket == '}') & (curly_unclosed > 0):
        curly_unclosed -= 1
    elif (bracket == ']') & (square_unclosed > 0):
        square_unclosed -= 1
    elif (bracket == ')') & (round_unclosed > 0):
        round_unclosed -= 1
    else:
        curly_unclosed += 1
if curly_unclosed + square_unclosed + round_unclosed == 0:
    print('True')
else:
    print('False')