public = ["UCLA", "UCSD", "UC Fullerton", "UC Berkley"]
private = {"Stanford", "Caltech","USC"}

def addcol(public, private):
    y_n = input("Would you like to add a college to the list? (y/n)")
    if y_n == "y":
        new_col = input("What is the name of the new college? ")
        col_type = input("Is this college 1) public or 2) private? ")
        if col_type == "1":
            public[new_col] = 1
            print("Here are your public colleges: ", public )
        elif col_type == "2":
            private[new_col] = 2
            print("Here are your public colleges: ", )
addcol()