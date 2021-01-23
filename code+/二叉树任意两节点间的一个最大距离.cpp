#include <iostream>
#include <vector>
#include <stack> 
using namespace std;

typedef char ElemType;
//定义一个链表节点
struct Node {
    ElemType data;
    Node* left, * right;
    Node(ElemType value) {
        data = value;
        left = NULL;
        right = NULL;
    }
};
//先序构造二叉树
Node* CreateBiTree() {
    Node* current = NULL;
    ElemType value;
    cin >> value;//输入键值
    if (value == '#') {//标识当前子树为空，转向下一节点
        return NULL;
    }
    else {   //递归的创建左右子树
        current = new Node(value);
        current->left = CreateBiTree();
        current->right = CreateBiTree();
        return current;
    }
}
//先序遍历 递归
void preOrder(Node* root) {
    if (root == NULL)
        return;
    else {
        cout << root->data << "  -->  ";     //首先打印根节点
        preOrder(root->left);				 //接着遍历左子树
        preOrder(root->right);				 //接着遍历右子树
    }
}

struct Info { //任何子树，返回信息的结构体
    int maxDistance;
    int height;
    Info(int dis, int h) {
        maxDistance = dis;
        height = h;
    }
};

Info* process(Node* root) {//返回最大BST的根结点
    if (root == NULL) {
        return new Info(0, 0);
    }
    Info* leftInfo = process(root->left);
    Info* rightInfo = process(root->right);
    int height = max(leftInfo->height, rightInfo->height) + 1;
    int maxDistance = max(
        max(leftInfo->maxDistance, rightInfo->maxDistance),//跟当前节点无关的左右子树的最大距离
        leftInfo->height + rightInfo->height + 1);//跟当前节点有关的，左右子树的高度加上当前节点
    return new Info(maxDistance, height);
}

int maxDistance(Node* root) {//求二叉树的最大BST 方法二
    return process(root)->maxDistance;
}

int main(void) {
    Node* root = NULL, * curnode = NULL, * nextnode = NULL;
    cout << "按前序遍历方式创建树" << endl;
    //"ABDG##H###CE#I##F##";
    root = CreateBiTree(); //构造一个二叉树
    preOrder(root);			//前序遍历 递归
    cout << endl;
    cout << maxDistance(root) << endl;//递归
    return 0;
}