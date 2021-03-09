##Slicing Lists and Strings


#list[start:end:step]
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list[3:8])
print(my_list[1:])
print(my_list[1:-2:2])
print(my_list[::-1])

for i in my_list[:-2]:
    print(i)
for j in my_list[-1: 1: -1]:
    if j%2 == 0:
        even =  '{} is even number'.format(j)
        print (even)
    else:
        odd =  '{} is odd number'.format(j)
        print (odd)



#string slicing
sample_url = 'http://www.facebook.com'
print (sample_url)
print(sample_url[::-1])
print(sample_url[-4:])
print(sample_url[7:])
print(sample_url[11:-4])
