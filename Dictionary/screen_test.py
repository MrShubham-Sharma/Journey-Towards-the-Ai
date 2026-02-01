def check_placement_status(score):
    if score >= 40:
        return "Eligible for Interview"
    elif score >= 15:
        return "Waitlisted for Round 2"
    else:
        return "Try again next drive"

# Test it with your recent score
print(f"Status: {check_placement_status(14)}")