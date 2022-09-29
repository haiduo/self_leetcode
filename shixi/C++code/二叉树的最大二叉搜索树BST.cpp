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
//方法1
void in(Node* root, vector<Node*> &arr) {//复制二叉树的节点信息到vector
    if (root == NULL) {
        return;
    }
    in(root->left, arr);
    arr.push_back(root);
    in(root->right, arr);
}

int getBSTSize(Node* curroot) {//判断是否为BST，若是返回大小
    if (curroot == NULL) {
        return 0;
    }
    vector<Node*> arr;
    in(curroot, arr);
    for (int i = 1; i < arr.size(); i++)
    {
        if (arr[i]->data <= arr[i - 1]->data) {
            return 0;
        }
    }
    return arr.size();
}

int maxSubBSTSize1(Node* root) {//求最大BST的大小(BST的节点数) 方法1
    if (root == NULL) {
        return 0;
    }
    int h = getBSTSize(root);
    if (h != 0) {
        return h;//这棵二叉树为BST，返回大小
    }
    return max(maxSubBSTSize1(root->left), maxSubBSTSize1(root->right));
}

//方法2
struct Info { //任何子树，返回信息的结构体
    bool isBST; //是否整体全是BST
    int maxSubBSTSize; //最大的满足BST的节点个数
    int minval; //整棵树的最小值
    int maxval; //整棵树的最大值
    Info(bool is, int size, int mi, int ma) {
        isBST = is;
        maxSubBSTSize = size;
        minval = mi;
        maxval = ma;
    }
};

Info* process(Node* root) {//返回最大BST的根结点
    if (root == NULL) {
        return NULL;
    }
    Info* leftInfo = process(root->left);
    Info* rightInfo = process(root->right);
    int minval = root->data;
    int maxval = root->data;
    int maxSubBSTSzie = 0;
    if (leftInfo != NULL) {
        minval = min(minval, leftInfo->minval);
        maxval = max(maxval, leftInfo->maxval);
        maxSubBSTSzie = max(maxSubBSTSzie, leftInfo->maxSubBSTSize);
    }
    if (rightInfo != NULL) {
        minval = min(minval, rightInfo->minval);
        maxval = max(maxval, rightInfo->maxval);
        maxSubBSTSzie = max(maxSubBSTSzie, rightInfo->maxSubBSTSize);
    }
    bool isBST = false;
    if ((leftInfo == NULL ? true : (leftInfo->isBST && leftInfo->maxval < root->data)) &&
        (rightInfo == NULL ? true : (rightInfo->isBST && rightInfo->minval > root->data))) {
        isBST = true;
        maxSubBSTSzie = (leftInfo == NULL ? 0 : leftInfo->maxSubBSTSize) + (rightInfo == NULL ? 0 : rightInfo->maxSubBSTSize) + 1;
    }
    return new Info(isBST, maxSubBSTSzie, minval, maxval);
}

int maxSubBSTSize2(Node* root) {//求二叉树的最大BST 方法二
    if (root == NULL) {
        return 0;
    }
    return process(root)->maxSubBSTSize;
}

int main(void) {
    Node* root = NULL, * curnode = NULL, * nextnode = NULL;
    cout << "按前序遍历方式创建树" << endl;
    //"ABDG##H###CE#I##F##";
    root = CreateBiTree(); //构造一个二叉树
    preOrder(root);			//前序遍历 递归
    cout << endl;
    cout << maxSubBSTSize1(root) << endl;//方法1，向量数组，递归
    cout << maxSubBSTSize2(root) << endl;//方法2，动态规划，递归
    return 0;
}