
result = [i*i for i in [1,2,3,4,5]]
print(result)        

def square_nums(nums):
    for i in nums:
        yield (i*i)

my_list = list(square_nums([1,2,3,4,5]))
print(my_list)