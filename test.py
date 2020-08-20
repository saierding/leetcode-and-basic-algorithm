def aStarSearch(problem, heuristic=nullHeuristic):
    import copy
    open = util.PriorityQueue()
    starth = heuristic(problem.getStartState(), problem)
    startg = 0
    startTrack = [None]
    initCost = 0
    bestG = 0
    start_node = [problem.getStartState(), startTrack, initCost]
    open.push(start_node, startg + 2*starth)
    closed = []
    best_g = {problem.getStartState(): 100000}
    while not open.isEmpty():
        s = open.pop()
        if s[0] not in closed or s[2] < best_g.get(s[0]):
            closed.append(s[0])
            best_g[s[0]] = s[2]
            if problem.isGoalState(s[0]):
                return s[1][1:]
            for c in problem.getSuccessors(s[0]):
                ch = heuristic(c[0], problem)
                cg = s[2] + c[2]
                Closed = copy.deepcopy(s[1])
                Closed.append(c[1])
                cData = [c[0], Closed, cg]
                if c[0] not in closed:
                    best_g[c[0]] = cg
                if heuristic(c[0], problem)<10000:
                    open.push(cData, cg + 2*ch)