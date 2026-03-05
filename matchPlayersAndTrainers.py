class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        """
        :type players: List[int]
        :type trainers: List[int]
        :rtype: int
        """
        players.sort()
        trainers.sort()
        x=len(players)-1
        y=len(trainers)-1
        i=0
        j=0
        while i<=x and j<=y:
            if players[i]>trainers[j]:
                j+=1
            else:
                i+=1
                j+=1
        return i   
