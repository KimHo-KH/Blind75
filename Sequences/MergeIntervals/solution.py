class Solution:
    def merge(self, intervals):
        # Sort the intervals based on the start time
        intervals.sort(key=lambda x: x[0])
        
        merged_intervals = []
        
        # Iterate through each interval
        for interval in intervals:
            # If the list of merged intervals is empty or if the current
            # interval does not overlap with the previous one
            if not merged_intervals or interval[0] > merged_intervals[-1][1]:
                # Append the current interval to the list of merged intervals
                merged_intervals.append(interval)
            else:
                # Update the end time of the last interval in the merged list
                # to the maximum of the current and previous end times
                merged_intervals[-1][1] = max(merged_intervals[-1][1], interval[1])
        
        return merged_intervals
