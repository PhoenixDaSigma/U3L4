# Phoenix Valent
	# U3L4
		# Binary Search

# (◕_◕)    
#  ᑌ ᑌ ￣ᑌ     lucky cat had better things to do, lucky autism creature is taking her place

def binarySearch(target, nums, pointer = 0):
	if target in nums:
		midpoint = int(len(nums)/2)
		if nums[midpoint] != target:
			if nums[midpoint] > target:
				return binarySearch(target, nums[:midpoint], nums[:midpoint][0])
			elif nums[midpoint] < target:
				return binarySearch(target, nums[midpoint:], nums[midpoint:][0])
		else:
			return target-1 # so it returns the index
	else:
		return None

def main():
	nums = [x for x in range(1, 10)] # list comprehension B)

	test1 = binarySearch(2, nums)
	print("\n\nTest 1 - search for 2")
	print(f"Your returned index: {test1}")
	print(f"Test passed? {test1 == 1}\n\n")

	test2 = binarySearch(7, nums)
	print("Test 2 - search for 7")
	print(f"Your returned index: {test2}")
	print(f"Test passed? {test2 == 6}\n\n")

	test3 = binarySearch(9, nums)
	print("Test 3 - search for 9")
	print(f"Your returned index: {test3}")
	print(f"Test passed? {test3 == 8}\n\n")
    
	test4 = binarySearch(99, nums)
	print("Test 4 - number doesn't exist")
	print(f"Your returned index: {test4}")
	print(f"Test passed? {test4 == None}\n\n")

if __name__ == "__main__":
	main()