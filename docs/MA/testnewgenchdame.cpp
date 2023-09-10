#include <iostream>
#include <vector>
#include <list>
#include <algorithm>
#include <cstdlib>
#include <ctime>
#include <chrono>
#include <cmath>
#include <sstream>
#include <string>

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

void generate_children_schlagen_XO(int y, int x, const std::vector<std::vector<int>> board, int player, bool new_b) {
    if (new_b) {children_schlagen_XO.clear();}
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

void generate_children_schlagen_WM(int y, int x, std::vector<std::vector<int>> board, int player, bool new_b) {
    if (new_b) {children_schlagen_WM.clear();}
    std::vector<std::pair<int, int>> directions = {{1, 1}, {-1, 1}, {1, -1}, {-1, -1}};
    std::vector<std::vector<int>> board_copy = board;
    //
    if (player==-2) {
        for (const auto& direction : directions) {
            int dy = direction.first;
            int dx = direction.second;
            for (int o=1; o<8; ++o) {
                if (y+(1+o)*dy>7 || x+(1+o)*dx>7 || y+(1+o)*dy<0 || x+(1+o)*dx<0) {break;}
                if (board_copy[y+o*dy][x+o*dx]<0) {break;}
                if (board_copy[y+o*dy][x+o*dx]>0) {
                    if (board_copy[y+(1+o)*dy][x+(1+o)*dx]==0) {
                        board_copy[y+(1+o)*dy][x+(1+o)*dx]=-2;
                        board_copy[y+o*dy][x+o*dx]=0;
                        board_copy[y][x]=0;
                        children_schlagen_WM.push_back(board_copy);
                        generate_children_schlagen_WM(y+(1+o)*dy, x+(1+o)*dx, board_copy, -2, false);
                        board_copy=board;
                        break;
                    }
                    else {break;}
                }
            }
        }
    }
    //
    else if (player==2) {
        for (const auto& direction : directions) {
            int dy = direction.first;
            int dx = direction.second;
            for (int o=1; o<8; ++o) {
                if (y+(1+o)*dy>7 || x+(1+o)*dx>7 || y+(1+o)*dy<0 || x+(1+o)*dx<0) {break;}
                if (board_copy[y+o*dy][x+o*dx]>0) {break;}
                if (board_copy[y+o*dy][x+o*dx]<0) {
                    if (board_copy[y+(1+o)*dy][x+(1+o)*dx]==0) {
                        board_copy[y+(1+o)*dy][x+(1+o)*dx]=2;
                        board_copy[y+o*dy][x+o*dx]=0;
                        board_copy[y][x]=0;
                        children_schlagen_WM.push_back(board_copy);
                        generate_children_schlagen_WM(y+(1+o)*dy, x+(1+o)*dx, board_copy, 2, false);
                        board_copy=board;
                        break;
                    }
                    else {break;}
                }
            }
        }
    }
    //
    children_schlagen_WM.reverse();
}

std::list<std::vector<std::vector<int>>> generate_children_WM(int y, int x, std::vector<std::vector<int>> board, int player) {
    std::vector<std::pair<int, int>> directions = {{1, 1}, {-1, 1}, {1, -1}, {-1, -1}};
    std::list<std::vector<std::vector<int>>> childrenWM1;
    std::list<std::vector<std::vector<int>>> childrenWM2;
    std::vector<std::vector<int>> board_copy = board;
    bool schlagen = false;
    
    //
    if (player==-2) {
        for (const auto& direction : directions) {
            int dy = direction.first;
            int dx = direction.second;

            for (int o=1; o<8; ++o) {
                schlagen = false;
                if (y+o*dy>7 || x+o*dx>7 || y+o*dy<0 || x+o*dx<0) {break;}
                if (board_copy[y+o*dy][x+o*dx] < 0) {break;}
                if (board_copy[y+o*dy][x+o*dx] > 0) {
                    if (!(y+(o+1)*dy>7) && !(x+(o+1)*dx>7) && !(y+(o+1)*dy<0) && !(x+(o+1)*dx<0)) {
                        schlagen = true;}
                }
                if (board_copy[y+o*dy][x+o*dx] == 0) {
                    board_copy[y+o*dy][x+o*dx] = -2;
                    board_copy[y][x] = 0;
                    childrenWM2.push_back(board_copy);
                    board_copy = board;
                }
                if (schlagen) {
                    if (board_copy[y+(o+1)*dy][x+(o+1)*dx] == 0) {
                        board_copy[y+(o+1)*dy][x+(o+1)*dx] = -2;
                        board_copy[y][x] = 0;
                        board_copy[y+o*dy][x+o*dx] = 0;
                        childrenWM1.push_back(board_copy);
                        children_schlagen_WM.clear();
                        generate_children_schlagen_WM(y+(o+1)*dy, x+(o+1)*dx, board_copy, -2, true);
                        std::list<std::vector<std::vector<int>>> children_s = children_schlagen_WM;
                        childrenWM1.insert(childrenWM1.end(), children_s.begin(), children_s.end());
                        board_copy = board;
                        schlagen = false;
                        break;
                    }
                    else {break;}
                }
            }
        }
    }
    else if (player==2) {
        for (const auto& direction : directions) {
            int dy = direction.first;
            int dx = direction.second;
            for (int o=1; o<8; ++o) {
                schlagen = false;
                if (y+o*dy>7 || x+o*dx>7 || y+o*dy<0 || x+o*dx<0) {break;}
                if (board_copy[y+o*dy][x+o*dx] > 0) {break;}
                if (board_copy[y+o*dy][x+o*dx] < 0) {
                    if (!(y+(o+1)*dy>7) && !(x+(o+1)*dx>7) && !(y+(o+1)*dy<0) && !(x+(o+1)*dx<0)) {
                        schlagen = true;}
                }
                if (board_copy[y+o*dy][x+o*dx] == 0) {
                    board_copy[y+o*dy][x+o*dx] = 2;
                    board_copy[y][x] = 0;
                    childrenWM2.push_back(board_copy);
                    board_copy = board;
                }
                if (schlagen) {
                    if (board_copy[y+(o+1)*dy][x+(o+1)*dx] == 0) {
                        board_copy[y+(o+1)*dy][x+(o+1)*dx] = 2;
                        board_copy[y][x] = 0;
                        board_copy[y+o*dy][x+o*dx] = 0;
                        childrenWM1.push_back(board_copy);
                        children_schlagen_WM.clear();
                        generate_children_schlagen_WM(y+(o+1)*dy, x+(o+1)*dx, board_copy, -2, true);
                        std::list<std::vector<std::vector<int>>> children_s = children_schlagen_WM;
                        childrenWM1.insert(childrenWM1.end(), children_s.begin(), children_s.end());
                        board_copy = board;
                        schlagen = false;
                        break;
                    }
                    else {break;}
                }
            }
        }
    }
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



//

std::vector<std::vector<int>> board={
            {0,0,0,0,0,0,0,0},
            {0,0,0,0,0,2,0,0},
            {0,0,0,0,0,0,-1,0},
            {0,0,0,0,0,1,0,0},
            {0,0,0,0,0,0,0,0},
            {0,0,0,0,0,1,0,0},
            {0,0,0,0,0,0,0,0},
            {0,0,0,0,0,0,0,-2}

        };

main() {
    std::cout<<"jhk"<<std::endl;
    std::list<std::vector<std::vector<int>>> children=generate_children(board, -1);
    for (auto child : children) {print_board(child);}
    std::cout<<"jhk"<<std::endl;
}
