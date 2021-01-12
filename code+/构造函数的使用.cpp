#include <iostream>
#include <string>

using namespace std;

class Str{

	string a1;
public:
	Str();
	Str(string &a);
	Str(const Str &str);
	~Str();
	string getstring();
};

	Str::Str(string &a){
		a1=a;
		cout<<"denfine a construct function"<<endl;
	}
	Str::Str(const Str &str){
		this->a1=str.a1;
		cout<<"define a copy construct function"<<endl;
	}
	Str::~Str(){
		cout<<"use a destruct function"<<endl;
	}
	
	string Str::getstring(){
			return a1;
		}

int main(){

	string a="asdsds";
	Str str2(a);
	cout<<str2.getstring()<<endl;
	Str str1(str2);
	cout<<str1.getstring()<<endl;
	return 0;
}