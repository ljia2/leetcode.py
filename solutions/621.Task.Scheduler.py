import string

class GreedySolution:
    def leastInterval(self, tasks, n):
        """

        Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters
        represent different tasks.Tasks could be done without original order.
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

        这道题好在没有让我们输出任务安排结果，而只是问所需的时间总长，那么我们就想个方法来快速计算出所需时间总长即可。我们仔细观察上面两个例子可以发现，都分成了(mx - 1)块，再加上最后面的字母，其中mx为最大出现次数。比如例子1中，A出现了4次，所以有A---模块出现了3次，再加上最后的A，每个模块的长度为4。例子2中，CE-出现了2次，再加上最后的CE，每个模块长度为3。我们可以发现，模块的次数为任务最大次数减1，模块的长度为n+1，最后加上的字母个数为出现次数最多的任务，可能有多个并列。这样三个部分都搞清楚了，写起来就不难了，我们统计每个大写字母出现的次数，然后排序，这样出现次数最多的字母就到了末尾，然后我们向前遍历，找出出现次数一样多的任务个数，就可以迅速求出总时间长了，下面这段代码可能最不好理解的可能就是最后一句了，那么我们特别来讲解一下。先看括号中的第二部分，前面分析说了mx是出现的最大次数，mx-1是可以分为的块数，n+1是每块中的个数，而后面的 25-i 是还需要补全的个数，用之前的例子来说明：

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
        # there are 26 - index task with highest frequency

        least_slots = (max_freq - 1) * (n + 1) + 26 - index
        return max(least_slots, len(tasks))