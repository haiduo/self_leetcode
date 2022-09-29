#include <iostream>
#include <string.h>
#include <regex>
#include <stdlib.h>
#include <sstream>

using namespace std;

bool ipCheck(string str);
bool ipCheck2(char *str);
bool checkIP(string tempIP);
void output(bool b);
int main()
{
    string strIP;
    //方法一
    output(ipCheck("23.135.2.255"));
    output(ipCheck("065.135.2.255"));
    output(ipCheck("0.135.2.256"));
    output(ipCheck(".135.2.256"));
    //方法二
    char str[] = ".135.2.255";
    output(ipCheck2(str));
    //方法三
    getline(cin, strIP);
    output(checkIP(strIP));
    return 0;
}

//方法一：正则表达式
bool ipCheck(string str)
{
    if (!str.empty())
    {
        // 定义正则表达式
        //ip地址范围：(1~255).(0~255).(0~255).(0~255)
        string ipRegEx = "^([1-9]|([1-9][0-9])|(1[0-9][0-9])|(2[0-4][0-9])|(25[0-5]))(\\.([0-9]|([1-9][0-9])|(1[0-9][0-9])|(2[0-4][0-9])|(25[0-5]))){3}$";

        // 判断ip地址是否与正则表达式匹配
        if (regex_match(str, regex(ipRegEx)))
            return true;
        else
            return false;
    }
    return false;
}

//方法二：拆分成字符串动态数组判断
bool ipCheck2(char *str)
{
    if (string(str).empty())
        return false;
    char *buf = NULL;
    char *ptr = NULL;
    int n = 0;
    ptr = strtok_s(str, ".", &buf);
    char **parts = new char *[4];
    while (ptr != NULL)
    {
        *(parts + n) = ptr;
        ptr = strtok_s(NULL, ".", &buf);
        n++;
    }

    //不是4段，false
    if (n != 4)
    {
        delete[] parts;
        return false;
    }
    for (int i = 0; i < n; i++)
    {
        try
        {
            int num = atoi(parts[i]);
            //如果不在正确范围，并且考虑前导0，即 065.192.168.211
            if (num < 0 || num > 255 || (num != 0 && parts[i][0] == '0'))
            {
                delete[] parts;
                return false;
            }
        }
        catch (exception e)
        { //数字格式异常
            cout << "ipv4 format error!" << endl;
            delete[] parts;
            return false;
        }
    }
    return true;
}

//方法三：拆分成字符串向量判断
//注意：当字符串为空时，也会返回一个空字符串
void split(string &s, string &delim, vector<string> *ret)
{
    size_t last = 0;
    size_t index = s.find_first_of(delim, last);
    while (index != string::npos)
    {
        if (index - last > 0)
        {
            ret->push_back(s.substr(last, index - last));
        }
        last = index + 1;
        index = s.find_first_of(delim, last);
    }
    if (index - last > 0)
    {
        ret->push_back(s.substr(last, index - last));
    }
}

bool checkIP(string tempIP)
{
    vector<string> str;
    string delim = ".";
    split(tempIP, delim, &str); //分割字符串
    if (str.size() != 4)
    {
        return false;
    }
    else
    {
        for (vector<string>::iterator iter = str.begin(); iter != str.end(); ++iter)
        {
            int transInt = 0;
            stringstream ss;
            ss << (*iter);
            if (*iter != "0" && (*iter)[0] == '0')
            {
                return false;
            }
            ss >> transInt;
            if (transInt < 0 || transInt > 255) //判断是否是合法的数字
            {
                return false;
            }
        }
        return true;
    }
}

void output(bool b)
{
    if (b)
    {
        cout << "YES" << endl;
    }
    else
    {
        cout << "NO" << endl;
    }
}
