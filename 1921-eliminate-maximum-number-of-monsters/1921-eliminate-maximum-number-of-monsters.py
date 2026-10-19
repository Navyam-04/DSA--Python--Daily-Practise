class Solution:
    def eliminateMaximum(self, dist: list[int], speed: list[int]) -> int:
        arrival_time=[]
        for d,s in zip(dist,speed):
            arrival_time.append(d/s)
        arrival_time.sort()
        for current_minute in range(len(arrival_time)):
            if arrival_time[current_minute]<= current_minute:
                return current_minute
        return len(arrival_time)

        