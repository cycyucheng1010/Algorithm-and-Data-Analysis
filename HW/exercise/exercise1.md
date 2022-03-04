# 01程式與資料結構
## 習題
### 1. 何者最不適用用來描述一個演算法?
   * **組合語言**，不易說明及理解。
### 2. 何者代表處理之流程圖符號?

![image](https://user-images.githubusercontent.com/62127656/156813021-544f3928-23bb-4c41-8d87-ff458811e6a5.png)

### 3. 請問流程圖中的菱形符號代表甚麼?

![image](https://user-images.githubusercontent.com/62127656/156813084-d453b37f-7848-4ed1-94db-7a446be01b84.png)

### 4. 何者不是演算法特性的研究範圍?
   * **程式語言的選擇**，演算法是一種數學方法，可以透過各種語言去實踐。
### 5. 對於演算法的定義何者錯誤?
   * **可以有無窮迴圈**這個選項是錯誤的，根據演算法特性中的有限性，不可以無窮迴圈，必須在有限的步驟中完成或終止
### 6. 在程式實作資料抽象化中可分為三個階段來討論，哪個不屬於三個層次之一?
   * 不包含**位元資料型態**可參考下圖

![image](https://user-images.githubusercontent.com/62127656/156814559-4b314621-2809-496f-9bd9-74f989eb73c2.png)


### 7. 簡述資料結構的定義?
   * 將各種資料組織結構化後，作為一個個體來使用
### 8. 演算法的定義及重要特性?
   * 是一個解決問題，並且用來達到目的方法。
   
   ![image](https://user-images.githubusercontent.com/62127656/156825932-807b46a2-afc6-4f77-a861-d42d55688295.png)

   
### 9. what is the relationship between a program and an algrithm?
   * prigrams = algrithms + data structures
### 10. Determine what the following flow graph computes?

![image](https://user-images.githubusercontent.com/62127656/156815931-6743f55f-52ce-4992-9210-80d010acb01d.png)

   * (a) when n=5 , value of output = 10
   * (b) when n=100, value of output= 4950
   * (c) ```f(n ) = 1*2*3....*(n-1)*n for n = 1,2,.....```
   ```mermaid
  flowchart TD
  input[/input/]--> begin(i equal 1 and out equal 1)
  begin(i equal 1 and out equal 1)-->decision{i small or equal n?}
  decision{i small or equal  n?}-->|F|F[/output out/]
  decision{i small or equal  n?}-->|T|T(out equal out multiplied i and i equal i plus 1)
  T(out equal out multiplied i and i equal i plus 1)-->decision{i small or equal n?}
  
   ```
### 11. Rewrite the following C program segement using the do/while structure
```c
for( i=0 ' i<6 ; i++)
  counter++;
```
   * my ans:
   ```c
   do {
        counter++;
        i++;
    }while(i<6);
   ```
### 12. 用迴圈寫一個C語言的費氏數列
   * my ans
```c
    #include<stdio.h>

int main(void){
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
```
