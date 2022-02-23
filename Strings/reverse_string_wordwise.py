
def rev_string_word_wise(str) -> str:
    words = str.split(' ')
    ans = ""
    print(words)
    for word in words[::-1]:
        ans = ans + word + " "

    return ans[:-1]


print(rev_string_word_wise("Adi is a good boy."))
