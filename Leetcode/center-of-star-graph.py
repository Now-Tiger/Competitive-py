
# ------------------------------------------ Find center of star graph ------------------------------------------
#
#       There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where
# there is one center node and exactly n - 1 edges that connect the center node with every other node.
# You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between 
# the nodes ui and vi. Return the center of the given star graph.
#
# Example 1 :
#
# Input: edges = [[1,2],[2,3],[4,2]]
# Output: 2
# Explanation: As shown in the figure above, node 2 is connected to every other node, so 2 is the center.
#
# Example 2 :
#
# Input: edges = [[1,2],[5,1],[1,3],[1,4]]
# Output: 1
#
# ----------------------------------------------------------------------------------------------------------------

class Solution(object):
    def findCenter(self, edges) :
        node = set()
        
        for edge in edges :
            if edge[0] in node :
                return edge[0]
            if edge[1] in node :
                return edge[1]

            node.add(edge[0])
            node.add(edge[1])

        return node

if __name__ == '__main__' :
    # Example 1 :
    nodes = [[1,2],[2,3],[4,2]]
    res = Solution.findCenter(Solution, nodes)
    print(res)

    # Example 2 :
    nodes2 = [[1,2],[5,1],[1,3],[1,4]]
    res = Solution.findCenter(Solution, nodes2)
    print(res)

# $ python center-of-star-graph.py
# 2
# 1