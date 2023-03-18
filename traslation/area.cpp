#include <iostream>

int area(int width, int height) {
    int area = width * height;
    return area;
}

int main() {
    std::cout << area(4, 3) << std::endl;
    return 0;
}