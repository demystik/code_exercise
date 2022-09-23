// #include <stdio.h>
// // #include <string.h>
//
// // int main(void)
// // {
// //     char iso[] = "six-year-olds";
// //     int i = 0, j, len;
// //     len = strlen(iso);
// //     char arr[len];
//
// //     while (iso[i] != '\0')
// //     {
// //         if (i == 0)
// //             (arr[i] = iso[i]);
// //         else
// //         {
// //             j = 0;
// //             while (arr[j] != '\0')
// //             {
// //                 if (arr[j] == iso[i] && iso[i] != '-' &&  iso[i] != '_')
// //                 {
// //                     printf(" %s isn't an isogram\n", iso);
// //                     return (0);
// //                 }
// //                 j++;
// //             }
// //             (arr[i] = iso[i]);
// //         }
// //         i++;
// //     }
// //     printf("%s is an isogram\n", iso);
// // return (0);
// // }
//
// #include <stdbool.h>
// #include <string.h>
// #include <stdio.h>
//
// bool is_isogram(const char phrase[]);
//
// bool is_isogram(const char phrase[])
// {
//     if (!phrase)
//             return false;
//                 int i = 0, j, len = 0;
//                     while (phrase[len] != '\0')
//                             len++;
//                                 char arr[len];
//                                     while (phrase[i] != '\0')
//                                         {
//                                                 if (i == 0)
//                                                             arr[i] = phrase[i];
//                                                                     else
//                                                                             {
//                                                                                         j = 0;
//                                                                                                     while (arr[j] != '\0')
//                                                                                                                 {
//                                                                                                                                   
//                                                                                                                                                   if (arr[j] == phrase[i] || (phrase[i] == (arr[j] + 32))  || (phrase[i] == (arr[j] - 32)))
//                                                                                                                                                                   {
//                                                                                                                                                                                       if (phrase[i] != '-' && phrase[i] != '_' && phrase[i] != ' ')
//                                                                                                                                                                                                               return false;
//                                                                                                                                                                                                                               }
//                                                                                                                                                                                                                                               j++;
//                                                                                                                                                                                                                                                           }
//                                                                                                                                                                                                                                                                       arr[i] = phrase[i];
//                                                                                                                                                                                                                                                                               }
//                                                                                                                                                                                                                                                                                       i++;
//                                                                                                                                                                                                                                                                                           }
//                                                                                                                                                                                                                                                                                           return true;
//                                                                                                                                                                                                                                                                                           }
//
//                                                                                                                                                                                                                                                                                           int main(void)
//                                                                                                                                                                                                                                                                                           {
//                                                                                                                                                                                                                                                                                               bool ret;
//                                                                                                                                                                                                                                                                                                   const char phrase[] = "isogram";
//                                                                                                                                                                                                                                                                                                       ret = is_isogram(phrase);
//                                                                                                                                                                                                                                                                                                           if (ret == true)
//                                                                                                                                                                                                                                                                                                                   printf("yes!!");
//                                                                                                                                                                                                                                                                                                                       else
//                                                                                                                                                                                                                                                                                                                               printf("NOOO!!");
//                                                                                                                                                                                                                                                                                                                               }
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
