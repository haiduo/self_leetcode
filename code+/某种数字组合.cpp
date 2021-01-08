#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
/* 
递归。以每次两位，也就是十位和个位，每次当遇到 位数（十位）大于等于9 或者 十位大于等于个位时，就停止，
仅仅需要将递增变量t乘以-10,根据最后的和为负数就不添加，为正加入vector，排序，第一个则为最小的，输出。
*/

int t = 1;//全局变量t

int su(int b, int i)
{
    int a, sum = 0;
    a = i;
    b = b - a;
    if (a >= b || a >= 9)//因为只能0-9，所以a等于9就退出，并且a一旦大于等于b就退出，因为下一步就会有重复元素
    {
        t *= -10;
        if (b > 100)//排除后面900以上的大数导致的误差
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
    int n, a = 0, b = 0;//n为输入的正整数，a为第一个加数，b为第二个加数，以a，b为为组合依次遍历，直到找到N所有的加数位数（0-9）不重复。
    vector<int> v;
    for (n = 1; n < 100; n++)
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
