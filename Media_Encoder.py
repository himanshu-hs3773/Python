def optimalSum(fileSizes: [int]) -> int:

    fileSizes = sorted(fileSizes, reverse=True)
    sums_arr = [0] * (len(fileSizes)+1)
    temp_sum = float('-inf')
    start = 0

    if not len(fileSizes):
        return -1
    while len(fileSizes) > 1:

        if temp_sum < fileSizes[-2]:
            sums_arr[start + 1] += sums_arr[start] + fileSizes[-1]
            fileSizes.pop()
            temp_sum = sums_arr[start + 1]
            start += 1

        else:
            sums_arr[start + 1] += fileSizes[-1] + fileSizes[-2]
            fileSizes.pop()
            fileSizes.pop()
            temp_sum = sums_arr[start + 1]
            start += 1

    if len(fileSizes) == 1:
        sums_arr[start + 1] += fileSizes[0] + sums_arr[start]

    return sum(sums_arr[2:])
