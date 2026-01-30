#include <iostream>
#include <string>


void happyBirthday(std::string n){
    std::cout << n;

}

void second(int age);

int main(){
    std::string name = "Bro";
    int age = 10;
    happyBirthday(name);
    second(age);

}

void second(int age){
    std::cout << age;


}
