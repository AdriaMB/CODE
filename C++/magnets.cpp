#include <iostream>
#include <string>

int main(){
    int groups = 0; // minimum there is going to be a group

    int n; // number of lines
    std::cin >> n;



    char prev = '-';
    for(int i = 0; i < n; i++){
        std::string magnet;
        std::cin >> magnet;
        char first = magnet[0]; // first charge. returns a char


        switch(first){
            case '0':

                //std::cout << "Previous     First\n";
                //std::cout << prev << "            " << first << "\n\n";

                if(prev == '0'){
                    //std::cout << "New group \n";
                    groups++;
                }
                prev = magnet[1];
                break;

            case '1':

                //std::cout << "Previous     First\n";
                //std::cout << prev << "            " << first << "\n\n";

                if(prev == '1') {
                    //std::cout << "New group \n";
                    groups++;
                }
                prev = magnet[1];
                break;

            default:
                break;
        }


    }
    groups++;
    std::cout << groups;

}
