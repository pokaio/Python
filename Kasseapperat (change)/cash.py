# Port of the cash program from C to Python
def main():
    # Prompt input from user for amount of change
    while True:
        received = float(input("Change: ")) * 100
        if received > 0:
            break
        else:
            print("Invalid input")
    # Calculate change, 50c, 25c, 10c & 1c
    half = 0
    quarts = 0
    tens = 0
    ones = 0
    while received >= 50:
        received -= 50
        half += 1
    while received >= 25:
        received -= 25
        quarts += 1
    while received >= 10:
        received -= 10
        tens += 1
    while received >= 1:
        received -= 1
        ones += 1
    print(f"Halves:{half}")
    print(f"Quarts:{quarts}")
    print(f"Tens:{tens}")
    print(f"Ones:{ones}")
    print(f"Coins: {half + quarts + tens + ones}")

if __name__ == "__main__":
    main()
