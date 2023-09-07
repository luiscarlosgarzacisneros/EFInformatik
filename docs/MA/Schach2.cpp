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

//-1:B
//-2:L
//-3:X
//-4:T
//-5:Q
//-6:K
//-7:Z not moved towerT
//-8:Y not moved kingK
//-9:F en passant B (just moved 2 forw)

//1:b
//2:l
//3:x
//4:t
//5:q
//6:k
//7:z not moved towert
//8:y not moved kingk
//9:f en passant b (just moved 2 forw)

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

//

void print_board(const std::vector<std::vector<int>>& board) {
    std::cout << "  1   2   3   4   5   6   7   8\n";
    std::cout << "---------------------------------\n";
    for (int i=0; i<8; ++i) {
        std::cout << i+1 << " ";
        for (int j=0; j<8; ++j) {
            if (board[i][j]==1 || board[i][j]==9) {std::cout << 'b';}
            else if (board[i][j]==2) {std::cout << 'l';}
            else if (board[i][j]==3) {std::cout << 'x';}
            else if (board[i][j]==4 || board[i][j]==7) {std::cout << 't';}
            else if (board[i][j]==5) {std::cout << 'q';}
            else if (board[i][j]==6 || board[i][j]==8) {std::cout << 'k';}
            else if (board[i][j]==-1 || board[i][j]==-9) {std::cout << 'B';}
            else if (board[i][j]==-2) {std::cout << 'L';}
            else if (board[i][j]==-3) {std::cout << 'X';}
            else if (board[i][j]==-4 || board[i][j]==-7) {std::cout << 'T';}
            else if (board[i][j]==-5) {std::cout << 'Q';}
            else if (board[i][j]==-6 || board[i][j]==-8) {std::cout << 'K';}
            else if (board[i][j]==0) {std::cout << ' ';}
            std::cout << " ";
        }
        std::cout << '\n';
        std::cout << "---------------------------------\n";
    }
}

//

int minimax_counter=0;

std::vector<std::vector<std::vector<int>>> generate_children(const std::vector<std::vector<int>> position, int playerk);//declaration weil gcKk gc in def hat und gc gcKk in def hat.

