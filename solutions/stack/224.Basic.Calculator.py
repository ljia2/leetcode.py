class Solution:
    def calculate(self, s):
        """
        Implement a basic calculator to evaluate a simple expression string.

        The expression string may contain open ( and closing parentheses ),
        the plus + or minus sign -, non-negative integers and empty spaces .

        Example 1:

        Input: "1 + 1"
        Output: 2
        Example 2:

        Input: " 2-1 + 2 "
        Output: 3
        Example 3:

        Input: "(1+(4+5+2)-3)+(6+8)"
        Output: 23
        Note:
        You may assume that the given expression is always valid.
        Do not use the eval built-in library function.

        :type s: str
        :rtype: int
        """
        if s is None or s == "":
            return 0

        num_stack = []
        op_stack = []
        index = 0
        while index < len(s):
            c = s[index]
            if c == ' ':
                index += 1
                continue
            elif c == '(':
                op_stack.append(c)
                index += 1
            elif c == '+' or c == '-':
                op_stack.append(c)

                next_index = index + 1
                while next_index < len(s):
                    if s[next_index] == ' ':
                        next_index += 1
                    elif s[next_index] == '(':
                        op_stack.append(s[next_index])
                        next_index += 1
                        break
                    elif s[next_index].isalnum():
                        (op2, next_index) = self.parseNum(s, next_index)
                        op1 = num_stack.pop()
                        op = op_stack.pop()
                        if op == '+':
                            num_stack.append(op1 + op2)
                        elif op == '-':
                            num_stack.append(op1 - op2)
                        break
                index = next_index
            elif c == ')':
                # TO DO
                while op_stack:
                    op = op_stack.pop()
                    if op == '+':
                        num1 = num_stack.pop()
                        num2 = num_stack.pop()
                        num_stack.append(num2 + num1)
                    elif op == '-':
                        num1 = num_stack.pop()
                        num2 = num_stack.pop()
                        num_stack.append(num2 - num1)
                    elif op == '(':
                        # when pop a left parenthesis, we need to evaluate the last operator
                        if op_stack:
                            op = op_stack.pop()
                            num1 = num_stack.pop()
                            num2 = num_stack.pop()
                            if op == '+':
                                num_stack.append(num2+num1)
                            elif op == '-':
                                num_stack.append(num2-num1)
                        break
                index += 1
            elif c.isalnum():
                (num, index) = self.parseNum(s, index)
                num_stack.append(num)

        while op_stack:
            op = op_stack.pop()
            if op == '+':
                num1 = num_stack.pop()
                num2 = num_stack.pop()
                num_stack.append(num2 + num1)
            elif op == '-':
                num1 = num_stack.pop()
                num2 = num_stack.pop()
                num_stack.append(num2 - num1)

        return num_stack.pop()

    def parseNum(self, s, start):
        num = int(s[start])
        next_index = start + 1
        while next_index < len(s):
            if s[next_index].isalnum():
                num = num * 10 + int(s[next_index])
                next_index += 1
            else:
                break
        return num, next_index

def main():
    s = Solution()
    print(s.calculate("""( 45 + (12 - 13) ) + (868 - 897)"""))
    print(s.calculate(" 2-1 + 2 "))
    print(s.calculate("2-4-(8+2-6+(8+4-(1)+8-10))"))


if __name__ == "__main__":
    main()
