#include <iostream>
#include <string>

using namespace std;
/*  
输入：
aabbccbbaa
aabbcccbbaa
输出：
abcba
false
*/
bool is_double_symmetrical(const string &str){
    const int n = str.length();
    if (n & 1){//位与操作
        return false;
    }
    if (n <= 0){
        return true;
    }
    int i1 = 0, i2 = 1, j1 = n - 1, j2 = j1 - 1;
    while (i1 <= j1){
        if (str[i1] != str[i2] || str[j1] != str[j2]){//判断前后是否为重复字符
            return false;
        }
        if (str[i1] != str[j1]){//判断是否为回文
            return false;
        }
        i1 += 2;
        i2 += 2;
        j1 -= 2;
        j2 -= 2;
    }
    return true;
}

string deduplicate(const string &str){
    if (str.empty()){
        return "";
    }
    const int n = str.length();
    if (n & 1){//deduplicate()依赖上一个函数的结果，如果上一个函数的逻辑不对，在这里加判断能够快速定位问题
        return "<invalid>";
    }
    string res;
    res.reserve(n >> 1);// 确定新的分配存储的最小长度
    for (int i = 0; i < n; i += 2){
        res.push_back(str[i]);
    }
    return move(res);//将一个左值强制转化为右值引用，继而可以通过右值引用使用该值，以用于移动语义。从实现上讲，std::move基本等同于一个类型转换：static_cast<T&&>(lvalue);
}

int main(){
    string str;
    while(cin>>str){
        if (is_double_symmetrical(str)){
            cout << deduplicate(str) << endl;
        }
        else{
            cout<<"false"<<endl;
        }
    }
    return 0;
}