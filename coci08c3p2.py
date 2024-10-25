## Secret Sentence....

sentence = input()

vowel = 'aeiouAEIOU'
#sentence+='$'
#print(sentence)
decoded = ''
i = 0
while i<len(sentence):
    if sentence[i] in vowel:
        #print(i, sentence[i])
        decoded += sentence[i]
        i += 3
    else:
        decoded += sentence[i]
        i += 1

print(decoded)


    