#include <iostream>
#include <vector>
#include <list>
#include <algorithm>
#include <cstdlib>
#include <ctime>
#include <chrono>
#include <cmath>
#include <sstream>

//

bool is_int(int value) {
    std::string input = std::to_string(value);
    std::istringstream iss(input);
    int extracted_value;
    return (iss >> extracted_value) && (iss.eof());
}

int generate_random_int(int min, int max) {
    int random_number=min+rand()%(max-min+1);
    return random_number;
}

std::vector<std::vector<int>> deepcopy(const std::vector<std::vector<int>>& board) {
    std::vector<std::vector<int>> board_copy;
    for (const std::vector<int>& row : board){
        std::vector<int> new_y;
        for (const int& x : row){
            new_y.push_back(x);
        }
        board_copy.push_back(new_y);
    }
    return board_copy;
}

void print_board(const std::vector<std::vector<int>>& board) {
    std::cout<<"  1   2   3   4   5   6   7   8"<<std::endl;
    std::cout<<"---------------------------------"<<std::endl;
    for (int i=0; i<8; ++i) {
        std::cout << "I ";
        for (int j = 0; j < 8; ++j) {
            if (board[i][j]==-1) {std::cout<< "O";}
            else if (board[i][j]==1) {std::cout<<"X";}
            else if (board[i][j]==-2) {std::cout<<"M";}
            else if (board[i][j]==2) {std::cout<<"W";}
            else {std::cout << " ";}
            std::cout << " I ";
        }
        std::cout<<i+1 <<std::endl;
        std::cout<<"---------------------------------"<<std::endl;
    }
}

//

std::list<std::vector<std::vector<int>>> children_schlagen_XO;
std::list<std::vector<std::vector<int>>>  children_schlagen_WM;

void generate_children_schlagen_XO(int y, int x, const std::vector<std::vector<int>> board, int player, bool new_flag) {
    if (new_flag) {children_schlagen_XO.clear();}
    //
    std::vector<std::vector<int>> board_copy = board;
    //
    if (player==1) {
        if (y - 2 > -1 && x - 2 > -1 && board_copy[y - 2][x - 2]==0) {
            if (board_copy[y-1][x-1] < 0) {
                board_copy[y- 1][x-1] = 0;
                board_copy[y-2][x-2] = 1;
                board_copy[y][x] = 0;
                if (y - 2 ==0) {
                    board_copy[y-2][x-2] = 2;
                }
                children_schlagen_XO.push_back(board_copy);
                generate_children_schlagen_XO(y - 2, x - 2, board_copy, player, false);
                board_copy = board;
            }
        }
        if (y - 2 > -1 && x + 2 < 8 && board_copy[y-2][x+2]==0) {
            if (board_copy[y-1][x+1] < 0) {
                board_copy[y-1][x+1] = 0;
                board_copy[y-2][x+2] = 1;
                board_copy[y][x] = 0;
                if (y - 2 ==0) {
                    board_copy[y-2][x + 2] = 2;
                }
                children_schlagen_XO.push_back(board_copy);
                generate_children_schlagen_XO(y - 2, x + 2, board_copy, player, false);
                board_copy = board;
            }
        }
    }
    else if (player==-1) {
        if (y + 2 < 8 && x - 2 > -1 && board_copy[y+2][x-2]==0) {
            if (board_copy[y+1][x-1] > 0) {
                board_copy[y+1][x-1] = 0;
                board_copy[y+2][x-2] = -1;
                board_copy[y][x] = 0;
                if (y+2 ==7) {
                    board_copy[y+2][x - 2] = -2;
                }
                children_schlagen_XO.push_back(board_copy);
                generate_children_schlagen_XO(y + 2, x - 2, board_copy, player, false);
                board_copy = board;
            }
        }
        if (y + 2 < 8 && x + 2 < 8 && board_copy[y+2][x+2]==0) {
            if (board_copy[y+1][x+1] > 0) {
                board_copy[y+1][x+1] = 0;
                board_copy[y+2][x+2] = -1;
                board_copy[y][x] = 0;
                if (y + 2 ==7) {
                    board_copy[y + 2][x + 2] = -2;
                }
                children_schlagen_XO.push_back(board_copy);
                generate_children_schlagen_XO(y + 2, x + 2, board_copy, player, false);
                board_copy = board;
            }
        }
    }
    std::reverse(children_schlagen_XO.begin(), children_schlagen_XO.end());
}

void generate_children_schlagen_WM(int y, int x, std::vector<std::vector<int>> board, int player, bool new_flag) {
    if (new_flag) {children_schlagen_WM.clear();}
    //
    std::vector<std::vector<int>> board_copy = board;
    //
    if (player==-2) {
        //
        for (int o=0; o<7; ++o) {
            if (y + 2 + o > 7 || x + 2 + o > 7) {break;}
            if (board_copy[y + 1 + o][x + 1 + o] < 0) {break;}
            if (board_copy[y + 1 + o][x + 1 + o] > 0) {
                if (board_copy[y + 2 + o][x + 2 + o] == 0) {
                    board_copy[y + 2 + o][x + 2 + o] = -2;
                    board_copy[y + 1 + o][x + 1 + o] = 0;
                    board_copy[y][x] = 0;
                    children_schlagen_WM.push_back(board_copy);
                    generate_children_schlagen_WM(y + 2 + o, x + 2 + o, board_copy, -2, false);
                    board_copy = board;
                    break;
                }
                else {break;}
            }
        }
        //
        for (int o=0; o<7; ++o) {
            if (y - 2 - o < 0 || x + 2 + o > 7) {break;}
            if (board_copy[y - 1 - o][x + 1 + o] < 0) {break;}
            if (board_copy[y - 1 - o][x + 1 + o] > 0) {
                if (board_copy[y - 2 - o][x + 2 + o] == 0) {
                    board_copy[y - 2 - o][x + 2 + o] = -2;
                    board_copy[y - 1 - o][x + 1 + o] = 0;
                    board_copy[y][x] = 0;
                    children_schlagen_WM.push_back(board_copy);
                    generate_children_schlagen_WM(y - 2 - o, x + 2 + o, board_copy, -2, false);
                    board_copy = board;
                    break;
                }
                else {break;}
            }
        }
        //
        for (int o=0; o<7; ++o) {
            if (y - 2 - o < 0 || x - 2 - o < 0) {break;}
            if (board_copy[y - 1 - o][x - 1 - o] < 0) {break;}
            if (board_copy[y - 1 - o][x - 1 - o] > 0) {
                if (board_copy[y - 2 - o][x - 2 - o] == 0) {
                    board_copy[y - 2 - o][x - 2 - o] = -2;
                    board_copy[y - 1 - o][x - 1 - o] = 0;
                    board_copy[y][x] = 0;
                    children_schlagen_WM.push_back(board_copy);
                    generate_children_schlagen_WM(y - 2 - o, x - 2 - o, board_copy, -2, false);
                    board_copy = board;
                    break;
                }
                else {break;}
            }
        }
        //
        for (int o=0; o<7; ++o) {
            if (y + 2 + o > 7 || x - 2 - o < 0) {break;}
            if (board_copy[y + 1 + o][x - 1 - o] < 0) {break;}
            if (board_copy[y + 1 + o][x - 1 - o] > 0) {
                if (board_copy[y + 2 + o][x - 2 - o] == 0) {
                    board_copy[y + 2 + o][x - 2 - o] = -2;
                    board_copy[y + 1 + o][x - 1 - o] = 0;
                    board_copy[y][x] = 0;
                    children_schlagen_WM.push_back(board_copy);
                    generate_children_schlagen_WM(y + 2 + o, x - 2 - o, board_copy, -2, false);
                    board_copy = board;
                    break;
                }
                else {break;}
            }
        }

    }
    //
    else if (player == 2) {
        //
        for (int o=0; o<7; ++o) {
            if (y + 2 + o > 7 || x + 2 + o > 7) {break;}
            if (board_copy[y + 1 + o][x + 1 + o] > 0) {break;}
            if (board_copy[y + 1 + o][x + 1 + o] < 0) {
                if (board_copy[y + 2 + o][x + 2 + o] == 0) {
                    board_copy[y + 2 + o][x + 2 + o] = 2;
                    board_copy[y + 1 + o][x + 1 + o] = 0;
                    board_copy[y][x] = 0;
                    children_schlagen_WM.push_back(board_copy);
                    generate_children_schlagen_WM(y + 2 + o, x + 2 + o, board_copy, 2, false);
                    board_copy = board;
                    break;
                }
                else {break;}
            }
        }
        //
        for (int o=0; o<7; ++o) {
            if (y - 2 - o < 0 || x + 2 + o > 7) {break;}
            if (board_copy[y - 1 - o][x + 1 + o] > 0) {break;}
            if (board_copy[y - 1 - o][x + 1 + o] < 0) {
                if (board_copy[y - 2 - o][x + 2 + o] == 0) {
                    board_copy[y - 2 - o][x + 2 + o] = 2;
                    board_copy[y - 1 - o][x + 1 + o] = 0;
                    board_copy[y][x] = 0;
                    children_schlagen_WM.push_back(board_copy);
                    generate_children_schlagen_WM(y - 2 - o, x + 2 + o, board_copy, 2, false);
                    board_copy = board;
                    break;
                }
                else {break;}
            }
        }
        //
        for (int o = 0; o < 7; ++o) {
            if (y - 2 - o < 0 || x - 2 - o < 0) {break;}
            if (board_copy[y - 1 - o][x - 1 - o] > 0) {break;}
            if (board_copy[y - 1 - o][x - 1 - o] < 0) {
                if (board_copy[y - 2 - o][x - 2 - o] == 0) {
                    board_copy[y - 2 - o][x - 2 - o] = 2;
                    board_copy[y - 1 - o][x - 1 - o] = 0;
                    board_copy[y][x] = 0;
                    children_schlagen_WM.push_back(board_copy);
                    generate_children_schlagen_WM(y - 2 - o, x - 2 - o, board_copy, 2, false);
                    board_copy = board;
                    break;
                }
                else {break;}
            }
        }
        //
        for (int o=0; o<7; ++o) {
            if (y + 2 + o > 7 || x - 2 - o < 0) {break;}
            if (board_copy[y + 1 + o][x - 1 - o] > 0) {break;}
            if (board_copy[y + 1 + o][x - 1 - o] < 0) {
                if (board_copy[y + 2 + o][x - 2 - o] == 0) {
                    board_copy[y + 2 + o][x - 2 - o] = 2;
                    board_copy[y + 1 + o][x - 1 - o] = 0;
                    board_copy[y][x] = 0;
                    children_schlagen_WM.push_back(board_copy);
                    generate_children_schlagen_WM(y + 2 + o, x - 2 - o, board_copy, 2, false);
                    board_copy = board;
                    break;
                }
                else {break;}
            }
        }
    }
    //
    std::reverse(children_schlagen_WM.begin(), children_schlagen_WM.end());
}

