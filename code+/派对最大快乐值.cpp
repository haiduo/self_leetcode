#include <iostream>
#include <vector>
#include <stack> 
using namespace std;

struct Employee {//多叉树
    int happy;
    vector<Employee *> nexts;
    Employee(int h) {
        happy = h;
    }
};
//先序构造二叉树
Employee* CreateBiTree() {
    Employee* current = NULL;
    char value;
    cin >> value;//输入键值
    if (value == '#') {//标识当前子树为空，转向下一节点
        return NULL;
    }
    else {   //递归的创建左右子树
        current = new Employee(value);
        for (Employee *next : current->nexts){
                next = CreateBiTree();    
        }
        return current;
    }
}
//先根遍历 递归
void preOrder(Employee* root) {
    if (root == NULL)
        return;
    else {
        cout << root->happy << "  -->  ";     //首先打印根节点
        for(Employee *next : root->nexts){
            preOrder(next);
        }
    }
}

struct Info { //返回信息的结构体
    int yes;//头节点来时，整棵树的最大值
    int no;//头节点不来时，整棵树的最大值
    Info(int y, int n) {
        yes = y;
        no = n;
    }
};

Info* process(Employee* x) {//返回最大BST的根结点
    if (x->nexts.size() == 0) {//直接下属为空的时候（也就是基层员工）
        return new Info(x->happy, 0);
    }
    int yes = x->happy;//x来的时候
    int no = 0;//x不来的时候
    for (Employee *next : x->nexts){
        Info *nextInfo = process(next);
        yes += nextInfo->no;
        no += max(nextInfo->yes, nextInfo->no);
    }
    return new Info(yes, no);
}

int maxHappy(Employee *boss) {//根节点为老板
    if (boss == NULL){
        return 0;
    }
    Info *all = process(boss);
    return max(all->yes, all->no);//老板来与不来的情况的最大值
}

int main(void) {
    Employee* root = NULL;
    cout << "按前序遍历方式创建树" << endl;
    //"ABDG##H###CE#I##F##";
    root = CreateBiTree(); //构造一个多叉树
    preOrder(root);			//先根遍历 递归
    cout << endl;
    cout << maxHappy(root) << endl;//动态规划，递归
    return 0;
}