std::vector<std::vector<std::vector<int>>> gcKk(int y, int x, const std::vector<std::vector<int>> pos, int player) {
    std::vector<std::vector<int>> boardc = pos;
    std::vector<std::vector<std::vector<int>>> childrenK;
    //
    if (player==-6 || player==-8) {
        if (y+1<8 && x+1<8) {
            if (boardc[y+1][x+1]>=0) {
                boardc[y][x]=0;
                boardc[y+1][x+1]=-6;
                childrenK.push_back(boardc);
                boardc = pos;
            }
        }
        if (y+1<8 && x-1>-1) {
            if (boardc[y+1][x-1]>=0) {
                boardc[y][x]=0;
                boardc[y+1][x-1]=-6;
                childrenK.push_back(boardc);
                boardc = pos;
            }
        }
        if (y-1>-1 && x+1<8) {
            if (boardc[y-1][x+1]>=0) {
                boardc[y][x]=0;
                boardc[y-1][x+1]=-6;
                childrenK.push_back(boardc);
                boardc = pos;
            }
        }
        if (y-1>-1 && x+1<8) {
            if (boardc[y-1][x-1]>=0) {
                boardc[y][x]=0;
                boardc[y-1][x-1]=-6;
                childrenK.push_back(boardc);
                boardc = pos;
            }
        }
        if (x+1<8) {
            if (boardc[y][x+1]>=0) {
                boardc[y][x]=0;
                boardc[y][x+1]=-6;
                childrenK.push_back(boardc);
                boardc = pos;
            }
        }
        if (x-1>-1) {
            if (boardc[y][x-1]>=0) {
                boardc[y][x]=0;
                boardc[y][x-1]=-6;
                childrenK.push_back(boardc);
                boardc = pos;
            }
        }
        if (y+1<8) {
            if (boardc[y+1][x]>=0) {
                boardc[y][x]=0;
                boardc[y+1][x]=-6;
                childrenK.push_back(boardc);
                boardc = pos;
            }
        }
        if (y-1>-1) {
            if (boardc[y-1][x]>=0) {
                boardc[y][x]=0;
                boardc[y-1][x]=-6;
                childrenK.push_back(boardc);
                boardc = pos;
            }
        }
    }
    else if (player==6 || player==8) {
        if (y+1<8 && x+1<8) {
            if (boardc[y+1][x+1]<=0) {
                boardc[y][x]=0;
                boardc[y+1][x+1]=6;
                childrenK.push_back(boardc);
                boardc = pos;
            }
        }
        if (y+1<8 && x-1>-1) {
            if (boardc[y+1][x-1]<=0) {
                boardc[y][x]=0;
                boardc[y+1][x-1]=6;
                childrenK.push_back(boardc);
                boardc = pos;
            }
        }
        if (y-1>-1 && x+1<8) {
            if (boardc[y-1][x+1]<=0) {
                boardc[y][x]=0;
                boardc[y-1][x+1]=6;
                childrenK.push_back(boardc);
                boardc = pos;
            }
        }
        if (y-1>-1 && x+1<8) {
            if (boardc[y-1][x-1]<=0) {
                boardc[y][x]=0;
                boardc[y-1][x-1]=6;
                childrenK.push_back(boardc);
                boardc = pos;
            }
        }
        if (x+1<8) {
            if (boardc[y][x+1]<=0) {
                boardc[y][x]=0;
                boardc[y][x+1]=6;
                childrenK.push_back(boardc);
                boardc = pos;
            }
        }
        if (x-1>-1) {
            if (boardc[y][x-1]<=0) {
                boardc[y][x]=0;
                boardc[y][x-1]=6;
                childrenK.push_back(boardc);
                boardc = pos;
            }
        }
        if (y+1<8) {
            if (boardc[y+1][x]<=0) {
                boardc[y][x]=0;
                boardc[y+1][x]=6;
                childrenK.push_back(boardc);
                boardc = pos;
            }
        }
        if (y-1>-1) {
            if (boardc[y-1][x]<=0) {
                boardc[y][x]=0;
                boardc[y-1][x]=6;
                childrenK.push_back(boardc);
                boardc = pos;
            }
        }
    }
    //Rochade
    if (player==-8) {
        if (boardc[0][0]==-7 && boardc[0][1]==0 && boardc[0][2]==0 && boardc[0][3]==0) {
            boardc[0][2]=-6;
            boardc[0][3]=-4;
            boardc[0][0]=0;
            boardc[0][4]=0;
            bool legal = true;
            for (auto child : generate_children(boardc, 6)) {
                if (child[0][2]>0 || child[0][3]>0 || child[0][4]>0) {legal = false; break;}
            }
            if (legal) {childrenK.push_back(boardc);}
            boardc = pos;
        }
        if (boardc[0][7]==-7 && boardc[0][6]==0 && boardc[0][5]==0) {
            boardc[0][6]=-6;
            boardc[0][5]=-4;
            boardc[0][7]=0;
            boardc[0][4]=0;
            bool legal = true;
            for (auto child : generate_children(boardc, 6)) {
                if (child[0][4]>0 || child[0][5]>0 || child[0][6]>0) {legal = false; break;}
            }
            if (legal) {childrenK.push_back(boardc);}
            boardc = pos;
        }
    }
    else if (player==8) {
        if (boardc[7][0]==7 && boardc[7][1]==0 && boardc[7][2]==0 && boardc[7][3]==0) {
            boardc[7][2]=6;
            boardc[7][3]=4;
            boardc[7][0]=0;
            boardc[7][4]=0;
            bool legal = true;
            for (auto child : generate_children(boardc, -6)) {
                if (child[7][2]<0 || child[7][3]<0 || child[7][4]<0) {legal = false; break;}
            }
            if (legal) {childrenK.push_back(boardc);}
            boardc = pos;
        }
        if (boardc[7][7]==7 && boardc[7][6]==0 && boardc[7][5]==0) {
            boardc[7][6]=6;
            boardc[7][5]=4;
            boardc[7][7]=0;
            boardc[7][4]=0;
            bool legal = true;
            for (auto child : generate_children(boardc, -6)) {
                if (child[7][4]<0 || child[7][5]<0 || child[7][6]<0) {legal = false; break;}
            }
            if (legal) {childrenK.push_back(boardc);}
            boardc = pos;
        }
    }
    //
    return childrenK;
}

