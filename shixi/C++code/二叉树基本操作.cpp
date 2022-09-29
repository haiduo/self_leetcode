#include <iostream>
#include <vector>
#include <stack> 
#include <queue>
#include <unordered_map>
#include <string>
#include <iomanip>
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
//先序遍历 非递归
void preOrder1(Node* root) {
    if (root == NULL) {
        return;
    }
    else {
        stack<Node*> s;
        s.push(root);
        while (!s.empty())
        {
            root = s.top();
            cout << root->data << "  -->  ";
            s.pop();
            if (root->right != NULL) {
                s.push(root->right);
            }
            if (root->left != NULL) {
                s.push(root->left);
            }
        }
    }
}

//后序遍历 非递归 两个栈
void preOrder2(Node* root) {
    if (root == NULL) {
        return;
    }
    else {
        stack<Node*> s;
        stack<Node*> s1;
        s.push(root);
        while (!s.empty())
        {
            root = s.top();
            s1.push(root);
            s.pop();
            if (root->left != NULL) {
                s.push(root->left);
            }
            if (root->right != NULL) {
                s.push(root->right);
            }
        }
        while (!s1.empty())
        {
            root = s1.top();
            cout << root->data << "  -->  ";
            s1.pop();
        }
    }
}

//后序遍历 非递归 一个栈
void preOrder2_1(Node* root) {
    if (root == NULL) {
        return;
    }
    else {
        stack<Node*> s;
        s.push(root);
        Node* c = NULL;
        while (!s.empty())
        {
            c = s.top();
            if (c->left != NULL && root != c->left && root != c->right) {
                s.push(c->left);
            }
            else if (c->right != NULL && root != c->right) {
                s.push(c->right);
            }
            else {
                root = s.top();
                cout << root->data << "  -->  ";
                s.pop();
                root = c;
            }
        }
    }
}

//中序遍历 非递归
void preOrder3(Node* root) {
    if (root == NULL) {
        return;
    }
    else {
        stack<Node*> s;
        while (!s.empty() || root != NULL)
        {
            if (root != NULL) {
                s.push(root);
                root = root->left;
            }
            else {
                root = s.top();
                cout << root->data << "  -->  ";
                s.pop();
                root = root->right;
            }
        }
    }
}
//层次 队列
void level(Node* root) {
    if (root == NULL) {
        return;
    }
    else {
        queue <Node*> q;
        q.push(root);
        while (!q.empty()) {
            Node* cur = q.front();
            cout << cur->data << "  -->  ";
            q.pop();
            if (cur->left != NULL) {
                q.push(cur->left);
            }
            if (cur->right != NULL) {
                q.push(cur->right);
            }
        }
    }
}
//二叉树的宽度 使用哈希字典
int maxWidthUseMap(Node* root) {
    if (root == NULL) {
        return 0;
    }
    else {
        queue<Node*> q;
        q.push(root);
        //key,在那一层value
        unordered_map<Node*, int> levelmap;
        levelmap[root] = 1;
        int curLevel = 1;//当前正在统计那一层
        int curLevelWidth = 0;//当前层curLeveld的宽度
        int maxwidth = 0;//记录最大的层的宽度
        while (!q.empty()) {
            Node* cur = q.front();
            q.pop();
            int curNodeLevel = levelmap[cur]; //当前节点所在哪一层
            if (cur->left != NULL) {
                levelmap[cur->left] = curNodeLevel + 1;
                q.push(cur->left);
            }
            if (cur->right != NULL) {
                levelmap[cur->right] = curNodeLevel + 1;
                q.push(cur->right);
            }
            if (curNodeLevel == curLevel) {
                curLevelWidth++; //若当前节点还在当前层，则当前层宽度加1
            }
            else {
                maxwidth = max(maxwidth, curLevelWidth);//否则比较是否为最大宽度层
                curLevel++; //进入下一层
                curLevelWidth = 1; //从下一层的第一个结点开始，宽度为1，继续上述操作
            }
        }
        maxwidth = max(maxwidth, curLevelWidth); //上述是每到下一层比较上一层的宽度，最后一层没有下一层统计，所以需要专门比较
        return maxwidth;
    }
}
//二叉树的宽度 未使用哈希字典
int maxWidthNoMap(Node* root) {
    if (root == NULL) {
        return 0;
    }
    else {
        queue<Node*> q;
        q.push(root);
        Node* curEnd = root;//当前层，最右节点是谁
        Node* nextEnd = NULL;//下一层，最右节点是谁
        int curLevelWidth = 0;//当前层curLeveld的宽度(也就是当前层的节点数)
        int maxwidth = 0;//记录最大的层的宽度
        while (!q.empty()) {
            Node* cur = q.front();
            q.pop();
            if (cur->left != NULL) {
                q.push(cur->left);
                nextEnd = cur->left;
            }
            if (cur->right != NULL) {
                q.push(cur->right);
                nextEnd = cur->right;
            }
            curLevelWidth++; //当前层每弹出一个节点，则当前层宽度加1
            if (cur == curEnd) {
                maxwidth = max(maxwidth, curLevelWidth);//比较是否为最大宽度层
                curLevelWidth = 0; //从下一层开始, 没有弹出任何节点，宽度为0，继续上述操作
                curEnd = nextEnd;
            }
        }
        return maxwidth;
    }
}

