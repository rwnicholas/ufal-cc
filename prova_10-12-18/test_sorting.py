# Python3 program for implementation of Shell Sort 

def shellSort(arr): 
	count = 0
	# Start with a big gap, then reduce the gap 
	n = len(arr) 
	gap = n//2

	# Do a gapped insertion sort for this gap size. 
	# The first gap elements a[0..gap-1] are already in gapped 
	# order keep adding one more element until the entire array 
	# is gap sorted 
	while gap > 0: 

		for i in range(gap,n): 

			# add a[i] to the elements that have been gap sorted 
			# save a[i] in temp and make a hole at position i 
			temp = arr[i] 

			# shift earlier gap-sorted elements up until the correct 
			# location for a[i] is found 
			j = i 
			while j >= gap and arr[j-gap] >temp: 
				count+=1
				arr[j] = arr[j-gap] 
				j -= gap 

			# put temp (the original a[i]) in its correct location 
			arr[j] = temp 
		gap //= 2
	print(count)


# Driver code to test above 
arr = [7,2,9,4,3,8,6,1,7,2,9,4,3,8,6,1,7,2,9,4,3,8,6,1,7,2,9,4,3,8,6,1,7,2,9,4,3,8,6,1,7,2,9,4,3,8,6,1,7,2,9,4,3,8,6,1,7,2,9,4,3,8,6,1,7,2,9,4,3,8,6,1]

n = len(arr)

shellSort(arr) 

print(arr)

# This code is contributed by Mohit Kumra 
