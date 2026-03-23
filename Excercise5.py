
        
def main2():
    for n in range(21):
        if n%3 == 0 and n%5 == 0:
            print(f"{n}: Data Science")
        elif n%3 == 0 :
            print(f"{n}: Data")
        elif n%5 == 0:
            print(f"{n}: Science")
        else:
            print(n) 
               
def main():
    loss = 10.0
    print("Simulating Model Training")
    
    while loss > 0:
        print(f"Printing model loss: {loss}")
        loss = loss-1.5
    else:
        print("Stoping loop")
        

# main();

main2();