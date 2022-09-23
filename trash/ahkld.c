nclude <stdio.h>

int main(void){    
	    int n = 10;
	        int num2, diff, sum = 0, total = 0;
		    num2 = n;
		        while (n != 0)
				    {
					            sum += n;
						            n--;
							        }
			    sum*=sum;
			        while (num2 != 0)
					    {
						            total += (num2 * num2);
							            num2--;
								        }
				    diff = sum - total;
				        printf("%d - %d is %d\n",sum, total, diff);
}
