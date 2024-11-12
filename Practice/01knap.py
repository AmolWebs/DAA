items_arr = [[50,8],[100,16],[150,32],[200,40]] #[[profit,weight]]
w = 64 #Knapsack capacity
    # val=[50,100,150,200] #value array
    # wt=[8,16,32,40] # Weight array
    # W=64
Profit = 0

items_arr = sorted(items_arr, key = lambda x : x[0] / x[1], reverse = True)
for i in range(len(items_arr)):
	itemWt = items_arr[i][1]
	itemP = items_arr[i][0]
	if(itemWt > w):
		break
	else:
		Profit += itemP
		w -= itemWt
print("Name : Amol Subhash Dangat \nRoll No : 09\n\n")
print("Maximum Profit : ",Profit)