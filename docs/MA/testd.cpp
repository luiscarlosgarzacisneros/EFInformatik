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

//

int schlagen_XO_c=3;
int schlagen_WM_c=5;
int WM_c=5;

std::vector<int> gorc_XO_schlagen_children;
std::vector<std::vector<int>> gorc_XO_schlagen_children_delete;
std::vector<int> gorc_WM_schlagen_children;
std::vector<std::vector<int>> gorc_WM_schlagen_children_delete;

void gorc_XO_schlagen(int y, int x, std::vector<std::vector<int>>& boardc, int player, std::vector<std::vector<int>>& delete_list) {
    bool geschlagen = false;
    if (player == 1) {
        if (y-2>-1 && x-2>-1 && boardc[y-2][x-2]==0 && boardc[y-1][x-1]<0) {
            geschlagen = true;
            delete_list.push_back({y-1, x-1});
            gorc_XO_schlagen(y-2, x-2, boardc, player, delete_list);
        }
        if (y-2>-1 && x+2<8 && boardc[y-2][x+2]==0 && boardc[y-1][x+1]<0) {
            geschlagen = true;
            delete_list.push_back({y-1, x+1});
            gorc_XO_schlagen(y-2, x+2, boardc, player, delete_list);
        }
        if (!geschlagen) {
            gorc_XO_schlagen_children.push_back((y+1) * 10 + (x+1));
            gorc_XO_schlagen_children_delete.push_back(delete_list);
        }
    }
    else if (player == -1) {
        if (y+2<8 && x-2>-1 && boardc[y+2][x-2]==0 && boardc[y+1][x-1]>0) {
            geschlagen = true;
            delete_list.push_back({y+1, x-1});
            gorc_XO_schlagen(y+2, x-2, boardc, player, delete_list);
        }
        if (y+2<8 && x+2<8 && boardc[y+2][x+2]==0 && boardc[y+1][x+1]>0) {
            geschlagen = true;
            delete_list.push_back({y+1, x+1});
            gorc_XO_schlagen(y+2, x+2, boardc, player, delete_list);
        }
        if (!geschlagen) {
            gorc_XO_schlagen_children.push_back((y+1) * 10 + (x+1));
            gorc_XO_schlagen_children_delete.push_back(delete_list);
        }
    }
}

