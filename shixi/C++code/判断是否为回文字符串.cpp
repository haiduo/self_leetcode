#include <iostream>
#include <string>

using namespace std;

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
    if (n & 1){
        return "<invalid>";
    }
    string res;
    res.reserve(n >> 1);//3493888
    for (int i = 0; i < n; i += 2){
        res.push_back(str[i]);
    }
    return move(res);
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