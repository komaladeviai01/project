#include<stdio.h>
int loop()
{
   int i,j;
   for(int i=0;i<5;i++)
   {
    printf("\n");
    for(int j=0;j<i;j++)
    {
     printf("#\n");
    }
  }
    return 0;
  
}