def read_input(input_file):
    with open(input_file) as input_handle:
        password_db = input_handle.readlines()
        return [line.strip() for line in password_db]


if __name__ == "__main__":
    db = read_input("input.txt")
    good_passwords = 0
    for entry in db:
        props = entry.replace("-", " ").split()
        pos1 = int(props[0])
        pos2 = int(props[1])
        letter = props[2][0]
        pwd = props[3]
        if (pwd[pos1 - 1] == letter) != (pwd[pos2 - 1] == letter):
            print("OK")
            good_passwords += 1
        else:
            print("Nope")
    print(good_passwords)
