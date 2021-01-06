#include <iostream>
using namespace std;

int main() {
    int n, sum=1;
    cout<<"the number of days:";
    cin >> n;
    if (n == 1)
        cout << 1;
    else{
        for (int i = 1; i < n; i++){
            sum = (sum + (n-i)) * 2;
        }
        cout <<"the sum of peaches:"<< sum << endl;
    }
	system("pause");
    return 0;
}