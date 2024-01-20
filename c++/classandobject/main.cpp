#include <iostream>
using namespace std;
class myfirstvalue
{
public:
    int a;
    int b;
    int add()
    {
    cout<<(a+b);
    cin>>a>>b;
    }
};
int main()
{
    int a,b;
    cin>>a>>b;
    a=a+b;
    cout<<a;
    return 0;
}
