# 2) Loss calculator
goods_price = 200
profit = 0
counterfiet_money = 1000   #value of counterfiet_money
shopkeeper_1 = counterfiet_money   # counterfiet_money given by customer to shopkeeper_1
#Shopkeeper_2 has a change of 1000Rs
shopkeeper_2 = 1000
# counterfiet_money exchanged from shopkeeper_1 to shopkeeper_2
counterfiet_money = shopkeeper_2 
shopkeeper_1 = 1000
customer_change = shopkeeper_1 - goods_price
#shopkeeper_2 returns the counterfiet_money 
shopkeeper_1 = counterfiet_money
loss = counterfiet_money + goods_price
print("Customer change is : ",customer_change)
print("The Loss Encountered by Shopkeeper_1 is ",loss)
