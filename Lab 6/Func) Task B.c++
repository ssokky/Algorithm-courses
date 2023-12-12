#include <iostream>
using namespace std;

double power(double a, int n) {
    double result = 1.0;
    
    for (int i = 0; i < n; ++i) {
        result *= a;
    }
    
    return result;
}

int main() {
    double a;
    int n;
    
    cin >> a >> n;
    
    double result = power(a, n);
    
    cout << result << endl;
    
    return 0;
}
