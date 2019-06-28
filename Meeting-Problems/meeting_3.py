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
    lowest_val = prices[0]
    potential_options = []
    # Go through each value in prices
    for idx, val in enumerate(prices):
        print('Iteration:', idx)
        print('lowest_val:', lowest_val, 'val:', val)
        # if the val is less than lowest value, set lowest_val to that val and continue
        if val <= lowest_val:
            print('Set lowest value')
            lowest_val = val
            continue
        # if we found a potential profit
        if val > lowest_val:
            print('found a potential profit, added to potential options.')
            # add the value to our list of potential values
            potential_options.append(val)
            # Don't do this yet!: max_profit += val - lowest_val 
            # If we haven't reached the end
            try:
                # set the lowest_val to the next val if its less than or equal to where we're at.
                if prices[idx+1] <= val:
                        lowest_val = prices[idx+1]
                # If not, we keep our lowest value where its at.
            except IndexError:
                print(potential_options)
                max_profit = max(potential_options) - lowest_val
                return max_profit

    return max_profit

# print(maxProfit([7,1,5,3,6,4])) # 7
# print(maxProfit([7,1,5])) # 4
print(maxProfit([1,2,3,4,5])) # 4
# potential_options.append(val)
# if val <= prices[idx+1]:
#     min_val = prices[idx+1]
#     max_profit += max(potential_options)
#     potential_options = []