#used for iterating over a list and access each item individually

nums = [1,2,3,4,5,6,7,8,9,0]

for items in nums: #items is a loop variable that holds one value of elements in the nums variable
    print(items)

#use can also use while loops but the code will be longer
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

i = 0
while i < len(letters): #checks if i is less than the length of the letters list
    print(letters[i]) #outputs the letter at each index of i
    i = i + 1 #increments the index by 1