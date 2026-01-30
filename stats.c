// write a c program that prints the number of days in a month
#include <stdio.h>
int main() {
    int month, year;
    printf("Enter the month and year: ");
    scanf("%d %d", &month, &year);
    switch (month) {
        case 1:
            printf("31 days");
            break;
        case 2:
            if (year % 4 == 0 && year % 100 != 0 || year % 400 == 0)
                printf("29 days");
                else

