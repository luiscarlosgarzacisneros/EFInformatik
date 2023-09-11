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

int schlagen_XO_c=3;
int schlagen_WM_c=5;
int WM_c=5;

std::vector<int> gorc_XO_schlagen_children;
std::vector<std::vector<std::vector<int>>> gorc_XO_schlagen_children_delete;
std::vector<int> gorc_WM_schlagen_children;
std::vector<std::vector<std::vector<int>>> gorc_WM_schlagen_children_delete;


void gorc_XO_schlagen(int y, int x, std::vector<std::vector<int>>& boardc, int player, std::vector<std::vector<int>>& delete_list) {
    bool geschlagen = false;
    if (player == 1) {
        if (y-2>-1 && x-2>-1 && boardc[y-2][x-2] == 0 && boardc[y-1][x-1]<0) {
            geschlagen = true;
            std::vector<std::vector<int>> delete_list_1 = delete_list;
            delete_list_1.push_back({y-1, x-1});
            gorc_XO_schlagen(y-2, x-2, boardc, player, delete_list_1);
        }
        if (y-2>-1 && x+2<8 && boardc[y-2][x+2]==0 && boardc[y-1][x+1]<0) {
            geschlagen = true;
            std::vector<std::vector<int>> delete_list_2 = delete_list;
            delete_list_2.push_back({y-1, x+1});
            gorc_XO_schlagen(y-2, x+2, boardc, player, delete_list_2);
        }
        if (!geschlagen) {
            gorc_XO_schlagen_children.push_back((y+1)*10 + (x+1));
            gorc_XO_schlagen_children_delete.push_back(delete_list);
        }
    }
    else if (player == -1) {
        if (y+2<8 && x-2>-1 && boardc[y+2][x-2]==0 && boardc[y+1][x-1]>0) {
            geschlagen = true;
            std::vector<std::vector<int>> delete_list_1 = delete_list;
            delete_list_1.push_back({y+1, x-1});
            gorc_XO_schlagen(y+2, x-2, boardc, player, delete_list_1);
        }
        if (y+2<8 && x+2<8 && boardc[y+2][x+2]==0 && boardc[y+1][x+1]>0) {
            geschlagen = true;
            std::vector<std::vector<int>> delete_list_2 = delete_list;
            delete_list_2.push_back({y+1, x+1});
            gorc_XO_schlagen(y+2, x+2, boardc, player, delete_list_2);
        }
        if (!geschlagen) {
            gorc_XO_schlagen_children.push_back((y+1)*10 + (x+1));
            gorc_XO_schlagen_children_delete.push_back(delete_list);
        }
    }
}

