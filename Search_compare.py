#David Vayman
#search_compare.py
import time
import random
def main():
	def sequential_search(a_list,item):
		time_start = time.time()
		pos = 0
		found = False
		
		while pos < len(a_list) and not found:
			if a_list[pos] == item:
				found = True
			else:
				pos = pos + 1
		time_end = time.time()
		return (found, time_end - time_start)
		



	def ordered_sequential_search(a_list, item):
		time_start = time.time()
		pos = 0
		found = False
		stop = False
		while pos < len(a_list) and not found and not stop:
			if a_list[pos] == item:
				found = True
			else:
				if a_list[pos] > item:
					stop = True
				else: 
					pos = pos + 1
		time_end = time.time()
		return (found, time_end - time_start)



	def binary_search_iterative(a_list, item):
		time_start = time.time()
		first = 0
		last = len(a_list) - 1
		found = False
		
		while first <= last and not found:
			midpoint = (first + last) // 2
			if a_list[midpoint] == item:
				found = True
			else:
				if item < a_list[midpoint]:
					last = midpoint - 1
				else:
					first = midpoint + 1
		time_end = time.time()
		return (found, time_end - time_start)
		
		
		
	def binary_search_recursive(a_list, item):
		time_start = time.time()
		if len(a_list) == 0:
			time_end = time.time()
			return (False, time_end - time_start)
		else:
			midpoint = len(a_list) // 2
		if a_list[midpoint] == item:
			time_end = time.time()
			return (True, time_end - time_start)
		else:
			if item < a_list[midpoint]:
				return binary_search_recursive(a_list[:midpoint], item)
			else:
				return binary_search_recursive(a_list[midpoint + 1:], item)
				

	input_list_500 = []
	input_list_1k = []
	input_list_10k = []

	sq_outputs_500 = []
	sq_outputs_1k = []
	sq_outputs_10k = []

	osq_outputs_500 = []
	osq_outputs_1k = []
	osq_outputs_10k = []

	bsi_outputs_500 = []
	bsi_outputs_1k = []
	bsi_outputs_10k = []

	bsr_outputs_500 = []
	bsr_outputs_1k = []
	bsr_outputs_10k = []
				
	for i in xrange(100):
		for y in xrange(500):
			input_list_500.append(random.random() * 1000)
		for q in xrange(1000):
			input_list_1k.append(random.random() * 5000)
		for p in xrange (10000):
			input_list_10k.append(random.random() * 100000)
		## Sequential Search Outputs
		sq_outputs_500.append(sequential_search(input_list_500,-1)[1])
		sq_outputs_1k.append(sequential_search(input_list_1k,-1)[1])
		sq_outputs_10k.append(sequential_search(input_list_10k,-1)[1])
		## Sorting Lists for Sequential/Binary Searches
		input_list_500.sort()
		input_list_1k.sort()
		input_list_10k.sort()
		## Ordered Sequential Search Outputs
		osq_outputs_500.append(ordered_sequential_search(input_list_500,-1)[1])
		osq_outputs_1k.append(ordered_sequential_search(input_list_1k,-1)[1])
		osq_outputs_10k.append(ordered_sequential_search(input_list_10k,-1)[1])
		## Binary Search Iterative Outputs
		bsi_outputs_500.append(binary_search_iterative(input_list_500,-1)[1])
		bsi_outputs_1k.append(binary_search_iterative(input_list_1k,-1)[1])
		bsi_outputs_10k.append(binary_search_iterative(input_list_10k,-1)[1])
		## Binary Search Recursive Outputs
		bsr_outputs_500.append(binary_search_recursive(input_list_500,-1)[1])
		bsr_outputs_1k.append(binary_search_recursive(input_list_1k,-1)[1])
		bsr_outputs_10k.append(binary_search_recursive(input_list_10k,-1)[1])	
		
	# Computing Averages for Outputs
	sq_average_500 = sum(sq_outputs_500) / float(len(sq_outputs_500))
	sq_average_1k = sum(sq_outputs_1k) / float(len(sq_outputs_1k))
	sq_average_10k = sum(sq_outputs_10k) / float(len(sq_outputs_10k))

	osq_average_500 = sum(osq_outputs_500) / float(len(osq_outputs_500))
	osq_average_1k = sum(osq_outputs_1k) / float(len(osq_outputs_1k))
	osq_average_10k = sum(osq_outputs_10k) / float(len(osq_outputs_10k))

	bsi_average_500 = sum(bsi_outputs_500) / float(len(bsi_outputs_500))
	bsi_average_1k = sum(bsi_outputs_1k) / float(len(bsi_outputs_1k))
	bsi_average_10k = sum(bsi_outputs_500) / float(len(bsi_outputs_10k))

	bsr_average_500 = sum(bsr_outputs_500) / float(len(bsr_outputs_500))
	bsr_average_1k = sum(bsr_outputs_1k) / float(len(bsr_outputs_1k))
	bsr_average_10k = sum(bsr_outputs_500) / float(len(bsr_outputs_10k))

	# Printing Outputs

	print "Sequential Search took %10.7f seconds, on average, to run over a list of length 500" % sq_average_500
	print "Sequential Search took %10.7f seconds, on average, to run over a list of length 1000" % sq_average_1k
	print "Sequential Search took %10.7f seconds, on average, to run over a list of length 10000" % sq_average_10k
	print "\n"
	print "Ordered Sequential Search took %10.7f seconds, on average, to run over a list of length 500" % osq_average_500
	print "Ordered Sequential Search took %10.7f seconds, on average, to run over a list of length 1000" % osq_average_1k
	print "Ordered Sequential Search took %10.7f seconds, on average, to run over a list of length 10000" % osq_average_10k
	print "\n"
	print "Binary Search Iterative took %10.7f seconds, on average, to run over a list of length 500" % bsi_average_500
	print "Binary Search Iterative took %10.7f seconds, on average, to run over a list of length 1000" % bsi_average_1k
	print "Binary Search Iterative took %10.7f seconds, on average, to run over a list of length 10000" % bsi_average_10k
	print "\n"
	print "Binary Search Recursive took %10.7f seconds, on average, to run over a list of length 500" % bsr_average_500
	print "Binary Search Recursive took %10.7f seconds, on average, to run over a list of length 1000" % bsr_average_1k
	print "Binary Search Recursive took %10.7f seconds, on average, to run over a list of length 10000" % bsr_average_10k

main()
