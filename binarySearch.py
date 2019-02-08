def binarySearch(data, target):
	    first = 0
	    last = len(data)-1
	    found = False
	
	    while first<=last and not found:
	        midpoint = (first + last)//2
	        if data[midpoint] == target:
	            found = True
	        else:
	            if target < data[midpoint]:
	                last = midpoint-1
	            else:
	                first = midpoint+1
	
	    return found
testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(testlist, 42))
print(binarySearch(testlist, 82))