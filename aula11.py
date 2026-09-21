numA = int(input("numero A: "))
numB = int(input("numero B: "))
if numA < numB:
    numA, numB = numB, numA

while numB != 0:
    resto = numA % numB
    numA = numB 
    numB = resto

print(f"MDC = {numA}") 

# MMC ()
    
   