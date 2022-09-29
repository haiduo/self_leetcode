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

struct Info {//Info 返回信息的结构体
    bool isBalanced;
    int height;
    Info (bool b, int h ) {
        isBalanced = b;
        height = h;
    }
};

Info * process(Node *root) {
    if (root == NULL) {
        return new Info(true, 0);
    }
    Info *leftInfo = process(root->left);
    Info *rightInfo = process(root->right);
    int height = max(leftInfo->height, rightInfo->height) + 1;
    bool isBalanced = true;
    if (!leftInfo->isBalanced || !rightInfo->isBalanced || abs(leftInfo->height - rightInfo ->height) > 1){
        isBalanced =false;
    }
    return new Info(isBalanced, height);
}

bool isBalanced(Node *root) {
    return process(root)->isBalanced;
}

int main(void) {
    Node* root = NULL, * curnode = NULL, * nextnode = NULL;
    cout << "按前序遍历方式创建树" << endl;
    //"ABDG##H###CE#I##F##";
    root = CreateBiTree(); //构造一个二叉树
    preOrder(root);			//前序遍历 递归
    cout<<endl;
    cout << isBalanced(root)<<endl;//是否为平衡二叉树
    return 0;
}