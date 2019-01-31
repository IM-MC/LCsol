def combinationSum2(candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        arr = []

        def backtrack(n, target, index, candidates, curr, arr):
            if n == target:
                listCopy = list(curr)
                listCopy.sort()
                if listCopy not in arr:
                    arr.append(listCopy)
                return

            for i in range(index, len(candidates)):
                if n + candidates[i] > target:
                    continue

                n += candidates[i]
                curr.append(candidates[i])
                backtrack(n, target, i+1, candidates, curr, arr)
                n -= candidates[i]
                del curr[-1]

        backtrack(0, target, 0, candidates, [], arr)
        return arr

print(combinationSum2([10,1,2,7,6,1,5], 8))
