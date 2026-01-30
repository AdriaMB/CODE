#include <iostream>

namespace first{
    int x = 1;
    int y = 1;

}
namespace second{
    int x = 2;
}

int main(){
    /**
    int x = 0;
    std::cout << x; // prints value x = 0
    std::cout << first::x;
    std::cout << second::x<<"\n";

    using namespace first; // we can put it anywhere, it seems
    std::cout << x; // it still prints x = 0 because in the namespace of main, x=0 was defined
    std::cout << y; // y only exists in namespace first
    std::cout << first::x;
    std::cout << second::x<<"\n";
    */

    using  std::cout;
    using  std::string;
    cout << "This message has no std::cout, only cout\n";
    string example = "And this is a string without the std";
    cout << example;

    return 0;

}
