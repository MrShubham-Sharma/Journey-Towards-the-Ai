SGPA =[8.5, 0.0, 9.2, 0.0, 7.8]
while 0.0 in SGPA:
    print(" we found the Error Value Which Was Removed")
    SGPA.remove(0.0)
print(f"The Corection SGPA after are {SGPA} ")


scores = [8.5, 0.0, 9.2, 0.0, 7.8]

# Translated: "Keep 's' for every 's' in scores if 's' is not 0.0"
clean_scores = [s for s in scores if s != 0.0]

print(clean_scores)