std::vector<std::vector<int>> gorc_XO(int y, int x, std::vector<std::vector<int>>& boardc, int player) {
    std::vector<int> childrenXO;
    gorc_XO_schlagen_children.clear();
    gorc_XO_schlagen_children_delete.clear();
    //
    if (player==1) {
        if (y-1>-1 && x-1>-1 && boardc[y-1][x-1]==0) {childrenXO.push_back(1);}
        if (y-1>-1 && x+1<8 && boardc[y-1][x+1]==0) {childrenXO.push_back(2);}
        if (y-2>-1 && x-2>-1 && boardc[y-2][x-2]==0) {
            if (boardc[y-1][x-1]<0) {std::vector<std::vector<int>> dl; gorc_XO_schlagen(y, x, boardc, player, dl);}
        }
        if (y-2>-1 && x+2<8 && boardc[y-2][x+2]==0) {
            if (boardc[y-1][x+1]<0) {std::vector<std::vector<int>> dl; gorc_XO_schlagen(y, x, boardc, player, dl);}
        }
    }
    else if (player==-1) {
        if (y+1<8 && x-1>-1 && boardc[y+1][x-1]==0) {childrenXO.push_back(1);}
        if (y+1<8 && x+1<8 && boardc[y+1][x+1]==0) {childrenXO.push_back(2);}
        if (y+2<8 && x-2>-1 && boardc[y+2][x-2]==0) {
            if (boardc[y+1][x-1]>0) {std::vector<std::vector<int>> dl; gorc_XO_schlagen(y, x, boardc, player, dl);}
        }
        if (y+2<8 && x+2<8 && boardc[y+2][x+2]==0) {
            if (boardc[y+1][x+1]>0) {std::vector<std::vector<int>> dl; gorc_XO_schlagen(y, x, boardc, player, dl);}
        }
    }
    //
    for (int i=0; i<schlagen_XO_c; ++i) {
        childrenXO.insert(childrenXO.end(), gorc_XO_schlagen_children.begin(), gorc_XO_schlagen_children.end());
    }
    //
    if (childrenXO.empty()) {std::vector<std::vector<int>> empty_vector; return empty_vector;}
    else {
        //
        int r=generate_random_int(0, childrenXO.size()-1);
        int n=childrenXO[r];
        //
        if (player==1) {
            if (n==1) {
                boardc[y][x]= 0;
                if (y-1==0) {boardc[y-1][x-1]= 2;}
                else {boardc[y-1][x-1]= 1;}
                return boardc;
            }
            else if (n==2) {
                boardc[y][x]= 0;
                if (y-1==0) {boardc[y-1][x+1]= 2;}
                else {boardc[y-1][x+1] = 1;}
                return boardc;
            }
            else {// schlagen
                int n_y= (n/10)-1;
                int n_x= (n%10)-1;
                boardc[y][x]= 0;
                if (n_y==0) {boardc[n_y][n_x]= 2;}
                else {boardc[n_y][n_x]= 1;}
                std::vector<std::vector<int>> delete_list = gorc_XO_schlagen_children_delete[std::distance(gorc_XO_schlagen_children.begin(), std::find(gorc_XO_schlagen_children.begin(), gorc_XO_schlagen_children.end(), n))];
                for (const auto& feld : delete_list) {boardc[feld[0]][feld[1]]= 0;}
                return boardc;
            }
        }
        else if (player==-1) {
            if (n==1) {
                boardc[y][x]= 0;
                if (y+1==7) {boardc[y-1][x-1]= -2;}
                else {boardc[y+1][x-1]= -1;}
                return boardc;
            }
            else if (n==2) {
                boardc[y][x]= 0;
                if (y+1==7) {boardc[y-1][x+1]= -2;}
                else {boardc[y+1][x+1] = -1;}
                return boardc;
            }
            else {// schlagen
                int n_y= (n/10)-1;
                int n_x= (n%10)-1;
                boardc[y][x]= 0;
                if (n_y==0) {boardc[n_y][n_x] = -2;}
                else {boardc[n_y][n_x]= -1;}
                std::vector<std::vector<int>> delete_list = gorc_XO_schlagen_children_delete[std::distance(gorc_XO_schlagen_children.begin(), std::find(gorc_XO_schlagen_children.begin(), gorc_XO_schlagen_children.end(), n))];
                for (const auto& feld : delete_list) {boardc[feld[0]][feld[1]]= 0;}
                return boardc;
            }
        }
    }
}

