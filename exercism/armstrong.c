#include <stdio.h>

/**
 * power - This function calculate the power of a number
 * @x: The x value
 * @y: The power
 * Author - Thaoban Abdrasheed
 * Return:the power
 */
int power(int x, int y)
{
    int total = 1;
    while (y != 0)
    {
        total *= x;
        y--;
    }
    return (total);
}

/**
 * check_num_dig - This function check the cal the number of digits
 * @arm: The number
 * Author - Abdrasheed Thaoban
 * Return: The number of digits
 */
int check_num_dig(int arm)
{
    int i;
    i = 0;
    while (arm)
    {
        arm = arm/10;
        i++;
    }
return (i);
}

/**
 * check_if_arm - This function checks if a num is armstrong
 * @num: The number to check
 * @i: The number of digits in a number
 * Author - Thaoban Abdrasheed
 * Return: 1 if it's armstrong and 0 otherwise
 */
int check_if_arm(int num, int i)
{
	int mod, rem, total, init;
	total = 0;
	init = num;
	while (num != 0)
	{
		mod = num % 10;
		rem = num / 10;
		num = rem;
		total += power(mod,  i);
	}
	if (init == total)
		return (1);
	return (0);
}


/**
 * main - main function for Exercism C challenge
 * Author - Thaoban Abdrasheed
 * @argv: argument vector
 * @argc: args counter
 * 
 * Return: Zero on success
 */
int main(void)
{
    int num_dig, ret_val;
    int num = 153;

    num_dig = check_num_dig(num);
    ret_val = check_if_arm(num, num_dig);
    if (ret_val == 1)
        printf("%d is an armstrong number! :)\n", num);
    else
	printf("%d is not an armstrong number! :(\n", num);
return (0);
}