std::list<std::vector<std::vector<int>>> generate_children_WM(int y, int x, std::vector<std::vector<int>> board, int player) {
    std::list<std::vector<std::vector<int>>> childrenWM1;
    std::list<std::vector<std::vector<int>>> childrenWM2;
    std::vector<std::vector<int>> board_copy = board;
    bool schlagen = false;

    if (player == -2) {
        for (int o=0; o<7; ++o) {
            schlagen = false;
            if (y + 1 + o > 7 || x + 1 + o > 7) {break;}
            if (board_copy[y + 1 + o][x+ 1 + o] < 0) {break;}
            if (board_copy[y + 1 + o][x + 1 + o] > 0) {
                if (!(y + 2 + o > 7) && !(x + 2 + o > 7)) {schlagen = true;}
            }
            if (board_copy[y + 1 + o][x + 1 + o]==0) {
                board_copy[y + 1 + o][x + 1 + o]=-2;
                board_copy[y][x] = 0;
                childrenWM2.push_back(board_copy);
                board_copy = board;
            }
            if (schlagen) {
                if (board_copy[y + 2 + o][x + 2 + o]==0) {
                    board_copy[y + 2 + o][x + 2 + o]=-2;
                    board_copy[y][x] = 0;
                    board_copy[y + 1 + o][x + 1 + o]=0;
                    childrenWM1.push_back(board_copy);
                    //
                    children_schlagen_WM.clear();
                    generate_children_schlagen_WM(y + 2 + o, x + 2 + o, board_copy, -2, true);
                    std::list<std::vector<std::vector<int>>> r_children = children_schlagen_WM;
                    childrenWM1.insert(childrenWM1.end(), r_children.begin(), r_children.end());
                    board_copy = board;
                    schlagen = false;
                    break;
                }
                else {break;}
            }
        }
        //
        for (int o=0; o<7; ++o) {
            schlagen = false;
            if (y + 1 + o > 7 || x - 1 - o < 0) {break;}
            if (board_copy[y + 1 + o][x - 1 - o] < 0) {break;}
            if (board_copy[y + 1 + o][x - 1 - o] > 0) {
                if (!(y + 2 + o > 7) && !(x - 2 - o < 0)) {schlagen = true;}
            }
            if (board_copy[y + 1 + o][x - 1 - o]==0) {
                board_copy[y + 1 + o][x - 1 - o]=-2;
                board_copy[y][x] = 0;
                childrenWM2.push_back(board_copy);
                board_copy = board;
            }
            if (schlagen) {
                if (board_copy[y + 2 + o][x - 2 - o]==0) {
                    board_copy[y + 2 + o][x - 2 - o]=-2;
                    board_copy[y][x] = 0;
                    board_copy[y + 1 + o][x - 1 - o]=0;
                    childrenWM1.push_back(board_copy);
                    //
                    children_schlagen_WM.clear();
                    generate_children_schlagen_WM(y + 2 + o, x - 2 - o, board_copy, -2, true);
                    std::list<std::vector<std::vector<int>>> r_children = children_schlagen_WM;
                    childrenWM1.insert(childrenWM1.end(), r_children.begin(), r_children.end());
                    board_copy = board;
                    schlagen = false;
                    break;
                }
                else {break;}
            }
        }
        //
        for (int o=0; o<7; ++o) {
            schlagen = false;
            if (y - 1 - o < 0 || x - 1 - o < 0) {break;}
            if (board_copy[y - 1 - o][x - 1 - o] < 0) {break;}
            if (board_copy[y - 1 - o][x - 1 - o] > 0) {
                if (!(y - 2 - o < 0) && !(x - 2 - o < 0)) {schlagen = true;}
            }
            if (board_copy[y - 1 - o][x - 1 - o]==0) {
                board_copy[y - 1 - o][x - 1 - o]=-2;
                board_copy[y][x] = 0;
                childrenWM2.push_back(board_copy);
                board_copy = board;
            }
            if (schlagen) {
                if (board_copy[y - 2 - o][x - 2 - o]==0) {
                    board_copy[y - 2 - o][x - 2 - o]=-2;
                    board_copy[y][x] = 0;
                    board_copy[y - 1 - o][x - 1 - o]=0;
                    childrenWM1.push_back(board_copy);
                    //
                    children_schlagen_WM.clear();
                    generate_children_schlagen_WM(y - 2 - o, x - 2 - o, board_copy, -2, true);
                    std::list<std::vector<std::vector<int>>> r_children = children_schlagen_WM;
                    childrenWM1.insert(childrenWM1.end(), r_children.begin(), r_children.end());
                    board_copy = board;
                    schlagen = false;
                    break;
                }
                else {break;}
            }
        }
        //
        for (int o=0; o<7; ++o) {
            schlagen = false;
            if (y - 1 - o < 0 || x + 1 + o > 7) {break;}
            if (board_copy[y - 1 - o][x + 1 + o] < 0) {break;}
            if (board_copy[y - 1 - o][x + 1 + o] > 0) {
                if (!(y - 2 - o < 0) && !(x + 2 + o > 7)) {schlagen = true;}
            }
            if (board_copy[y - 1 - o][x + 1 + o]==0) {
                board_copy[y - 1 - o][x + 1 + o]=-2;
                board_copy[y][x] = 0;
                childrenWM2.push_back(board_copy);
                board_copy = board;
            }
            if (schlagen) {
                if (board_copy[y - 2 - o][x + 2 + o]==0) {
                    board_copy[y - 2 - o][x + 2 + o]=-2;
                    board_copy[y][x] = 0;
                    board_copy[y - 1 - o][x + 1 + o]=0;
                    childrenWM1.push_back(board_copy);
                    //
                    children_schlagen_WM.clear();
                    generate_children_schlagen_WM(y - 2 - o, x + 2 + o, board_copy,-2, true);
                    std::list<std::vector<std::vector<int>>> r_children = children_schlagen_WM;
                    childrenWM1.insert(childrenWM1.end(), r_children.begin(), r_children.end());
                    board_copy = board;
                    schlagen = false;
                    break;
                }
                else {break;}
            }
        }
    }
    //
    else if (player == 2) {
        //
        for (int o = 0; o < 7; ++o) {
            schlagen = false;
            if (y + 1 + o > 7 || x + 1 + o > 7) {break;}
            if (board_copy[y + 1 + o][x + 1 + o] > 0) {break;}
            if (board_copy[y + 1 + o][x + 1 + o] < 0) {
                if (!(y + 2 + o > 7) && !(x + 2 + o > 7)) {schlagen = true;}
            }
            if (board_copy[y + 1 + o][x + 1 + o] == 0) {
                board_copy[y + 1 + o][x + 1 + o] = 2;
                board_copy[y][x] = 0;
                childrenWM2.push_back(board_copy);
                board_copy = board;
            }
            if (schlagen) {
                if (board_copy[y + 2 + o][x + 2 + o] == 0) {
                    board_copy[y + 2 + o][x + 2 + o] = 2;
                    board_copy[y][x] = 0;
                    board_copy[y + 1 + o][x + 1 + o] = 0;
                    childrenWM1.push_back(board_copy);
                    //
                    children_schlagen_WM.clear();
                    generate_children_schlagen_WM(y + 2 + o, x + 2 + o, board_copy, 2, true);
                    std::list<std::vector<std::vector<int>>> r_children = children_schlagen_WM;
                    childrenWM1.insert(childrenWM1.end(), r_children.begin(), r_children.end());
                    board_copy = board;
                    schlagen = false;
                    break;
                }
                else {break;}
            }
        }
        //
        for (int o = 0; o < 7; ++o) {
            schlagen = false;
            if (y + 1 + o > 7 || x - 1 - o < 0) {break;}
            if (board_copy[y + 1 + o][x - 1 - o] > 0) {break;}
            if (board_copy[y + 1 + o][x - 1 - o] < 0) {
                if (!(y + 2 + o > 7) && !(x - 2 - o < 0)) {schlagen = true;}
            }
            if (board_copy[y + 1 + o][x - 1 - o] == 0) {
                board_copy[y + 1 + o][x - 1 - o] = 2;
                board_copy[y][x] = 0;
                childrenWM2.push_back(board_copy);
                board_copy = board;
            }
            if (schlagen) {
                if (board_copy[y + 2 + o][x - 2 - o] == 0) {
                    board_copy[y + 2 + o][x - 2 - o] = 2;
                    board_copy[y][x] = 0;
                    board_copy[y + 1 + o][x - 1 - o] = 0;
                    childrenWM1.push_back(board_copy);
                    //
                    children_schlagen_WM.clear();
                    generate_children_schlagen_WM(y + 2 + o, x - 2 - o, board_copy, 2, true);
                    std::list<std::vector<std::vector<int>>> r_children = children_schlagen_WM;
                    childrenWM1.insert(childrenWM1.end(), r_children.begin(), r_children.end());
                    board_copy = board;
                    schlagen = false;
                    break;
                }
                else {break;}
            }
        }
        //
        for (int o = 0; o < 7; ++o) {
            schlagen = false;
            if (y - 1 - o < 0 || x - 1 - o < 0) {break;}
            if (board_copy[y - 1 - o][x - 1 - o] > 0) {break;}
            if (board_copy[y - 1 - o][x - 1 - o] < 0) {
                if (!(y - 2 - o < 0) && !(x - 2 - o < 0)) {schlagen = true;}
            }
            if (board_copy[y - 1 - o][x - 1 - o] == 0) {
                board_copy[y - 1 - o][x - 1 - o] = 2;
                board_copy[y][x] = 0;
                childrenWM2.push_back(board_copy);
                board_copy = board;
            }
            if (schlagen) {
                if (board_copy[y - 2 - o][x - 2 - o] == 0) {
                    board_copy[y - 2 - o][x - 2 - o] = 2;
                    board_copy[y][x] = 0;
                    board_copy[y - 1 - o][x - 1 - o] = 0;
                    childrenWM1.push_back(board_copy);
                    //
                    children_schlagen_WM.clear();
                    generate_children_schlagen_WM(y - 2 - o, x - 2 - o, board_copy, 2, true);
                    std::list<std::vector<std::vector<int>>> r_children = children_schlagen_WM;
                    childrenWM1.insert(childrenWM1.end(), r_children.begin(), r_children.end());
                    board_copy = board;
                    schlagen = false;
                    break;
                }
                else {break;}
            }
        }
        //
        for (int o = 0; o < 7; ++o) {
            schlagen = false;
            if (y - 1 - o < 0 || x + 1 + o > 7) {break;}
            if (board_copy[y - 1 - o][x + 1 + o] > 0) {break;}
            if (board_copy[y - 1 - o][x + 1 + o] < 0) {
                if (!(y - 2 - o < 0) && !(x + 2 + o > 7)) {schlagen = true;}
            }
            if (board_copy[y - 1 - o][x + 1 + o] == 0) {
                board_copy[y - 1 - o][x + 1 + o] = 2;
                board_copy[y][x] = 0;
                childrenWM2.push_back(board_copy);
                board_copy = board;
            }
            if (schlagen) {
                if (board_copy[y - 2 - o][x + 2 + o] == 0) {
                    board_copy[y - 2 - o][x + 2 + o] = 2;
                    board_copy[y][x] = 0;
                    board_copy[y - 1 - o][x + 1 + o] = 0;
                    childrenWM1.push_back(board_copy);
                    //
                    children_schlagen_WM.clear();
                    generate_children_schlagen_WM(y - 2 - o, x + 2 + o, board_copy, 2, true);
                    std::list<std::vector<std::vector<int>>> r_children = children_schlagen_WM;
                    childrenWM1.insert(childrenWM1.end(), r_children.begin(), r_children.end());
                    board_copy = board;
                    schlagen = false;
                    break;
                }
                else {break;}
            }
        }
    }
    //
    childrenWM1.insert(childrenWM1.end(), childrenWM2.begin(), childrenWM2.end());
    return childrenWM1;
}

