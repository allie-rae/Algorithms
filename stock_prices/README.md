# Stock Prices

You want to write a bot that will automate the task of day-trading for you while you're going through Lambda. You decide to have your bot just focus on buying and selling Amazon stock. 

Write a function `find_max_profit` that receives as input a list of stock prices. Your function should return the maximum profit that can be made from a single buy and sell. You must buy first before selling; no shorting is allowed here.

For example, `find_max_profit([1050, 270, 1540, 3800, 2])` should return 3530, which is the maximum profit that can be made from a single buy and then sell of these stock prices. 

## Testing

Run the test file by executing `python test_stock_prices.py`.

You can also test your implementation manually by executing `python stock_prices.py [integers_separated_by_a_single_space]`

## Hints

 For this problem, we essentially want to find the maximum difference between the smallest and largest prices in the list of prices, but we also have to make sure that the max profit is computed by subtracting some price by another price that comes _before_ it; it can't come after it in the list of prices. 

 So what if we kept track of the `current_min_price_so_far` and the `max_profit_so_far`? 

 # Function takes an array of stock prices
 # Function finds the max num in the array
 # Function finds the min num in the array that is to the left of the max num
 # Function subtracts min num from max num
 # Function returns new num from the above subtraction, which is max profit 

 # Q: What if the max num is the leftmost num? 
 # A: Then we would have to search for the next largest num 

 # Q: What if the array goes [maxnum, secondlargestnum]? 
 # A: We have to find the largest num that has a SMALLER num before it somewhere in the array

 # Q: What if there is no num that has a smaller num to the left? 
 # A: Find the minimum loss.

 # Rethink...
 # Function subtracts each num to the left from each num in the array
 # Function returns largest num


# [1050, 270, 1540, 3800, 2]
# hint: `current_min_price_so_far` and `max_profit_so_far`

 # Example:
 # def (arr)
 #      for current_index in arr:
            
 #         if current_index > 1:
 #              subtract arr[current_index] from each element to the left
 #              return max_profit_so_far
 #              