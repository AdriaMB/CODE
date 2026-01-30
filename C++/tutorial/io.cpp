#include <iostream>
#include <string>

int main(){
    std::string name;
    int age;

    /**
    std::cout << "Hello, what is your name? ";
    std::getline(std::cin, name);

    std::cout << "And your age? ";
    std::cin >> age;

    std::cout << "Your name is " << name << " and you are " << age;
    */

    std::cout << "And your age? ";
    std::cin >> age;

    std::cout << "Hello, what is your name? ";
    std::getline(std::cin >> std::ws, name);
    // we have to put the std::ws. If not, it would take the \n from the previous input (the age), and it would considere it as the next line, thus not taking the real name

    std::cout << "Your name is " << name << " and you are " << age;
}
