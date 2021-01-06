#include <iostream>
#include <string.h>
#include <math.h>
#include <cstdlib>
using namespace std;

bool light(int c,int n, int i, int a[]);
int main()
{
    int k=1,n, s = 0,c;
    cout << "input a number n:";
    cin >> n;
    c=n;
    int a[n];
    for (int i = 0; i < n; i++)
        a[i] = 1;
    light(c,n, ++k, a);
    for (int i = 0; i < n; i++)
        if (a[i] == 1)
            s++;

    cout << "lighting sum:" << s << endl;
    system("pause");
    return 0;
}

bool light(int c,int n, int k, int a[])
{
    
    if (c == 0)
        return false;
    else
    {

        for (int j=1; (k*j)-1<n; j++)
        {
            a[k * j - 1] *= -1;
        }
        return light(c-1,n, ++k, a);
    }
}
