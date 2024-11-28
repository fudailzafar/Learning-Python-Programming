# From a file containing numbers separated by comma, print the count of even numbers.

count = 0
with open("practice.txt", "r") as f:
    data = f.read()

    nums = data.split(",")
    for val in nums: 
        if(int(val) % 2 == 0):
            count += 1

print(count)

    # print(nums)
    # num = ""
    # for i in range(len(data)):
    #     if(data[i] == ","):
    #         print(int(num))
    #         num = ""
    #     else:
    #         num += data[i]