std::list<std::vector<std::vector<int>>> generate_children(const std::vector<std::vector<int>> board, int player) {
    std::list<std::vector<std::vector<int>>> children1;
    std::list<std::vector<std::vector<int>>> children2;
    std::vector<std::vector<int>> board_copy = board;

    for (int y=0; y<8; ++y) {
        for (int x=0; x <8; ++x) {
            if (player==1) {
                if (board_copy[y][x] == 1) {
                    if (y - 1 > -1 && x - 1 > -1 && board_copy[y - 1][x - 1] == 0) {
                        board_copy[y - 1][x - 1] = 1;
                        board_copy[y][x] = 0;
                        if (y - 1 == 0) {
                            board_copy[y - 1][x - 1] = 2;
                            children1.push_back(board_copy);
                        }
                        children2.push_back(board_copy);
                        board_copy = board;
                    }
                    if (y - 1 > -1 && x + 1 < 8 && board_copy[y - 1][x + 1] == 0) {
                        board_copy[y - 1][x + 1] = 1;
                        board_copy[y][x] = 0;
                        if (y - 1 == 0) {
                            board_copy[y - 1][x + 1] = 2;
                            children1.push_back(board_copy);
                        }
                        children2.push_back(board_copy);
                        board_copy = board;
                    }
                    //
                    children_schlagen_XO.clear();
                    generate_children_schlagen_XO(y, x, board_copy, 1, true);
                    std::list<std::vector<std::vector<int>>> children_s = children_schlagen_XO;
                    children1.insert(children1.end(), children_s.begin(), children_s.end());
                    //
                }
                else if (board_copy[y][x] == 2) {
                    //
                    std::list<std::vector<std::vector<int>>> children_wm = generate_children_WM(y, x, board_copy, 2);
                    children1.insert(children1.end(), children_wm.begin(), children_wm.end());
                    //
                }
            }
            else if (player==-1) {
                if (board_copy[y][x] == -1) {
                    if (y + 1 < 8 && x - 1 > -1 && board_copy[y + 1][x - 1] == 0) {
                        board_copy[y + 1][x - 1] = -1;
                        board_copy[y][x] = 0;
                        if (y + 1 == 7) {
                            board_copy[y + 1][x - 1] = -2;
                            children1.push_back(board_copy);
                        }
                        children2.push_back(board_copy);
                        board_copy = board;
                    }
                    if (y + 1 < 8 && x + 1 < 8 && board_copy[y + 1][x + 1] == 0) {
                        board_copy[y + 1][x + 1] = -1;
                        board_copy[y][x] = 0;
                        if (y + 1 == 7) {
                            board_copy[y + 1][x + 1] = -2;
                            children1.push_back(board_copy);
                        }
                        children2.push_back(board_copy);
                        board_copy = board;
                    }
                    //
                    children_schlagen_XO.clear();
                    generate_children_schlagen_XO(y, x, board_copy, -1, true);
                    std::list<std::vector<std::vector<int>>> children_s = children_schlagen_XO;
                    children1.insert(children1.end(), children_s.begin(), children_s.end());
                    //
                }
                else if (board_copy[y][x] == -2) {
                    //
                    std::list<std::vector<std::vector<int>>> children_wm = generate_children_WM(y, x, board_copy, -2);
                    children1.insert(children1.end(), children_wm.begin(), children_wm.end());
                    //
                }
            }
        }
    }
    std::list<std::vector<std::vector<int>>> children_list;
    children_list.insert(children_list.end(), children1.begin(), children1.end());
    children_list.insert(children_list.end(), children2.begin(), children2.end());
    return children_list;
}

