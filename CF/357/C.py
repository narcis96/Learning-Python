import heapq
h = []
ans = []
for i in range(int(input())):		
	s = input()
	if s[0] == 'i':
		data = int(s.split()[1])
		heappush(h, data)
		ans.append(s)
	elif s[0] == 'g':
		data = int(s.split()[1]) 
		while h and h[0] < data:
			heappop(h)
			ans.append('removeMin')
		if (not h) or (h[0] > data):
			heappush(h, data)
			ans.append('insert ' + str(data))
		ans.append(s)
	else:
		if not h:
			ans.append('insert 0')
		else:
			heappop(h)
		ans.append('removeMin')

print(len(ans))
print("\n".join(ans))

