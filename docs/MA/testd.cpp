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


int generate_random_int(int min, int max) {
    int random_number=min+rand()%(max-min+1);
    return random_number;
}

//& or not?

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

std::vector<std::vector<int>> gorc_WM(int y, int x, std::vector<std::vector<int>> boardc, int player) {
    std::vector<int> childrenWM;
    gorc_WM_schlagen_children.clear();
    gorc_WM_schlagen_children_delete.clear();
    //
    if (player==2) {
        //1: ur
        for (int i=0; i<7; ++i) {
            if (y+1+i>7 || x+1+i>7) {break;}
            if (boardc[y+1+i][x+1+i]>0) {break;}
            if (boardc[y+1+i][x+1+i]==0) {childrenWM.push_back(11+i);}
            if (boardc[y+1+i][x+1+i]<0) {
                if (!(y+2+i>7) && !(x+2+i>7)) {
                    if (boardc[y+2+i][x+2+i]==0) {gorc_WM_schlagen(y, x, boardc, player, {}); break;}
                    else {break;}
                }
                else {break;}
            }
        }
        //2: ul
        for (int i=0; i<7; ++i) {
            if (y+1+i>7 || x-1-i<0) {break;}
            if (boardc[y+1+i][x-1-i]>0) {break;}
            if (boardc[y+1+i][x-1-i]==0) {childrenWM.push_back(21+i);}
            if (boardc[y+1+i][x-1-i]<0) {
                if (!(y+2+i>7) && !(x-2-i<0)) {
                    if (boardc[y+2+i][x-2-i]==0) {gorc_WM_schlagen(y, x, boardc, player, {}); break;}
                    else {break;}
                }
                else {break;}
            }
        }
        //3: or
        for (int i=0; i<7; ++i) {
            if (y-1-i<0 || x+1+i>7) {break;}
            if (boardc[y-1-i][x+1+i]>0) {break;}
            if (boardc[y-1-i][x+1+i]==0) {childrenWM.push_back(31+i);}
            if (boardc[y-1-i][x+1+i]<0) {
                if (!(y-2-i<0) && !(x+2+i>7)) {
                    if (boardc[y-2-i][x+2+i]==0) {gorc_WM_schlagen(y, x, boardc, player, {}); break;}
                    else {break;}
                }
                else {break;}
            }
        }
        //4: ol
        for (int i=0; i<7; ++i) {
            if (y-1-i<0 || x-1-i<0) {break;}
            if (boardc[y-1-i][x-1-i]>0) {break;}
            if (boardc[y-1-i][x-1-i]==0) {childrenWM.push_back(41+i);}
            if (boardc[y-1-i][x-1-i]<0) {
                if (!(y-2-i<0) && !(x-2-i<0)) {
                    if (boardc[y-2-i][x-2-i]==0) {gorc_WM_schlagen(y, x, boardc, player, {}); break;}
                    else {break;}
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
            if (boardc[y+1+i][x+1+i]==0) {childrenWM.push_back(11+i);}
            if (boardc[y+1+i][x+1+i]>0) {
                if (!(y+2+i>7) && !(x+2+i>7)) {
                    if (boardc[y+2+i][x+2+i]==0) {gorc_WM_schlagen(y,x,boardc,player,{}); break;}
                    else {break;}
                }
                else {break;}
            }
        }
        //2: ul
        for (int i=0; i<7; ++i) {
            if (y+1+i>7 || x-1-i<0) {break;}
            if (boardc[y+1+i][x-1-i]<0) {break;}
            if (boardc[y+1+i][x-1-i]==0) {childrenWM.push_back(21+i);}
            if (boardc[y+1+i][x-1-i]>0) {
                if (!(y+2+i>7) && !(x-2-i<0)) {
                    if (boardc[y+2+i][x-2-i]==0) {gorc_WM_schlagen(y,x,boardc,player,{}); break;}
                    else {break;}
                }
                else {break;}
            }
        }
        //3: or
        for (int i=0; i<7; ++i) {
            if (y-1-i<0 || x+1+i>7) {break;}
            if (boardc[y-1-i][x+1+i]<0) {break;}
            if (boardc[y-1-i][x+1+i]==0) {childrenWM.push_back(31+i);}
            if (boardc[y-1-i][x+1+i]>0) {
                if (!(y-2-i<0) && !(x+2+i>7)) {
                    if (boardc[y-2-i][x+2+i]==0) {gorc_WM_schlagen(y,x,boardc,player,{}); break;}
                    else {break;}
                }
                else {break;}
            }
        }
        //4: ol
        for (int i=0; i<7; ++i) {
            if (y-1-i<0 || x-1-i<0) {break;}
            if (boardc[y-1-i][x-1-i]<0) {break;}
            if (boardc[y-1-i][x-1-i]==0) {childrenWM.push_back(41+i);}
            if (boardc[y-1-i][x-1-i]>0) {
                if (!(y-2-i<0) && !(x-2-i<0)) {
                    if (boardc[y-2-i][x-2-i]==0) {gorc_WM_schlagen(y,x,boardc,player,{}); break;}
                    else {break;}
                }
                else {break;}
            }
        }
    }
    //
    for (int i=0; i<schlagen_WM_c; ++i) {
    childrenWM.insert(childrenWM.end(), gorc_WM_schlagen_children.begin(), gorc_WM_schlagen_children.end());
    }
    //
    if (childrenWM.empty()) {std::vector<std::vector<int>> empty_vector; return empty_vector;}
    else {
        //
        int r=generate_random_int(0, childrenWM.size()-1);
        int n=childrenWM[r];
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
        else if (n>100) { // schlagen
            int n_y=(n-100)/10;
            int n_x=(n-100)%10;
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
        if (!child.empty()) {
            break;
        }
    }
    //
    if (!child.empty()) {return child;}
    else {return {{0}};}
}

