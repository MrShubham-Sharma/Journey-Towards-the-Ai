# 1. THE MANUAL: We tell the worker how to use the logbook
def site_audit(**expenses):
    print("---- Bill Items -----")
    # 'expenses' is now the Logbook: {'Cement': 2000, 'Sand': 1500}
    for name, cost in expenses.items():
        print(f"{name} Rs.{cost}")
    total = sum(expenses.values()) 
    # The worker adds 2000 + 1500 = 3500.
    
    print("---------------")
    return total # The worker walks out of the office with the number 3500.
# 2. THE TRIGGER: We fill the logbook
result = site_audit(Cement=2000, Sand=1500)
print(f"The Total expence for all Material is :{result}")