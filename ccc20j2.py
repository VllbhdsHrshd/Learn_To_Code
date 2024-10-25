## Epidemiology
## Threshold ---> P
#Initial_day ---> N
# Rate of infection ---> R

P_threshold = int(input())
N_initialDay = int(input())
R_rateOfInfection = int(input())

current = N_initialDay
today= current
day = 0
while current<P_threshold:
    today *= R_rateOfInfection
    current += today
    day += 1
    
print(day)


