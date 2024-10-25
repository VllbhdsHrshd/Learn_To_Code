password = input()

lowerCase_range = list(range(ord('a'), ord('z')+1))
upperCase_range = list(range(ord('A'),ord('Z')+1))
digitRange = list(range(ord('0'),ord('9')+1))
isValid = True
count_lower, count_higher, count_digi = 0,0,0
#print(lowerCase_range, upperCase_range, digitRange)
lengthFlag = True
if len(password)<8 or len(password)>12:
    #print('Invalid')
    lengthFlag = False


for j in range(len(password)):
    if ord(password[j]) in lowerCase_range:
        count_lower+=1
        #isValid = True
    elif ord(password[j]) in upperCase_range:
        count_higher+=1
        #isValid = True
    elif ord(password[j]) in digitRange:
        count_digi+=1
        #isValid = True
    else:
        #print('Invalid')
        isValid = False
        break

#print(count_digi, count_higher, count_lower)
if lengthFlag and isValid and count_digi>=1 and count_higher>=2 and count_lower>=3:
    print('Valid')
else:
    print('Invalid')