//

bool verloren1(const std::vector<std::vector<int>>& pos, int player) {
    int player2 =(player==1) ? 2 : -2;
    int eval=0;
    //
    for (size_t sl=0; sl < pos.size(); ++sl) {
        eval+=std::count(pos[sl].begin(), pos[sl].end(), player);
        eval+=std::count(pos[sl].begin(), pos[sl].end(), player2);
    }
    return (eval == 0) ? true : false;
}

bool keine_zugmoeglichkeiten(const std::vector<std::vector<int>>& pos, int player) {
    std::list<std::vector<std::vector<int>>> children = generate_children(pos, player);
    return children.empty() ? true : false;
}

bool verloren2(const std::vector<std::vector<int>>& pos, int player) {
    int player2 =(player==1) ? 2 : -2;
    int eval=0;
    //
    for (size_t sl=0; sl < pos.size(); ++sl) {
        eval+=std::count(pos[sl].begin(), pos[sl].end(), player);
        eval+=std::count(pos[sl].begin(), pos[sl].end(), player2);
    }
    if (eval==0 || keine_zugmoeglichkeiten(pos, player)) {return true;}
    else {return false;}
}

//

std::vector<int> X_matrix = {2, 0, 0, 1, 2, 3, 4, 5};
std::vector<int> O_matrix = {5, 4, 3, 2, 1, 0, 0, 2};

int evaluate_position(const std::vector<std::vector<int>>& pos, int player) {
    int eval = 0;
    if (player == 1) {
        int anz_X = 0;
        int anz_O = 0;
        int anz_W = 0;
        int anz_M = 0;
        for (size_t l = 0; l < pos.size(); ++l) {
            for (int o = 0; o < pos[l].size(); ++o) {
                if (pos[l][o] == 1) {
                    eval += 9;
                    anz_X += 1;
                    eval += X_matrix[l];
                }
                else if (pos[l][o] == -1) {
                    eval += -11;
                    anz_O += 1;
                    eval += -O_matrix[l];
                }
                else if (pos[l][o] == 2) {
                    eval += 49;
                    anz_W += 1;
                }
                else if (pos[l][o] == -2) {
                    eval += -51;
                    anz_M += 1;
                }
            }
        }
        //
        if (anz_X == 0 && anz_W == 0) {eval += -8888;}
        else if (anz_O == 0 && anz_M == 0) {eval += 8888;}
        return eval;
    }
    //
    else if (player == -1) {
        int anz_X = 0;
        int anz_O = 0;
        int anz_W = 0;
        int anz_M = 0;
        for (size_t l = 0; l < pos.size(); ++l) {
            for (int o = 0; o < pos[l].size(); ++o) {
                if (pos[l][o] == 1) {
                    eval += -11;
                    anz_X += 1;
                    eval += -X_matrix[l];
                }
                else if (pos[l][o] == -1) {
                    eval += 9;
                    anz_O += 1;
                    eval += O_matrix[l];
                }
                else if (pos[l][o] == 2) {
                    eval += -51;
                    anz_W += 1;
                }
                else if (pos[l][o] == -2) {
                    eval += 49;
                    anz_M += 1;
                }
            }
        }
        //
        if (anz_X == 0 && anz_W == 0) {eval += 8888;}
        else if (anz_O == 0 && anz_M == 0) {eval += 8888;}
        return eval;
    }
    return eval;
}

//

class HumanPlayer {
public:
    HumanPlayer(int token) : token(token) {}

    int token=token;

    std::vector<int> eingabe() {
        try {
            int vx, vy, zx, zy;
            std::cout <<"von x: ";
            std::cin>> vx;
            std::cout <<"von y: ";
            std::cin>> vy;
            std::cout <<"zu x: ";
            std::cin>> zx;
            std::cout <<"zu y: ";
            std::cin >> zy;
            //
            vx -= 1;
            vy -= 1;
            zx -= 1;
            zy -= 1;
            //
            if (vy < 8 && vy > -1 && vx < 8 && vx > -1 && zy < 8 && zy > -1 && zx < 8 && zx > -1 && is_int(vx) && is_int(vy)&& is_int(zx)&& is_int(zy)) {
                    return {vy, vx, zy, zx};
            }
            else {
                std::cin.clear();
                std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
                std::cout << "EINGABE NICHT KORREKT1" << std::endl;
                return eingabe();
            }
        }
        catch (...) {
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            std::cout << "EINGABE NICHT KORREKT1" << std::endl;
            return eingabe();
        }
    }

    std::vector<int> eingabe_schlagen_XO(int vy, int vx, const std::vector<std::vector<int>>& pos, int token) {
        std::vector<int> result;
        //
        bool korrekt = false;
        //
        try {
            int zx, zy;
            std::cout << "zu x: ";
            std::cin >> zx;
            std::cout << "zu y: ";
            std::cin >> zy;
            zx -= 1;
            zy -= 1;
            //
            if (!is_int(zy) || !is_int(zx)) {
                std::cin.clear();
                std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
                std::cout << "EINGABE NICHT KORREKT3" << std::endl;
                return eingabe_schlagen_XO(vy, vx, pos, token);
            }
            //
            if (zx == vx && zy == vy) {korrekt = true;}
            if (zy < 8 && zy > -1 && zx < 8 && zx > -1) {
                if (token == 1) {
                    if (zy == vy - 2 && zx == vx - 2 && pos[vy][vx] == 1 && pos[zy][zx] == 0 && pos[vy - 1][vx - 1] < 0) {korrekt = true;}
                    else if (zy == vy - 2 && zx == vx + 2 && pos[vy][vx] == 1 && pos[zy][zx] == 0 && pos[vy - 1][vx + 1] < 0) {korrekt = true;}
                }
                else if (token ==-1) {
                    if (zy == vy + 2 && zx == vx - 2 && pos[vy][vx] == -1 && pos[zy][zx] == 0 && pos[vy + 1][vx - 1] > 0) {korrekt = true;}
                    else if (zy == vy + 2 && zx == vx + 2 && pos[vy][vx] == -1 && pos[zy][zx] == 0 && pos[vy + 1][vx + 1] > 0) {korrekt = true;}
                }
            }
            //
            if (korrekt) {result = {zy, zx}; return result;}
            else {
                std::cin.clear();
                std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
                std::cout << "EINGABE NICHT KORREKT3" << std::endl;
                return eingabe_schlagen_XO(vy, vx, pos, token);}
            //
        }
        catch (...) {
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            std::cout << "EINGABE NICHT KORREKT3" << std::endl;
            return eingabe_schlagen_XO(vy, vx, pos, token);
        }
    }

