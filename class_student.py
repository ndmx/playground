class Student:
    def __init__(self, name, house):
        self.name = name
        self.name = house


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")
    return student

if __name__ == '__main__':
    main()
