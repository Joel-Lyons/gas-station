class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        start_position = 0
        gas_tank = 0
        n = len(gas)
        i = start_position
        while start_position < n:
            gas_amt = gas[i]
            cost_amt = cost[i]
            gas_tank += gas_amt
            if i + 1 < n:
                i += 1
            else:
                i = 0
            if gas_tank < cost_amt:
                gas_tank = 0
                start_position += 1
            else:
                if start_position == i:
                    return i
                gas_tank -= cost_amt
        return -1