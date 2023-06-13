#include <iostream>
#include <vector>


std::vector<std::vector<int>> board =
{
    {-4, -2, -3, -5, -6, -3, -2, -4},
    {-1, -1, -1, -1, -1, -1, -1, -1},
    {0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, -1, -1, 0, 0, 0, 0},
    {0, 0, 0, 0, 6, 5, 0, 0},
    {0, -1, 0, 0, 0, 0, 0, 0},
    {1, 1, 1, 1, 1, 1, 1, 1},
    {4, 2, 3, 5, 6, 3, 2, 4}
};


bool spieler(std::vector<std::vector<int>> pos)
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
    //
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
    //x und q
    else if ((pos[vy][vx]==3||pos[vy][vx]==5) && pos[zy][zx]<=0){
        if (zy>vy&&zx>vx){
            for (int i=1;i<8;i++){
                if (vy+i==zy && vx+i==zx){
                    korrekt=true;
                    break;
                }
                else if (pos[vy+i][vx+i]!=0){
                    break;
                }
            }
        }
        else if (zy<vy&&zx>vx){
            for (int i=1;i<8;i++){
                if (vy-i==zy && vx+i==zx){
                    korrekt=true;
                    break;
                }
                else if (pos[vy-i][vx+i]!=0){
                    break;
                }
            }
        }
        else if (zy>vy&&zx<vx){
            for (int i=1;i<8;i++){
                if (vy+i==zy && vx-i==zx){
                    korrekt=true;
                    break;
                }
                else if (pos[vy+i][vx-i]!=0){
                    break;
                }
            }
        }
        else if (zy<vy&&zx<vx){
            for (int i=1;i<8;i++){
                if (vy-i==zy && vx-i==zx){
                    korrekt=true;
                    break;
                }
                else if (pos[vy-i][vx-i]!=0){
                    break;
                }
            }
        }
    }
    //t und q
    else if ((pos[vy][vx]==4||pos[vy][vx]==5) && pos[zy][zx]<=0){
        if (zy>vy&&zx==vx){
            for (int i=1;i<8;i++){
                if (vy+i==zy){
                    korrekt=true;
                    break;
                }
                else if (pos[vy+i][vx]!=0){
                    break;
                }
            }
        }
        else if (zy<vy&&zx==vx){
            for (int i=1;i<8;i++){
                if (vy-i==zy){
                    korrekt=true;
                    break;
                }
                else if (pos[vy-i][vx]!=0){
                    break;
                }
            }
        }
        else if (zy==vy&&zx<vx){
            for (int i=1;i<8;i++){
                if (vx-i==zx){
                    korrekt=true;
                    break;
                }
                else if (pos[vy][vx-i]!=0){
                    break;
                }
            }
        }
        else if (zy==vy&&zx>vx){
            for (int i=1;i<8;i++){
                if (vx+i==zx){
                    korrekt=true;
                    break;
                }
                else if (pos[vy][vx+i]!=0){
                    break;
                }
            }
        }
    }
    //k
    else if (pos[vy][vx]==6 && pos[zy][zx]<=0){
        if (vx+1==zx&&vy==zx){korrekt=true;}
        else if (vx==zx&&vy+1==zx){korrekt=true;}
        else if (vx-1==zx&&vy==zx){korrekt=true;}
        else if (vx==zx&&vy-1==zx){korrekt=true;}
        //
        else if (vx+1==zx&&vy+1==zx){korrekt=true;}
        else if (vx+1==zx&&vy-1==zx){korrekt=true;}
        else if (vx-1==zx&&vy+1==zx){korrekt=true;}
        else if (vx-1==zx&&vy-1==zx){korrekt=true;}
    }
    //
    if (korrekt){pos[zy][zx]=pos[vy][vx]; pos[vy][vx]=0; board=pos;}
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
    std::cout<<std::boolalpha << spieler(board) << std::endl;
    printboard(board);
    return 0;
}
