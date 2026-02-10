#include <iostream>
/**
struct monster{
    std::string name;
    double HP;
    double CA;
}

struct player{
    std::string name;
    double HP;
    double CA;

}
*/

class Character{
    public:
        std::string name;
        double HP;
        int CA;

    Character(std::string name){
        this->name = name;
        this->HP = 15;
        this->CA = 6;

    }
};  // class definition has ; afterwards

void encounter(){
    int num;

    srand(time(NULL));
    num = (rand() % 5)+1; // number between 1 and 5

    switch (num){
        case 1:
            break;
        case 2:
            break;
        case 3:
            break;
        case 4:
            break;
        case 5:
            break;
        default:
            break;
    }
}


int main(){

    std::cout << "Which is your character's name?: ";
    std::string player_name;
    std::cin >> player_name;
    Character player(player_name);

    std::cout << "You are the warrior " << player.name << ", with HP = 15 and CA = 6\n";




}
