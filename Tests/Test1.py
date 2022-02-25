# Ques 1
# Find the second max of a list

from multiprocessing.sharedctypes import Value


def secondMax(my_list):
    my_max = 0
    max_2 = 0
    for curr in (my_list):
        if (curr > my_max):
            max_2 = my_max
            my_max = curr
        elif (curr > max_2):
            max_2 = curr
    return max_2


list = [4, 3, 2, 1]
print(secondMax(list))

# Ques 2
# Find the highest frequency character in a string


def getHighestFreqChar(str):
    dic = {}
    for ch in str:
        if ch in dic:
            dic[ch] += 1
        else:
            dic[ch] = 1
    max_fr = 0
    ans = 0
    for key, value in dic.items():
        if value > max_fr:
            max_fr = value
            ans = key
    return ans, max_fr


str = "Adiisasmartaboy"
print(getHighestFreqChar(str))
