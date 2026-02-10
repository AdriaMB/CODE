#include <iostream>
#include <cmath>

int almost_lucky_recursion(int n, int aux, int i){
    if (i == 0){

        //std::cout << aux << "\n";
        //std::cout << aux+3 << "\n";

        if (n % aux == 0 || n % (aux+3) == 0)       return 0;
        else return 1;
    }
    else{
        int a = almost_lucky_recursion(n, aux, i-1);
        if (a == 0){
            return 0;
        }
        else{
            return almost_lucky_recursion(n, aux+3*pow(10,i), i-1);;
        }
    }

}

int main(){
    int n;
    std::cin >> n;
    // for n to be almost lucky, it must be divided by some lucky number, which are those that only contain 4s and/or 7s

    if(n < 4){
        std::cout << "NO\n";
        return 0;
    }

    int limit = 0, m = n;
    while(m > 0){
        m /= 10;
        limit++; // a number of 1 digit would have limit 1
    }


    //std::cout << "The limit of this input is: " << limit << "\n";

    for(int i = 0; i < limit; i++){
        int aux;
        switch(i){
            case 0:
                aux = 4;
                break;
            case 1:
                aux = 44;
                break;
            case 2:
                aux = 444;
                break;
            default:
                std::cout << "NO\n";
                return 0;
        }

        //std::cout << "We try iteration " << i << " with aux = " << aux <<"\n";

        int res = almost_lucky_recursion(n, aux, i);
        if(res == 0){
            std::cout << "YES\n"; // Found
            return 0;
        }
        // else keep searching
    }
    // It didn't find any number to divide n'
    std::cout << "NO\n";
    return 0;

}
