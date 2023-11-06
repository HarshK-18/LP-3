#include <iostream>
using namespace std;

// Function to calculate Fibonacci number using recursion
int fibonacci(int n) {
    if (n <= 1) {
        return n;
    } else {
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
}

int main() {
    int n;
    cout << "Enter the number of terms you want in the Fibonacci series: ";
    cin >> n;
    
    cout << "Fibonacci Series using recursion: ";
    for (int i = 0; i < n; ++i) {
        cout << fibonacci(i) << " ";
    }
    cout<<endl;
    cout<<fibonacci(n);
    return 0;
}


//Non Recursive Approach
#include <iostream>

int fibonacci(int n) {
    if (n <= 1) {
        return n;
    }

    int prev = 0;
    int current = 1;
    int next;

    for (int i = 2; i <= n; ++i) {
        next = prev + current;
        prev = current;
        current = next;
    }

    return current;
}

int main() {
    int n;
    std::cout << "Enter the number of terms in Fibonacci series: ";
    std::cin >> n;

    std::cout << "Fibonacci series using non-recursive approach:" << std::endl;
    for (int i = 0; i < n; ++i) {
        std::cout << fibonacci(i) << " ";
    }

    std::cout << std::endl;
    return 0;
}
