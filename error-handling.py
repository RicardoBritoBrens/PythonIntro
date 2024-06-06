# 

# def main():
#     open('/path/to/mars.jpg')

# if __name__ == '__main__':
#     main()
    
# def main():
#     try:
#         configuration = open('config.txt')
#     except FileNotFoundError:
#         print("Couldn't find the config.txt file!")

# if __name__ == '__main__':
#     main()

def water_left(astronauts, water_left, days_left):
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    if total_water_left < 0:
        raise RuntimeError(f"There is not enough water for {astronauts} astronauts after {days_left} days!")
    return f"Total water left after {days_left} days is: {total_water_left} liters"

try:
    output = water_left(5, 100, 2)
except RuntimeError as err:
    alert_navigation_system(err)
print(output)