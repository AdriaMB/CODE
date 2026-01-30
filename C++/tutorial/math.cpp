#include <iostream>
#include <cmath>   // needed for the functions max, pow, sqrt...


int main(){
    using std::cout;
    using std::cin;

    double x = 2;
    double y = 4;
    double z;

    z = std::max(x, y); cout << z << "\n";

    double a;
    double b;
    double c;

    cout << "Enter side A: ";
    cin >> a;
    cout << "Enter side B: ";
    cin >> b;

    a = pow(a, 2); // rise to 2
    b = pow(b, 2);
    c = sqrt(a +b);

    cout << "The side C is: " <<c;
    return 0;


}
