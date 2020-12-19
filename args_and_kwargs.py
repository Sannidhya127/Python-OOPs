# we will learn about *args and **kwargs here
# varname = input("tell us your name:\n")
# varrole = input("tell us your roll no:\n")
# varaddress = input("tell us your address:\n")

# if varrole == "\n":


def DetPrint(*args):
    # args[0] = varname
    if len(args) == 3:
        print("The name is", args[0], ".The roll no is ",
              args[1], "and the address is", args[2])
    elif len(args) == 2:
        print("The name is", args[0], ".The roll no is ", args[1])

    else:
        print("The name is", args[0])


DetPrint("Sannidhya Dasgupya")
