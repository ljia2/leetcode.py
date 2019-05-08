class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        On a single threaded CPU, we execute some functions.  Each function has a unique id between 0 and N-1.

        We store logs in timestamp order that describe when a function is entered or exited.

        Each log is a string with this format: "{function_id}:{"start" | "end"}:{timestamp}".
        For example, "0:start:3" means the function with id 0 started at the beginning of timestamp 3.
        "1:end:2" means the function with id 1 ended at the end of timestamp 2.

        A function's exclusive time is the number of units of time spent in this function.
        Note that this does not include any recursive calls to child functions.

        Return the exclusive time of each function, sorted by their function id.
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
                    # pop the ending function
                    lf, st = func_stack.pop()
                    # update ending function execution time
                    fun2time[lf] += t - st + 1
                    if func_stack:
                        (lf, _) = func_stack.pop()
                        # update last function's new start time
                        func_stack.append((lf, t + 1))
                else:
                    raise Exception("Log Label Error:", log)
            else:
                raise Exception("Log Format Error: ", log)
        return fun2time



