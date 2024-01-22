import time 
import multiprocessing

square_list=[]
def calc_square(numbers):
    global square_list
    for n in numbers:
        print("Square" + str(n*n))
        square_list.append(n*n)
        print("within a Square", str(square_list))

if __name__ == "__main__":
    arr=[2,3,8,9]
    t1=multiprocessing.Process(target=calc_square,args=(arr,))
    t1.start()
    t1.join()


print("done in"  + str(square_list))
print("Huh ...I am done with all my work now! ")