void gorc_WM_schlagen(int y, int x, std::vector<std::vector<int>>& boardc, int player, std::vector<std::vector<int>>& delete_list) {
    bool geschlagen = false;
    std::vector<std::pair<int, int>> directions = {{1, 1}, {-1, 1}, {1, -1}, {-1, -1}};
    //
    if (player == 2) {
        for (const auto& direction : directions) {
            int dy = direction.first;
            int dx = direction.second;
            for (int i= 1; i<8; ++i) {
                if (y+i*dy>7 ||x+i*dx>7 || y+i*dy<0 || x+i*dx<0) {break;}
                if (boardc[y+i*dy][x+i*dx]>0) {break;}
                if (boardc[y+i*dy][x+i*dx]<0) {
                    bool r = false;
                    for (const auto& piece : delete_list) {
                        if (piece[0]==y+i*dy && piece[1]==x+i*dx) {r=true; break;}
                    }
                    if (r) {break;}
                    if (!(y+(i+1)*dy>7) && !(x+(i+1)*dx>7) && !(y+(i+1)*dy<0) && !(x+(i+1)*dx<0) && boardc[y+(i+1)*dy][x+(i+1)*dx]==0) {
                        geschlagen = true;
                        delete_list.push_back({y+i*dy, x+i*dx});
                        gorc_WM_schlagen(y+(i+1)*dy, x+(i+1)*dx, boardc, player, delete_list);
                        break;
                    }
                    else {break;}
                }
            }
        }
    }
    //
    else if (player==-2) {
        for (const auto& direction : directions) {
            int dy = direction.first;
            int dx = direction.second;
            for (int i=1; i<8; ++i) {
                if (y+i*dy>7 || x+i*dx>7 || y+i*dy<0 || x+i*dx<0) {break;}
                if (boardc[y+i*dy][x+i*dx]<0) {break;}
                if (boardc[y+i*dy][x+i*dx]>0) {
                    bool r = false;
                    for (const auto& piece : delete_list) {
                        if (piece[0]==y+i*dy && piece[1]==x+i*dx) {r=true; break;}
                    }
                    if (r) {break;}
                    if (!(y+(i+1)*dy>7) && !(x+(i+1)*dx>7) && !(y+(i+1)*dy<0) && !(x+(i+1)*dx<0) && boardc[y+(i+1)*dy][x+(i+1)*dx]==0) {
                        geschlagen = true;
                        delete_list.push_back({y+i*dy, x+i*dx});
                        gorc_WM_schlagen(y+(i+1)*dy, x+(i+1)*dx, boardc, player, delete_list);
                        break;
                    }
                    else {break;}
                }
            }
        }
    }
    //
    if (!geschlagen) {
        gorc_WM_schlagen_children.push_back(((y+1)*10) + ((x+1) +100));
        gorc_WM_schlagen_children_delete.push_back(delete_list);
    }
}

std::vector<std::vector<int>> gorc_WM(int y, int x, std::vector<std::vector<int>>& boardc, int player) {
    std::vector<int> children_WM;
    std::vector<std::vector<int>> directions = {{1, 1, 10}, {1, -1, 20}, {-1, 1, 30}, {-1, -1, 40}};
    gorc_WM_schlagen_children.clear();
    gorc_WM_schlagen_children_delete.clear();

    if (player == 2) {
        for (const auto& direction : directions) {
            int dy = direction[0];
            int dx = direction[1];
            int d = direction[2];
            for (int i=1; i<8; ++i) {
                if (y+i*dy>7 || x+i*dx>7 || y+i*dy<0 || x+i*dx<0) {break;}
                if (boardc[y+i*dy][x+i*dx]>0) {break;}
                if (boardc[y+i*dy][x+i*dx]==0) {children_WM.push_back(d + i);}
                if (boardc[y+i*dy][x+i*dx]<0) {
                    if (!(y+(i+1)*dy>7) && !(x+(i+1)*dx>7) && !(y+(i+1)*dy<0) && !(x+(i+1)*dx<0)) {
                        if (boardc[y+(i+1)*dy][x+(i+1)*dx]==0) {
                            std::vector<std::vector<int>> del_vector;
                            gorc_WM_schlagen(y, x, boardc, player, del_vector);
                            break;
                        }
                        else {break;}
                    }
                    else {break;}
                }
            }
        }
    }
    else if (player == -2) {
        for (const auto& direction : directions) {
            int dy = direction[0];
            int dx = direction[1];
            int d = direction[2];
            for (int i=1; i<8; ++i) {
                if (y+i*dy>7 || x+i*dx>7 || y+i*dy<0 || x+i*dx<0) {break;}
                if (boardc[y+i*dy][x+i*dx]<0) {break;}
                if (boardc[y+i*dy][x+i*dx]==0) {children_WM.push_back(d + i);}
                if (boardc[y+i*dy][x+i*dx]>0) {
                    if (!(y+(i+1)*dy>7) && !(x+(i+1)*dx>7) && !(y+(i+1)*dy<0) && !(x+(i+1)*dx<0)) {
                        if (boardc[y+(i+1)*dy][x+(i+1)*dx]==0) {
                            std::vector<std::vector<int>> del_vector;
                            gorc_WM_schlagen(y, x, boardc, player, del_vector);
                            break;
                        }
                        else {break;}
                    }
                    else {break;}
                }
            }
        }
    }
    //
    for (int i=0; i<schlagen_WM_c; ++i) {
    children_WM.insert(children_WM.end(), gorc_WM_schlagen_children.begin(), gorc_WM_schlagen_children.end());
    }
    //
    if (children_WM.empty()) {std::vector<std::vector<int>> empty_vector; return empty_vector;}
    else {
        //
        int r=generate_random_int(0, children_WM.size()-1);
        int n=children_WM[r];
        //
        if (n>10 && n<20) { //ur
            boardc[y][x]=0;
            boardc[y+(n-10)][x+(n-10)]=2;
            return boardc;
        }
        else if (n>20 && n<30) { //ul
            boardc[y][x]=0;
            boardc[y+(n-20)][x-(n-20)]=2;
            return boardc;
        }
        else if (n>30 && n<40) { //or
            boardc[y][x]=0;
            boardc[y-(n-30)][x+(n-30)]=2;
            return boardc;
        }
        else if (n>40 && n<50) { //ol
            boardc[y][x]=0;
            boardc[y-(n-40)][x-(n-40)]=2;
            return boardc;
        }
        else if (n>100) { //schlagen
            int n_y=((n-100)/10)-1;
            int n_x=((n-100)%10)-1;
            boardc[y][x]=0;
            boardc[n_y][n_x]=player;
            //
            std::vector<std::vector<int>> delete_list = gorc_WM_schlagen_children_delete[std::find(gorc_WM_schlagen_children.begin(), gorc_WM_schlagen_children.end(), n) - gorc_WM_schlagen_children.begin()];
            for (const auto& feld : delete_list) {boardc[feld[0]][feld[1]]= 0;}
            return boardc;
        }
    }
}

