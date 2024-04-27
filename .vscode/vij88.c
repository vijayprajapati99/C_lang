#include <stdio.h>

int main() {
    float dividend, divisor, quotient;

    printf("Enter dividend: ");
    scanf("%f", &dividend);

    printf("Enter divisor: ");
    scanf("%f", &divisor);
    // Check if the divisor is not zero to avoid division by zero error
    if (divisor != 0) {
        quotient = dividend / divisor;
        printf("Quotient = %.2f\n", quotient);
    } else {
        printf("Error: Division by zero\n");
    }
    return 0;
}