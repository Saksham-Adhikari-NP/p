#include <stdio.h>

int main() {
    int i, j, k, space;

    // Set the number of rows for the pyramid
    int rows = 5;

    // Initialize space variable
    space = rows;

    // Loop through each row
    for (i = 0; i < rows; i++) {
        // Print leading spaces
        for (k = 0; k < space; k++) {
            printf(" ");
        }
        space--; // decrement space for each row

        // Print smiley face characters
        for (j = 0; j <= 2 * i - 1; j++) {
            printf(":");
        }
        printf("\n");
    }

    return 0;
}