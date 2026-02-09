def the_material(material_site,*cost):
    total = sum(cost)
    return f"Bill for {material_site} is: Rs.{total}"
Total_bill = the_material("Cement and Concreate",2000,6000)
print(Total_bill)