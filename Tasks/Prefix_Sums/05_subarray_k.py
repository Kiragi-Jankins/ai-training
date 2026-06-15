def subarrays_sum_equals_K(nums, k):
    tmp_dict = {0: 1}
    cur_sum = 0
    k_cnt = 0
    for i in range(len(nums)):
        cur_sum += nums[i]
        if cur_sum - k in tmp_dict:
            k_cnt += tmp_dict[cur_sum - k]
        tmp_dict[cur_sum] = tmp_dict.get(cur_sum, 0) + 1
    return k_cnt