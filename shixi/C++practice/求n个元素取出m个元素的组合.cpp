#include <iostream>
#include <string.h>
#include <math.h>
#include <cstdlib>
using namespace std;

int comm(int n, int k);
int main()
{
    int n, k;
    cout << "Please enter two integers n and k:";
    cin >> n >> k;
    cout << "c(n,k)=" << comm(n, k) << endl;

    system("pause");
    return 0;
}

int comm(int n, int k)
{
    if (k > n)
        return 0;
    else
    {
        if (n == k || k == 0)
            return 1;
        else
        {
            return comm(n - 1, k) + comm(n - 1, k - 1);
        }
    }
}