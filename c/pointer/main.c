#include <stdio.h>
#include <stdlib.h>

int main()
{
int a=7,b=5;
printf("Enter the A value.....%d\n",a);
printf("Enter the address......%p\n",&a);
printf("Enter the size.....%d\n",sizeof(a));
printf("Enter the B value.......%d\n",b);
printf("Enter the address b......%p\n",&b);


/*int *p=&a;
printf("Enter the P value........%p\n",p);
printf("Enter the address.........%p\n",&p);
printf("values stored of the adders...%p\n",p);
*/
/*char s[20]="komala";
printf("Enter the s.....%s\n",s);
printf("Enter the address......%p\n",&s);
printf("---------------------------\n");

char *p="komala";
printf("enter the p values......................%p\n",p);
printf("enter the address.......................%p\n",&p);
printf("values stored of the address.............%s\n",p);
printf("-----------------------------\n");
char **q=&p;
printf("enter the q.........................................%p\n",q);
printf("enter the address....................................%p\n",&q);
printf("values stored of the address.........................%p\n",*q);
*/



float f=(float)a/b;
printf("enter the value f...........%f\n",f);
printf("enter the address............%p\n",&f);
printf("-------------------------------\n");
 float *c=&f;
 printf("enter the value c.........%p\n",c);
 printf("enter the address............%p\n",&c);
 printf("values stored of the address......%p\n",c);

return 0;
}

