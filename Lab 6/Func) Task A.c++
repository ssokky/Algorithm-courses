#include <iostream>
using namespace std;

int min(int a, int b, int c, int d) {
    int min_value = a;
    
    if (b < min_value) {
        min_value = b;
    }
    
    if (c < min_value) {
        min_value = c;
    }
    
    if (d < min_value) {
        min_value = d;
    }
    
    return min_value;
}

int main() {
    int a, b, c, d;
    cin >> a >> b >> c >> d;
    
    int result = min(a, b, c, d);
    
    cout << result << endl;
    
    return 0;
}
