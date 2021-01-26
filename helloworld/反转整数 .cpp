#include <iostream>
using namespace std;

class Integer {
private:
	int _num;
	//getLength()函数获取_num长度
	int getLength() {
	}
public:
	//Integer类构造函数
	Integer(int num) {
		_num = num;
	}
	//反转_num
	int inversed() {
		int s = 0;
		while (_num / 10 != 0) {
			s += (_num % 10);
			s *= 10;
			_num /=10;
		}
		s += _num;
		return s;
	}
};

int main() {
	int n;
	cin >> n;
	Integer integer(n);
	cout << integer.inversed() << endl;
	return 0;
}