def canPartitionKSubsets(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        bucket = [0]*k
        avg = sum(nums)/k
        nums.sort(reverse=True)

        def helper(i):
            if i == len(nums):
                return len(set(bucket)) == 1

            for j in range(k):
                bucket[j] += nums[i]

                if bucket[j] <= avg and helper(i+1):
                    return True

                bucket[j] -= nums[i]

                if bucket[j] == 0:
                    break

            return False

        return helper(0)
