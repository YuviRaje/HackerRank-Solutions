# Enter your code here. Read input from STDIN. Print output to STDOUT

s1 = str(input())
s2 = str(input())

# print s1.count(s2) -- for non-overlapping sequences

count = 0
for i in range(len(s1)):
    if s1[i:].startswith(s2):
		count += 1
    #i += x
print (count)