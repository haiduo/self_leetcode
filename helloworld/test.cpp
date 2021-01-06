#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int t = 1;

int su(int b, int i)
{
    int a, sum = 0;
    a = i;
    b = b - a;
    if (a >= b || a >= 9)
    {
        t *= -10;
        if (b > 100)
            b /= 100;
        else if (b > 10)
            b /= 10;
        sum = a * t + b;
    }
    else
    {
        if ((b / 10) != 0)
        {
            sum += su(b, i + 1);
            t *= 10;
            sum += a * t;
        }
        else
        {
            t *= 10;
            sum = a * t + b;
        }
    }
    return sum;
}

int main()
{
    int n, a = 0, b = 0;
    vector<int> v;
    for (n = 1; n < 1000; n++)
    {
        v.clear();
        for (int i = 0; i < 9; i++)
        {
            int sum = 0;
            t = 1;
            a = i;
            b = n - a;
            if ((b / 10) != 0)
            {
                sum += su(b, i + 1);
                t *= 10;
                sum += a * t;
            }
            else
            {
                t *= 10;
                sum = a * t + b;
            }
            if (sum > -1)
                v.push_back(sum);
        }
        sort(v.begin(), v.end());
        if (!v.empty())
            cout << "n=" << n << ":" << v[0] << endl;
        else
            cout << "n=" << n << ":" << -1 << endl;
    }
    system("pause");
    return 0;
}
