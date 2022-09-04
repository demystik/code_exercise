#include <stdio.h>
#include <string.h>

int main(void)
{
int diff = 0, count = 0;
char *strand1 = "CAGTTGCAACTGCAT";
char *strand2 = "ATGCCATACTGTTA";

int len = strlen(strand1);
int len2 = strlen(strand2);

if (len != len2)
{
    printf("%s","different number of DNA");
    return (0);
}
while (count != len)
{
    if (strand1[count] == strand2[count])
        diff++;
    count++;
}
printf("diff is %d",diff);
return (0);
}