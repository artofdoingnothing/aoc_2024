import random

def read_and_parse_from_file(file_name):
    with open(file_name, 'r') as reader:
        lines = reader.readlines()
        calibrations = {}
        for line in lines:
            final_value, base_values = line.split(":")
            if final_value in calibrations.keys():
                final_value = f"{final_value}:{random.randint(0, 100)}"
            calibrations[final_value] = [int(x) for x in base_values.split()]
        return calibrations

def mul(x,y):
    return x * y

def add(x,y):
    return x + y

calibrations = read_and_parse_from_file(file_name="./day_7/real_data.txt")

valid_calibration_sum = 0
operations = ['*', '+']
for key, values in calibrations.items():
    final_value = int(key.split(":")[0])
    results = []
    for idx, value in enumerate(values):
        new_results = []
        if idx == 0:
            results.append(value)
            continue
        for result in results:
            new_results.append(mul(result, value))
            new_results.append(add(result, value))
        results = new_results

    if final_value in results:
        valid_calibration_sum += final_value
        

print(valid_calibration_sum)
    


