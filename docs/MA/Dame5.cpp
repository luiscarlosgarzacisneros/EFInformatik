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
    int extractedValue;
    return (iss >> extractedValue) && (iss.eof());
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

bool verloren1(const std::vector<std::vector<int>>& pos, int player) {
    int player2 =(player==1) ? 2 : -2;
    int eval=0;
    //
    for (size_t sl=0; sl < pos.size(); ++sl) {
        eval+=std::count(pos[sl].begin(), pos[sl].end(), player);
        eval+=std::count(pos[sl].begin(), pos[sl].end(), player2);
    }
    eval==0 ? return true : return false;
}

//keine_zugmoeglichkeiten

//verloren2

std::vector<std::vector<int>> children_schlagen_XO;
std::vector<std::vector<int>> children_schlagen_WM;

void generate_children_schlagen_XO(int y, int x, const std::vector<std::vector<int>>& board, int player, bool new_flag) {
    if (new_flag) {
        children_schlagen_XO.clear();
    }
    std::vector<std::vector<int>> board_copy = board;

    if (player==1) {
        if (y - 2 > -1 && x - 2 > -1 && board_copy[y - 2][x - 2]==0) {
            if (board_copy[y - 1][x - 1] < 0) {
                board_copy[y - 1][x - 1] = 0;
                board_copy[y - 2][x - 2] = 1;
                board_copy[y][x] = 0;
                if (y - 2 == 0) {
                    board_copy[y - 2][x - 2] = 2;
                }
                children_schlagen_XO.push_back(board_copy);
                generate_children_schlagen_XO(y - 2, x - 2, board_copy, player, false);
                board_copy = board;
            }
        }
        if (y - 2 > -1 && x + 2 < 8 && board_copy[y - 2][x + 2]==0) {
            if (board_copy[y - 1][x + 1] < 0) {
                board_copy[y - 1][x + 1] = 0;
                board_copy[y - 2][x + 2] = 1;
                board_copy[y][x] = 0;
                if (y - 2 == 0) {
                    board_copy[y - 2][x + 2] = 2;
                }
                children_schlagen_XO.push_back(board_copy);
                generate_children_schlagen_XO(y - 2, x + 2, board_copy, player, false);
                board_copy = board;
            }
        }
    }
    else if (player==-1) {
        if (y + 2 < 8 && x - 2 > -1 && board_copy[y + 2][x - 2]==0) {
            if (board_copy[y + 1][x - 1] > 0) {
                board_copy[y + 1][x - 1] = 0;
                board_copy[y + 2][x - 2] = -1;
                board_copy[y][x] = 0;
                if (y + 2 == 7) {
                    board_copy[y + 2][x - 2] = -2;
                }
                children_schlagen_XO.push_back(board_copy);
                generate_children_schlagen_XO(y + 2, x - 2, board_copy, player, false);
                board_copy = board;
            }
        }
        if (y + 2 < 8 && x + 2 < 8 && board_copy[y + 2][x + 2]==0) {
            if (board_copy[y + 1][x + 1] > 0) {
                board_copy[y + 1][x + 1] = 0;
                board_copy[y + 2][x + 2] = -1;
                board_copy[y][x] = 0;
                if (y + 2 == 7) {
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

void generate_children_schlagen_WM(int y, int x, std::vector<std::vector<int>>& board, int player, bool new_flag) {
    if (new_flag) {children_schlagen_WM.clear();}
    //
    std::vector<std::vector<int>> board_copy = board;
    //
    if (player == -2) {
        //
        for (int o = 0; o < 7; ++o) {
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
        for (int o = 0; o < 7; ++o) {
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
        for (int o = 0; o < 7; ++o) {
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
        for (int o = 0; o < 7; ++o) {
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
        for (int o = 0; o < 7; ++o) {
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
        for (int o = 0; o < 7; ++o) {
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
        for (int o = 0; o < 7; ++o) {
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




std::vector<std::vector<int>> generate_children(const std::vector<std::vector<int>>& board, int player) {
    std::vector<std::vector<int>> children1;
    std::vector<std::vector<int>> children2;
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
                    // Call genchildrenschlagen and add results to children1
                    std::vector<std::vector<int>> children_s = genchildrenschlagen(y, x, board_copy, 1, true);
                    children1.insert(children1.end(), children_s.begin(), children_s.end());
                    //
                }
                else if (board_copy[y][x] == 2) {
                    // Call genchildrenWM and add results to children1
                    std::vector<std::vector<int>> children_wm = genchildrenWM(y, x, board_copy, 2);
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
                    // Call genchildrenschlagen and add results to children1
                    std::vector<std::vector<int>> children_s = genchildrenschlagen(y, x, board_copy, -1, true);
                    children1.insert(children1.end(), children_s.begin(), children_s.end());
                    //
                }
                else if (board_copy[y][x] == -2) {
                    // Call genchildrenWM and add results to children1
                    std::vector<std::vector<int>> children_wm = genchildrenWM(y, x, board_copy, -2);
                    children1.insert(children1.end(), children_wm.begin(), children_wm.end());
                    //
                }
            }
        }
    }

    children1.insert(children1.end(), children2.begin(), children2.end());
    return children1;
}


