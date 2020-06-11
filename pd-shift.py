# Alexandros' Tuition Python Tutorial
# Pandas shift() Function
# Slides: Instagram @azurewill
# https://www.instagram.com/p/CBQ3l5ug0ir/
# Code: GitHub @lxndroc
# https://github.com/lxndroc/Instagram-Python-Tutorials/blob/master/pd-shift.py
# Video: YouTube Alexandros' Tuition
# https://https://youtu.be/gYFse-eNPS8

# Slide 1 - Pandas shift() Function - What Can It Do?
# Easily shift rows or columns of a DataFrame

# Slide 2 - Why?
# Perform calculations or return to a previous state

# Slide 3 - A Sample DataFrame
import pandas as pd

df = pd.DataFrame({
    'Date': [1, 2, 3, 4, 5],
    'Volume': [1, 2, 3, 4, 5],
    'Price': [34, 61, 202, 108, 96]
})
#print(df)
'''
   Date  Volume  Price
0     1       1     34
1     2       2     61
2     3       3    202
3     4       4    108
4     5       5     96
'''
# Slide 4 - A New First Row With Zeros - How?
# Shifting all rows 1 row down
#print(df.shift(1, fill_value=0))
'''
   Date  Volume  Price
0     0       0      0
1     1       1     34
2     2       2     61
3     3       3    202
4     4       4    108
'''
# Slide 5 - A New Column With The Previous Values Of Another Column - How?
# Shifting 'Price' column 1 column right
df['Prev_price'] = df['Price'].shift(1, fill_value=0)
print(df)
'''
   Date  Volume  Price  Prev_price
0     1       1     34           0
1     2       2     61          34
2     3       3    202          61
3     4       4    108         202
4     5       5     96         108
'''