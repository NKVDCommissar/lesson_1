def strcounter(string):
    dict = {}
    for i in string:
        dict[i] = dict.get(i, 0) + 1
    for i, cnt in dict.items():
        print(i, cnt)

string = "rarchik"
strcounter(string)