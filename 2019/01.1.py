def read_input(input_file):
    with open(input_file) as input_handle:
        raw_modules = input_handle.readlines()
        modules_masses = [int(mass) for mass in raw_modules]
        return modules_masses


def compute_fuel(mass):
    fuel = mass // 3 - 2
    return fuel


if __name__ == "__main__":
    modules_masses = read_input("01.input")
    fuel_requirements = sum([compute_fuel(mass) for mass in modules_masses])

    print(fuel_requirements)
