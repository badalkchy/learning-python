a='badal'

# f = len(a)
# print(f)

# b=a.upper()
# print(b)

# c=a[0].upper()
# # d=a[0]
# print(c)

for i in range(len(a)):
    if i % 2 != 0:
        print(a[i].upper(), end='\t')
    else:
        print(a[i], end='\t')

        