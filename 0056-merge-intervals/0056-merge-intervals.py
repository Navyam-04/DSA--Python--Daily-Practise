class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        merged=[intervals[0]]
        for i in range(1,len(intervals)):
            current_start,current_end=intervals[i]
            last_merged_st,last_merged_end=merged[-1]
            if current_start <= last_merged_end:
                merged[-1][1]=max(current_end,last_merged_end)
            else:
                merged.append(intervals[i])
        return merged

        