std::vector<std::vector<std::vector<int>>> gcLl(int y, int x, const std::vector<std::vector<int>> pos, int player) {
    std::vector<std::vector<int>> boardc = pos;
    std::vector<std::vector<std::vector<int>>> childrenL;
    //
    int direction_y[] = {-2, -2, 2, 2, 1, -1, 1, -1};
    int direction_x[] = {1, -1, 1, -1, 2, 2, -2, -2};
    //
    if (player==-2) {
        for (int i=0; i<8; ++i) {
            int new_y= y+direction_y[i];
            int new_x= x+direction_x[i];
            if (new_y>-1 && new_y<8 && new_x>-1 && new_x<8 && pos[new_y][new_x]>=0) {
                boardc=pos;
                boardc[y][x]=0;
                boardc[new_y][new_x]=-2;
                childrenL.push_back(boardc);
            }
        }
    }
    else if (player==2) {
        for (int i=0; i<8; ++i) {
            int new_y= y+direction_y[i];
            int new_x= x+direction_x[i];
            if (new_y>-1 && new_y<8 && new_x>-1 && new_x<8 && pos[new_y][new_x] <= 0) {
                boardc=pos;
                boardc[y][x]=0;
                boardc[new_y][new_x]=2;
                childrenL.push_back(boardc);
            }
        }
    }
    //
    return childrenL;
}

std::vector<std::vector<std::vector<int>>> gcBb(int y, int x, const std::vector<std::vector<int>> pos, int player) {
    std::vector<std::vector<int>> boardc = pos;
    std::vector<std::vector<std::vector<int>>> childrenB;
    //
    if (player==-1) {
        if (y==1 && boardc[y+2][x]==0 && boardc[y+1][x]==0) {
            boardc[y][x]=0;
            boardc[y+2][x]=-9;
            childrenB.push_back(boardc);
            boardc=pos;
        }
        if (y+1<8) {
            if (boardc[y+1][x]==0) {
                boardc[y][x]=0;
                boardc[y+1][x]=-1;
                if (y+1==7) {boardc[y+1][x]=-5;}
                childrenB.push_back(boardc);
                boardc=pos;
            }
        }
        if (x-1>-1 && y+1<8) {
            if (boardc[y+1][x-1]>0) {
                boardc[y][x]=0;
                boardc[y+1][x-1]=-1;
                if (y+1==7) {boardc[y+1][x-1]=-5;}
                childrenB.push_back(boardc);
                boardc=pos;
            }
        }
        if (x+1<8 && y+1<8) {
            if (boardc[y+1][x+1]>0) {
                boardc[y][x]=0;
                boardc[y+1][x+1]=-1;
                if (y+1==7) {boardc[y+1][x+1]=-5;}
                childrenB.push_back(boardc);
                boardc=pos;
            }
        }
        //en passant
        if (x-1>-1 && y+1<8) {
            if (boardc[y][x-1]==-9 && boardc[y+1][x-1]==0) {
                boardc[y][x]=0;
                boardc[y+1][x-1]=-1;
                boardc[y][x-1]=0;
                childrenB.push_back(boardc);
                boardc=pos;
            }
        }
        if (x+1<8 && y+1<8) {
            if (boardc[y][x+1]==-9 && boardc[y+1][x+1]==0) {
                boardc[y][x]=0;
                boardc[y+1][x+1]=-1;
                boardc[y][x+1]=0;
                childrenB.push_back(boardc);
                boardc=pos;
            }
        }
    }
    else if (player==1) {
        if (y==6 && boardc[y-2][x]==0 && boardc[y-1][x]==0) {
            boardc[y][x]=0;
            boardc[y-2][x]=9;
            childrenB.push_back(boardc);
            boardc=pos;
        }
        if (y-1>-1) {
            if (boardc[y-1][x]==0) {
                boardc[y][x]=0;
                boardc[y-1][x]=1;
                if (y-1==0) {boardc[y-1][x]=5;}
                childrenB.push_back(boardc);
                boardc = pos;
            }
        }
        if (x-1>-1 && y-1>-1) {
            if (boardc[y-1][x-1]<0) {
                boardc[y][x]=0;
                boardc[y-1][x-1]=1;
                if (y-1==0) {boardc[y-1][x-1]=5;}
                childrenB.push_back(boardc);
                boardc = pos;
            }
        }
        if (x+1<8 && y-1>-1) {
            if (boardc[y-1][x+1]<0) {
                boardc[y][x]=0;
                boardc[y-1][x+1]=1;
                if (y-1==0) {boardc[y-1][x+1]=5;}
                childrenB.push_back(boardc);
                boardc=pos;
            }
        }
        //en passant
        if (x-1>-1 && y-1>-1) {
            if (boardc[y][x-1]==9 && boardc[y-1][x-1]==0) {
                boardc[y][x]=0;
                boardc[y-1][x-1]=1;
                boardc[y][x-1]=0;
                childrenB.push_back(boardc);
                boardc=pos;
            }
        }
        if (x+1<8 && y-1>-1) {
            if (boardc[y][x+1]==9 && boardc[y-1][x+1]==0) {
                boardc[y][x]=0;
                boardc[y-1][x+1]=1;
                boardc[y][x+1]=0;
                childrenB.push_back(boardc);
                boardc=pos;
            }
        }
    }
    return childrenB;
}

