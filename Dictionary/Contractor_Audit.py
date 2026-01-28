material_costs ={"Cement": 450,"Sand": 800,"Tiels":1000}
# The price of Cement just went up!
material_costs["Cement"] = 500 # Now it prints 500, not 450

# take an input 
material = input(f"which cost of material do you want to kmow? (Cement,Sand,Tiels)")

# .get use for check the material clearly if it's not there then it will show material is not found !
result = material_costs.get(material, "material is not found !")
print(result)