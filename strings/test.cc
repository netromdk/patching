#include <string>
#include <iostream>

const std::string str("std::string example.");
const char *cstr = "And a char* string, too.";

int main() {
  std::cout << str << "\n"
            << cstr << "\n";
  return 0;
}
