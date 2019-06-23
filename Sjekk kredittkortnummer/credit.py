# Port of credit program from C to Python
"""
What this program does:
"""
def main():
    # Prompt card number from.
    # Checks if the ccard starts with 34 or 37 and is x-digits long
    while True:
        ccard = "378282246310005"#input("Credit card nr.:")
        if len(ccard) == 15 and (ccard[:2] == "34" or ccard[:2] == "37"):
            break
        else:
            print("Invalid input")
    """
    The formula (Luhn's algorithm):
    0. Multiply ever oher digit by 2, startint with the number's second-to-last-digit,
       and then add those product's digits together
    1. Add the sum of the sum of the digits that weren't multiplied by 2.
    2. If the total's last digit is 0 (or, put more formally, if the total modulo 10 is congruent to 0),
       the number is valid!
    """
    # 0. Multiplying every other digit and adding the product's digits together
    # --Multypling the digits--
    def multiply():
        index = 1
        multiply.product = ""
        for i in range(7):
            x = int(ccard[index]) * 2
            multiply.product += str(x)
            index += 2
    multiply()
    # --Adding the digit's of the products--
    def addition():
        addition.total = 0
        index = 0
        for i in range(len(multiply.product)):
            addition.total += int(multiply.product[index])
            index += 1
    addition()

    # 1. Adding the digits that were not multiplied
    def addition2():
        index = 0
        addition2.total = 0
        for i in range(8):
            addition2.total += int(ccard[index])
            index += 2
    addition2()

    # 2. Check if the number is valid
    def check():
        if (addition.total + addition2.total) % 10 == 0:
            return True
        else:
            return False
    check()

    print(
        "Credit card number entered:", ccard, "\n"
        "The sum of the digits of every other product:", addition.total, "\n"
        "The sum of the other digits:", addition2.total, "\n"
        "The sum of the above two:", addition.total + addition2.total, "\n"
        "The credit card is:", check()
        )

if __name__ == "__main__":
    main()
