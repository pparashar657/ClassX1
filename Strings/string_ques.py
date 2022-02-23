# Ques 1:


# input = "Pawan"
# output = "nawaP"

def reverse(str) -> str:
    idx = len(str) - 1
    ans = ""
    while(idx >= 0):
        ans = ans + str[idx]
        idx = idx - 1
    return ans


def reverse2(str) -> str:
    ans = ""
    for ch in str:
        ans = ch + ans
    return ans


ans = reverse2("Adi is a good boy")
print(ans)
