letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","x","y","z","w"]
nums = ["0","1","2","3","4","5","6","7","8","9"]

def process_desc(description):

    description_lower = description.lower()   # Everything to lowercase
    
    for char in ["_","-", ",",")","(","[","]","/",";"]:        #Replace "_","-", ",",")","(","[","]","/",";" with a space
        description_lower = description_lower.replace(char, " ")


    for char_num in range(len(description_lower)-1):  #if a letter next to a number is found, add a space between
        if description_lower[char_num+1] in letters and description_lower[char_num] in nums:
            left = description_lower[0:char_num+1]
            right = description_lower[char_num+1:]
            
            description_lower = left + " " + right


    for char_num in range(len(description_lower)-1):    #if a number next to a letter is found, add a space between
        if description_lower[char_num+1] in nums and description_lower[char_num] in letters:
            left = description_lower[0:char_num+1]
            right = description_lower[char_num+1:]
            
            description_lower = left + " " + right

    for char_num in range(len(description_lower)-1): #if a point is between two letters, replace with a space
        if description_lower[char_num-1] in letters and description_lower[char_num+1] in letters and description_lower[char_num] == ".":
            left = description_lower[0:char_num]
            right = description_lower[char_num+1:]

            description_lower = left+ " " + right


    return description_lower