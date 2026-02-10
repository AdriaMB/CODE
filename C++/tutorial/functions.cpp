#include <iostream>
#include <string>

int num = 0;

void happyBirthday(std::string n){
    int num = 1;

    std::cout << n;
    std::cout << ::num; // when putting ::, we refer to the global version of the variable.

}

void second(int age);

int main(){
    std::string name = "Bro";
    int age = 10;
    happyBirthday(name);
    second(age);


    std::cout<<num;

}

void second(int age){
    std::cout << age;

    int num = 2;
    std::cout << num;
}
