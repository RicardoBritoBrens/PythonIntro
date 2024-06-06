# function with no arguments
#def rocket_parts():
    #return 'payload, propellant, structure'        
# output = rocket_parts()
# print(output)
# print(str(rocket_parts))

# function with a single arguments
# def distance_from_earth(destination):
#     if destination == 'Moon':
#         return '238,855'
#     else:
#         return 'Unable to compute to that destination'
# print(distance_from_earth('Moon'))
# print(distance_from_earth('Earth'))

# # function with multiple arguments
# def days_to_complete(distance, speed):
#     hours = distance/speed
#     return hours/24
# # print(str(days_to_complete(238855, 75)))

# total_days = days_to_complete(238855, 75)
# print(str(round(total_days)))

# from datetime import timedelta, datetime

# def arrival_time(destination, hours=51):
#     now = datetime.now()
#     arrival = now + timedelta(hours=hours)
#     return arrival.strftime(f"{destination} Arrival: %A %H:%M")

# print(arrival_time('Orbit', 0.13))

# def sequence_time(*args):
#     total_minutes = sum(args)
#     if total_minutes < 60:
#         return f"Total time to launch is {total_minutes} minutes"
#     else:
#         return f"Total time to launch is {total_minutes/60} hours"
    
# print(sequence_time(4,14,18,20,25,80,90,100,150,250))