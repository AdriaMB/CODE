#include <iostream>
#include <string>

int main(){
    using std::string;
    using std::cout;
    using std::cin;

    int n;
    cin >> n;

    for(int i = 0; i < n; i++){
        int number;
        cin >> number;
        string line;
        std::getline(cin>>std::ws, line);

        cout << "Soy John M. y nunca " << line << "\n";
    }

    return 0;
}
