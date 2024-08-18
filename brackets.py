class Solution:
    def isValid(self, t: str) -> bool:

        stack = []
        if len(t) <= 0:
            return False
        for i in range(len(t)):
            if t[i] == '(':
                stack.append('(')
            if t[i] == '[':
                stack.append('[')
            if t[i] == '{':
                stack.append('{')

            if t[i] == ')':
                if len(stack) > 0:
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                else:
                    return False
            if t[i] == ']':
                if len(stack) > 0:
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
                else:
                    return False
            if t[i] == '}':
                if len(stack) > 0:
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        if len(stack) > 0:
            return False
        else:
            return True



test1 = "()"
test2 = "(){}[]"
test3 = "(]"
test4 = "({{[]}})"
test5 = "(({{[]}})"
test = Solution()
print(test.isValid(test1))
print(test.isValid(test2))
print(test.isValid(test3))
print(test.isValid(test4))
print(test.isValid(test5))