    std::vector<int> eingabe_schlagen_WM(int vy, int vx, const std::vector<std::vector<int>>& pos, int token) {
        std::vector<int> result;
        //
        bool korrekt = false;
        //
        try {
            int zx, zy;
            std::cout << "zu x: ";
            std::cin >> zx;
            std::cout << "zu y: ";
            std::cin >> zy;
            zx -= 1;
            zy -= 1;
            //
            if (!is_int(zy) || !is_int(zx)) {
                std::cin.clear();
                std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
                std::cout << "EINGABE NICHT KORREKT4" << std::endl;
                return eingabe_schlagen_WM(vy, vx, pos, token);
            }
            if (zx == vx && zy == vy) {korrekt = true;}
            if (zy<8 && zy>-1 && zx<8 && zx>-1) {
                if (token==1) {
                    //
                    for (int i = 0; i < 7; ++i) {
                        if (vy + 2 + i > 7 || vx + 2 + i > 7) {break;}
                        if (pos[vy + 1 + i][vx + 1 + i] > 0) {break;}
                        if (pos[vy + 1 + i][vx + 1 + i] < 0 && pos[vy + 2 + i][vx + 2 + i] == 0 && vy + 2 + i == zy && vx + 2 + i == zx) {
                            korrekt = true; break;}
                    }
                    //
                    for (int i = 0; i < 7; ++i) {
                        if (vy + 2 + i > 7 || vx - 2 - i < 0) {break;}
                        if (pos[vy + 1 + i][vx - 1 - i] > 0) {break;}
                        if (pos[vy + 1 + i][vx - 1 - i] < 0 && pos[vy + 2 + i][vx - 2 - i] == 0 && vy + 2 + i == zy && vx - 2 - i == zx) {korrekt = true; break; }
                    }
                    //
                    for (int i = 0; i < 7; ++i) {
                        if (vy - 2 - i < 0 || vx - 2 - i < 0) {break;}
                        if (pos[vy - 1 - i][vx - 1 - i] > 0) {break;}
                        if (pos[vy - 1 - i][vx - 1 - i] < 0 && pos[vy - 2 - i][vx - 2 - i] == 0 && vy - 2 - i == zy && vx - 2 - i == zx) {korrekt = true; break;}
                    }
                    //
                    for (int i = 0; i < 7; ++i) {
                        if (vy - 2 - i < 0 || vx + 2 + i > 7) {break;}
                        if (pos[vy - 1 - i][vx + 1 + i] > 0) {break;}
                        if (pos[vy - 1 - i][vx + 1 + i] < 0 && pos[vy - 2 - i][vx + 2 + i] == 0 && vy - 2 - i == zy && vx + 2 + i == zx) {korrekt = true; break;}
                    }
                }
                else if (token == -1) {
                    //
                    for (int i = 0; i < 7; ++i) {
                        if (vy + 2 + i > 7 || vx + 2 + i > 7) {break;}
                        if (pos[vy + 1 + i][vx + 1 + i] < 0) {break;}
                        if (pos[vy + 1 + i][vx + 1 + i] > 0 && pos[vy + 2 + i][vx + 2 + i] == 0 && vy + 2 + i == zy && vx + 2 + i == zx) {korrekt = true; break;}
                    }
                    //
                    for (int i = 0; i < 7; ++i) {
                        if (vy + 2 + i > 7 || vx - 2 - i < 0) {break;}
                        if (pos[vy + 1 + i][vx - 1 - i] < 0) {break;}
                        if (pos[vy + 1 + i][vx - 1 - i] > 0 && pos[vy + 2 + i][vx - 2 - i] == 0 && vy + 2 + i == zy && vx - 2 - i == zx) {korrekt = true; break;}
                    }
                    //
                    for (int i = 0; i < 7; ++i) {
                        if (vy - 2 - i < 0 || vx - 2 - i < 0) {break;}
                        if (pos[vy - 1 - i][vx - 1 - i] < 0) {break;}
                        if (pos[vy - 1 - i][vx - 1 - i] > 0 && pos[vy - 2 - i][vx - 2 - i] == 0 && vy - 2 - i == zy && vx - 2 - i == zx) {korrekt = true; break;}
                    }
                    //
                    for (int i = 0; i < 7; ++i) {
                        if (vy - 2 - i < 0 || vx + 2 + i > 7) {break;}
                        if (pos[vy - 1 - i][vx + 1 + i] < 0) {break;}
                        if (pos[vy - 1 - i][vx + 1 + i] > 0 && pos[vy - 2 - i][vx + 2 + i] == 0 && vy - 2 - i == zy && vx + 2 + i == zx) {korrekt = true; break;}
                    }
                }
            }
            //
            if (korrekt) {result = {zy, zx}; return result;}
            else {
                std::cin.clear();
                std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
                std::cout << "EINGABE NICHT KORREKT4" << std::endl;
                return eingabe_schlagen_WM(vy, vx, pos, token);
            }
        }
        //
        catch (...) {
            std::cin.clear();
                std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
                std::cout << "EINGABE NICHT KORREKT4" << std::endl;
                return eingabe_schlagen_WM(vy, vx, pos, token);
        }
    }

    //

    bool schlagen_moeglich_XO(int y, int x, const std::vector<std::vector<int>>& pos, int token) {
        bool moeglich = false;
        //
        if (token==1) {
            if (y-2>-1 && x-2>-1) {
                if (pos[y-2][x-2] == 0 && pos[y-1][x-1] <0) {moeglich = true;}
            if (y-2 >-1 && x+2<8) {
                if (pos[y - 2][x + 2] == 0 && pos[y - 1][x + 1] <0) {moeglich = true;}
            }
        }
        else if (token==-1) {
            if (y+2<8 && x-2>-1) {
                if (pos[y+2][x-2] == 0 && pos[y+1][x-1] >0) {moeglich = true;}
            }
            if (y+2<8 && x+2<8) {
                if (pos[y+2][x+2] == 0 && pos[y+1][x+1] >0) {moeglich = true;}
            }
        }
        //
        return moeglich;
        }
    }

    bool schlagen_moeglich_WM(int y, int x, const std::vector<std::vector<int>>& pos, int token) {
        bool moeglich=false;

        if (token==1) {
            for (int i = 0; i < 7; ++i) {
                if (y + 2 + i > 7 || x + 2 + i > 7) {break;}
                if (pos[y + 1 + i][x + 1 + i] > 0) {break;}
                if (pos[y + 1 + i][x + 1 + i] < 0) {
                    if (pos[y + 2 + i][x + 2 + i] == 0) {moeglich = true;break;}
                    else {break;}
                }
            }
            if (!moeglich) {
                for (int i = 0; i < 7; ++i) {
                    if (y - 2 - i < 0 || x + 2 + i > 7) {break;}
                    if (pos[y - 1 - i][x + 1 + i] > 0) {break;}
                    if (pos[y - 1 - i][x + 1 + i] < 0) {
                        if (pos[y - 2 - i][x + 2 + i] == 0) {moeglich = true; break;}
                        else {break;}
                    }
                }
            }
            if (!moeglich) {
                for (int i = 0; i < 7; ++i) {
                    if (y - 2 - i < 0 || x - 2 - i < 0) {break;}
                    if (pos[y - 1 - i][x - 1 - i] > 0) {break;}
                    if (pos[y - 1 - i][x - 1 - i] < 0) {
                        if (pos[y - 2 - i][x - 2 - i] == 0) {moeglich = true; break;}
                        else {break;}
                    }
                }
            }
            if (!moeglich) {
                for (int i = 0; i < 7; ++i) {
                    if (y + 2 + i > 7 || x - 2 - i < 0) {break;}
                    if (pos[y + 1 + i][x - 1 - i] > 0) {break;}
                    if (pos[y + 1 + i][x - 1 - i] < 0) {
                        if (pos[y + 2 + i][x - 2 - i] == 0) {moeglich = true; break;}
                        else {break;}
                    }
                }
            }
        }
        //
        else if (token == -1) {
            for (int i = 0; i < 7; ++i) {
                if (y + 2 + i > 7 || x + 2 + i > 7) {break;}
                if (pos[y + 1 + i][x + 1 + i] < 0) {
                    break;
                }
                if (pos[y + 1 + i][x + 1 + i] > 0) {
                    if (pos[y + 2 + i][x + 2 + i] == 0) {
                        moeglich = true;
                        break;
                    } else {
                        break;
                    }
                }
            }
            if (!moeglich) {
                for (int i = 0; i < 7; ++i) {
                    if (y - 2 - i < 0 || x + 2 + i > 7) {break;}
                    if (pos[y - 1 - i][x + 1 + i] < 0) {break;}
                    if (pos[y - 1 - i][x + 1 + i] > 0) {
                        if (pos[y - 2 - i][x + 2 + i] == 0) {moeglich = true; break;}
                        else {break;}
                    }
                }
            }
            if (!moeglich) {
                for (int i = 0; i < 7; ++i) {
                    if (y - 2 - i < 0 || x - 2 - i < 0) {break;}
                    if (pos[y - 1 - i][x - 1 - i] < 0) {break;}
                    if (pos[y - 1 - i][x - 1 - i] > 0) {
                        if (pos[y - 2 - i][x - 2 - i] == 0) {moeglich = true; break;}
                        else {break;}
                    }
                }
            }
            if (!moeglich) {
                for (int i = 0; i < 7; ++i) {
                    if (y + 2 + i > 7 || x - 2 - i < 0) {break;}
                    if (pos[y + 1 + i][x - 1 - i] < 0) {break;}
                    if (pos[y + 1 + i][x - 1 - i] > 0) {
                        if (pos[y + 2 + i][x - 2 - i] == 0) {moeglich = true; break;}
                        else {break;}
                    }
                }
            }
        }
        //
        return moeglich;
    }

    //

