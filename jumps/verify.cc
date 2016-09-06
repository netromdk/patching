#include <iostream>

bool verify(int n);

int main() {
  int input;
  std::cout << "Serial number: ";
  std::cin >> input;
  if (verify(input)) {
    std::cout << "Correct!\n";
  }
  else {
    std::cout << "Incorrect!\n";
  }
  return 0;
}

bool verify(int n) {
  return n % 2 == 0;
}
