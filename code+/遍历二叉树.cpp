#include <iostream>
#include <vector>
#include <stack> 
#include <queue>
#include <unordered_map>
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
    }else{
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

//后序遍历 非递归 两个栈
void preOrder2(Node* root) {
    if (root == NULL) {
        return ;
    }else{
        stack<Node*> s;
        stack<Node*> s1;
        s.push(root);
        while ( !s.empty()) 
        {
            root = s.top();
            s1.push(root);
            s.pop();            
            if(root->left != NULL){
                s.push(root->left);
            }
            if(root->right != NULL){
                s.push(root->right);
            }
        }   
         while ( !s1.empty()) 
        {
            root = s1.top();
            cout<<root->data<<"  -->  ";
            s1.pop();
        }
    } 
}

//后序遍历 非递归 一个栈
void preOrder2_1(Node* root) {
    if (root == NULL) {
        return ;
    }else{
        stack<Node*> s;
        s.push(root);
        Node* c=NULL;
        while ( !s.empty()) 
        {
            c = s.top();          
            if(c->left != NULL && root != c->left && root != c->right ){
                s.push(c->left);
            }else if (c->right != NULL && root != c->right){
                s.push(c->right);
            }else{
                root = s.top();
                cout<<root->data<<"  -->  ";
                s.pop();
                root = c;
            }
        }
    } 
}

//中序遍历 非递归
void preOrder3(Node* root) {
    if (root == NULL) {
        return ;
    }else{
        stack<Node*> s;
        while ( !s.empty() || root != NULL) 
        {
            if(root != NULL){
                s.push(root);
                root = root->left;
            }else{
                root = s.top();
                cout<<root->data<<"  -->  ";
                s.pop();
                root = root->right;
            }
        }   
    } 
}

void level(Node *root){
    if (root == NULL){
        return;
    }else{
        queue <Node *> q;
        q.push(root);
        while (!q.empty()){
            Node* cur = q.front();
            cout << cur->data <<"  -->  ";
            q.pop();
            if (cur->left != NULL){
                q.push(cur->left);
            }
            if (cur->right != NULL){
                q.push(cur->right); 
            }
        }
    }
}

int maxWidthUseMap (Node* root){
    if(root == NULL){
        return 0;
    }else{
        queue<Node*> q;
        q.push(root);
        //key,在那一层value
        unordered_map<Node* ,int> levelmap;
        levelmap[root]=1;
        int curLevel =1;//当前正在统计那一层
        int curLevelWidth = 0;//当前层curLeveld的宽度
        int maxwidth = 0;//记录最大的层的宽度
        while (!q.empty()){
            Node* cur = q.front();
            q.pop();
            int curNodeLevel = levelmap[cur]; //当前节点所在哪一层
            if(cur->left != NULL) {
                levelmap[cur->left] = curNodeLevel + 1;
                q.push(cur->left);
            }
            if(cur->right != NULL) {
                levelmap[cur->right] = curNodeLevel + 1;
                q.push(cur->right);
            }
            if (curNodeLevel == curLevel){
                curLevelWidth++; //若当前节点还在当前层，则当前层宽度加1
            }else{
                maxwidth = max(maxwidth , curLevelWidth);//否则比较是否为最大宽度层
                curLevel++; //进入下一层
                curLevelWidth = 1; //从下一层的第一个结点开始，宽度为1，继续上述操作
            }
        }
        maxwidth = max(maxwidth , curLevelWidth); //上述是每到下一层比较上一层的宽度，最后一层没有下一层统计，所以需要专门比较
        return maxwidth;
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
    cout<<endl;   
    preOrder2(root);        //后序 两个栈 非递归  
    cout<<endl;   
    preOrder2_1(root);        //后序 一个栈 非递归  
    cout<<endl;   
    preOrder3(root);        //中序 非递归  
    cout<<endl;   
    level(root);        //层次 队列   
    cout<<endl;   
    cout<<maxWidthUseMap(root);        //树的宽度 队列  
    return 0;
}