## Happy or Sad ??

face = {'Happy':':-)','Sad':':-('}

count_happy, count_sad = 0,0

sentence = input()

count_happy = sentence.count(face['Happy'])
count_sad = sentence.count(face['Sad'])

if count_happy==0 and count_sad==0:
    print('none')
elif count_happy>count_sad:
    print('happy')
elif count_sad>count_happy:
    print('sad')
else:
    print('unsure')
    
