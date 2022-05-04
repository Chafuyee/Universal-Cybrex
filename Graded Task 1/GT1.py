

def maximum_profit(int_list):
    #Variable Legend:

        # int_list = Original list of variables to be processed
        # cheapest_stock = buy_stock = initial buy value
        # buy_index = location of initial buy value
        # sell_list = list of appropriate values to be tested for a sell_stock
        # highest_stock = sell_stock = initial sell value
        # sell_index = Location of initial sell value
        # initial_stock_list = List of all values including intial buy and sell stock values and the values inbetween
        # stock_distance = length between initial buy and sell values including the values themselves
        # remaining_list = List of values appropriate to be tested for duplicates of lower stock_distance length
        # profit = Evaluation that determines whether or not there is profit to be made from the list values
        # output_tuple = Final output variable that includes the indexes of the most suitable buy and sell values

    #Calculating the initial lowest appropriate stock value
    if len(int_list) == 0:
        return None

    for index in range(len(int_list)):
        if index == 0:
            cheapest_stock = int_list[index]
        else:
            if int_list[index] < cheapest_stock:
                if len(int_list[index+1:]) != 0 :
                    cheapest_stock = int_list[index]

    #Assigning the buy stock index and value; creating the sell_list
    buy_stock = cheapest_stock
    buy_index = int_list.index(buy_stock)
    sell_list = int_list[buy_index+1:]
    if len(sell_list) == 0:
        return None
        
    #Calculating the initial highest appropriate stock value
    for index in range(len(sell_list)):
        if (index == 0) and (len(sell_list) != 0):
            highest_stock = sell_list[index]
        else:
            if sell_list[index] > highest_stock:
                highest_stock = sell_list[index]
                sell_index = sell_list.index(highest_stock)
    sell_stock = highest_stock

    buy_stock_list = [value for value in int_list if (value == buy_stock)]
    buy_length = len(buy_stock_list)
    temp_index = 0
    temp_buy_index = 0
    temp_sell_index = 0 
    after_buy_stock = False

    for index in range(buy_length):
        in_loop = True
        for iteration in range(temp_index, len(int_list)):
            if in_loop == True:
                if int_list[iteration] == buy_stock:
                    temp_buy_index = iteration
                    after_buy_stock = True
                if (int_list[iteration]) == sell_stock and (after_buy_stock == True):
                    temp_sell_index = iteration
                    temp_length = temp_sell_index - temp_buy_index
                    in_loop = False
                    after_buy_stock = False
                    if index == 0:
                        smallest_length = temp_length
                        buy_index = temp_buy_index
                        sell_index = temp_sell_index
                    elif temp_length < smallest_length:
                        smallest_length = temp_length
                        buy_index = temp_buy_index
                        sell_index = temp_sell_index
        temp_index = temp_sell_index+1
        
    #Calculating the profit value and accounting for a "No profit to be made" scenario
    profit = sell_stock - buy_stock
    if profit <= 0:
        return None
        
    #Assigning the final output tuple and returning said output
    output_tuple = (buy_index, sell_index)
    return (output_tuple)

prices = [20, 21, 22, 23, 23, 19, 22, 15, 17, 18]
recommend = maximum_profit(prices)
if recommend is None:
    print('No profit to be made')
else:
    print('Buy @ ' + str(prices[recommend[0]]) + ' on ' + str(recommend[0]))
    print('Sell @ ' + str(prices[recommend[1]]) + ' on ' + str(recommend[1])) 

#Testing

#If there is more than one possible trade (i.e. a pair of buy/sell days) must return buy and sell days that are closest togethor.
    #E.g. rightmost buy days and leftmost sell days (if they are equal)

#If the prior case occurs and both distances are the same, always prioritise the earliest trade

#If there are NO PROFITABLE TRADES at all, such as if the stocks are falling consistently, then the function should return none.

#Cases
prices0 = [122, 123, 126, 121, 119, 123, 121, 119, 115, 119, 121, 122, 121, 119, 118]
prices1 = [235, 196, 140, 65, 32, 9]
prices2 = [1, 2, 3, 4, 2, 2, 1, 2, 4, 2, 1, 4]
prices3 = [1, 1, 4, 4, 2, 2, 1, 2, 4, 2, 1, 4]
prices4 = [235, 196, 140, 30, 32, 9]
prices5 = [122, 123, 126, 121, 119, 123, 121, 119, 115, 119, 121, 122, 121, 119, 118]
prices6 = []
prices7 = [4, 4, 5, 7]
prices8 = [2, 10]
prices9 = [2, 2, 2]


#Unused Code
"""
sell_index += (len(int_list[:buy_index]) +1)
removed_list = int_list[:sell_index]
removed_length = len(removed_list)
intial_stock_list = int_list[buy_index:sell_index+1]
stock_distance = len(intial_stock_list)
remaining_list = int_list[sell_index+1:]
print(remaining_list)
temp_distance = 2
new_sequence = False
"""

"""
for index in range(len(remaining_list)):
    stock_value = remaining_list[index]
    if stock_value == buy_stock:
        in_loop = True
        temp_buy_index = removed_length + index
    if stock_value == sell_stock:
        in_loop == False
        temp_sell_index = removed_length + index
        if temp_distance < stock_distance:
            buy_index = temp_buy_index
            sell_index = temp_sell_index
            return (buy_index, sell_index)
    if in_loop == True:
        temp_distance += 1
"""

"""
for index in range(len(remaining_list)):
    if remaining_list[index] == buy_stock:
        new_sequence = True
        temp_buy_index = removed_length + index+1
    if remaining_list[index] == sell_stock:
        new_sequence = False
        temp_sell_index = removed_length + index+1
        if temp_distance <= stock_distance:
            print(temp_sell_index, temp_buy_index)
            return(temp_buy_index, temp_sell_index)
    if new_sequence == True:
        temp_distance += 1
"""