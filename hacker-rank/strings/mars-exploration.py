import sys

def count_changed(S):
    S_list = list(S)
    SOS = ['S', 'O', 'S']
    i = 0
    error_count = 0

    for c in S_list:
        if c != SOS[i]:
            error_count += 1
        i = (i+1)%3

    return error_count

def main():
    S = input().strip()
    print(count_changed(S))

if __name__ == '__main__':
    main()