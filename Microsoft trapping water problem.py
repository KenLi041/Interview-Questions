#This trapping rain water problem is from Microsoft online assessment May 2021
#An element of the array can store water if there are higher bars on the left and the right. 
#The amount of water to be stored in every position can be found by finding the heights of bars on the left and right sides. 
#The total amount of water stored is the summation of the water stored in each index.
#For example – Consider the array arr[] = {3, 0, 2, 0, 4}. 
#Three units of water can be stored in two indexes 1 and 3, and one unit of water at index 2.

#1. Brute force solution: Traverse the array from start to that index and find the maximum height (a) and 
#Traverse the array from the current index to the end, and find the maximum height (b).
#The amount of water that will be stored in this column is min(a,b) – array[i], add this value to the total amount of water stored
def totalwater(array, n):
    answer = 0
    for i in range(1, n-1): #traverse array
        left = array[i]
        for j in range(i):
            left = max(left, array[j]) #find the max height on the index's left
  
        right = arr[i]
        for j in range(i + 1, n): #same logic
            right = max(right, arr[j])
  
        # calculate max water trapped, 关键要想到这个公式
        answer = answer + (min(left, right) - array[i])#该index i左右相2高中相对矮的-该index value which is height因每个宽度都是1 so 1 index储存的就是高度差
  
    return answer

#记得时空复杂度O(N^2) because nested loops for i...for j...    Space complexity O(1) no extra space needed
#记住for(...)是O(N), for里有for就是O(N^2), so O(N^3)就是3层for loop

#Better solution using stack with O(N) and O(N)!
#Loop while the Stack is not empty and the current bar has a height greater than the top bar of the stack,
#Store the index of the top bar in pop_height and pop it from the Stack.
#Find the distance between the left bar(current top) of the popped bar and the current bar.
#Find the minimum height between the top bar and the current bar.
#The maximum water that can be trapped is distance * min_height.
#The water trapped, including the popped bar, is (distance * min_height) – height[pop_height].
#Add that to the answer.

def maxWater(height):
    answer = 0

    # make stack for bars
    bars = []
    
    # get size of given height array
    n = len(height)
    
    
    for i in range(n):
        
        # Remove bars from the stack
        # until the condition holds
        while(len(bars) != 0 and (height[bars[-1]] < height[i])):
            
            # store the height of the top & pop.
            pop_height = height[bars[-1]]
            bars.pop()
            
            #If no bar in stack, means reaching most left
            if(len(bars) == 0):
                break
            
            #find distance between left and right boundary of popped bar
            distance = i - bars[-1] - 1
            
            # Calculate min
            min_height = min(height[bars[-1]], height[i])-pop_height
            
            answer += distance * min_height
        
        # If stack empty / current bar height less/equal to the top bar of stack
        stack.append(i)
    
    return answer
