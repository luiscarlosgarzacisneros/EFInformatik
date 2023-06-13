#include <iostream>
#include <vector>


std::vector<std::vector<int>> board =
{
    {-4, -2, -3, -5, -6, -3, -2, -4},
    {-1, -1, -1, -1, -1, -1, -1, -1},
    {0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0},
    {1, 1, 1, 1, 1, 1, 1, 1},
    {4, 2, 3, 5, 6, 3, 2, 4}
};


bool eingabeueberpruefung(std::vector<std::vector<int>> pos)
{
    int eingabevy;
    int eingabevx;
    int eingabezy;
    int eingabezx;
    std::cout << "von y: ";
    std::cin >> eingabevy;
    std::cout << "von x: ";
    std::cin >> eingabevx;
    std::cout << "zu y: ";
    std::cin >> eingabezy;
    std::cout << "zu x: ";
    std::cin >> eingabezx;
    int vy = eingabevy-1;
    int vx = eingabevx-1;
    int zy = eingabezy-1;
    int zx = eingabezx-1;

    if (vy > 7 || vy < 0 || vx > 7 || vx < 0 || zy > 7 || zy < 0 || zx > 7 || zx < 0) {
        std::cout << "\nEingabe ist nicht korrekt" << std::endl;
        return false;
    }
    bool korrekt=false;
    //b
    if (pos[vy][vx]==1){
        //2 nach vorne
        if (pos[vy-1][vx]==0 && vy-2==zy && vx==zx && pos[vy-2][vx]==0 && vy==6){
            korrekt=true;
        }
        //1 nach vorne
        else if (pos[vy-1][vx]==0 && vy-1==zy && vx==zx){
            korrekt=true;
        }
        //schlagen
        else if (zy==vy-1 && vx-1==zx && pos[zy][zx]<=-1){
            korrekt=true;
        }
        else if (zy==vy-1 && vx+1==zx && pos[zy][zx]<=-1){
            korrekt=true;
        }
    }
    //l
    else if (pos[vy][vx]==2 && pos[zy][zx]<=0){
        if (zy==vy-2 && zx==vx+1){korrekt=true;}
        else if (zy==vy-2 && zx==vx-1){korrekt=true;}
        else if (zy==vy+2 && zx==vx+1){korrekt=true;}
        else if (zy==vy+2 && zx==vx-1){korrekt=true;}
        else if (zy==vy+1 && zx==vx+2){korrekt=true;}
        else if (zy==vy-1 && zx==vx+2){korrekt=true;}
        else if (zy==vy+1 && zx==vx-2){korrekt=true;}
        else if (zy==vy-1 && zx==vx-2){korrekt=true;}
    }
    return korrekt;

}


void printboard(std::vector<std::vector<int>> pos)
{
    int number(1);
    std::cout << "    1   2   3   4   5   6   7   8  " << "\n";
    for (auto r : pos) {
        std::cout << "  +---+---+---+---+---+---+---+---+" << "\n";
        std::cout<<number<<" ";
        for (auto element : r) {
            std::cout<<"| ";
            if (element == 1) {
                std::cout << "b";}
            else if (element == 2) {
                std::cout << "l";}
            else if (element == 3) {
                std::cout << "x";}
            else if (element == 4) {
                std::cout << "t";}
            else if (element == 5) {
                std::cout << "q";}
            else if (element == 6) {
                std::cout << "k";}
            else if (element == -1) {
                std::cout << "B";}
            else if (element == -2) {
                std::cout << "L";}
            else if (element == -3) {
                std::cout << "X";}
            else if (element == -4) {
                std::cout << "T";}
            else if (element == -5) {
                std::cout << "Q";}
            else if (element == -6) {
                std::cout << "K";}
            else if (element == 0) {
                std::cout << " ";}
            std::cout << " ";
        }
        std::cout << "|" << "\n";
        number=number+1;
    }
    std::cout << "  +---+---+---+---+---+---+---+---+" << "\n";
}

int main()
{
    printboard(board);
    std::cout << "Result: " << std::boolalpha << eingabeueberpruefung(board) << std::endl;

    return 0;
}
