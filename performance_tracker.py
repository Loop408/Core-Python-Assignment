# Program: Student Performance Tracker

def average_scores(data):
    """Calculates each student's average marks."""
    result = {}
    for name, marks in data.items():
        result[name] = round(sum(marks) / len(marks), 2)
    return result

def best_student(avg_dict):
    """Finds the student with maximum average."""
    top = max(avg_dict, key=lambda x: avg_dict[x])
    return top

# Example run
marks_data = {"John": [85, 78, 92], "Alice": [88, 79, 95], "Bob": [70, 75, 80]}
avg = average_scores(marks_data)
print("Student Averages:", avg)
print("Best Performer:", best_student(avg))
