With open("Material.txt","r") as material_file:
seek(10)
data = material_file.read(5)
print(data)