std::vector<std::vector<int>> generate_one_random_child(std::vector<std::vector<int>> boardcopy, int player) {
    //
    std::vector<int> pieces_y;
    std::vector<int> pieces_x;
    if (player==1) {
        for (int y=0; y<8; ++y) {
            for (int x=0; x<8; ++x) {
                if (boardcopy[y][x]==1) {pieces_y.push_back(y); pieces_x.push_back(x);}
                else if (boardcopy[y][x]==2) {for (int i=0; i<WM_c; ++i) {pieces_y.push_back(y); pieces_x.push_back(x);}}
            }
        }
    } else if (player==-1) {
        for (int y=0; y<8; ++y) {
            for (int x=0; x<8; ++x) {
                if (boardcopy[y][x]==-1) {pieces_y.push_back(y); pieces_x.push_back(x);}
                else if (boardcopy[y][x]==-2) {for (int i=0; i<WM_c; ++i) {pieces_y.push_back(y); pieces_x.push_back(x);}}
            }
        }
    }
    //
    if (pieces_x.empty()) {return {{0}};}
    //
    std::vector<std::vector<int>> child;
    for (int i=0; i<30; ++i) {
        int n=generate_random_int(0, pieces_y.size()-1);
        int y=pieces_y[n];
        int x=pieces_x[n];
        //
        if (player==1) {
            if (boardcopy[y][x]==1) {child=gorc_XO(y, x, boardcopy, 1);}
            else if (boardcopy[y][x]==2) {child=gorc_WM(y, x, boardcopy, 2);}
        }
        else if (player==-1) {
            if (boardcopy[y][x]==-1) {child=gorc_XO(y, x, boardcopy, -1);}
            else if (boardcopy[y][x]==-2) {child=gorc_WM(y, x, boardcopy, -2);}
        }
        //
        if (!child.empty()) {break;}
    }
    //
    if (!child.empty()) {return child;}
    else {std::vector<std::vector<int>> empty_vector; return empty_vector;}
}

//

std::vector<std::vector<int>> board={
            {0,0,0,0,0,0,0,0},
            {0,0,0,0,0,0,0,0},
            {0,0,0,0,0,0,0,0},
            {0,0,1,0,1,0,0,0},
            {0,0,0,2,0,0,0,0},
            {0,0,0,0,1,0,0,0},
            {0,0,0,0,0,0,0,0},
            {0,0,0,0,0,0,0,0}

        };

main() {
    for (int i=0; i<9; ++i) {
        std::cout<<"jhk"<<std::endl;
        std::vector<std::vector<int>> child=generate_one_random_child(board, 1);
        print_board(child);
        std::cout<<"jhk"<<std::endl;

    }
}
