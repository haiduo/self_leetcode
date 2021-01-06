#include <iostream>
#include <iomanip>
#include <vector>
using namespace std;
//matrix:螺旋矩阵 (x,y)第一个元素的坐标 start为第一个元素的值 n为矩阵的大小 
void setMatrix(int **matrix, int x, int y, int start, int n){
	if(n<=0)
		return;
	if(n==1){
		matrix[x][y] = start;
		return;
	}
	//上边 
	for(int j=y; j<n+y-1; ++j){
		matrix[x][j] = start++;
	}
	//右边
	for(int i=x; i<x+n-1; ++i){
		matrix[i][x+n-1] = start++;
	}
	//下边
	for(int j=n+y-1; j>y; --j){
		matrix[n+x-1][j] = start++;
	}
	//左边
	for(int i=x+n-1; i>x; --i){
		matrix[i][y] = start++;
	} 
	//递归 
	setMatrix(matrix, x+1, y+1, start, n-2);	
}

int main(){
    int n;
    cout<<"input n of square:";
	cin >> n;
	int **matrix = new int*[n]; //螺旋矩阵（二维数组）分配空间 
	for (int i = 0; i<n; i++){
		matrix[i] = new int[n];
	}
	setMatrix(matrix, 0, 0, 1, n);
    //打印螺旋矩阵
  	for(int i = 0; i < n; i++) {
      	for (int j = 0; j < n; j++)
      		cout << setw(4) << matrix[i][j];
    	cout << endl;
   	}
    system("pause");
	return 0;
} 
