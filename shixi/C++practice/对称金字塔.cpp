#include <iostream>
using namespace std;

int main(int argc, char *argv[])
{
    int n;
    cout<<"input a n (0<n<10) :"; 
    cin>>n;
    for(int i=0;i<n;i++){
        for(int j=0;j<n-i-1;j++) cout<<' ';
        for(int j=0;j<2*i+1;j++) cout<<'*';
        cout<<endl;
    }
    for(int i=1;i<n;i++){
        for(int j=1;j<i+1;j++) cout<<' ';
        for(int j=0;j<2*(n-i-1)+1;j++) cout<<'*';
        cout<<endl;
    }
    cout << endl;
    system("pause");
    return 0;
}


