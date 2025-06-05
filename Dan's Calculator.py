def prompt():
    print("Please enter variables in desired order of operation")
    var1 = input("What is your first variable?\n")
    var2 = input("What is your second variable?\n")
    num_op = input("What is your operation? ( + - /  * % )\n")

    if num_op == "+":
        add = int(var1) + int(var2)
        print("\nYour output is " + str(add))
    if num_op == "-":
        sub = int(var1) + int(var2)
        print("\nYour output is " + str(sub))
    if num_op == "/":
        div = int(var1) / int(var2)
        print("\nYour output is " + str(div))
    if num_op == "*":
        mult = int(var1) * int(var2)
        print("\nYour output is " + str(mult))
    if num_op == "%":
        mod = int(var1) % int(var2)
        print("\nYour output is " + str(mod))
    else:
        prog = input("You just completed your first operation on this program! Would you like to input another "
                     "operation?\n")
        if prog.lower() == "yes":
            print("Sounds good!")
            prompt()
        elif prog.lower() == "no":
            print("Goodbye!")
            breakpoint()
print("Dan's Calculator\n")
print("Welcome user! This python built calculator takes two variables and 1 operation (so far)")
prompt()
