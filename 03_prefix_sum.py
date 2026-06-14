def query_sum(querys, nums):
    sums = [0]
    
    for i in range(len(nums)):
        sums.append(sums[i] + nums[i])

    res = []

    for query in querys:
        res.append(sums[query[1] + 1] - sums[query[0]])

    return res