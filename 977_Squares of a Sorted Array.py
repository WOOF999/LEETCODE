def sortedSquares(nums):
    squares=list()
    for number in nums:
        squares.append(number*number)
    squares.sort()
    return squares

nums=[-4,-1,0,3,10]
print(sortedSquares(nums))


