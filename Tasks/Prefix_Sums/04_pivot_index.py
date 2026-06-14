def pivot_index(nums):
    summa = sum(nums)
    tmp_sum = 0
    for i in range(len(nums)):
        if tmp_sum == summa - tmp_sum - nums[i]:
            return i
        tmp_sum += nums[i]
    else:
        return -1