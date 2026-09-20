""" count=0
while count < 10:
    count =  count+1
    if count == 5:
        continue
    #print(count)
    if count == 6:
            break

    #print(count) """

    # For loop
sample = ["server1", "server2", "server3", "server4"]

# membership operator: 'in'
# value = "server1" in sample
# print(value)

# Use case 1: Print all elements inside a list
for val in sample:
  print(enumerate(val))
for idx, value in enumerate(sample):
    print(idx, value)

    print(list(range(1,10,2)))

for idx in range(len(sample)):
   print(idx,sample[idx])

   a,b= (1,2)
   print(a,b)
