#include<stdio.h>

int main(){
    int a,b;
    printf("Enter a number\n");
    scanf("%d",&a);
    if(a%2==0)
    {printf("%dthe number is even\n",a);}
    else 
    {
       printf("%d the number is odd\n",a);
    }
    
    return 0;
}