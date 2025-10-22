# Program: Customer Feedback Percentage Calculator

def feedback_summary(rating_list):
    """Calculates positive feedback percentage."""
    if len(rating_list) == 0:
        return "No feedback received."
    positives = sum(1 for r in rating_list if r >= 4)
    percent = (positives / len(rating_list)) * 100
    return round(percent, 2)

# Example run
feedback = [5, 4, 3, 5, 2, 4, 1, 5]
print(f"Positive Feedback Score: {feedback_summary(feedback)}%")
