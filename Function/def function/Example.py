def trip_total(train, hotel, food):
    total = train + hotel + food
    return total
result = trip_total(1500, 3000, 2000)
print(f"The total Darjeeling budget is: Rs.{result}")


def Material_total(fruit,flavor):
    juise_price = fruit + flavor
    return juise_price
liquid = Material_total(500,300)
print(f"the total cost of juise is Rs.{liquid}")

def AI_Prediction_Machine(data, weight):
    prediction = data * weight
    return prediction

final_result = AI_Prediction_Machine(0.85, 10)
print(f"The AI says: {final_result}")