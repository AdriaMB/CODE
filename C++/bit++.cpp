#include <iostream>
#include <string>

int main(){
    int n;
    std::cin >> n;
    int res = 0;
    for(int i = 0; i < n ; i++){
        std::string line;
        std::cin >> line;
        char op = line[1];
        switch(op){
            case '+':
                res++;
                break;
            case '-':
                res--;
                break;
            default:
                break;
        }
    }
    std::cout << res;


}
