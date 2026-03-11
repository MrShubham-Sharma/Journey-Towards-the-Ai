sample_text = "  python_programming_2026  "

# 1. Strip whitespace and convert to upper case
clean_text = sample_text.strip().upper()

# 2. Extract only the year (last 4 characters)
year_only = clean_text[-4:]

# 3. Reverse only the 'PYTHON' part (first 6 characters)
reversed_start = clean_text[:6][::-1]

print(f"Full Cleaned Text: {clean_text}")
print(f"Extracted Year: {year_only}")
print(f"Reversed Prefix: {reversed_start}")