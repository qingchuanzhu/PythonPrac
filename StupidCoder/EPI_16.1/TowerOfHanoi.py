class Solution:

    NUM_PEGS = 3
    numOfMoves = 0

    def computeTowerHanoi(self, numRings):
        """
        :type numRings: int
        """
        self.moveTopRingsToPeg(numRings, 1, 3)
        print('Number of moves = %s' % self.numOfMoves)

    def moveTopRingsToPeg(self, num_topRings, sourcePegID, targetPegID):
        if num_topRings == 1:
            print('move ring from %s --> %s' % (sourcePegID, targetPegID))
            self.numOfMoves += 1
        else:
            midPegID = 6 - sourcePegID - targetPegID
            self.moveTopRingsToPeg(num_topRings - 1, sourcePegID, midPegID)
            print('move ring from %s --> %s' % (sourcePegID, targetPegID))
            self.numOfMoves += 1
            self.moveTopRingsToPeg(num_topRings - 1, midPegID, targetPegID)


s = Solution()
s.computeTowerHanoi(6)
