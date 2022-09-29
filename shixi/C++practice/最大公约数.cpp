#include <iostream>
#include <string.h>
#include <math.h>
#include <cstdlib>
using namespace std;

int com_div(int a, int b);
int main()
{
    int a, b, n;
    cout << "input tow number (1<=a,b<=100000000):";
    cin >> a >> b;
    cout << "the biggest common divisor is :" << com_div(a, b) << endl;
    system("pause");
    return 0;
}

int com_div(int a, int b)
{
    if (a == b)
        return a;
    else
       return a > b ? com_div(a - b, b) : com_div(a, b - a);
}

// 方法二
// int com_div(int a, int b);
// int main()
// {
//     int a, b, n;
//     cout << "input tow number (1<=a,b<=100000000):";
//     cin >> a >> b;
//     cout << "the biggest common divisor is :" << com_div(b, a) << endl;
//     system("pause");
//     return 0;
// }

// int com_div(int a, int b)
// {
//     if (a%b==0)
//         return b;
//     else
//        return com_div(b, a%b);
// }