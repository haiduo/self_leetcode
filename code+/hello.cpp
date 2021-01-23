#include <iostream>

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
bool down;
//i是节点所在的层数，N代表一共多少层， down==true为凹 down==false为凸
void printProcess(int i, int N, bool down) {
    if (i > N) {
        return ;
    }else{
        printProcess(i+1, N, true);
        cout<<(down ? "凹": "凸");
        printProcess(i+1, N, false);
    }
}
//打印纸条经过N此折叠后的凹凸次数
void printAllFolds(int N) {
    printProcess(1, N, true);
}

int main(){
    Node* root = NULL;
    int N=0;
    cin>>N;
    printAllFolds(N);
    return 0;
}