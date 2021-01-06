#include <iostream>
#include <math.h>
using namespace std;

int main(int argc, char *argv[])
{
    int n,sum=0;
    cout<<"input a n(binary number 0<length(n)<10):"; 
    cin>>n;

    for(int i=0;n>0;i++){
        sum+=n%10*pow(2,i);
        n/=10;
        cout<<endl;
    }
    cout <<"convey to the decimal:"<<sum<< endl;
    system("pause");
    return 0;
}


