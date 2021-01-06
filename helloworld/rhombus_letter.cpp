#include <iostream>
using namespace std;

int main(int argc, char *argv[])
{
    int n;
	char l;
    cout<<"input a captical letter and high(n) of rhombus (1<=n<=26) :"; 
    cin>>l>>n;
	cout<<endl;
	for(int j=0;j<n-1;j++) cout<<' ';
        cout<<l;
	cout<<endl;
	l++;
	l=char((l-'A')%26+'A');
    for(int i=1;i<n;i++){
        for(int j=0;j<n-i-1;j++) cout<<' ';
        cout<<l;
		for(int j=1;j<2*i;j++) cout<<' ';
		cout<<l;
		l++;
		l=char((l-'A')%26+'A');
        cout<<endl;
    }
	l--;
    for(int i=1;i<n-1;i++){
		l--;
		l=char((l-'A'+26)%26+'A');
        for(int j=1;j<i+1;j++) cout<<' ';
        cout<<l;
		for(int j=1;j<2*(n-i-1);j++) cout <<' ';
		cout<<l;
        cout<<endl;
    }
	l--;
	l=char((l-'A'+26)%26+'A');
	for(int j=1;j<(n-1)+1;j++) cout <<' ';
		cout<<l;
    cout << endl;
	cout<<endl;
    system("pause");
    return 0;
}


