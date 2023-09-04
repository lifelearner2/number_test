# print numbers from 1 up until MAX_NUMBER, inclusive
MAX_NUMBER = 100

def main():
   
    # TODO: your code here
   
    #prints 1-100 and checks if there's a remainder or not to determine if it's even or odd
    for i in range(100):
        num = i
      
        if i % 2 == 0: 
            print (num +1, "is odd")
        if i % 2 !=0:
            print(num +1, " is even")





if __name__ == "__main__":
    main()