#include <iostream>

using namespace std;

int max(int m,int n);
int min(int m,int n);

int main()
{
	int N,L,i,maxT,minT;
	cout<<"input N and L:";//N is the number of ants;L is the length of branch (N<+L)
	while(cin>>N>>L)
	{
		int d[N];
		i=0,maxT=0,minT=0;
		cout<<"input evey sites of ants:";
		while(i<N)
		{
			cin>>d[i];
			i++;
		}
		for(i=0;i<N;i++)
		{
			maxT=max(maxT,max(d[i],L-d[i]));
			minT=max(minT,min(d[i],L-d[i]));
			
		}
		printf("The minimum time is: %d\nThe maximum time is: %d\n\n",minT,maxT);
		cout<<"input N and L:";
	}
	
	return 0;
}
int max(int m,int n)
{
	return m>n?m:n;
}
int min(int m,int n)
{
	return m<n?m:n;
}