    std::vector<std::vector<int>> player_schlagen_chain_XO(int vy, int vx, std::vector<std::vector<int>>& pos, int token) {
        if (schlagen_moeglich_XO(vy, vx, pos, token)) {
            print_board(pos);
            //
            std::vector<int> input_move = eingabe_schlagen_XO(vy, vx, pos, token);
            int zy=input_move[0];
            int zx=input_move[1];
            //
            if (zx==vx && zy==vy) {}//um nicht mehr zu shlagen
            //
            if (token==1) {
                if (zy==vy-2 && zx==vx-2) {
                    pos[vy][vx]= 0;
                    pos[zy][zx]= 1;
                    if (zy==0) {pos[zy][zx]=2;}
                    pos[vy -1][vx -1] = 0;
                    print_board(pos);
                    //
                    vy=zy;
                    vx=zx;
                    return player_schlagen_chain_XO(vy, vx, pos, token);
                }
                else if (zy==vy-2 && zx == vx + 2) {
                    pos[vy][vx]= 0;
                    pos[zy][zx]= 1;
                    if (zy==0) {pos[zy][zx]= 2;}
                    pos[vy -1][vx +1]= 0;
                    print_board(pos);
                    //
                    vy=zy;
                    vx=zx;
                    return player_schlagen_chain_XO(vy, vx, pos, token);
                }
            }
            //
            else if (token==-1) {
                if (zy==vy+2 && zx==vx-2) {
                    pos[vy][vx]= 0;
                    pos[zy][zx]= -1;
                    if (zy==0) {pos[zy][zx]= -2;}
                    pos[vy +1][vx -1]= 0;
                    print_board(pos);
                    //
                    vy=zy;
                    vx=zx;
                    return player_schlagen_chain_XO(vy, vx, pos, token);
                }
                else if (zy==vy+2 && zx==vx+2) {
                    pos[vy][vx]= 0;
                    pos[zy][zx]= -1;
                    if (zy==0) {pos[zy][zx]= -2;}
                    pos[vy +1][vx +1] = 0;
                    print_board(pos);
                    //
                    vy=zy;
                    vx=zx;
                    return player_schlagen_chain_XO(vy, vx, pos, token);
                }
            }
        }
        //
        else {return pos;}
    }

    std::vector<std::vector<int>> player_schlagen_chain_WM(int vy, int vx, std::vector<std::vector<int>>& pos, int token) {
        if (schlagen_moeglich_WM(vy, vx, pos, token)) {
            print_board(pos);
            //
            std::vector<int> input_move = eingabe_schlagen_WM(vy, vx, pos, token);
            int zy=input_move[0];
            int zx=input_move[1];
            //
            if (zx==vx && zy==vy) {} // um nicht mehr zu schlagen
            //
            if (token==1) {
                if (zy<vy && zx<vx) {
                    pos[vy][vx] = 0;
                    pos[zy][zx] = 2;
                    pos[zy + 1][zx + 1] = 0;
                    print_board(pos);
                    //
                    vy = zy;
                    vx = zx;
                    return player_schlagen_chain_WM(vy, vx, pos, token);
                }
                else if (zy>vy && zx<vx) {
                    pos[vy][vx] = 0;
                    pos[zy][zx] = 2;
                    pos[zy - 1][zx + 1] = 0;
                    print_board(pos);
                    //
                    vy = zy;
                    vx = zx;
                    return player_schlagen_chain_WM(vy, vx, pos, token);
                }
                else if (zy<vy && zx>vx) {
                    pos[vy][vx] = 0;
                    pos[zy][zx] = 2;
                    pos[zy + 1][zx - 1] = 0;
                    print_board(pos);
                    //
                    vy=zy;
                    vx=zx;
                    return player_schlagen_chain_WM(vy, vx, pos, token);
                }
                else if (zy>vy && zx>vx) {
                    pos[vy][vx] = 0;
                    pos[zy][zx] = 2;
                    pos[zy - 1][zx + 1] = 0;
                    print_board(pos);
                    //
                    vy=zy;
                    vx=zx;
                    return player_schlagen_chain_WM(vy, vx, pos, token);
                }
            }
            else if (token==-1) {
                if (zy<vy && zx<vx) {
                    pos[vy][vx]= 0;
                    pos[zy][zx]= -2;
                    pos[zy + 1][zx + 1]= 0;
                    print_board(pos);
                    //
                    vy=zy;
                    vx=zx;
                    return player_schlagen_chain_WM(vy, vx, pos, token);
                }
                else if (zy>vy && zx<vx) {
                    pos[vy][vx]= 0;
                    pos[zy][zx]= -2;
                    pos[zy - 1][zx + 1]= 0;
                    print_board(pos);
                    //
                    vy=zy;
                    vx=zx;
                    return player_schlagen_chain_WM(vy, vx, pos, token);
                }
                else if (zy<vy && zx>vx) {
                    pos[vy][vx]= 0;
                    pos[zy][zx]= -2;
                    pos[zy + 1][zx - 1]= 0;
                    print_board(pos);
                    //
                    vy=zy;
                    vx=zx;
                    return player_schlagen_chain_WM(vy, vx, pos, token);
                }
                else if (zy>vy && zx>vx) {
                    pos[vy][vx]= 0;
                    pos[zy][zx]= -2;
                    pos[zy - 1][zx + 1]= 0;
                    print_board(pos);
                    //
                    vy=zy;
                    vx=zx;
                    return player_schlagen_chain_WM(vy, vx, pos, token);
                }
            }
        }
        else {return pos;}
    }

    //

