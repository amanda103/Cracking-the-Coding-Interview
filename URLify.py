# URLify
# write a method to replace all spaces in string with "%20"

def URLify(s):
    URL_s = s

    URL_list = URL_s.split()

    char = "%20"
    return char.join(URL_list)


print(URLify("amanda is the best"))

sec = "what is happening here"

print(sec)

print(URLify(sec))

print(sec)