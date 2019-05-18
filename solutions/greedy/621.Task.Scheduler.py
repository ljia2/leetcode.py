class GreedySolution:
    def leastInterval(self, tasks, n):
        """

        Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters
        represent different tasks. Tasks could be done without original order.
        Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

        However, there is a non-negative cooling interval n that means between two same tasks,
        there must be at least n intervals that CPU are doing different tasks or just be idle.

        You need to return the least number of intervals the CPU will take to finish all the given tasks.

        Example 1:
        Input: tasks = ["A","A","A","B","B","B"], n = 2
        Output: 8
        Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
        Note:
        
        The number of tasks is in the range [1, 10000].
        The integer n is in the range [0, 100].


        :type tasks: List[str]
        :type n: int
        :rtype: int


        10000 of tasks hints for at most O(nlogn)

        这道题让我们安排CPU的任务，规定在两个相同任务之间至少隔n个时间点。说实话，刚开始博主并没有完全理解题目的意思，
        后来看了大神们的解法才悟出个道理来。下面这种解法参考了大神fatalme的帖子，由于题目中规定了两个相同任务之间至少隔n个时间点，
        那么我们首先应该处理的出现次数最多的那个任务，先确定好这些高频任务，然后再来安排那些低频任务。如果任务F的出现频率最高，为k次，
        那么我们用n个空位将每两个F分隔开，然后我们按顺序加入其他低频的任务，来看一个例子：

        AAAABBBEEFFGG 3

        我们发现任务A出现了4次，频率最高，于是我们在每个A中间加入三个空位，如下：

        A---A---A---A

        AB--AB--AB--A   (加入B)

        ABE-ABE-AB--A   (加入E)

        ABEFABE-ABF-A   (加入F，每次尽可能填满或者是均匀填充)

        ABEFABEGABFGA   (加入G)

        再来看一个例子：

        ACCCEEE 2

        我们发现任务C和E都出现了三次，那么我们就将CE看作一个整体，在中间加入一个位置即可：

        CE-CE-CE

        CEACE-CE   (加入A)

        注意最后面那个idle不能省略，不然就不满足相同两个任务之间要隔2个时间点了。

        这道题好在没有让我们输出任务安排结果，而只是问所需的时间总长，那么我们就想个方法来快速计算出所需时间总长即可。
        我们仔细观察上面两个例子可以发现，都分成了(mx - 1)块，再加上最后面的字母，其中mx为最大出现次数。
        比如例子1中，A出现了4次，所以有A---模块出现了3次，再加上最后的A，每个模块的长度为4。例子2中，CE-出现了2次，再加上最后的CE，每个模块长度为3。我们可以发现，模块的次数为任务最大次数减1，模块的长度为n+1，最后加上的字母个数为出现次数最多的任务，可能有多个并列。这样三个部分都搞清楚了，写起来就不难了，我们统计每个大写字母出现的次数，然后排序，这样出现次数最多的字母就到了末尾，然后我们向前遍历，找出出现次数一样多的任务个数，就可以迅速求出总时间长了，下面这段代码可能最不好理解的可能就是最后一句了，那么我们特别来讲解一下。先看括号中的第二部分，前面分析说了mx是出现的最大次数，mx-1是可以分为的块数，n+1是每块中的个数，而后面的 25-i 是还需要补全的个数，用之前的例子来说明：

        AAAABBBEEFFGG 3

        A出现了4次，最多，mx=4，那么可以分为mx-1=3块，如下：

        A---A---A---

        每块有n+1=4个，最后还要加上末尾的一个A，也就是25-24=1个任务，最终结果为13：

        ABEFABEGABFGA

        再来看另一个例子：

        ACCCEEE 2

        C和E都出现了3次，最多，mx=3，那么可以分为mx-1=2块，如下：

        CE-CE-

        每块有n+1=3个，最后还要加上末尾的一个CE，也就是25-23=2个任务，最终结果为8：

        CEACE-CE

        好，那么此时你可能会有疑问，为啥还要跟原任务个数len相比，取较大值呢？我们再来看一个例子：

        AAABBB 0

        A和B都出现了3次，最多，mx=3，那么可以分为mx-1=2块，如下：

        ABAB

        每块有n+1=1个？你会发现有问题，这里明明每块有两个啊，为啥这里算出来n+1=1呢，
        因为给的n=0，这有没有矛盾呢，没有！因为n表示相同的任务间需要间隔的个数，那么既然这里为0了，说明相同的任务可以放在一起，这里就没有任何限制了，
        我们只需要执行完所有的任务就可以了，所以我们最终的返回结果一定不能小于任务的总个数len的，这就是要对比取较大值的原因了。

        """

        taskfreq = [0] * 26
        for task in tasks:
            index = ord(task) - ord('A')
            taskfreq[index] += 1
        taskfreq.sort()
        max_freq = taskfreq[-1]
        index = len(taskfreq) - 1
        while index > -1 and taskfreq[index] == max_freq:
            index -= 1
        least_slots = (max_freq - 1) * (n + 1) + 26 - index

        # len(tasks) is the lower bound of least minimum slots.
        return max(least_slots, len(tasks))

