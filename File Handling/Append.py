# 'a' stands for APPEND (Add to the end)
site_file = open("Site Audit.txt", "a") 

site_file.write("Bricks = 4000.Rs\n")

site_file.close()

site_file = open("Site Audit.txt", "a") 
site_file.write("Bricks = 4000.Rs\n")
site_file.write("The Cost Of Today Is 4000.Rs\n")
site_file.close()