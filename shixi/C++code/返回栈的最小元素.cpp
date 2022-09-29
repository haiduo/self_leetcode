#include<iostream>  
#include <stack>  
#include <cassert>  
using  namespace std;
/* 
方法 使用两个栈，一个栈用来保存当前的元素，记做：stackData，一个栈用来保存压入操作每一步的最小元素，记做：stackMin。
入栈：当stackData栈中压入一个数据时，判断satckMin中是否为空。若为空，将该元素压入stackMin栈中。若不空，判断两者之间的大小，
当前者小于或等于后者时，将前者中的数据压入后者中；当前者大于后者时，不进行任何操作。
出栈：出栈的时候判断要出栈的元素是否等于辅助栈顶元素，如果是，也将辅助栈顶元素出栈。否则无操作。
*/
class Stack{
public:
	void Push(int data){
		stackData.push(data);
		if (stackMin.empty()){
			stackMin.push(data);
		}
		else{
			if (data <= stackMin.top()){
				stackMin.push(data);
			}
		}
	}
	void Pop(){
		assert(!stackData.empty() && !stackMin.empty());
		if (stackData.top() == stackMin.top())
		{
			stackMin.pop();
		}
		stackData.pop();
	}
	int GetMin(){
		assert(!stackMin.empty());
		return stackMin.top();
	}
 private:
	stack<int> stackData;
	stack<int> stackMin;
};
 int main(){
	Stack s;
	s.Push(25);  
	s.Push(36);
	s.Push(15);
	s.Pop();
	s.Push(50);
	s.Push(53);
	cout << s.GetMin() << endl;
	system("pause");
	return 0;
}//15