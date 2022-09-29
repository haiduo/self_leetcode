#include <stdio.h>

struct Point{
    double x;
    double y;
};

double mult(Point a, Point b, Point c){
    return (b.y-c.y)*(a.x-c.x) - (b.x-c.x)*(a.y-c.y);
}

bool solution(Point aa, Point bb, Point cc, Point dd){
    if(mult(aa, cc, dd)*mult(bb, cc, dd)>0){
        return false;
    }
    if(mult(cc, aa, bb)*mult(dd, aa, bb)>0){
        return false;
    }
    return true;
}

int main(){
    Point aa = {0.0, 0.0};
    Point bb = {10.0, 10.0};
    Point cc = {0.0, 0.0};
    Point dd = {10.0, -10.0};
    bool ret;
    ret = solution(aa, bb, cc, dd);
    printf("%d\n", ret);
    return 0;
}