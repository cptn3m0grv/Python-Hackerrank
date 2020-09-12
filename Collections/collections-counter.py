from collections import Counter

shoes_num = int(input())
shoes_count = Counter(map(int, input().split(" ")))
cust = int(input())

total_amount = 0
for i in range(cust):

    cust_size, cust_price = map(int, input().split(" "))

    if(shoes_count[cust_size]): 
        total_amount = total_amount + cust_price
        shoes_count[cust_size] = shoes_count[cust_size] - 1
        


print(total_amount)