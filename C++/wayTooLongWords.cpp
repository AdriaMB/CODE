#include <iostream>
#include <string>


int main(){
    int iterations;
    std::cin  >> iterations; // number of repetitions
    for(int i = 0; i < iterations; i++){
       std::string word;
       std::cin >> word; // word
       int length = word.length();
       if(length > 10){
           std::cout << word[0] + std::to_string(length-2) + word[length-1] + "\n";
       }
       else{
            std::cout << word + "\n";
       }
    }
}
