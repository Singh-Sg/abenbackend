""" 
Problem Overview: String Compression: Implement a string compressionion using python. For example, aaaabbbccddddddee would become
a4b3c2d6e2. If the length of the string is not reduced, return the original string
"""


def compression(input):
    s = input
    i = 0
    abc = []
    final = ""
    if len(s) == 1:
        print(s[0])
        return s[0]
    while i < len(s):
        count = 1
        for j in range(i + 1, len(s)):
            if s[j] == s[i]:
                count += 1
            else:
                break
        list = [s[i], count]
        abc.append(list)
        i += count

    for i in range(0, len(abc)):
        final = final + (abc[i][0] + str(abc[i][1]))
    print(final)
    return final


assert compression("bbcceeee") == "b2c2e4"
assert compression("aaabbbcccaaa") == "a3b3c3a3"
assert compression("a") == "a"
