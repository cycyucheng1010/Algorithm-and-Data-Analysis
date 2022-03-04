#include<stdio.h>

int main(void){
    //do while
    int i,counter = 0;
    do {
        counter++;
        printf("counter:%d\n",counter);
        i++;
    }while(i<6);
    //Fibonacci
    int j,n;
    int fib=0;
    int fib0=0;
    int fib1=1;
    printf("plz input a number ");
    scanf("%d", &n);
    if(n==0){
        printf("fib=%d",fib0);
    }
    else if(n==1){
        printf("fib=%d",fib1);
    }
    else{
        for(j=2;j<=n;j++){
            fib = fib0 +fib1;
            fib0 = fib1;
            fib1 = fib;
        }
    }
    printf("f(n)=%d\n",fib);
    return 0;
}