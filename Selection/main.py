from random import randrange
import time
import math

#PLEASE GO THROUGH README.txt first

##reads inpput file
def read_file(input) :
    array = []
    with open(input) as f:
        for line in f:
            #input file contains csv
            curr_line = line.split(',')
            for i in curr_line :
                j = float(i)
                array.append(j)
        return array
def create_output(algo, name, output, time_taken, pos) :
    file_name = algo + "_" + name
    with open(file_name, 'w') as f:
        f.write("Rank " + str(pos) + " element of " + name + ": " + output + "\n")
        f.write("Time taken = "+ str(time_taken))

#FOR RANDOM SELECT
def randomized_select(A, p , r, i) :
    if(p == r):
        return A[p]
    q = randomized_partition(A, p, r) #pivot
    # print("q = "+str(q))
    k = q-p+1
    # print("k = " + str(k))
    if(i == k):
        return A[q]
    elif(i < k):
        return randomized_select(A, p, q-1, i)
    else:
        return randomized_select(A, q+1, r, i-k)

def randomized_partition(A, p, r) :
    i = randrange(p, r)
    A[r], A[i] = A[i], A[r]
    return partition(A, p, r)

def partition(A, p, r) :
    x = A[r]
    i = p-1
    for j in range(p, r) :
        if(A[j] <= x) :
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1


def random_select(array, pos) :
    output = randomized_select(array, 0, len(array)-1, pos)
    # print("Rank " + str(pos) + " element of " + input + " = " + str(output))
    return output


#FOR DETERMINISTIC SELECTION

def insertion_sort(arr, start, end) :
    for i in range(start, end) :
        j = i
        while(j > 0 and arr[j-1] > arr[j]) :
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j-=1
    return arr

# def find_median(start, end) :
#     length = end-start
#     median_index = math.ceil(length/2) - 1
#     return median_index

def pivot_partition(arr, p, r, x) :
    pivot_index = -1
    for i in range (p, r) :
        if(arr[i] == x) :
            pivot_index = i
    if(pivot_index > 0) :
        arr[r], arr[pivot_index] = arr[pivot_index], arr[r]
    return partition(arr, p, r)
    
def select(A, p , r, i) :
    if(p==r) :
        return A[p]

    for x in range(p, r, 5) :
        insertion_sort(A, x, min(i+5, r))
        
    length = r-p+1
    total_meds = math.ceil(length/5)

    med_index = math.floor(total_meds/2)

    remainder = length%5
    if(remainder == 0) :
        remainder_index = 0
    else:
        remainder_index = math.ceil(remainder/2)
    
    if(total_meds == 1) :
        pivot = A[med_index]
    else :
        if(remainder_index > 0) :
            new_arr = A[p+2:r:5] + [A[-remainder_index]]
        else :
            new_arr = A[p+2:r:5]
        pivot = select(new_arr, 0, len(new_arr)-1, med_index)
    
    q = pivot_partition(A, p, r, pivot) #pivot
    k = q-p+1
    if(k == i):
        return A[q]
    elif(i < k):
        return select(A, p, q-1, i)
    else:
        return select(A, q+1, r, i-k)


def deter(input_array, pos) :
    output = select(input_array, 0, len(input_array)-1, pos)
    # print("Rank " + str(pos) + " element of " + input + " = " + str(output))
    return output

# CHECKER PROGRAM
def checker(arr, result, rank) :
    if(result not in arr): 
        return "Result not in input array"
    counter = -1
    for i in range(len(arr)) :
        if(arr[i] <= result) :
            counter += 1
    if((counter+1) == rank) :
        return True
    else :
        return False


def main() :
    input_name = str(input("Enter name of the input file: "))
    rank = int(input("Enter which smallest element you want to find: "))
    input_array = read_file(input_name)
    assert(rank <= len(input_array) and rank != 0), "Invalid Rank!"
    
    #change the range int he for loop below to obtain deter_selection average time from running n times
    deter_time = 0
    for i in range(1) :
        start_time = time.time()
        deter_result = deter(input_array, rank)
        deter_time += (time.time() - start_time)
    deter_time = deter_time/1

    create_output("deter", input_name, str(deter_result), deter_time, rank)

    #change the range int he for loop below to obtain random_selection average time from running n times
    rand_time = 0
    for i in range(1) :
        start_time = time.time()
        rand_result = random_select(input_array, rank)
        rand_time += (time.time() - start_time)
    rand_time = rand_time/1

    #To test if the checker works given the incorrect ith smallest, type an incorrect value for rand_result below
    # rand_result = <incorrect value>   
    create_output("random_", input_name, str(rand_result), rand_time, rank)
    #checker
    rand_algo = checker(input_array, rand_result, rank)
    deter_algo = checker(input_array, deter_result, rank)
    result_name = "result_" + input_name
    
    with open(result_name, 'w') as f:
        f.write("Random Selection gives <<" + str(rand_algo) + ">> result\n")
        f.write("Deterministic Selection gives <<" + str(deter_algo) + ">> result\n")
        f.write("Input size: " + str(len(input_array)))    

#The loop below was used to run multiple files at once for time analysis required in the report
# for i in range(30, 31) :
#     input_name = "input"+str(i)+".txt"
#     input_array = read_file(input_name)
#     main("input"+str(i)+".txt", input_array, randrange(1, len(input_array)))

main()
    



