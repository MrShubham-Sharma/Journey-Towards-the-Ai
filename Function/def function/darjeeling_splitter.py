def Total_bill(hotel_rent,number_of_friends ):
    tax = hotel_rent * 12 /100
    splited_bill = (hotel_rent + tax) / number_of_friends
    return splited_bill
Per_head_contry = Total_bill(1400,4)
print(f"the Split ammount per person is MRP.Rs.{Per_head_contry:.2f}")