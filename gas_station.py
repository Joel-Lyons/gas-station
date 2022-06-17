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
        i = 0

        while start_position < n:
            gas_amt = gas[i]
            cost_amt = cost[i]
            gas_tank += gas_amt

            if gas_tank >= cost_amt:
                gas_tank -= cost_amt
                i = 0 if i + 1 >= n else i + 1
                if start_position == i:
                    return i
            else:
                gas_tank = 0
                start_position += 1
                i = start_position
        return -1