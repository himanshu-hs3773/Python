fileSizes = [4, 8, 6, 12]

fileSizes = sorted(fileSizes, reverse=True)

print("a thing queue: ", fileSizes, "\n")

sums_arr = [0] * (len(fileSizes)+1)
temp_sum = float('-inf')
queue_size = len(fileSizes) + 1
start = 0

if not len(fileSizes):
    print(sum(sums_arr[2:]))
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

print(sum(sums_arr[2:]))