    std::vector<std::vector<int>> player(std::vector<std::vector<int>>& pos) {
        while (true) {
            std::vector<int> input_move = eingabe();
            int vy=input_move[0];
            int vx=input_move[1];
            int zy=input_move[2];
            int zx=input_move[3];
            //
            if (token == 1) {
                //X normal
                if (zy == vy - 1 && zx == vx - 1 && pos[vy][vx] == 1 && pos[zy][zx] == 0) {
                    pos[vy][vx] = 0;
                    pos[zy][zx] = 1;
                    if (zy == 0) {pos[zy][zx] = 2;}
                    return pos;
                }
                else if (zy == vy - 1 && zx == vx + 1 && pos[vy][vx] == 1 && pos[zy][zx] == 0) {
                    pos[vy][vx] = 0;
                    pos[zy][zx] = 1;
                    if (zy == 0) {pos[zy][zx] = 2;}
                    return pos;
                }
                //schlagen
                else if (zy == vy - 2 && zx == vx - 2 && pos[vy][vx] == 1 && pos[zy][zx] == 0 && pos[vy - 1][vx - 1] < 0) {
                    pos[vy][vx] = 0;
                    pos[zy][zx] = 1;
                    if (zy == 0) {pos[zy][zx] = 2;}
                    pos[vy - 1][vx - 1] = 0;
                    return player_schlagen_chain_XO(zy, zx, pos, this->token);
                }
                else if (zy == vy - 2 && zx == vx + 2 && pos[vy][vx] == 1 && pos[zy][zx] == 0 && pos[vy - 1][vx + 1] < 0) {
                    pos[vy][vx] = 0;
                    pos[zy][zx] = 1;
                    if (zy == 0) {pos[zy][zx] = 2;}
                    pos[vy - 1][vx + 1] = 0;
                    return player_schlagen_chain_XO(zy, zx, pos, this->token);
                }
                // M normal + erstes Mal schlagen
                else if (pos[vy][vx] == 2 && pos[zy][zx] == 0 && zy < vy && zx < vx) {
                    for (int i = 0; i < 7; ++i) {
                        if (vy - i - 1 < 0 || vx - i - 1 < 0) {break;}
                        if (vy - i - 1 == zy && vx - i - 1 == zx) {
                            pos[vy][vx] = 0;
                            pos[zy][zx] = 2;
                            return pos;
                        }
                        if (pos[vy - i - 1][vx - i - 1] > 0) {break;}
                        if (pos[vy - i - 1][vx - i - 1] < 0) {
                            if (!(vy - i - 2 < 0 || vx - i - 2 < 0)) {
                                if (vy - i - 2 == zy && vx - i - 2 == zx) {
                                    pos[vy][vx] = 0;
                                    pos[zy][zx] = 2;
                                    pos[vy - i - 1][vx - i - 1] = 0;
                                    return player_schlagen_chain_WM(zy, zx, pos, this->token);
                                }
                                else {break;}
                            }
                            else {break;}
                        }
                    }
                }
                else if (pos[vy][vx] == 2 && pos[zy][zx] == 0 && zy > vy && zx < vx) {
                    for (int i = 0; i < 7; ++i) {
                        if (vy + i + 1 > 7 || vx - i - 1 < 0) {break;}
                        if (vy + i + 1 == zy && vx - i - 1 == zx) {
                            pos[vy][vx] = 0;
                            pos[zy][zx] = 2;
                            return pos;
                        }
                        if (pos[vy + i + 1][vx - i - 1] > 0) {break;}
                        if (pos[vy + i + 1][vx - i - 1] < 0) {
                            if (!(vy + i + 2 > 7 || vx - i - 2 < 0)) {
                                if (vy + i + 2 == zy && vx - i - 2 == zx) {
                                    pos[vy][vx] = 0;
                                    pos[zy][zx] = 2;
                                    pos[vy + i + 1][vx - i - 1] = 0;
                                    return player_schlagen_chain_WM(zy, zx, pos, this->token);
                                }
                                else {break;}
                            }
                            else {break;}
                        }
                    }
                }
                else if (pos[vy][vx] == 2 && pos[zy][zx] == 0 && zy < vy && zx > vx) {
                    for (int i = 0; i < 7; ++i) {
                        if (vy - i - 1 < 0 || vx + i + 1 > 7) {break;}
                        if (vy - i - 1 == zy && vx + i + 1 == zx) {
                            pos[vy][vx] = 0;
                            pos[zy][zx] = 2;
                            return pos;
                        }
                        if (pos[vy - i - 1][vx + i + 1] > 0) {break;}
                        if (pos[vy - i - 1][vx + i + 1] < 0) {
                            if (!(vy - i - 2 < 0 || vx + i + 2 > 7)) {
                                if (vy - i - 2 == zy && vx + i + 2 == zx) {
                                    pos[vy][vx] = 0;
                                    pos[zy][zx] = 2;
                                    pos[vy - i - 1][vx + i + 1] = 0;
                                    return player_schlagen_chain_WM(zy, zx, pos, this->token);
                                }
                                else {break;}
                            }
                            else {break;}
                        }
                    }
                }
                else if (pos[vy][vx] == 2 && pos[zy][zx] == 0 && zy > vy && zx > vx) {
                    for (int i = 0; i < 7; ++i) {
                        if (vy + i + 1 > 7 || vx + i + 1 > 7) {break;}
                        if (vy + i + 1 == zy && vx + i + 1 == zx) {
                            pos[vy][vx] = 0;
                            pos[zy][zx] = 2;
                            return pos;
                        }
                        if (pos[vy + i + 1][vx + i + 1] > 0) {break;}
                        if (pos[vy + i + 1][vx + i + 1] < 0) {
                            if (!(vy + i + 2 > 7 || vx + i + 2 > 7)) {
                                if (vy + i + 2 == zy && vx + i + 2 == zx) {
                                    pos[vy][vx] = 0;
                                    pos[zy][zx] = 2;
                                    pos[vy + i + 1][vx + i + 1] = 0;
                                    return player_schlagen_chain_WM(zy, zx, pos, this->token);
                                }
                                else {break;}
                            }
                            else {break;}
                        }
                    }
                }
            }
            //
            else if (token == -1) {
                if (zy == vy + 1 && zx == vx - 1 && pos[vy][vx] == -1 && pos[zy][zx] == 0) {
                    pos[vy][vx] = 0;
                    pos[zy][zx] = -1;
                    if (zy == 7) {pos[zy][zx] = -2;}
                    return pos;
                }
                else if (zy == vy + 1 && zx == vx + 1 && pos[vy][vx] == -1 && pos[zy][zx] == 0) {
                    pos[vy][vx] = 0;
                    pos[zy][zx] = -1;
                    if (zy == 7) {pos[zy][zx] = -2;}
                    return pos;
                }
                else if (zy == vy + 2 && zx == vx - 2 && pos[vy][vx] == -1 && pos[zy][zx] == 0 && pos[vy + 1][vx - 1] > 0) {
                    pos[vy][vx] = 0;
                    pos[zy][zx] = -1;
                    if (zy == 0) {pos[zy][zx] = -2;}
                    pos[vy + 1][vx - 1] = 0;
                    return player_schlagen_chain_XO(zy, zx, pos, this->token);
                }
                else if (zy == vy + 2 && zx == vx + 2 && pos[vy][vx] == -1 && pos[zy][zx] == 0 && pos[vy + 1][vx + 1] > 0) {
                    pos[vy][vx] = 0;
                    pos[zy][zx] = -1;
                    if (zy == 0) {pos[zy][zx] = -2;}
                    pos[vy + 1][vx + 1] = 0;
                    return player_schlagen_chain_XO(zy, zx, pos, this->token);
                }
                else if (pos[vy][vx] == -2 && pos[zy][zx] == 0 && zy < vy && zx < vx) {
                    for (int i = 0; i < 7; ++i) {
                        if (vy - i - 1 < 0 || vx - i - 1 < 0) {break;}
                        if (vy - i - 1 == zy && vx - i - 1 == zx) {
                            pos[vy][vx] = 0;
                            pos[zy][zx] = -2;
                            return pos;
                        }
                        if (pos[vy - i - 1][vx - i - 1] < 0) {break;}
                        if (pos[vy - i - 1][vx - i - 1] > 0) {
                            if (!(vy - i - 2 < 0 || vx - i - 2 < 0)) {
                                if (vy - i - 2 == zy && vx - i - 2 == zx) {
                                    pos[vy][vx] = 0;
                                    pos[zy][zx] = -2;
                                    pos[vy - i - 1][vx - i - 1] = 0;
                                    return player_schlagen_chain_WM(zy, zx, pos, this->token);
                                }
                                else {break;}
                            }
                            else {break;}
                        }
                    }
                }
                else if (pos[vy][vx] == -2 && pos[zy][zx] == 0 && zy > vy && zx < vx) {
                    for (int i = 0; i < 7; ++i) {
                        if (vy + i + 1 > 7 || vx - i - 1 < 0) {break;}
                        if (vy + i + 1 == zy && vx - i - 1 == zx) {
                            pos[vy][vx] = 0;
                            pos[zy][zx] = -2;
                            return pos;
                        }
                        if (pos[vy + i + 1][vx - i - 1] < 0) {break;}
                        if (pos[vy + i + 1][vx - i - 1] > 0) {
                            if (!(vy + i + 2 > 7 || vx - i - 2 < 0)) {
                                if (vy + i + 2 == zy && vx - i - 2 == zx) {
                                    pos[vy][vx] = 0;
                                    pos[zy][zx] = -2;
                                    pos[vy + i + 1][vx - i - 1] = 0;
                                    return player_schlagen_chain_WM(zy, zx, pos, this->token);
                                }
                                else {break;}
                            }
                            else {break;}
                        }
                    }
                }
                else if (pos[vy][vx] == -2 && pos[zy][zx] == 0 && zy < vy && zx > vx) {
                    for (int i = 0; i < 7; ++i) {
                        if (vy - i - 1 < 0 || vx + i + 1 > 7) {break;}
                        if (vy - i - 1 == zy && vx + i + 1 == zx) {
                            pos[vy][vx] = 0;
                            pos[zy][zx] = -2;
                            return pos;
                        }
                        if (pos[vy - i - 1][vx + i + 1] < 0) {break;}
                        if (pos[vy - i - 1][vx + i + 1] > 0) {
                            if (!(vy - i - 2 < 0 || vx + i + 2 > 7)) {
                                if (vy - i - 2 == zy && vx + i + 2 == zx) {
                                    pos[vy][vx] = 0;
                                    pos[zy][zx] = -2;
                                    pos[vy - i - 1][vx + i + 1] = 0;
                                    return player_schlagen_chain_WM(zy, zx, pos, this->token);
                                }
                                else {break;}
                            }
                            else {break;}
                        }
                    }
                }
                else if (pos[vy][vx] == -2 && pos[zy][zx] == 0 && zy > vy && zx > vx) {
                    for (int i = 0; i < 7; ++i) {
                        if (vy + i + 1 > 7 || vx + i + 1 > 7) {break;}
                        if (vy + i + 1 == zy && vx + i + 1 == zx) {
                            pos[vy][vx] = 0;
                            pos[zy][zx] = -2;
                            return pos;
                        }
                        if (pos[vy + i + 1][vx + i + 1] < 0) {break;}
                        if (pos[vy + i + 1][vx + i + 1] > 0) {
                            if (!(vy + i + 2 > 7 || vx + i + 2 > 7)) {
                                if (vy + i + 2 == zy && vx + i + 2 == zx) {
                                    pos[vy][vx] = 0;
                                    pos[zy][zx] = -2;
                                    pos[vy + i + 1][vx + i + 1] = 0;
                                    return player_schlagen_chain_WM(zy, zx, pos, this->token);
                                }
                                else {break;}
                            }
                            else {break;}
                        }
                    }
                }
            }
            std::cout << "EINGABE NICHT KORREKT2" << std::endl;
        }
    }

    std::vector<std::vector<int>> get_move(std::vector<std::vector<int>>& board) {
        return player(board);
    }
};

//

int minimax_counter=0;

class MinimaxNode {
public:
    MinimaxNode() : value(0), value_not_none(false), children(), board(), player_am_zug(0), token(0), depth(0), expanded(false) {}

    int value;
    bool value_not_none;
    std::vector<MinimaxNode> children;
    std::vector<std::vector<int>> board;
    int player_am_zug;
    int token;
    int depth;
    bool expanded;

    std::vector<MinimaxNode> expand_node() {
        std::vector<MinimaxNode> new_children;
        std::list<std::vector<std::vector<int>>> list_of_positions = generate_children(this->board, this->player_am_zug);
        for (const std::vector<std::vector<int>>& board_position : list_of_positions) {
            MinimaxNode child;
            child.board = board_position;
            child.player_am_zug = -this->player_am_zug;
            child.token = this->token;
            child.depth = this->depth + 1;
            child.value_not_none = false;
            child.value=0;
            child.children;
            new_children.push_back(child);

        }
        return new_children;
    }

