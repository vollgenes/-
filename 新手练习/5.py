temperature_list = [36.4, 36.5, 35.6, 38.4, 36.7, 36.5, 37.9, 36.1, 37.2]
for temperature in temperature_list:
    if temperature >= 38:
        print(temperature)
        print("完球了")
temperature_dict = {"1": 36.4, "2": 36.5, "3": 35.6, "4": 38.4, "5": 36.7, "6": 36.5, "7": 37.9, "8": 36.1, "9": 37.2}
for staff_id, temperature in temperature_dict.items():
    if temperature >= 38:
        print(staff_id)
temperature_dict = {"1": 36.4, "2": 36.5, "3": 35.6, "4": 38.4, "5": 36.7, "6": 36.5, "7": 37.9, "8": 36.1, "9": 37.2}
for temperature_tuple in temperature_dict.items():
    staff_id = temperature_tuple[0]
    temperature = temperature_tuple[1]
    if temperature >= 38:
        print(staff_id)
total = 0
for i in range(1, 101):
    total = total + i
    print(total)
