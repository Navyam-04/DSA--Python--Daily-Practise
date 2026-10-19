from collections import Counter
class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        if n==0:
            return len(tasks)
        task_count=list(Counter(tasks).values())
        max_freq=max(task_count)
        max_freq_count = task_count.count(max_freq)
        interval=(max_freq -1)*(n+1)+max_freq_count
        return max(interval, len(tasks))


        