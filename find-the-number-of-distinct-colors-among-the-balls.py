class Solution(object):
    def queryResults(self, limit, queries):
        """
        :type limit: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n=len(queries)
        result=[]
        color_map={}
        ball_arr={}
        for i in range(n):
            ball, color=queries[i]
            if ball in ball_arr:
                prev_color=ball_arr[ball]
                color_map[prev_color]-=1
                if color_map[prev_color]==0:
                    del color_map[prev_color]
            ball_arr[ball]=color
            color_map[color]=color_map.get(color, 0)+1
            result.append(len(color_map))
        return result

