#include<stdio.h>
 int main()
 {
    int a;
     printf("enter the value");
     scanf("%d",&a);
if(a==2)
{ 
    int a1,b1,op;
    printf("enter a value for a1\t");
    scanf("%d",&a1);
    printf("enter a value for b1\t");
    scanf("%d",&b1);
    printf("select the operator");
    scanf("%d",&op);

switch(op)
{
case 1:
printf("you are select addition\n");
printf("added value of a1 and b1 is %d\n",a1+b1);
break;
case 2:
printf("you are select subtraction\n");
printf("sub value of a1 and b1 is %d\n",a1-b1);
break;
case 3:
printf("you are select multipult\n");
printf("multiple value of a1 and b1 is %d\n",a1*b1);
break;
}
 }
else 
{
    int a1,b1,c1,op;
 printf("enter the value A1"); 
 scanf("%d",&a1);
 printf("enter the value B1");
 scanf("%d",&b1);
 printf("enter the value C1");
 scanf("%d",&c1);
printf("select the operator");
    scanf("%d",&op);
switch(op)
{
case 1:
printf("you are select addition\n");
printf("added value of a1 and b1 and c1 is %d\n",a1+b1+c1);
break;
case 2:
printf("you are select subtraction\n");
printf("sub value of a1 and b1 and c1 is %d\n",a1-b1-c1);
break;
case 3:
printf("you are select multipult\n");
printf("multiple value of a1 and b1 and c1 is %d\n",a1*b1);
break;
}
}
return 0;
 }