### How about use Queue?
from collections import Counter
from heapq import heappush, heappop

class HeapSolution:
    def leastInterval(self, tasks, n):
        """
        Instead of making use of sorting as done in the last approach,
        we can also make use of a Max-Heap(queue) to pick the order in which the tasks need to be executed.
        But we need to ensure that the heapification occurs only after the intervals of cooling time, nn, as done in the last approach.


        To do so, firstly, we put only those elements from map into the queue which have non-zero number of instances.
        Then, we start picking up the largest task from the queue for current execution.
        (Again, at every instant, we update the current time as well.)
        We pop this element from the queue.
        We also decrement its pending number of instances and if any more instances of the current task are pending,
        we store them(count) in a temporary temptemp list, to be added later on back into the queuequeue.
        We keep on doing so, till a cycle of cooling time has been finished.
        After every such cycle, we add the generated temptemp list back to the queuequeue for considering the most critical task again.

        We keep on doing so till the queuequeue(and temptemp) become totally empty.
        At this instant, the current value of timetime gives the required result.


        :param tasks:
        :param n:
        :return:
        """
        task_freq = Counter(tasks)
        hq = []
        for task in task_freq.keys():
            heappush(hq, ( -task_freq[task], task))

        ans = 0
        solution = []
        while hq:
            tmp_task = []
            # for each slot, arrange only one job per kind
            for i in range(n+1):
                ans += 1
                if hq:
                    freq, task = heappop(hq)
                    solution.append(task)
                    if freq + 1 < 0:
                        tmp_task.append((freq + 1, task))
                    if not hq and not tmp_task:
                        break
                else:
                    solution.append(" ")

            for freq, task in tmp_task:
                heappush(hq, (freq, task))
        print("".join(solution))
        return ans