std::vector<std::vector<std::vector<int>>> gcTtXxQq(int y, int x, const std::vector<std::vector<int>> pos, int player, std::vector<int> direction_y, std::vector<int> direction_x) {
    std::vector<std::vector<std::vector<int>>> children;
    std::vector<std::vector<int>> boardc;
    //
    if (player<0) {
        for (int dir=0; dir<direction_y.size(); ++dir) {
            for (int step=1; step<8; ++step) {
                int new_y = y+step * direction_y[dir];
                int new_x = x+step * direction_x[dir];
                //
                if (new_y>-1 && new_y<8 && new_x>-1 && new_x<8) {
                    if (pos[new_y][new_x]>=0) {
                        if (pos[new_y][new_x]!=0) {
                            boardc=pos;
                            boardc[y][x]=0;
                            boardc[new_y][new_x]=player;
                            children.push_back(boardc);
                        }
                        else {
                            boardc=pos;
                            boardc[y][x]=0;
                            boardc[new_y][new_x]=player;
                            children.push_back(boardc);
                        }
                    }
                    else {break;}
                }
                else {break;}
            }
        }
    }
    else if (player>0) {
        for (int dir=0; dir<direction_y.size(); ++dir) {
            for (int step = 1; step <8; ++step) {
                int new_y = y + step * direction_y[dir];
                int new_x = x + step * direction_x[dir];
                //
                if (new_y>-1 && new_y<8 && new_x>-1 && new_x<8) {
                    if (pos[new_y][new_x]<=0) {
                        if (pos[new_y][new_x]!=0) {
                            boardc=pos;
                            boardc[y][x]=0;
                            boardc[new_y][new_x]=player;
                            children.push_back(boardc);
                        }
                        else {
                            boardc=pos;
                            boardc[y][x]=0;
                            boardc[new_y][new_x]=player;
                            children.push_back(boardc);
                        }
                    }
                    else {break;}
                }
                else {break;}
            }
        }
    }
    //
    return children;
}