std::vector<std::vector<int>> gorc_XO(int y, int x, std::vector<std::vector<int>> boardc, int player) {
    std::vector<int> childrenXO;
    gorc_XO_schlagen_children.clear();
    gorc_XO_schlagen_children_delete.clear();
    //
    if (player==1) {
        if (y-1>-1 && x-1>-1 && boardc[y-1][x-1]==0) {childrenXO.push_back(1);}
        if (y-1>-1 && x+1<8 && boardc[y-1][x+1]==0) {childrenXO.push_back(2);}
        if (y-2>-1 && x-2>-1 && boardc[y-2][x-2]==0) {
            if (boardc[y-1][x-1]<0) {gorc_XO_schlagen(y, x, boardc, player, {});}
        }
        if (y-2>-1 && x+2<8 && boardc[y-2][x+2]==0) {
            if (boardc[y-1][x+1]<0) {gorc_XO_schlagen(y, x, boardc, player, {});}
        }
    }
    else if (player==-1) {
        if (y+1<8 && x-1>-1 && boardc[y+1][x-1]==0) {childrenXO.push_back(1);}
        if (y+1<8 && x+1<8 && boardc[y+1][x+1]==0) {childrenXO.push_back(2);}
        if (y+2<8 && x-2>-1 && boardc[y+2][x-2]==0) {
            if (boardc[y+1][x-1]>0) {gorc_XO_schlagen(y, x, boardc, player, {});}
        }
        if (y+2<8 && x+2<8 && boardc[y+2][x+2]==0) {
            if (boardc[y+1][x+1]>0) {gorc_XO_schlagen(y, x, boardc, player, {});}
        }
    }
    //
    for (int i=0; i<schlagen_XO_c; ++i) {
        childrenXO.insert(childrenXO.end(), gorc_XO_schlagen_children.begin(), gorc_XO_schlagen_children.end());
    }
    //
    if (childrenXO.empty()) {
        return std::vector<std::vector<int>> ();
    }
    else {
        int n = childrenXO[rand() % childrenXO.size()];
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
                int n_y= n/10;
                int n_x= n%10;
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
                int n_y= n/10;
                int n_x= n%10;
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

void gorc_WM_schlagen(int y, int x, std::vector<std::vector<int>>& boardc, int player,std::vector<std::vector<int>>& delete_list){
    bool geschlagen=false;
    if (player==2) {
        //1: ur
        for(int i=0; i<7; ++i) {
            if (y+1+i>7 || x+1+i>7) {break;}
            if (boardc[y+1+i][x+1+i]>0) {break;}
            if (boardc[y+1+i][x+1+i]<0) {
                bool r=false;
                for (const auto& piece : delete_list) {
                    if (piece[0]==y+1+i && piece[1]==x+1+i) {r=true; break;}
                }
                if (r) {break;}
                if (!y+2+i>7 && !x+2+i>7 && boardc[y+2+i][x+2+i]==0) {
                    geschlagen=true;
                    delete_list.push_back({y+1+i, x+1+i});
                    gorc_WM_schlagen(y+2+i, x+2+i, boardc, player, delete_list);
                    break;
                }
                else {break;}
            }
        }
        //2: ul
        for (int i=0; i<7; ++i) {
            if (y+1+i>7||x-1-i<0) {break;}
            if (boardc[y+1+i][x-1-i]>0) {break;}
            if (boardc[y+1+i][x-1-i]<0) {
                bool r=false;
                for (const auto& piece : delete_list) {
                    if (piece[0]==y+1+i && piece[1]==x-1-i) {r=true; break;}
                }
                if (r) {break;}
                if (!y+2+i>7 && !x-2-i<0 && boardc[y+2+i][x-2-i]==0) {
                    geschlagen=true;
                    delete_list.push_back({y+1+i, x-1-i});
                    gorc_WM_schlagen(y+2+i, x-2-i, boardc, player, delete_list);
                    break;
                }
                else {break;}
            }
        }
        //3: or
        for (int i=0; i<7; ++i) {
            if (y-1-i<0||x+1+i>7) {break;}
            if (boardc[y-1-i][x+1+i]>0) {break;}
            if (boardc[y-1-i][x+1+i]<0){
                bool r=false;
                for (const auto& piece : delete_list){
                    if (piece[0]==y-1-i && piece[1]==x+1+i){r=true; break;}
                }
                if (r) {break;}
                if (!y-2-i<0 && !x+2+i>7 && boardc[y-2-i][x+2+i]==0) {
                    geschlagen=true;
                    delete_list.push_back({y-1-i, x+1+i});
                    gorc_WM_schlagen(y-2-i, x+2+i, boardc, player, delete_list);
                    break;
                }
                else {break;}
            }
        }
        //4: ol
        for (int i=0; i<7; ++i) {
            if (y-1-i<0||x-1-i<0) {break;}
            if (boardc[y-1-i][x-1-i]>0) {break;}
            if (boardc[y-1-i][x-1-i]<0) {
                bool r=false;
                for(const auto& piece : delete_list) {
                    if(piece[0]==y-1-i && piece[1]==x-1-i) {r=true; break;}
                }
                if (r) {break;}
                if (!y-2-i<0 && !x-2-i<0 && boardc[y-2-i][x-2-i]==0) {
                    geschlagen=true;
                    delete_list.push_back({y-1-i, x-1-i});
                    gorc_WM_schlagen(y-2-i, x-2-i, boardc, player, delete_list);
                    break;
                } 
                else {break;}
            }
        }
    }
    //
    else if (player==-2) {
        //1: ur
        for (int i=0; i<7; ++i) {
            if (y+1+i>7 || x+1+i>7) {break;}
            if (boardc[y+1+i][x+1+i]<0) {break;}
            if (boardc[y+1+i][x+1+i]>0) {
                bool r=false;
                for (const auto& piece : delete_list) {
                    if (piece[0]==y+1+i && piece[1]==x+1+i) {r=true; break;}
                }
                if (r) {break;}
                if (!y+2+i>7 && !x+2+i>7 && boardc[y+2+i][x+2+i]==0) {
                    geschlagen=true;
                    delete_list.push_back({y+1+i, x+1+i});
                    gorc_WM_schlagen(y+2+i, x+2+i, boardc, player, delete_list);
                    break;
                }
                else {break;}
            }
        }
        //2: ul
        for (int i=0; i<7; ++i) {
            if (y+1+i>7 || x-1-i<0) {break;}
            if (boardc[y+1+i][x-1-i]<0) {break;}
            if (boardc[y+1+i][x-1-i]>0) {
                bool r=false;
                for (const auto& piece : delete_list) {
                    if (piece[0]==y+1+i && piece[1]==x-1-i) {r=true; break;}
                }
                if (r) {break;}
                if (!y+2+i>7 && !x-2-i<0 && boardc[y+2+i][x-2-i]==0) {
                    geschlagen=true;
                    delete_list.push_back({y+1+i, x-1-i});
                    gorc_WM_schlagen(y+2+i, x-2-i, boardc, player, delete_list);
                    break;
                }
                else {break;}
            }
        }
        //3: or
        for (int i=0; i<7; ++i) {
            if (y-1-i<0 || x+1+i<7) {break;}
            if (boardc[y-1-i][x+1+i]<0) {break;}
            if (boardc[y-1-i][x+1+i]>0) {
                bool r=false;
                for (const auto& piece : delete_list) {
                    if (piece[0]==y-1-i && piece[1]==x+1+i) {r=true; break;}
                }
                if (r) {break;}
                if (!y-2-i<0 && !x+2+i>7 && boardc[y-2-i][x+2+i]==0) {
                    geschlagen=true;
                    delete_list.push_back({y-1-i, x+1+i});
                    gorc_WM_schlagen(y-2-i, x+2+i, boardc, player, delete_list);
                    break;
                }
                else {break;}
            }
        }
        //4: ol
        for (int i=0; i<7; ++i) {
            if (y-1-i<0 || x-1-i<0) {break;}
            if (boardc[y-1-i][x-1-i]<0) {break;}
            if (boardc[y-1-i][x-1-i]>0) {
                bool r=false;
                for (const auto& piece : delete_list) {
                    if (piece[0]==y-1-i && piece[1]==x-1-i) {r=true; break;}
                }
                if (r) {break;}
                if (!y-2-i<0 && !x-2-i<0 && boardc[y-2-i][x-2-i]==0) {
                    geschlagen=true;
                    delete_list.push_back({y-1-i, x-1-i});
                    gorc_WM_schlagen(y-2-i, x-2-i, boardc, player, delete_list);
                    break;
                }
                else {break;}
            }
        }
    }
    //
    if (!geschlagen) {
        gorc_WM_schlagen_children.push_back(((y+1) * 10) + (((x+1) + 100)));
        gorc_WM_schlagen_children_delete.push_back(delete_list);
    }

}


