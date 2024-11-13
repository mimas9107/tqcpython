# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 11:16:42 2024

@author: user
"""
def print_hollow_inverted_half_pyramid(rows):
    for i in range(rows, 0, -1): # i=7,6,5,4,3,2,1
        for j in range(rows - i): # j=7-7, 7-6, 7-5, 7-4,... ,7-0
            print(" ", end="")    # 縮排空格
        for j in range(i):        # j=0~6, 0~5, 0~4,... ,0~1
            if (j == 0 or j == i - 1 or i == rows) :
                print("*", end="")
            else:
                if(j==rows):
                    print("*" , end="")
        print()
        
# Example usage
num_rows = 7
print("Hollow Inverted Half Pyramid:")
print_hollow_inverted_half_pyramid(num_rows)