std::vector<std::vector<std::vector<int>>> generate_children(std::vector<std::vector<int>> position, int playerk) {
    std::vector<std::vector<std::vector<int>>> children;
    // 9&-9 zu 1&-1
    if (playerk==6) {
        for (int y=0; y<position.size(); ++y) {
            for (int x=0; x<position[y].size(); ++x) {
                if (position[y][x]==9) {position[y][x]=1;}
            }
        }
    }
    else if (playerk==-6) {
        for (int y=0; y<position.size(); ++y) {
            for (int x=0; x<position[y].size(); ++x) {
                if (position[y][x]==-9) {position[y][x]=-1;}
            }
        }
    }
    //
    if (playerk==6) {
        for (int y=0; y<8; ++y) {
            for (int x=0; x<8; ++x) {
                if (position[y][x]==1) {
                    std::vector<std::vector<std::vector<int>>> new_children=gcBb(y, x, position, 1);
                    children.insert(children.end(), new_children.begin(), new_children.end());
                }
                else if (position[y][x]==6) {
                    std::vector<std::vector<std::vector<int>>> new_children=gcKk(y, x, position, 6);
                    children.insert(children.end(), new_children.begin(), new_children.end());
                }
                else if (position[y][x]==4 || position[y][x]==7) {
                    std::vector<std::vector<std::vector<int>>> new_children=gcTtXxQq(y, x, position, 4, {0, 0, 1, -1}, {0, 0, 1, -1});
                    children.insert(children.end(), new_children.begin(), new_children.end());                
                }
                else if (position[y][x]==3) {
                    std::vector<std::vector<std::vector<int>>> new_children=gcTtXxQq(y, x, position, 3, {1, -1, -1, 1}, {1, 1, -1, -1});
                    children.insert(children.end(), new_children.begin(), new_children.end());
                }
                else if (position[y][x]==5) {
                    std::vector<std::vector<std::vector<int>>> new_children=gcTtXxQq(y, x, position, 5, {1, -1, -1, 1, 0, 0, 1, -1}, {1, 1, -1, -1, 0, 0, 1, -1});
                    children.insert(children.end(), new_children.begin(), new_children.end());
                }
                else if (position[y][x]==2) {
                    std::vector<std::vector<std::vector<int>>> new_children=gcKk(y, x, position, 2);
                    children.insert(children.end(), new_children.begin(), new_children.end());
                }
                else if (position[y][x]==8) {
                    std::vector<std::vector<std::vector<int>>> new_children=gcKk(y, x, position, 8);
                    children.insert(children.end(), new_children.begin(), new_children.end());
                }
            }
        }
    }
    else if (playerk==-6) {
        for (int y=0; y<8; ++y) {
            for (int x=0; x<8; ++x) {
                if (position[y][x]==-1) {
                    std::vector<std::vector<std::vector<int>>> new_children=gcBb(y, x, position, -1);
                    children.insert(children.end(), new_children.begin(), new_children.end());
                }
                else if (position[y][x]==-6) {
                    std::vector<std::vector<std::vector<int>>> new_children=gcKk(y, x, position, -6);
                    children.insert(children.end(), new_children.begin(), new_children.end());
                }
                else if (position[y][x]==-4 || position[y][x]==-7) {
                    std::vector<std::vector<std::vector<int>>> new_children=gcTtXxQq(y, x, position, -4, {0, 0, 1, -1}, {0, 0, 1, -1});
                    children.insert(children.end(), new_children.begin(), new_children.end());                
                }
                else if (position[y][x]==-3) {
                    std::vector<std::vector<std::vector<int>>> new_children=gcTtXxQq(y, x, position, -3, {1, -1, -1, 1}, {1, 1, -1, -1});
                    children.insert(children.end(), new_children.begin(), new_children.end());
                }
                else if (position[y][x]==-5) {
                    std::vector<std::vector<std::vector<int>>> new_children=gcTtXxQq(y, x, position, -5, {1, -1, -1, 1, 0, 0, 1, -1}, {1, 1, -1, -1, 0, 0, 1, -1});
                    children.insert(children.end(), new_children.begin(), new_children.end());
                }
                else if (position[y][x]==-2) {
                    std::vector<std::vector<std::vector<int>>> new_children=gcKk(y, x, position, -2);
                    children.insert(children.end(), new_children.begin(), new_children.end());
                }
                else if (position[y][x]==-8) {
                    std::vector<std::vector<std::vector<int>>> new_children=gcKk(y, x, position, -8);
                    children.insert(children.end(), new_children.begin(), new_children.end());
                }
            }
        }
    }
    minimax_counter+=1;
    return children;
}

//
