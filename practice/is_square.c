#include <stdio.h>

int main(){
int n = 25;

for(int i = 0; i <= n/2; i++)
{
	if (i * i == n)
	{
		printf("True\n");
		return (0);
	}
}
printf("False\n");
return (0);
}
