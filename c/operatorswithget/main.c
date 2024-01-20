#include <stdio.h>
#include <stdlib.h>

int main()
{
    addition(getA(),getB());
    subtract(getA(),getB());
    multiplies(getA(),getB());
    divisionprogram(getA(),getB());
    modulesprogram(getA(),getB());
    incrementprogram(getA(),getB());
    decrementprogram(getA(),getB());
    logicalprogram(getA(),getB());
return 0;
}
int getA()
{
int a;
printf("enter the value :\n");
scanf("%d",&a);
return a;
}
int getB()
{
    int b;
    printf("enter the value:\n");
    scanf("%d",&b);
    return b;
}
int addition(int y,int x)
    {
    int z=x+y;
    printf("print value of z is:%d \n",z);
    }
  int sub(int y,int x)
  {
      int u=x-y;
      printf("print value of u:%d \n",u);
  return 0;
  }
