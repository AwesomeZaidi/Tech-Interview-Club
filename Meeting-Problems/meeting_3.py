# Warmup

# Lets say you are given a document that contains the price for a given stock on each day for a given year. 
# Write a program to find the maximum profit that could be attained by buying and selling one share of that stock.

def find(prices):
    '''
        Args: Prices: list
        Returns: max profit: int
    '''
    max_profit = 0
    min_val = prices[0]
    for val in prices:
        if val < min_val:
            min_val = val
            continue
        if val - min_val > max_profit:
            max_profit = val - min_val

    return max_profit


# print(find([100,2,5,200,50,1,400])) # 399 ✅



# Problem 1:

def maxProfit(prices):
    max_profit = 0
    min_val = prices[0]
    for val in prices:
        if val < min_val:
            min_val = val
            continue
        curr_val = val - min_val
        if val > min_val:
            max_profit += curr_val

    return max_profit

print(maxProfit([20,10,30,0,20])) # 40
