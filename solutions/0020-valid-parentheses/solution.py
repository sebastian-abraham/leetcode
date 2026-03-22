class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        counter = {")":"(", "}":"{", "]":"["}
        for symbol in s:
            if (symbol in counter):
                if len(stack) == 0:
                    return False
                elif stack [-1] == counter[symbol]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(symbol)
        return (len(stack) == 0)
