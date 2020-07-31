from decimal import * 

def run_timing():
    total = []
    while s := input("Enter 10 km run time: "):
        try:
            total.append(float(s))
        except ValueError as e:
            print("Enter a valid time.")
        
    print(f"Average of {sum(total)/len(total)}, over {len(total)} runs")

def beyond(*args):
    f , before , after = args
    new = str(f).split(".")
    return float(f"{new[0][-before:]}.{new[1][:after]}")

def exact():
    first = input("First decimal: ")
    second = input("Second decimal: ")
    return float(Decimal(first)+Decimal(second))

if __name__ == "__main__":
    # run_timing()
    print(beyond(1234.5678,2,3))
    print(exact())
