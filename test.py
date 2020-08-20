def aStarSearch(self,gameState,goal,heuristic):
    """
    astar的方法，heuristic用上面的发现敌人赶紧跑的策略
    """
    start =self.getCurrentObservation().getAgentState(self.index).getPosition()
    openSet = util.PriorityQueue()
    openSet.push(( start,[]), 0)
    visitedNodes = []
    while not openSet.isEmpty():
      node,trace=openSet.pop()
      if node == goal:
        if len(trace)==0:
          return 'Stop'

        return trace[0]
      if node not in visitedNodes:
        visitedNodes.append(node)
        successors=self.getSuccessors(node)
        for successor in successors:
          cost= len(trace +[successor[1]])+heuristic(gameState,successor[0])
          if successor not in visitedNodes:
            openSet.push((successor[0], trace + [successor[1]]), cost)
    if goal != self.home:
      return self.aStarSearch(gameState,self.home,self.enemyConcernHeuristic)
    return 'Stop'