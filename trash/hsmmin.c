#include <stdio.h>
#include <string.h>


int compute(const char *lhs, const char *rhs)
{
	int diff = 0, count = 0;
	const char *strand1;
	const char *strand2;
	if (!lhs || !rhs)
	{
		    printf("not lhs or not rhs");
		        return (0);
	}
	strand1 = lhs;
	strand2 = rhs;

	int len = strlen(strand1);
	int len2 = strlen(strand2);

	if (len != len2)
	{
		    printf("not same length\n");
		        return (-1);
	}
	while (count != len)
	{
		    if (strand1[count] != strand2[count])
			            diff++;
		        count++;
	}
	return diff;

}

int main(void)
{
	    int n;
	        const char *lhs;
		    const char *rhs;
		        lhs = "AAA";
			    rhs = "AATG";
			        n = compute(lhs,rhs);
				    printf("%d\n", n);


				    // int diff = 0, count = 0;
				    // // char *strand1 = "CAGTTGCAACTGCAT";
				    // // char *strand2 = "ATGCCATACTGTTA";
				    //
				    // // int len = strlen(strand1);
				    // // int len2 = strlen(strand2);
				    //
				    // // if (len != len2)
				    // // {
				    // //     printf("%s","different number of DNA");
				    // //     return (0);
				    // // }
				    // // while (count != len)
				    // // {
				    // //     if (strand1[count] == strand2[count])
				    // //         diff++;
				    // //     count++;
				    // // }
				    // // printf("diff is %d",diff);
				    //
				    // // char st[] = "hello";
				    //
				    // // printf("%c, %c", st[0], (st[0] - 32));
				    // // return (0);
				    // }
