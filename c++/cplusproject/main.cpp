#include <iostream>

using namespace std;

int main()
{
    int value1,value2,total,op;
    cout << "Enter value 1";
    cin>>value1;
    cout << "Enter value 2";
    cin>>value2;
    cout << "Enter Operator";
    cin >>op;

    switch(op)
{

case 1:
    total=value1+value2;
    cout << "added value of 1 and 2 \n"<<total;
    break;
case 2:
    total=value1-value2;
    cout << "sub value of 1 and 2 \n"<<total;
    break;
case 3:
    total=value1*value2;
    cout << "multipule value of 1 and 2 \n"<<total;
    break;
case 4:
    total=value1/value2;
    cout << "division value of 1 and 2 \n"<<total;
    break;
case 5:
    total=++value1;
    cout << "Increment value of 1 \n"<<total;
    break;
}
      return 0;
}
