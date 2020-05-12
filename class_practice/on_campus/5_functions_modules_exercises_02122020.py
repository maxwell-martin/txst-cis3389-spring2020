# Exercise 1
def check_pos_neg(a):
    if a > 0:
        return "positive"
    elif a == 0:
        return "zero"
    else:
        return "negative"

def main():
    a = int(input("Enter a number: "))
    n = check_pos_neg(a)
    print(n)

main()


# Exercise 3
def main():
    number = int(input("Enter a number: "))
    lower = int(input("Enter lower limit: "))
    upper = int(input("Enter upper limit: "))
    check_inrange(number, lower, upper)

def check_inrange(number, lower, upper):
    if number in range(lower, upper + 1):
        print("In range")
    else:
        print("Not in range")

main()


# Exercise 4 and 5
import random

HOTEL_COST_PER_NIGHT = 130
RENTAL_CAR_COST_PER_DAY = 60

def get_hotel_cost(nights):
    return nights * HOTEL_COST_PER_NIGHT

def get_flight_fare(location):
    if location.lower() == "dallas":
        return 183
    elif location.lower() == "gainesville":
        return 220
    elif location.lower() == "chicago":
        return 222
    elif location.lower() == "los angeles":
        return 475
    elif location.lower() == "new york":
        return 385
    elif location.lower() == "san francisco":
        return 440
    else:
        return "Not a correct city"

def get_rental_car_cost(days):
    car_cost = days * RENTAL_CAR_COST_PER_DAY
    if days >= 7:
        return car_cost - RENTAL_CAR_COST_PER_DAY
    elif days >= 3:
        return car_cost - RENTAL_CAR_COST_PER_DAY / 2
    else:
        return car_cost

def get_total_cost(nights, location, days):
    return get_hotel_cost(nights) + get_flight_fare(location) + get_rental_car_cost(days)

def check_budget(budget, total_cost):
    if budget > total_cost:
        return "Under budget"
    elif budget == total_cost:
        return "Equal to budget"
    else:
        return "Over budget"

def main():
    nights = int(input("Enter number of hotel nights: "))
    location = input("Enter location: ")
    days = int(input("Enter number of days to rent car: "))
    #budget = float(input("Enter budget: "))
    budget = random.randint(1500, 2000)
    print("Hotel cost: $", get_hotel_cost(nights), sep="")
    print("Flight cost: $", get_flight_fare(location), sep="")
    print("Rental car cost: $", get_rental_car_cost(days), sep="")
    print("Total cost: $", get_total_cost(nights, location, days), sep="")
    print("Budget is: $", budget)
    print("Budget information:", check_budget(budget, get_total_cost(nights, location, days)))
    
main()


# Exercise 6
import random

def is_negative(number):
    if number < 0:
        return True
    else:
        return False

def generate_count(lower, upper, total_numbers):
    count = 0
    for i in range(total_numbers):
        number = random.randint(lower, upper)
        print(number)
        if is_negative(number):
            count += 1
    return count

def main():
    count = generate_count(-100, 500, 30)
    print("Total negative numbers: ", count)

main()
