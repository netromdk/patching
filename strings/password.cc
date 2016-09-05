#include <string>
#include <iostream>

int main() {
  std::string attempt;
  for (;;) {
    std::cout << "Password: ";
    std::cin >> attempt;
    if (attempt == "AK9FJ31P") {
      std::cout << "You've entered the correct password!\n";
      return 0;
    }
    std::cout << "Invalid!\n";
  }
  return -1;
}
