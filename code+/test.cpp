#include <iostream>
#include <vector>
#include <stack> 
using namespace std;

typedef char ElemType;
//定义一个链表节点
struct Node{
    ElemType data;
    Node *left, *right;
    Node(ElemType value){
		data = value;
		left = NULL;
		right = NULL;
	}
};
//先序构造二叉树
Node* CreateBiTree(){
    Node* current = NULL; 
    ElemType value;
    cin >> value;//输入键值
    if(value == '#'){//标识当前子树为空，转向下一节点
        return NULL;
    }  
    else{   //递归的创建左右子树
        current = new Node(value);
        current->left = CreateBiTree();
        current->right = CreateBiTree();
        return current;
    }
}
//先序遍历 递归
void preOrder(Node* root){
	if(root == NULL)
		return;
	else{
		cout << root->data << "  -->  ";     //首先打印根节点
		preOrder(root->left);				 //接着遍历左子树
		preOrder(root->right);				 //接着遍历右子树
	}
}
//先序遍历 非递归
void preOrder1(Node* root) {
    if (root == NULL) {
        return ;
    }
    else
    {
       stack<Node*> s;
        s.push(root);
        while ( !s.empty()) 
        {
            root = s.top();
            cout<<root->data<<"  -->  ";
            s.pop();
            if(root->right != NULL){
                s.push(root->right);
            }
            if(root->left != NULL){
                s.push(root->left);
            }
        }   
    } 
}

int main(void){
    Node* root=NULL;
    cout << "按前序遍历方式创建树" <<endl;
    //"ABDG##H###CE#I##F##";
    root = CreateBiTree();
    preOrder(root);			//前序遍历 递归
    cout<<endl;
    preOrder1(root);        //前序 非递归   
    return 0;
}