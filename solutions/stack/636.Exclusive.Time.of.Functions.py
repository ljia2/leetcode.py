class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        fun2time = [0] * n
        func_stack = []
        for log in logs:
            fields = log.split(":")
            if len(fields) == 3:
                f, label, t = int(fields[0]), fields[1], int(fields[2])
                if label == 'start':
                    if func_stack: # not empty
                        lf, st = func_stack[-1]
                        fun2time[lf] += t - st # pause last function and update execution time
                    func_stack.append((f, t)) # insert current function
                elif label == 'end':
                    lf, st = func_stack.pop() # pop the ending function
                    fun2time[lf] += t - st + 1 # update ending function execution time
                    if func_stack:
                        (lf, _) = func_stack.pop()
                        func_stack.append((lf, t + 1)) # update last function's new start time
                else:
                    raise Exception("Log Label Error:", log)
            else:
                raise Exception("Log Format Error: ", log)
        return fun2time



