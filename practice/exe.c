#include <stdio.h>
#include <unistd.h>


int main (void)
{
	char cmd[] = "/usr/bin/ls";
	char *argv[] = {"ls", "-l", "/tmp", NULL};
	pid_t child, child1;
	child = fork();

	if (child < 0)
		printf("forking error\n");
	else if (child == 0)
	{
		if (execve(cmd, argv, NULL) == -1)
			printf("execve error\n");
		printf("inside child process\n");
	}
	else
		printf("inside parent process\n");
		child1 = fork();
		if (child1 < 0)
			printf("Error forking 2\n");
		else if (child1 == 0)
		{
			printf("hello from  new child\n");
			if (execve(cmd, argv, NULL) == -1)
				printf("error in execve 1\n");
		}
		else
			printf("_____\n");


return (0);
}
