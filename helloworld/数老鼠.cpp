#include <iostream>
using namespace std;

class Mouse
{
private:
public:
    static int num;
    Mouse()
    {
        num++;
    }

    Mouse(Mouse &m)
    {
        num++;
    }
    ~Mouse()
    {
        num--;
        cout << "析构函数后：" << Mouse::num << endl;
    }
};

void fn(Mouse m);
int Mouse::num;
int main()
{
    Mouse::num = 0;
    Mouse a;
    cout << Mouse::num << endl;
    Mouse b(a);
    cout << Mouse::num << endl;
    for (int i = 0; i < 10; ++i)
    {
        Mouse x;
        cout << Mouse::num << endl;
    }
    fn(a);
    cout << Mouse::num << endl;
    return 0;
}

void fn(Mouse m)
{
    cout << Mouse::num << endl;
    Mouse n(m);
    cout << Mouse::num << endl;
}