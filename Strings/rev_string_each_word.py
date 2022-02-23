
def rev_string_each_wise(str) -> str:
    words = str.split(' ')
    ans = ""
    print(words)
    for word in words:
        ans = ans + word[::-1] + " "

    return ans[:-1]


print(rev_string_each_wise("Adi is a good boy"))
