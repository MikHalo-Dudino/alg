#python
def correct(s):
    lenght = len(s)
    last = []
    stack = []
    for i in range(lenght):
        
        if s[i] == '(':
            stack.append(1)
            last.append(i + 1)
        elif s[i] == ')':
            last.pop()
            if stack.pop() != 1:
                return i + 1
        elif s[i] == '[':
            stack.append(2)
            last.append(i + 1)
        elif s[i] == ']':
            last.pop()
            if stack.pop() != 2:
                return i + 1
        elif s[i] == '{':
            stack.append(3)
            last.append(i + 1)
        elif s[i] == '}':
            last.pop()
            if stack.pop() != 3:
                return i + 1
    
    if len(stack) == 0: return "Success"
    else: return last[0]
print(correct(input()))
