# https://www.hackerrank.com/challenges/save-the-prisoner

def save_poisoned(num_prisoners, num_sweets, start_id):
    poisoned_prisoner = (num_sweets - ((num_prisoners - start_id)+1)) % num_prisoners
    return poisoned_prisoner if poisoned_prisoner > 0 else num_prisoners

def main():
    num_cases = int(input().strip())
    for _ in range(0, num_cases):
        num_prisoners, num_sweets, start_id = [int(x) for x in input().strip().split(' ')]
        print(save_poisoned(num_prisoners, num_sweets, start_id))

if __name__ == '__main__':
    main()