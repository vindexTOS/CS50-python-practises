val =  input("Change: ") 


cents = [1,5,10,25][::-1]




 
 

newVal = ""

  
while val.isalpha() or len(val)  <= 0:
    val = input("Change: ")

if val[0] == "0":
    val = val[1:]

hasDot = False

for char in val:
    if char == ".":
        hasDot = True
        break

for char in val:
    if char.isdigit() or (char == "." and not hasDot):
        newVal += char

if "." in newVal:
    newVal = int(float(newVal) * 100)  
else:
    newVal = int(newVal) * 100   

    



index =0
result =0
newVal = int(newVal)
while True:   
    
    if index > 3 or index < 0:
        index += 1
    
    if newVal >= cents[index]:
        
        newVal -= cents[index]
         
        index -= 1
        result += 1

    else:
        index+=1
        
    if newVal == 0:
        break


 
        
        
 

 
print (result)