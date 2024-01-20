#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a;
    int b;
    int c;
    printf("enter the value a");
    scanf("%d",&a);
    printf("enter the value b");
    scanf("%d",&b);
    additionprogram(a,b);
    subtractionprogram(a,b);
    divisionprogram(a,b);
    multipliesprogram(a,b);
    modulesprogram(a,b);
    incrementprogram(a,b);
    decrementprogram(a,b);
    logicalprogram(a,b);
    return 0;
}
int additionprogram(int a,int b)
{
    int c=a+b;
    printf("\n added value of a+b:%d\n",c);
}
int subtractionprogram(int a,int b)
{
    int c=a-b;
    printf("\n sub value of a-b:%d\n",c);
}
int divisionprogram(int a, int b)
{
    float c;
    c=(float)a/b;
    printf("\n divit value of a/b:%f\n",c);
}
int multipliesprogram(int a,int b)
{
    int c=a*b;
    printf("\n multiple value of a*b:%d\n",c);
}
int modulesprogram(int a,int b)
{
    int c=a%b;
    printf("\n modules value of a%b:%d\n",c);
}
int incrementprogram(int a)
{
  while(a<20)
  {
      printf("\n increment value of a:%d\n",a);
      a++;
  }
}
int decrementprogram(int a)
{
    while(a>10)
    {
        printf("\n decrement value of a:%d\n",a);
        a--;
    }
}
int logicalprogram(int a,int b)
{
    if(!(a>10&&b>20))
    {
        printf("\n logical value of AND:%d\n",!(a<10&&b<10));
        printf("\n logical value of OR:%d\n",(a>10||b<10));
    }
}



