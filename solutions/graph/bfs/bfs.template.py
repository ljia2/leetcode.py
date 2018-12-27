class BFS:
    def bfs(self, graph, start):
        # queue
        q = []
        # the state of visiting
        # 1) node only (when can not revisit nodes);
        # 2) node and other information (when can revisit node) see 847 and 86
        seen = dict()
        # start is the start state
        q.append(start)
        seen[start] = 1
        steps = 0
        while q:
            size = len(size)
            while size > 0:
                state = q.pop(0)
                if self.is_goal(state):
                    return steps
                for new_state in self.expend(state):
                    if new_state in seen.keys():
                        continue
                    q.append(new_state)
                    seen.add(new_state)
            steps += 1
        return -1