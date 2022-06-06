from datetime import datetime
import time
from application import people, salary

def main():
    print(f'Current time: {datetime.now().strftime("%b %d %Y %H:%M:%S")}')
    salary.calculate_salary()
    time.sleep(1)
    print(f'Current time: {datetime.now().strftime("%b %d %Y %H:%M:%S")}')
    people.get_employees()

if __name__ == '__main__':
    main()
