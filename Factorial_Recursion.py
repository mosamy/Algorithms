__author__ = 'mosamy'
# commit

def factorial(n):
    if n == 0:
        return 1
    else:
        # recurse = factorial(n-1)
        #result = n * recurse
        return n * factorial(n - 1)  #result


def main():
    print(factorial(1000))

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()