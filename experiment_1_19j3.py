# Write your code here :-)
string_1 ='+++===***'
string_2 ='!@#$%%'
string_3 ='!@#$%'


def freqSym(s):
    x = s

    res = ''
    j = 0
    for i in range(len(s)):
        if i+1==len(x):
            break
        elif s[i]==s[i+1]:
            pass
        else:
            res += str(i-j+1)+' '+s[i]+' '
            j = i + 1

    res+=str(i-j+1)+' '+s[i]+' '

    return res

print(freqSym(string_1))
print(freqSym(string_2))
print(freqSym(string_3))
