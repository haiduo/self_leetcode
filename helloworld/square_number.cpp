#include <iostream>
#include <math.h>
#include <string>
#include <iomanip>
using namespace std;

int main(int argc, char *argv[])
{
    int n,sum=0;
    cout<<"input a n( 0<n<=31):"; 
    cin>>n;

    for(int i=1;i<=n;i++){
        for(int j=1;j<=n;j++){
            //cout.width(4);cout.setf(ios::right); 格式方法1
            cout<<setw(4) <<(++sum);//setw(4)格式方法2 需要#include <iomanip>
            if(sum%n==0) cout<<endl;
        }  
    }
   
    system("pause");
    return 0;
}


