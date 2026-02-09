def safe_split(amount, people):
    try:
        share = amount / people
        return f"Each person pays: Rs.{share}"
    except ZeroDivisionError:
        return " Error: You can't split a bill with 0 people!"
    except TypeError:
        return " Error: Please enter numbers only (no words)!"

# Test both scenarios before committing
print(safe_split(5000, 5))    # Normal
print(safe_split(5000, 0))    # Zero Error
print(safe_split(5000, "4"))  # Type Error