#include <stdio.h>

/**
 * main - starting point of the program
 *
 * Description: print the size of various data type
 * Return: o if program execute prperly, else a non-zero number
*/
int main(void)
{
printf("Size of a char: %d byte(s)\n", (int) sizeof(char));
printf("Size of an int: %d byte(s)\n", (int) sizeof(int));
printf("Size of a long int: %d byte(s)\n", (int) sizeof(long int));
printf("Size of a long long int: %d byte(s)\n", (int) sizeof(long long int));
printf("Size of a float: %d byte(s)\n", (int) sizeof(float));
return (0);
}

