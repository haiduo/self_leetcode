#include <iostream>
#include <vector>

using namespace std;

int main()
{
	int N,L,i,maxT,minT;
	cout<<"input N and L:";//N is the number of ants;L is the length of branch (N<+L)
	while(cin>>N>>L)
	{
		vector<int> d;
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
