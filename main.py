import json


def print_field(field, value):
    print(field, end="")
    if type(value) == dict:
        print(": {}")
    elif type(value) == list:
        print(": []")
    else:
        print()


def main(path: str):
    file = open(path)
    data = json.load(file)
    target = data

    while type(target) != str:
        if type(target) == dict:
            for field in target:
                print_field(field, target[field])

            goto = input("next: ")
            while goto not in target:
                goto = input("next: ")
            target = target[goto]

        elif type(target) == list:
            index = 1
            for value in target:
                print_field(index, value)
                index += 1

            goto = input("next: ")
            while int(goto) not in range(1, len(target)+1):
                goto = input("next: ")
            target = target[int(goto)-1]
        print()

    print(target)

if __name__ == "__main__":
    print("path to the object json:")
    path = input()
    main(path)