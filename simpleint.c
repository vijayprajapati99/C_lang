#include <stdio.h>

int main() {
    float principal, rate, time;
    float simple_interest;

    printf("Enter the value of the principal: ");
    scanf("%f", &principal);

    printf("Enter the value of the rate: ");
    scanf("%f", &rate);

    printf("Enter the value of the time: ");
    scanf("%f", &time);

    simple_interest = principal * rate * time / 100;
    printf("The value of the simple interest is %f\n", simple_interest);

    return 0;
}