//二叉树的序列化 先序001
void pres(Node* root, queue<ElemType> &ans) {
    if (root == NULL) {
        ans.push('#');
    }
    else {
        ans.push(root->data); //中
        pres(root->left, ans); //左
        pres(root->right, ans); //右
    }
}
//二叉树的序列化 001
queue<ElemType> preSerial(Node* root) {
    queue<ElemType> prelist;
    pres(root, prelist);
    return prelist;
}

//由序列化构建二叉树 先序002
Node* preb(queue<ElemType> &ans) {
    ElemType data = ans.front();
    ans.pop();
    Node* root = NULL;
    if (data == '#') { //标识当前子树为空，转向下一节点
        return NULL;
    }
    else {//递归的创建左右子树
        root = new Node(data); //中
        root->left = preb(ans); //左
        root->right = preb(ans); //右
        return root;
    }
}
//反序列化 由序列化构建二叉树 先序002
Node* buildByPreQueue(queue<ElemType> prelist) {
    if (prelist.size() == 0) {
        return NULL;
    }
    else {
        return preb(prelist);
    }
}

//层次序列化 队列
queue<ElemType> levelSerial(Node* root) {
    queue<ElemType> ans;
    if (root == NULL) {
        ans.push('#');
    }
    else {
        ans.push(root->data);
        queue <Node*> q;
        q.push(root);
        while (!q.empty()) {
            root = q.front();
            q.pop();
            if (root->left != NULL) {
                ans.push(root->left->data);
                q.push(root->left);
            }else{
                ans.push('#');
            }
            if (root->right != NULL) {
                ans.push(root->right->data);
                q.push(root->right);
            }else{
                ans.push('#');
            }
        }
    }
    return ans;
}

//按层次反序列化 队列
Node* generateNode(ElemType data){
    if(data == '#'){
        return NULL;
    }
    return new Node(data);
}
//按层次反序列化 队列
Node* buildByLevelQueue(queue<ElemType> levelist) {
    if (levelist.size() == 0) {
        return NULL;
    }
    else {
        ElemType data = levelist.front();
        levelist.pop();
        Node* root = generateNode(data);
        queue <Node*> q;
        if (root != NULL){
            q.push(root);
        }
        Node *node = NULL;
        while (!q.empty()) {
            node = q.front();
            q.pop();
            ElemType data1 = levelist.front();
            levelist.pop();
            node->left = generateNode(data1);
            ElemType data2 = levelist.front();
            levelist.pop();
            node->right = generateNode(data2);
            if (node->left != NULL) {
                q.push(node->left);
            }
            if (node->right != NULL) {
                q.push(node->right);
            }
        }
        return root;
    }
}
//打印二叉树
void printInOrder(Node * root, int height, string to, int len ){
    if(root == NULL){
        return ;
    }else{
        printInOrder(root->right, height + 1, "v", len);//V表示指向父节点
        string val = to + root->data + to;
        cout.width((height * len) + len);          // 设置显示域宽10 
        cout.fill(' ');          // 在显示区域空白处用' '填充
        cout<<setiosflags(ios::right);   // 设置右对齐
        cout<<val<<endl;
        printInOrder(root->left, height + 1, "^", len);//^表示指向父节点
    }
}

int main(void) {
    Node* root = NULL;
    cout << "按前序遍历方式创建树" <<endl;
    //"ABDG##H###CE#I##F##"; #表示空节点
    root = CreateBiTree(); //构造一个二叉树

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

    cout<<maxWidthUseMap(root);        //二叉树的宽度 队列+map
    cout<<endl; 
    cout<<maxWidthNoMap(root);        //二叉树的宽度 队列
    cout << endl;

    queue<ElemType> ans = preSerial(root);        //二叉树的按先序序列化 队列
    queue<ElemType> prelist;
    while (!ans.empty()) {
        cout << ans.front();
        prelist.push(ans.front());
        ans.pop();
    }
    cout << endl;
    root = buildByPreQueue(prelist);        //反序列化构建二叉树 队列
    preOrder(root);			//前序遍历 递归
    cout << endl;

    queue<ElemType> ans1 = levelSerial(root);        //二叉树的按层次序列化 队列
    queue<ElemType> prelist1;
    while (!ans1.empty()) {
        cout << ans1.front();
        prelist1.push(ans1.front());
        ans1.pop();
    }
    cout << endl;

    root = buildByLevelQueue(prelist1);        //反序列化构建二叉树 队列
    preOrder(root);			//前序遍历 递归
    cout << endl;
    printInOrder(root, 0, "H",  5);//打印二叉树 横着打印 H代表头节点，0表示当前高度，5为数值data的宽度

    system("pause");
    return 0;
}