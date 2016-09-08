#include <iostream>
#include <unistd.h>

int main() {
  int score = 20; // 0x14
  while (true) {
    std::cout << "score = " << score << "\n";
    sleep(1);
  }
  return 0;
}
