colleges = ["Caltech", "UCLA", "Stanford", "UC Fullerton", "UC Berkley"]

def addcol(colleges):
    colleges.append(new_col)
    return colleges
    
def delcol(colleges):
    colleges.remove(app)
    return colleges

y_n = input("Would you like to update your list? (y/n) ")
while y_n == "y":
    edit = input("Do you want to add or remove from your list? (a/r) ")
    if edit == "a":
        new_col = input("What is the name of the new college/university? ")
        addcol(colleges)
        y_n = input("Would you like to update your list? (y/n) ")
    else:
        app = input("What college university have you finished applying to? ")
        if app not in colleges:
            print("Error: That item is not in your list.")
        else:
            delcol(colleges)
            y_n = input("Would you like to update your list? (y/n) ")

print("Colleges you still need to apply to: ", colleges)