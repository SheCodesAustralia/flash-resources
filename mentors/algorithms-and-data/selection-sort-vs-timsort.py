import time
import plotly.graph_objects as go

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

def sort_scores(values, method):
    start_time = time.time()
    if method == "selection":
        values = selection_sort(values)
    elif method == "timsort":
        values.sort()
    return time.time() - start_time

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


selection_times = []
timsort_times = []

for file_name in data_file_names:
    
    unsorted_scores_selection = []
    unsorted_scores_timsort = []
    
    with open(f"{file_name}.txt") as txt_file:
        for line in txt_file:
            unsorted_scores_selection.append(float(line))
            unsorted_scores_timsort.append(float(line))
    
    selection_time = sort_scores(unsorted_scores_selection, "selection")
    timsort_time = sort_scores(unsorted_scores_timsort, "timsort")

    selection_times.append(selection_time)
    timsort_times.append(timsort_time)
    
    print(file_name)
    print(TEMPLATE.format(algorithm="Selection Sort", time=selection_time))
    print(TEMPLATE.format(algorithm="Timsort", time=timsort_time))


list_size = ["10", "20", "30", "40", "50", "60", "70", "80", "90", "100"]
fig = go.Figure(data=[
    go.Bar(name="Selection Sort", x=list_size, y=selection_times),
    go.Bar(name="Timsort", x=list_size, y=timsort_times),

])
fig.show()
