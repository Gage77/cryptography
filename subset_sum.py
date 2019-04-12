def subset_sum(arr, total, i, mem):
    key = str(total) + ':' + str(i)
    if key in mem:
        return mem[key]
    if total == 0:
        return 1
    elif total < 0:
        return 0
    elif i < 0:
        return 0
    elif total < arr[i]:
        to_return = subset_sum(arr, total, i-1, mem)
    else:
        to_return = (subset_sum(arr, total - arr[i], i-1, mem) + subset_sum(arr, total, i-1, mem))
    mem[key] = to_return
    return to_return

mem = {}
print(subset_sum([3, 7, 19, 43, 89, 195], 260, 6, mem))
mem = {}
print(subset_sum([5, 11, 25, 61, 125, 261], 408, 6, mem))
mem = {}
print(subset_sum([2, 5, 12, 28, 60, 131, 257], 334, 7, mem))
mem = {}
print(subset_sum([4, 12, 15, 36, 75, 162], 214, 6, mem))