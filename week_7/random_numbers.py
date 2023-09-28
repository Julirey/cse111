import random
 
def main():
    numbers = [16.2, 75.1, 52.3]
    print(f'Numbers: {numbers}')
    append_random_numbers(numbers) 
    print(f'Numbers: {numbers}')
    append_random_numbers(numbers, quantity=3)
    print(f'Numbers: {numbers}')
 
def append_random_numbers(numbers_list, quantity = 1):
    for _ in range(quantity):
        random_number = round(random.uniform(0,50),1)
        numbers_list.append(random_number)
    
if __name__ == "__main__":
    main()