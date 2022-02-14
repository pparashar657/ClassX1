
def max_in_range(list, start, end):
    # ans = list[start]
    # for i in range(start, end+1):
    #     if(ans < list[i]):
    #         ans = list[i]
    # return ans

    return max(list[start:end+1])


list = [1, 5, 21, 4, 7, 8, 16]

print(max_in_range(list, 2, 4))
