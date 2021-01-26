#include <iostream>
#include <string>
using namespace std;
int main(){
    //定义一个string类对象
    string http = "www.runoob.com";
    //打印字符串长度
    cout << http.length() << endl;
    //拼接
    http.append("/C++");
    cout << http << endl; //打印结果为：www.runoob.com/C++
    //删除
    int pos = http.find("/C++"); //查找"C++"在字符串中的位置
    cout << pos << endl;
    http.replace(pos, 4, ""); //从位置pos开始，之后的4个字符替换为空，即删除
    cout << http << endl;
    //找子串runoob
    int first = http.find_first_of("."); //从头开始寻找字符'.'的位置
    int last = http.find_last_of(".");  //从尾开始寻找字符'.'的位置
    cout << http.substr(first + 1, last - first - 1) << endl; //提取"runoob"子串并打印
    system("pause");
    return 0;
}