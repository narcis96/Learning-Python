n,m = map(int,raw_input().split())
lst = []
for i in range(n):
    lst.append(map(int,raw_input().split()))
k = int(raw_input())
lst.sort(key = lambda x: x[k])
print "\n".join(map(lambda x: " ".join(map(str, x)),lst))