    int minimax(int alpha, int beta, bool max_player, const int max_depth) {
        //
        minimax_counter+=1;
        //
        if (this->depth==max_depth || verloren1(this->board,1) || verloren1(this->board,-1)) {
            this->value = evaluate_position(this->board, this->token);
            this->value_not_none=true;
            return this->value;
        }
        //
        if (!this->expanded) {this->children=this->expand_node(); this->expanded = true;}
        //
        if (max_player) {
            int max_value=-1000000;
            for (MinimaxNode& child : this->children) {
                int eval=child.minimax(alpha,beta,false,max_depth);
                if (eval>max_value) {max_value=eval;}
                //pruning
                if (eval>alpha) {alpha=eval;}
                if (beta<=alpha) {break;}
            }
            this->value=max_value;
            return max_value;
        }
        else if (!max_player) {
            int min_value=1000000;
            for (MinimaxNode& child : this->children) {
                int eval=child.minimax(alpha,beta,true,max_depth);
                if (eval<min_value) {min_value=eval;}
                //pruning
                if (eval<beta) {beta=eval;}
                if (beta<=alpha) {break;}
            }
            this->value=min_value;
            return min_value;
        }

    }

    void sort(bool max_player) {
        if (this->expanded) {
            //
            std::vector<MinimaxNode> not_none_children;
            std::list<MinimaxNode> none_children;
            std::vector<MinimaxNode> sorted_children;
            //
            for (const MinimaxNode& child : this->children) {
                if (!child.value_not_none) {none_children.push_back(child);}
                else if (child.value_not_none) {not_none_children.push_back(child);}
            }
            //
            if (max_player) {
                std::sort(not_none_children.begin(), not_none_children.end(),[](const MinimaxNode& a, const MinimaxNode& b) {return a.value > b.value;});
                //
                sorted_children.insert(sorted_children.end(), not_none_children.begin(), not_none_children.end());
                sorted_children.insert(sorted_children.end(), none_children.begin(), none_children.end());
                this->children=sorted_children;
                //
                for (MinimaxNode& child : not_none_children) {child.sort(false);}
            }
            else if (!max_player) {
                std::sort(not_none_children.begin(), not_none_children.end(),[](const MinimaxNode& a, const MinimaxNode& b) {return a.value < b.value;});
                //
                sorted_children.insert(sorted_children.end(), not_none_children.begin(), not_none_children.end());
                sorted_children.insert(sorted_children.end(), none_children.begin(), none_children.end());
                this->children=sorted_children;
                //
                for (MinimaxNode& child : not_none_children) {child.sort(true);}
            }
        }
    }

};

class MinimaxPlayer {
public:
    MinimaxPlayer(int token, std::vector<std::vector<int>> board) : token(token), board(board) {
        root_node.board = board;
        root_node.player_am_zug = token;
        root_node.token=token;
        root_node.value_not_none = false;
        root_node.value = 0;
        root_node.depth = 0;
        root_node.children = root_node.expand_node();
        root_node.expanded=true;
        //
        minimax_counter=0;
    }
    MinimaxNode root_node;
    int token;
    std::vector<std::vector<int>> board;
    int max_time=1;
    int max_depth=10;
    int starting_depth=1;

    std::vector<std::vector<int>> minimaxer(const int depth, const std::chrono::duration<double> vergangene_zeit) {
        auto start = std::chrono::high_resolution_clock::now();
        //
        std::vector<int> values;
        std::vector<MinimaxNode> best_moves;
        MinimaxNode best_move;
        int best_value = -1000000;
        std::vector<MinimaxNode>& root_node_children=root_node.children;
        std::vector<std::vector<int>> return_board;
        //
        for (MinimaxNode& child : root_node_children){
            int eval;
            eval=child.minimax(-1000000,1000000,false, depth);
            child.value=eval;
            std::cout<<"a ";//child wurde fertig berechnet
            //
            auto now = std::chrono::high_resolution_clock::now();
            std::chrono::duration<double> vergangene_zeit2 =(now+vergangene_zeit)-start;
            if (vergangene_zeit2.count() >= max_time) {std::cout<<" NICHT FERTIG"; break;}
        }
        //
        for (MinimaxNode& child : root_node_children) {values.push_back(child.value);}
        for (int v : values) {if (v > best_value) {best_value = v;}}
        for (MinimaxNode& child : root_node_children) {if (child.value==best_value) {best_moves.push_back(child);}}
        //
        //output---------
        std::cout << std::endl;
        std::cout << best_value << std::endl;
        std::cout<<"COUNTER: "; std::cout<<minimax_counter<<std::endl;
        //---------------
        best_move=best_moves[generate_random_int(0, best_moves.size()-1)];
        return_board=deepcopy(best_move.board);
        return return_board;

    }

    std::vector<std::vector<int>> minimaxerer(const std::vector<std::vector<int>> board_0) {
        auto start = std::chrono::high_resolution_clock::now();
        //
        int depth=this->starting_depth;
        std::vector<std::vector<int>> move;
        while (true) {
            //break
            auto now = std::chrono::high_resolution_clock::now();
            std::chrono::duration<double> vergangene_zeit = now - start;
            if (vergangene_zeit.count() >= max_time) {break;}
            else if (depth>max_depth) {break;}
            //calculate move
            std::cout<<"---DEPTH: ";
            std::cout<<depth<<std::endl;
            //
            std::vector<std::vector<int>> new_move=minimaxer(depth,vergangene_zeit);
            //
            for (MinimaxNode& child : root_node.children) {std::cout<<child.value;  std::cout<<", ";}
            std::cout<<std::endl;
            //sort+depth
            //this->root_node.sort(true);
            move=new_move;
            //
            for (MinimaxNode& child : root_node.children) {std::cout<<child.value;  std::cout<<", ";}
            std::cout<<std::endl;
            if (depth>max_depth) {break;}
            depth+=1;
        }
        return move;
    }

    std::vector<std::vector<int>> get_move(std::vector<std::vector<int>> board) {
        return minimaxerer(board);
    }
};

//

int max_turns=50;

class Dame {
public:
    Dame() : board(), turn(1) {
            board={
            {0,-1,0,-1,0,-1,0,-1},
            {-1,0,-1,0,-1,0,-1,0},
            {0,-1,0,-1,0,-1,0,-1},
            {0,0,0,0,0,0,0,0},
            {0,0,0,0,0,0,0,0},
            {1,0,1,0,1,0,1,0},
            {0,1,0,1,0,1,0,1},
            {1,0,1,0,1,0,1,0},

        };
    }

    int play() {
        int current = 1;

        while (true) {
            //-----------------------------------------
            HumanPlayer player_1(1);
            MinimaxPlayer player_2(-1, this->board);
            //-----------------------------------------
            std::cout<<this->turn<<std::endl;
            print_board(this->board);

            if (current==1) {
                std::cout <<"X ist am Zug"<<std::endl;
                std::vector<std::vector<int>> board_copy = deepcopy(this->board);
                std::vector<std::vector<int>> new_board = player_1.get_move(board_copy);
                this->board=new_board;
            }
            else if (current==2) {
                std::cout<<"O ist am Zug"<<std::endl;
                std::vector<std::vector<int>> board_copy = deepcopy(this->board);
                std::vector<std::vector<int>> new_board = player_2.get_move(board_copy);
                this->board=new_board;
            }
            //
            if (verloren2(this->board, -1)) {print_board(this->board); std::cout<<"X HAT GEWONNEN"<<std::endl; return 1;}
            else if (verloren2(this->board, 1)) {print_board(this->board); std::cout<<"O HAT GEWONNEN"<<std::endl; return -1;}
            else if (this->turn==max_turns) {print_board(this->board); std::cout<<"UNENTSCHIEDEN"<<std::endl; return 0;}
            //
            if (current==1) {current = 2;}
            else {current = 1;}
            this->turn += 1;
        }
    }


private:
    std::vector<std::vector<int>> board;
    int turn;
};

//

void spielen(int z) {
    std::cout<<"NEUES SPIEL"<<std::endl;
    int x_wins=0;
    int o_wins=0;
    int unentschieden=0;
    //
    for (int i=0; i<z; ++i) {
        Dame game;
        int r = game.play();
        if (r==1) {x_wins+=1;}
        else if (r== -1) {o_wins+=1;}
        else if (r==0) {unentschieden+= 1;}
        std::cout<<"X: "<<x_wins<<std::endl;
        std::cout<<"O: "<<o_wins<<std::endl;
        std::cout<<"-: "<<unentschieden<<std::endl;
    }
    std::cout<<"FERTIG"<<std::endl;
}

//

int main() {
    srand(time(0)); //seed
    spielen(3);
}

//sort?

