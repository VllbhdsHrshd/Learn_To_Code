## Who is in the middle?

l = int(input())
m = int(input())
n = int(input())

total = l + m + n
total -= (max(l,m,n)+min(l,m,n))
print(total)
