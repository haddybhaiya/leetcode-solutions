class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key = lambda x: x[1]-x[0],reverse = True)

        curr_energy = 0
        total_needed = 0
        for actual,mini in tasks:
            if curr_energy < mini:
                total_needed += (mini-curr_energy)
                curr_energy = mini
            curr_energy -= actual
        return total_needed