s = HeapSolution()
print(s.leastInterval(["A","A","A","B","B","B"], 2))
print(s.leastInterval(["G","C","A","H","A","G","G","F","G","J","H","C","A","G","E","A","H","E","F","D","B","D","H","H","E","G","F","B","C","G","F","H","J","F","A","C","G","D","I","J","A","G","D","F","B","F","H","I","G","J","G","H","F","E","H","J","C","E","H","F","C","E","F","H","H","I","G","A","G","D","C","B","I","D","B","C","J","I","B","G","C","H","D","I","A","B","A","J","C","E","B","F","B","J","J","D","D","H","I","I","B","A","E","H","J","J","A","J","E","H","G","B","F","C","H","C","B","J","B","A","H","B","D","I","F","A","E","J","H","C","E","G","F","G","B","G","C","G","A","H","E","F","H","F","C","G","B","I","E","B","J","D","B","B","G","C","A","J","B","J","J","F","J","C","A","G","J","E","G","J","C","D","D","A","I","A","J","F","H","J","D","D","D","C","E","D","D","F","B","A","J","D","I","H","B","A","F","E","B","J","A","H","D","E","I","B","H","C","C","C","G","C","B","E","A","G","H","H","A","I","A","B","A","D","A","I","E","C","C","D","A","B","H","D","E","C","A","H","B","I","A","B","E","H","C","B","A","D","H","E","J","B","J","A","B","G","J","J","F","F","H","I","A","H","F","C","H","D","H","C","C","E","I","G","J","H","D","E","I","J","C","C","H","J","C","G","I","E","D","E","H","J","A","H","D","A","B","F","I","F","J","J","H","D","I","C","G","J","C","C","D","B","E","B","E","B","G","B","A","C","F","E","H","B","D","C","H","F","A","I","A","E","J","F","A","E","B","I","G","H","D","B","F","D","B","I","B","E","D","I","D","F","A","E","H","B","I","G","F","D","E","B","E","C","C","C","J","J","C","H","I","B","H","F","H","F","D","J","D","D","H","H","C","D","A","J","D","F","D","G","B","I","F","J","J","C","C","I","F","G","F","C","E","G","E","F","D","A","I","I","H","G","H","H","A","J","D","J","G","F","G","E","E","A","H","B","G","A","J","J","E","I","H","A","G","E","C","D","I","B","E","A","G","A","C","E","B","J","C","B","A","D","J","E","J","I","F","F","C","B","I","H","C","F","B","C","G","D","A","A","B","F","C","D","B","I","I","H","H","J","A","F","J","F","J","F","H","G","F","D","J","G","I","E","B","C","G","I","F","F","J","H","H","G","A","A","J","C","G","F","B","A","A","E","E","A","E","I","G","F","D","B","I","F","A","B","J","F","F","J","B","F","J","F","J","F","I","E","J","H","D","G","G","D","F","G","B","J","F","J","A","J","E","G","H","I","E","G","D","I","B","D","J","A","A","G","A","I","I","A","A","I","I","H","E","C","A","G","I","F","F","C","D","J","J","I","A","A","F","C","J","G","C","C","H","E","A","H","F","B","J","G","I","A","A","H","G","B","E","G","D","I","C","G","J","C","C","I","H","B","D","J","H","B","J","H","B","F","J","E","J","A","G","H","B","E","H","B","F","F","H","E","B","E","G","H","J","G","J","B","H","C","H","A","A","B","E","I","H","B","I","D","J","J","C","D","G","I","J","G","J","D","F","J","E","F","D","E","B","D","B","C","B","B","C","C","I","F","D","E","I","G","G","I","B","H","G","J","A","A","H","I","I","H","A","I","F","C","D","A","C","G","E","G","E","E","H","D","C","G","D","I","A","G","G","D","A","H","H","I","F","E","I","A","D","H","B","B","G","I","C","G","B","I","I","D","F","F","C","C","A","I","E","A","E","J","A","H","C","D","A","C","B","G","H","G","J","G","I","H","B","A","C","H","I","D","D","C","F","G","B","H","E","B","B","H","C","B","G","G","C","F","B","E","J","B","B","I","D","H","D","I","I","A","A","H","G","F","B","J","F","D","E","G","F","A","G","G","D","A","B","B","B","J","A","F","H","H","D","C","J","I","A","H","G","C","J","I","F","J","C","A","E","C","H","J","H","H","F","G","E","A","C","F","J","H","D","G","G","D","D","C","B","H","B","C","E","F","B","D","J","H","J","J","J","A","F","F","D","E","F","C","I","B","H","H","D","E","A","I","A","B","F","G","F","F","I","E","E","G","A","I","D","F","C","H","E","C","G","H","F","F","H","J","H","G","A","E","H","B","G","G","D","D","D","F","I","A","F","F","D","E","H","J","E","D","D","A","J","F","E","E","E","F","I","D","A","F","F","J","E","I","J","D","D","G","A","C","G","G","I","E","G","E","H","E","D","E","J","B","G","I","J","C","H","C","C","A","A","B","C","G","B","D","I","D","E","H","J","J","B","F","E","J","H","H","I","G","B","D"], 1))

### Follow up: What is the given order of tasks can not be changed.

class VartionSolution:
    def leastInterval(self, tasks, n):
        if not tasks or n == 0:
            return tasks
        task2slot = dict()
        slot = 0
        for i, task in enumerate(tasks):
            if task not in task2slot.keys():
                slot += 1
                task2slot[task] = slot
            else:
                slot = max(slot + 1, task2slot[task] + n + 1)
                task2slot[task] = slot
        return slot

s = VartionSolution()
print(s.leastInterval(["A","A","A","B","B","B"], 2))
