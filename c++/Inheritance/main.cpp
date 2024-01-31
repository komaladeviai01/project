#include <iostream>

using namespace std;
class flower
{
public:
    void rose(){
    cout<<"the flower color"<<endl;
    }
    string mycolor(){
    string color="rose";
    return color;
    }
    int myweight(){
    int weight=15;
    return weight;

    }
};
int main()
{
flower fr;
fr.rose();
cout<<fr.mycolor()<<endl;
cout<<fr.myweight()<<endl;
    return 0;
}
