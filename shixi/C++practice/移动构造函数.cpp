#include <iostream>

using namespace std;

class IntNum
{

public:
    IntNum(int x = 0) : xptr(new int(x))
    { //构造函数

        cout << "Calling constructor..." << endl;
    }

    IntNum(const IntNum &n) : xptr(new int(*n.xptr))
    { //复制构造函数

        cout << "Calling copy constructor..." << endl;
    }
    /* 注：
    &&是右值引用，也就是函数返回的临时变量是右值 
    &是左值引用，也就是还存活的变量，类似数组元素
    */
    IntNum(IntNum &&n) : xptr(n.xptr)
    { //移动构造函数

        n.xptr = nullptr;
        //将传进来的临时对象（形参）的成员数据指针变为空指针，
        //并不是对当前对象（this）的成员数据指针,因为一个对象（借助成员数据指针）只能释放一次。

        cout << "Calling move constructor..." << endl;
    }

    ~IntNum()
    { //析构函数

        delete xptr;

        cout << "Destructing..." << endl;
    }
    int getInt() { return *xptr; }

private:
    int *xptr;
};

//返回值为IntNum类对象

IntNum getNum()
{

    IntNum a;

    return a;
}

int main()
{
    cout << getNum().getInt() << endl;
    return 0;
    system("pause");
}