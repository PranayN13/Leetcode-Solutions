class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        gas_tank = 0
        start = 0
        
        if (sum(gas) - sum(cost) < 0):
            return -1
        
        for i in range(n):
            gas_tank += gas[i] - cost[i]

            if gas_tank < 0:
                start = i+1
                gas_tank = 0
        return start
