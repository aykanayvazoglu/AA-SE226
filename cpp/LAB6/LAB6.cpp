#include <iostream>
#include <cmath>
using namespace std;

float recursive(int m){
    if(m==0){
        return 0;
    }
    else {
        return (pow((-1),(m+1))/m) + recursive((m-1)); // ^ is NOT the power operator. Disappointing
    }
}

float recursive(){
    int m = 0;
    cout << "Please enter an m (Overloaded!): ";
    cin >> m;

    if(m==0){
        return 0;
    }
    else {
        return (pow((-1),(m+1))/m) + recursive((m-1)); // ^ is NOT the power operator. Disappointing
    }
}

int main() {
    int x = 0;
    cout << "Please enter a number: ";
    cin >> x;
    cout << recursive(x) << endl;
    cout << recursive() << endl;
}
