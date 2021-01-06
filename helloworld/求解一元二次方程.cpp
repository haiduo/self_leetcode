#include <iostream>
#include <cmath>
using namespace std;

class Equation {
private:
	int _a, _b, _c;
public:
	Equation(int a, int b, int c) {
		_a = a;
		_b = b;
		_c = c;
	}
	void solve() {
		double d;
		if (_a != 0) {
			d = sqrt(pow(_b, 2) - 4 * (__int64)_a * (__int64)_c);
			if (d > 0) {
				cout << 1 << endl;
				cout << "x1=" << (-_b - d) / (2 * (__int64)_a) << "  x2=" << (-_b + d) / (2 * (__int64)_a) << endl;
			}
			else {
				if (d == 0)
				{
					cout << 2 << endl;
					cout << "x1=x2=" << (-_b + d) / (2 * (__int64)_a) << endl;
				}
				else {
					cout << 3 << endl;
					cout << "x1=" << (-_b) / (2 * (__int64)_a) << "+i" << sqrt(4 * (__int64)_a * (__int64)_c - pow(_b, 2))
						<< "  x2=" << (-_b) / (2 * (__int64)_a) << "-i" << sqrt(4 * (__int64)_a * (__int64)_c - pow(_b, 2)) << endl;
				}
			}
		}
		else
		{
			if (_b != 0) {
				cout << 6 << endl;
				cout << "x=" << (-_c) / _b << endl;
			}
			else
				if (_c != 0)
					cout << 4 << " NO solution" << endl;
				else
					cout << 5 << " Infinit  many solutions" << endl;
		}
	}
};

int main() {
	int a, b, c;
	cin >> a >> b >> c;
	Equation tmp(a, b, c);
	tmp.solve();
	return 0;
}