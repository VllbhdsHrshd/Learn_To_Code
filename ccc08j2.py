## Song Playlist

songs = 'ABCDE'
button = 0


while button != 4:
    button = int(input())
    presses = int(input())
    
    
    for i in range(presses):
        # button 1 send first to the last element...
        # button 2 send last element to the first position
        # button 3 swap the first two elements
        
        if button == 1:
            songs = songs[1:] + songs[0]
        elif button == 2:
            songs = songs[-1] + songs[:-1]
        elif button == 3:
            songs = songs[:2][::-1]+songs[2:]
    
output = ''
for song in songs:
    output+=song+' '
    
print(output[:-1])
    
            
            
        