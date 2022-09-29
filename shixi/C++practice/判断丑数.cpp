#include <iostream>
#include <string.h>
#include <math.h>
#include <cstdlib>
using namespace std;
//丑数（ ugly number ）： 把只包含质因子2、3和5的数称作丑数，
//例如：6、8都是丑数，但7、14不是。 习惯上把1当做第一个丑数。
int main()
{
    int n, t = 1;
    cout << "input a number(1<=n<=8000):";
    cin >> n;
    if (n == 1)
        cout << n << " is not a Ugly Number" << endl;
    else
    {
        for (int i = 2; i <= sqrt(n); i++)
        {
            if (n % i == 0)
            {
                t = 0;
                if ((i == 2 || i == 3 || i == 5))
                {
                    continue;
                }
                else
                {
                    cout << n << " is not a Ugly Number" << endl;
                    system("pause");
                    return 0;
                }
            }
        }
        if (t == 0)
        {
            cout << n << " is a Ugly Number" << endl;
        }
        else
        {
            cout << n << " is not a Ugly Number" << endl;
        }
    }
    system("pause");
    return 0;
}
