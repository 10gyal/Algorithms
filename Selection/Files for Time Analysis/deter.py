def insertion_sort(arr, start, end) :
    for i in range(start, end) :
        j = i
        while(j > 0 and arr[j-1] > arr[j]) :
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j-=1
    return arr

def find_median(start, end) :
    length = end-start
    median_index = math.ceil(length/2) - 1
    return median_index

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
    #check for invalid pos


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


def deter(input, pos) :
    input_array = read_file(input)
    assert(pos != 0 and pos <= len(input_array)), "Invalid Rank"
    output = select(input_array, 0, len(input_array)-1, pos)
    print("Rank " + str(pos) + " element of " + input + " = " + str(output))
    return output

start_time = time.time()  
for i in range(1, 15) :
    deter("input1.txt", i)
print(time.time()-start_time)


