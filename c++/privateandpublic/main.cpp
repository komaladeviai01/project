#include <iostream>
using namespace std;
class salaryprint
{
private:
    int salary;
public:
    string empname;
    void setsalary(int s)
    {
        salary=s;
    }
    int getsalary()
    {
        return salary;
    }
    int getsalaryprint()
    {
        cout<<salary;

    }
void getsalaryprint1()
{
    cout<<salary;
}
};
int main()
{
    salaryprint sp;
    sp.setsalary(80);
    cout<<sp.getsalary()<<endl;
    sp.getsalaryprint();
    sp.getsalaryprint1();
    if(80<=70)
    {
        cout<<"its a return type \n";
    }
    if(80>=40)
    {
        cout<<"\n its a return type.....";
    }
    return 0;

}







/*using namespace std;
class scooty
{
    public:
    string scootyname="honda\n";
    void messageprint(){
    cout<<"welcome to honda company\n";
    }

};
class scootytype
  {
    public:
    string scootytypename="honda dio";
    void messageprintfor(){
    cout<<"welcome to honda dio company\n";
    }
  };
    class brand:public scooty,public scootytype{
    };

int main()
{
    brand br;
    cout<<br.scootyname;
    br.messageprint();
    cout<<br.scootytypename;
    br.messageprintfor();

    return 0;

}*/



/*using namespace std;
class accesspecifie
{
private:
    int b=15;
public:
    int a,c;
    printb()
{

    c=b;
    cout<<c;
}
};
int main()
{
    accesspecifie as;
    as.a=25;
    cout<<as.a;
  as.printb();
    return 0;
}*/
