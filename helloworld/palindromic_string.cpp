#include <iostream>
#include <string.h>
#include <math.h>
#include <cstdlib>
using namespace std;

bool palindromic(string s, int i, int j);
int main()
{
    int i = 0, j;
    string s;
    cout << "input a string (s<100000):";
    cin >> s;
    j = s.length() - 1;
    if (s.length() == 0)
    {
        cout << "false";
        system("pause");
        return 0;
    }

    if (palindromic(s, i, j))
        cout << "true" << endl;
    else
        cout << "false" << endl;
    system("pause");
    return 0;
}

bool palindromic(string s, int i, int j)
{
    if (i >= j)
        return true;
    else
    {
        if (s[i] == s[j])
            return palindromic(s, ++i, --j);
        else
            return false;
    }
}
