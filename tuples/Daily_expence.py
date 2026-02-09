def the_Station(station,budget,*cost):
    total = sum(cost)
    if total > budget:
        status = " OVER BUDGET!"
    else:
        status = " Within Budget"
        
    return f"Bill for {station}: Rs.{total} | Status: {status}"
station_bill = the_Station("Mumbai Station", 500, 20, 15, 20)
print(station_bill)