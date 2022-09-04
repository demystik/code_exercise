#include <stdio.h>
#include <string.h>

int main(void)
{
    char *iso = "six-year-old";
    int i = 0, j, len;
    len = strlen(iso);
    char arr[len];

    while (iso[i] != '\0')
    {
        if (i == 0)
            (arr[i] = iso[i]);
        else
        {
            j = 0;
            while (arr[j] != '\0')
            {
                if (arr[j] == iso[i] && iso[i] != '-' & iso[i] != '_')
                {
                    printf(" %s isn't an isogram\n", iso);
                    return (0);
                }
                j++;
            }
            (arr[i] = iso[i]);
        }
        i++;
    }
    printf("%s is an isogram\n", iso);
return (0);
}
