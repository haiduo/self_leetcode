#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int i, k = 0, n, count = 0, N;
    vector<int> num;
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        cin >> n;
        num.push_back(n);
    }

    for (int i = 0; i < N; i++)
    {
        if (num[i] == 1)
        {
            count++;
            if (count == 5)
            {
                k++;
                count = 0;
            }
        }
        else
            count = 0;
    }
    cout << k << endl;
    system("pause");
    return 0;
}