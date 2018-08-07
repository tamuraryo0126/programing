def is_prime(n):
    prime_list=[2]
    sum=2
    for x in range(3,n+1, 2):
        for y in prime_list:
            if x%y==0: break
        else: 
            prime_list.append(x)
            sum+=x
    return sum
    
                
def main():
    N=int(input())
    if N==1:
        print("0")
    else:
        print(is_prime(N))
    

if __name__=="__main__":
    main()
