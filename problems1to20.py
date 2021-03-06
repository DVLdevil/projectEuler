

def p1():
    description = "If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000."
    
    print(description)
    sum = 0
    
    # method 1
    for i in range(1,1000):
        if(i%3==0 or i%5==0):
            sum += i
            
    print("\nanswer is " + str(sum))
    
    
def p2():
    description = "Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be: \n\n\t1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...\n\nBy considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms."
    
    print(description)
    sum = 0
    
    # method 1
    n1 = 1
    n2 = 2
    max = 4000000
    while(n2 < max):
        if n2%2 ==0:
            sum += n2
        temp = n1 + n2
        n1 = n2
        n2 = temp
    print("\nanswer is " + str(sum))    
   
def isPalindrome(number):
    front = str(number)[0:len(str(number))/2]
    back = "".join(reversed(str(number)[len(str(number))/2:]))
    print(front)
    print(back)
   
def p4():
    description = "A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99. \nFind the largest palindrome made from the product of two 3-digit numbers."
    n1 = n2 = 999
    
    product = n1*n2
    max = 1
    if(isPalindrome(product) and product > max):
        max = product
