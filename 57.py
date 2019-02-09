def insert(self, intervals, newInterval):
    """
    :type intervals: List[Interval]
    :type newInterval: Interval
    :rtype: List[Interval]
    """

    intervals.append(newInterval)

    sorted(intervals, lambda key=i : i.start)

    res = []

    for interval in intervals:
        if res:
            if interval.start < res[-1].end:
                res[-1].end = max(interval.end, res[-1].end)
        else:
            res.append(interval)

    return res
