TEMPLATE = '{algorithm:>18} {time:.10f}'

def selection_sort(values):
    for index in range(len(values)): 
        # Find the minimum element in remaining unsorted array 
        min_index = index
        for unsorted_array_index in range(index+1, len(values)): 
            if values[min_index] > values[unsorted_array_index]: 
                min_index = unsorted_array_index
        # Swap the found minimum element with the first element         
        values[index], values[min_index] = values[min_index], values[index] 
    return values


data_file_names = [
    "exam-results-10",
    "exam-results-20",
    "exam-results-30",
    "exam-results-40",
    "exam-results-50",
    "exam-results-60",
    "exam-results-70",
    "exam-results-80",
    "exam-results-90",
    "exam-results-100"
]


unsorted_scores_selection = []
unsorted_scores_timsort = []
with open("exam-results-10.txt") as txt_file:
    for line in txt_file:
        unsorted_scores_selection.append(float(line))
        unsorted_scores_timsort.append(float(line))
