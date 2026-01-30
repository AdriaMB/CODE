#include <iostream>
#include <string>

int main(){
    std::string name;

    std::cout << "Enter your name \n";
    std::getline(std::cin, name);

    if(!name.empty()){

        std::cout << "Your name is " << name << "\n";
        std::cout << "The index of your first white space is: " << name.find(' ') << "\n";

        name.append("@gmail.com");
        std::cout << "Your name is now " << name << "\n";

        std::cout << name.at(0) << "\n";

        name.insert(0, "@");
        std::cout << name << "\n";

        std::cout << name.erase(0, 3); // the first is inclusive, the last is not inclusive

        name.clear();


    }
    else{
        std::cout << "You didn't put anything\n";

    }



}
