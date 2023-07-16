#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <fcntl.h>
#include <sys/stat.h>

ssize_t read_textfile(const char *filename, size_t letters)
{
	ssize_t nread, nwrite;
	char *buffer;
	int fd;

	fd = open(filename, O_RDONLY);
	if (fd < 0)
		return (0);

	buffer = malloc(sizeof(char) * letters);
	if (buffer == NULL)
		return (0);

	nread = read(fd, buffer, letters);
	nwrite = write(STDOUT_FILENO, buffer, letters);

	close(fd);

	return (nwrite);
}
