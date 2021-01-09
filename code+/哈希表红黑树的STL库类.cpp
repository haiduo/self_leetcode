#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <set>
#include <map>
#include <vector>

using namespace std;
int main()
{
    vector<int> list;
    list.push_back(5);
    list.push_back(14);
    list.push_back(34);
    list.push_back(22);
    list.push_back(39);
    list.push_back(5);

    unordered_map<int, int> unordered_map1;//std::unordered_map 是以key来查找value而设计,不会根据key排序。
    for (int i = 0; i < list.size(); i++)
        unordered_map1[i] = list[i];
    cout << unordered_map1[0] << endl;
    for (unordered_map<int, int>::iterator i = unordered_map1.begin(); i != unordered_map1.end(); i++)
        cout << i->first << ' ' << i->second << endl;
    if (unordered_map1.find(3) != unordered_map1.end())//unordered_map也有find方法，得到的对象是一个iterator
        cout << "find key=" << unordered_map1.find(3)->first << ", value=" <<unordered_map1.find(3)->second << endl;
    if (unordered_map1.count(5) > 0)
        cout << "find 5: " << unordered_map1.count(5) << endl;//m.count(n)计算下标为n的位置有无数据，有返回1，无返回0

    unordered_set<int> unordered_set1;//std::unordered_set 是基于hash表的，因此并不是顺序存储。
    for (int i=0; i<list.size(); i++)
        unordered_set1.insert(list[i]);
    for (unordered_set<int>::iterator i = unordered_set1.begin(); i != unordered_set1.end(); i++)
        cout << *i << endl;
    cout << "find 39: " << *unordered_set1.find(39) << endl;
    cout << "count 14:" << unordered_set1.count(5) << endl;

    map<int, int> map1;//std::map 就是以key来查找value而设计，根据key排序。
    for (int i=0; i<list.size(); i++)
        map1[i] = list[i];
    for (map<int, int>::iterator i = map1.begin(); i != map1.end(); i++)
        cout << i->first << ' ' << i->second << endl;
    if (map1.find(3) != map1.end())
        cout << "find key=" << map1.find(3)->first << ", value=" << map1.find(3)->second << endl;
    if (map1.count(5) > 0)
        cout << "count 5: " << map1.count(5) << endl;

    set<int> set1;//std::set 是基于hash表的，因此并不是顺序存储。
    for (int i=0; i<list.size(); i++)
        set1.insert(list[i]);
    for (auto i = set1.begin(); i != set1.end(); i++)
        cout << *i << endl;
    cout << *set1.find(5) << endl;
    cout << set1.count(5) << endl;

    system("pause");
    return 0;
}