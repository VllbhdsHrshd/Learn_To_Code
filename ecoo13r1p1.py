# Take a Number....
# Take, Serve, Close, EOF/..

next_number = int(input())

num_late, num_wait = 0,0

line = ''

while line != 'EOF':
    line = input()
    if line == 'TAKE':
        num_late += 1
        num_wait+=1
        next_number+=1

        if next_number % 1000==0:
            next_number = 1

    elif line == 'SERVE':
        num_wait -= 1
    elif line =='CLOSE':
        print(num_late, num_wait, next_number)
        num_late = 0
        num_wait = 0


