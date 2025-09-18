#include <stdio.h>

int global_count = 0;
int magic_integer()
{
	return 1024 * global_count++;
}

int main()
{
	for (int i = 0; i < 10; i++)
		printf("%d\n", magic_integer());
	return 0;
}
