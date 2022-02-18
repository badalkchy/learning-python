ladka = 'badal'

a = {'Name' : ladka,
     'Roll.no:' : '19ERECS016',
     'Semester' : '4th'
     }

c = list(a.keys())

print(list(enumerate(c)))

# for i,j in enumerate(c):
#  print(i+1, j, a[j])

# FOR PRACTICE

b = {'Car':'oddi',
     'Bike': 'bmw',
     'Bicycle': 'ferarri',
     'Bus' : 'tata'
     }

d = list(b.keys())

print(d)

for i,j in enumerate(b):
     print(i,j, b[j])

