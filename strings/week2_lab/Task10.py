from operator import contains

mydict = {
}

inputsentence = input("Please input a sentence: ").lower()

for i in range(len(inputsentence)):
    if contains(mydict.keys(),inputsentence[i]):
        mydict[f'{inputsentence[i]}'] = mydict[inputsentence[i]] + 1
    elif inputsentence[i] == ' ':
        continue
    else:
        mydict[f'{inputsentence[i]}'] = 1

print(f"Letters are as follows: {mydict}")