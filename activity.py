#Andrew Eppinger
#CS 325 Fall 2020
#Homework #4 Problem #4

content_list = []                   #Var to store the each line of the act.text file
cases = []           #Var to store the numbers from each line after they're converted to ints
text_file = open('act.txt', 'r')
input = []

for line in text_file:              #Iterates through each line of the text file, storing each line in a list
    line = line.split(' ')
    content_list.append(line)

for line in content_list:           #Iterates through the list of lines, converts each number from a str to an int
    for i in range(len(line)):
        line[i] = int(line[i])

for list in content_list:           #The following code breaks up the input file into individual test cases
    input.append(list)

for data in content_list:
    while len(content_list) > 0:
        individual_case = []
        length = content_list[0][0]
        content_list = content_list[1:]
        while length > 0:
            individual_case.append(content_list[0])
            content_list = content_list[1:]
            length -= 1
        cases.append(individual_case)

def mergeSort(arr, key= lambda x : x):  #This merge sort code came from assignment #1.
    '''
    This function is used to sort start times from greatest to least. The key is used to facilitate the sorting of
    tuples, which was necessary to sort the finish times that correspond to the start times.
    '''

    if len(arr) > 1:            #Continues to split the list in half until there is only one element left
        mid = len(arr) // 2     #Finds the mid-point of the list
        L = arr[:mid]           #Allocates the left-portion to the variable L
        R = arr[mid:]           #Allocates the right-portion to the variable R
        mergeSort(L)            #Runs mergeSort again on the left and right halves
        mergeSort(R)
        i = j = k = 0           #Sets all vars to be used for sorting equal to 0

        while i < len(L) and j < len(R):
            if L[i] > R[j]:                 #Compares elements from the left and right halves
                arr[k] = L[i]               #sets the i'th ele equal to the larger of the two
                i += 1                      #Continues to the next index
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):               #Checks to see if any elements remain in the left and right havles.
            arr[k] = L[i]               #If so, the element(s) are assigned to the array.
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

def greedy_actvity_selector(start_times,finish_times):
    '''
    Sorts activities by selecting the last activity to start that is compatible with all previously selected
    activities using the greedy method. Modified 'Greedy-Activity_Selector' code from ch. 16.1  of the textbook.
    '''

    n = len(start_times)
    A = [a_dict[finish_times[0]]]   #Last activity always selected
    k = 0

    for m in range(n):
        if start_times[k] >= finish_times[m]:   #Iterates once through the list and checks the kth start time against
            A.append(a_dict[finish_times[m]])   #the mth finish time.
            k = m
    A.reverse()
    return A


output = []             #The following code iterates through each case, sorts one at a time, and calls the greedy
for case in cases:         #function on each.
    activity_list = []
    start_list = []
    finish_list = []
    for activity in case:
        activity_list.append(activity[0])
        start_list.append(activity[1])
        finish_list.append(activity[2])
    finish_dict = {activity_list[i]: finish_list[i] for i in range(len(finish_list))}   #Dictionaries are used to keep
    a_dict = {finish_list[i]: activity_list[i] for i in range(len(finish_list))}        #track of activity numbers and
    tuple_list = [(start_list[i], activity_list[i]) for i in range(0, len(activity_list))]#finish times after sorting
    mergeSort(tuple_list)
    sorted_finish_times = []
    sorted_start_times = []
    for tup in tuple_list:
        sorted_finish_times.append(finish_dict[tup[1]])
        sorted_start_times.append(tup[0])
    output.append(greedy_actvity_selector(sorted_start_times,sorted_finish_times))

act_output = ''             #The following code is used to output the results from the greedy function. All results
cases_length = len(output)  #are output to act.out.
case_conter = 1
while cases_length > 0:
    for case in output:
        act_count = str(len(case))
        act_output = act_output + 'Set ' + str(case_conter) +'\n' + 'Number of activities selected = ' + act_count +'\n'
        act_output = act_output + 'Activities: '
        for num in case:
            act_output = act_output + str(num) + ' '
        act_output = act_output +'\n' + '\n'
        case_conter += 1
        cases_length -= 1

print(act_output)
act_out = open('act.out','w')
act_out.write(act_output)
act_out.close()
text_file.close()
