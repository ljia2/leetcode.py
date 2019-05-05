# class Solution(object): # TLE
#     def addOperators(self, num, target):
#         """
#         Given a string that contains only digits 0-9 and a target value,
#         return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.
#
#         Example 1:
#
#         Input: num = "123", target = 6
#         Output: ["1+2+3", "1*2*3"]
#         Example 2:
#
#         Input: num = "232", target = 8
#         Output: ["2*3+2", "2+3*2"]
#         Example 3:
#
#         Input: num = "105", target = 5
#         Output: ["1*0+5","10-5"]
#         Example 4:
#
#         Input: num = "00", target = 0
#         Output: ["0+0", "0-0", "0*0"]
#         Example 5:
#
#         Input: num = "3456237490", target = 9191
#         Output: []
#
#         :type num: str
#         :type target: int
#         :rtype: List[str]
#
#         return all possibles, it hints for backtracking solutions.
#
#         """
#
#         if not num:
#             return []
#
#         digits = []
#         for c in num:
#             if c < '0' or c > '9':
#                 return []
#             digits.append(int(c))
#
#         if len(digits) == 1 and int(num) != target:
#             return []
#
#         ans = []
#         self.dfs(digits, target, 1, [digits[0]], ans)
#         return ans
#
#     def dfs(self, digits, target, level, path, ans):
#         if level == len(digits):
#             if path == [1, '+', 2, '+', 3, '-', 4, '*', 5, '+', 6, '+', 7, '-', 8, '*', 9]:
#                 print("debug here")
#             if self.eval(path) == target:
#                 print(path)
#                 ans.append("".join(map(lambda x:str(x), path)))
#             return
#
#         for op in ["+", "-", "*", None]:
#             if op:
#                 path.append(op)
#                 path.append(digits[level])
#                 self.dfs(digits, target, level+1, path, ans)
#                 path.pop()
#                 path.pop()
#             else:
#                 # you can not form a integer beginning with 0.
#                 if path[-1] > 0:
#                     d = path.pop()
#                     path.append(d*10 + digits[level])
#                     self.dfs(digits, target, level+1, path, ans)
#                     d = path.pop()
#                     path.append(d // 10)
#         return
#
#
#     ## How to evaluate a inexp by stack
#     def eval(self, input):
#         op_stack = []
#         num_stack = []
#
#         n = len(input)
#         for i in range(n):
#             if input[i] not in ["+", "-", "*"]:
#                 num_stack.append(input[i])
#             else:
#                 if input[i] == "+" or input[i] == "-":
#                     # the top op on op_stack has the same or greater precedence as thisOp
#                     while op_stack:
#                         op = op_stack.pop()
#                         num2 = num_stack.pop()
#                         num1 = num_stack.pop()
#                         if op == "+":
#                             num_stack.append(num1 + num2)
#                         elif op == "*":
#                             num_stack.append(num1 * num2)
#                         elif op == "-":
#                             num_stack.append(num1 - num2)
#                 op_stack.append(input[i])
#
#         # all high order operators has been processed.
#         # all operators have the same order.
#         while op_stack:
#             op = op_stack.pop()
#             num2 = num_stack.pop()
#             num1 = num_stack.pop()
#             if op == "+":
#                 num_stack.append(num1 + num2)
#             elif op == "*":
#                 num_stack.append(num1 * num2)
#             elif op == "-":
#                 num_stack.append(num1 - num2)
#         return num_stack[0]



class DFSSolution(object): # TLE
    def addOperators(self, num, target):
        """
        Given a string that contains only digits 0-9 and a target value,
        return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

        Example 1:

        Input: num = "123", target = 6
        Output: ["1+2+3", "1*2*3"]
        Example 2:

        Input: num = "232", target = 8
        Output: ["2*3+2", "2+3*2"]
        Example 3:

        Input: num = "105", target = 5
        Output: ["1*0+5","10-5"]
        Example 4:

        Input: num = "00", target = 0
        Output: ["0+0", "0-0", "0*0"]
        Example 5:

        Input: num = "3456237490", target = 9191
        Output: []

        :type num: str
        :type target: int
        :rtype: List[str]

        return all possibles, it hints for backtracking solutions.

        """

        if not num:
            return []

        if len(num) == 1 and int(num) != target:
            return []

        ans = []
        self.dfs(num, target, 0, "", 0, 0, ans)
        return ans

    def dfs(self, num, target, pos, expression, prev_eval, curr_eval, ans):
        if pos == len(num):
            if curr_eval == target:
                ans.append(expression)
            return

        for l in range(1, len(num) - pos + 1):
            str_n = num[pos:pos+l]

            if str_n[0] == "0" and len(str_n) > 1:
                break

            n = int(str_n)
            if pos == 0:
                self.dfs(num, target, pos + l, str_n, n, n, ans)
            else:
                self.dfs(num, target, pos + l, expression + "+" + str_n, n, curr_eval + n, ans)
                self.dfs(num, target, pos + l, expression + "-" + str_n, -n, curr_eval - n, ans)
                self.dfs(num, target, pos + l, expression + "*" + str_n, prev_eval*n, curr_eval - prev_eval + prev_eval*n, ans)
        return

s = DFSSolution()
print(s.addOperators("123", 6))
print(s.addOperators("123456789", 45))
