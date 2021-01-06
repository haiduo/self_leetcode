#include <iostream>
using namespace std;

int main(int argc, char *argv[])
{
    int n, sum, min, max;
    cout<<"input a count of list integers :"; 
    cin>>n;
    int a[n];
    cout<<"then input list integers :";
    cin>>a[0];
    sum=min=max=a[0];
    for(int i=1;i<n;i++){
        cin>>a[i];
        sum+=a[i];
        if(min<a[i]) min=a[i];
        if(max>a[i]) max=a[i];
    }
    cout<<"sum"<<sum<<"min:"<<min<<"max:"<<max;
    cout << endl;
    system("pause");
    return 0;
}


