__author__ = 'mosamy'

#making changes to the file

def factorial(n):
    result = 1
    if n == 0:
        result = 1
    else:
        for i in range(1, n+1, 1):
            result = result * i
    return  result



def main():
    print(factorial(100))

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()
