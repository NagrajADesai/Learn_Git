# Python is both compiled and interpreted language
## 1
## Exception handling
# Errors : ---> Compile time erro - syntax errors 
#          ---> Logical - gives wrong output
#          ---> Run time - error is getting when it is running (eg. if we divide any number by 0)
def exception_handling():
    a = 6
    b = 2
    try:
        print('Resource oprn')
        print(a/b)
        k = int(input('Give a number: '))
        print(k)

    # for different type of errors you have to specify different exceptions
    except ZeroDivisionError as e:
        print('You cannot divide a number by zero', e)
    except ValueError as e:
        print('Given number is invalid', e)
    # for common error
    except Exception as e:
        print('Someting went wrong')
    finally:
        print('Resource closed')

## 2
## Multitasling
# Use multiple Threds simultaniusly
# usually tasks are done by main tread
from time import sleep
from threading import *

class Hello(Thread):
    def run(self):
        for i in range(5):
            print('Hello')
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(5):
            print('Hi')
            sleep(1)

## 3 
## file handling

def file_handling():
# open and read the file
    f= open('mydata', 'r') 
    #print(f.read())
# write the file
# it creates new file if it is not exist
    f1 = open('abc','w')
    f1.write('Something')
# append in file
    f1 = open('abc', 'a')
    f1.write('new is happening')
# if we want to copy the data from mydata to abc
    for data in f:
        f1.write(data)

## 4
# Linear search
# using for loop
position = 0
def search(list,n):
    for i in list:
        if i == n:
            globals()['position'] = list.index(i)+1
            return True           
    else:
        return False
# using while loop
position1 = 0
def _search(list,n):
    i = 0
    while i < len(list):
        if list[i] == n:
            globals()['position1'] = i + 1
            return True
        i = i + 1
    return False

## 5
# Binary search --> In this method the list has to be sorted
position2 = 0
def binary_search(list,n):
    l = 0             # lower bound
    u = len(list) -1  # upper bound
    for i in range(u):
        mid = (l+u)//2
        if list[mid] == n:
            globals()['position2'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid + 1
            else:
                u = mid - 1
    else:
        return False

# 6
# Bubbol sort
# swap the altarnative numbers by compairing
def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
                print(nums)

# 7 
# selection sort
# swap the lowest element by that present element
def selection_sort(nums):
    for i in range(len(nums)-1):
        minpos = i 
        for j in range(i, len(nums)):
            if nums[j] < nums[minpos]:
                minpos = j 
        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp
        print(nums)


if __name__ == '__main__':
    # 1
    # Exception handling
    #exception_handling()

    # 2
    # Multitasking
    #t1 = Hello()
    #t2 = Hi()
    #t1.start()
    #sleep(0.2)
    #t2.start()
    # if you want to print this line at the end of the above task 
    #t1.join()
    #t2.join()
    # and when t1 and t2 are executed then the below line will execute
    #print('I will come at the end')

    # 3
    #file_handling()

    #4 # 5
#    list = [2,5,7,8,9,12,15,20,21]
 #   n = 20
    # only change the name of the function
 #   if binary_search(list,n):
 #      print(f'{n} found at: ',position2+1)
 #   else:
 #       print('Not found')

    #6 #7
    nums = [5,3,8,6,7,2]
    sort(nums)
    print(nums)
    