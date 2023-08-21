#include <iostream>
#include <vector>
#include <list>
# include <algorithm>
#include <cstdlib>
#include <ctime>


int generate_random_int(int min, int max) {
    srand(time(0)); //seed
    int random_number=min+rand()%(max-min+1);
    return random_number;
}

bool gewonnen(const std::vector<std::vector<int>>& board, int player) {
    bool gewonnen = false;
    // horizontal
    for (int q = 0; q < 4; ++q) {
        for (int w = 0; w < 6; ++w) {
            if (board[w][q] == player && board[w][q + 1] == player && board[w][q + 2] == player && board[w][q + 3] == player) {gewonnen = true;}
        }
    }
    // vertikal
    for (int q = 0; q < 7; ++q) {
        for (int w = 0; w < 3; ++w) {
            if (board[w][q] == player && board[w + 1][q] == player && board[w + 2][q] == player && board[w + 3][q] == player) {gewonnen = true;}
        }
    }
    // diagonal1
    for (int q = 0; q < 4; ++q) {
        for (int w = 0; w < 3; ++w) {
            if (board[w][q] == player && board[w + 1][q + 1] == player && board[w + 2][q + 2] == player && board[w + 3][q + 3] == player) {gewonnen = true;}
        }
    }
    // diagonal2
    for (int q = 0; q < 4; ++q) {
        for (int w = 0; w < 3; ++w) {
            if (board[w][q + 3] == player && board[w + 1][q + 2] == player && board[w + 2][q + 1] == player && board[w + 3][q] == player) {gewonnen = true;}
        }
    }
    return gewonnen;
}

bool game_over(const std::vector<std::vector<int>>& board) {
    bool over = true;
    for (int q = 0; q < 6; ++q) {
        if (board[0][q] == 0) {over = false; break;}
    }
    return over;
}

int evaluate_position(const std::vector<std::vector<int>>& board, int player) {
    int score=0;
    int otherplayer;
    if (player==1) {otherplayer=-1;} 
    else if (player==-1) {otherplayer=1;}
    //horizontal
    for (int q=0; q<4; ++q) {
        for (int w=0; w<6; ++w) {
            int empty=0;
            int other=0;
            int filled=0;
            //
            if (board[w][q]==player) {filled+=1;}
            else if (board[w][q]==0) {empty+=1;}
            else if (board[w][q]==otherplayer) {other+=1;}
            //
            if (board[w][q + 1]==player) {filled+=1;}
            else if (board[w][q+1]==0) {empty+=1;}
            else if (board[w][q+1]==otherplayer) {other+=1;}
            //
            if (board[w][q+2]==player) {filled+=1;}
            else if (board[w][q+2]==0) {empty+=1;}
            else if (board[w][q+2]==otherplayer) {other+=1;}
            //
            if (board[w][q+3]==player) {filled+=1;}
            else if (board[w][q+3]==0) {empty+=1;}
            else if (board[w][q+3]==otherplayer) {other+=1;}
            //
            if (other==0) {
                if (filled==4) {score+=10000;}
                if (filled==3) {score+=1000;}
                if (filled==2) {score+=3;}
            } else if (filled==0) {
                if (other==4) {score-=10000;}
                if (other==3) {score-=100;}
                if (other==2) {score-=3;}
            }
        }
    }
    //vertikal
    for (int q=0; q<7; ++q) {
        for (int w=0; w<3; ++w) {
            int empty=0;
            int other=0;
            int filled=0;
            //
            if (board[w][q]==player) {filled+=1;}
            else if (board[w][q]==0) {empty+=1;}
            else if (board[w][q]==otherplayer) {other+=1;}
            //
            if (board[w+1][q]==player) {filled+=1;}
            else if (board[w+1][q]==0) {empty+=1;}
            else if (board[w+1][q]==otherplayer) {other+=1;}
            //
            if (board[w+2][q]==player) {filled+=1;}
            else if (board[w+2][q]==0) {empty+=1;}
            else if (board[w+2][q]==otherplayer) {other+=1;}
            //
            if (board[w+3][q]==player) {filled+=1;}
            else if (board[w+3][q]==0) {empty+=1;}
            else if (board[w+3][q]==otherplayer) {other+=1;}
            //
            if (other==0) {
                if (filled==4) {score+=10000;}
                if (filled==3) {score+=10;}
                if (filled==2) {score+=1;}
            } else if (filled==0) {
                if (other==4) {score-=10000;}
                if (other==3) {score-=30;}
                if (other==2) {score-=1;}
            }
        }
    }
    //diagonal1
    for (int q=0; q<4; ++q) {
        for (int w=0; w<3; ++w) {
            int empty=0;
            int other=0;
            int filled=0;
            //
            if (board[w][q]==player) {filled+=1;}
            else if (board[w][q]==0) {empty+=1;}
            else if (board[w][q]==otherplayer) {other+=1;}
            //
            if (board[w+1][q+1]==player) {filled+=1;}
            else if (board[w+1][q+1]==0) {empty+=1;}
            else if (board[w+1][q+1]==otherplayer) {other+=1;}
            //
            if (board[w+2][q+2]==player) {filled+=1;}
            else if (board[w+2][q+2]==0) {empty+=1;}
            else if (board[w+2][q+2]==otherplayer) {other+=1;}
            //
            if (board[w+3][q+3]==player) {filled+=1;}
            else if (board[w+3][q+3]==0) {empty+=1;}
            else if (board[w+3][q+3]==otherplayer) {other+=1;}
            //
            if (other==0) {
                if (filled==4) {score+=10000;}
                if (filled==3) {score+=1000;}
                if (filled==2) {score+=3;}
            } else if (filled==0) {
                if (other==4) {score-=10000;}
                if (other==3) {score-=100;}
                if (other==2) {score-=3;}
            }
        }
    }
    //diagonal2
    for (int q=0; q<4; ++q) {
        for (int w=0; w<3; ++w) {
            int empty=0;
            int other=0;
            int filled=0;
            //
            if (board[w][q+3]==player) {filled+=1;}
            else if (board[w][q+3]==0) {empty+=1;}
            else if (board[w][q+3]==otherplayer) {other+=1;}
            //
            if (board[w+1][q+2]==player) {filled+=1;}
            else if (board[w+1][q+2]==0) {empty+=1;}
            else if (board[w+1][q+2]==otherplayer) {other+=1;}
            //
            if (board[w+2][q+1]==player) {filled+=1;}
            else if (board[w+2][q+1]==0) {empty+=1;}
            else if (board[w+2][q+1]==otherplayer) {other+=1;}
            //
            if (board[w+3][q]==player) {filled+=1;}
            else if (board[w+3][q]==0) {empty+=1;}
            else if (board[w+3][q]==otherplayer) {other+=1;}
            //
            if (other==0) {
                if (filled==4) {score+=10000;}
                if (filled==3) {score+=1000;}
                if (filled==2) {score+=3;}
            } else if (filled==0) {
                if (other==4) {score-=10000;}
                if (other==3) {score-=100;}
                if (other==2) {score-=3;}
            }
        }
    }
    //
    return score;
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

void fall(std::vector<std::vector<int>>& board, int y, int x, const int player) {
    if (y<=4){
        if (board[y + 1][x] == 0) {board[y + 1][x] = player; board[y][x] = 0; fall(board, y+1, x, player);}
    }
}

std::list<std::vector<std::vector<int>>> generate_children(std::vector<std::vector<int>>& board, const int player) {
    std::list<std::vector<std::vector<int>>> children;
    std::vector<std::vector<int>> board_copy;
    for (const int& x : board_copy[0]){
        board_copy=deepcopy(board);
        if (board_copy[0][x]==0){board_copy[0][x]=player;}
        fall(board_copy, 0, x, player);
        children.push_back(board_copy);
    }
    return children;
}

std::vector<std::vector<int>> generate_one_random_child(std::vector<std::vector<int>>& board, const int player) {
    std::vector<std::vector<int>> board_copy=deepcopy(board);
    int x;
    while (true) {
        int x=generate_random_int(0,6);
        if (board_copy[0][x]==0) {break;}
    }
    board_copy[0][x]=player;
    fall(board_copy, 0, x, player);
    return board_copy;
}

//

class HumanPlayer {
    public:
        HumanPlayer(int token) : token(token) {}
        int token;

        std::vector<std::vector<int>> player(std::vector<std::vector<int>>& board) {
            try {
                int x;
                std::cout<<"x: ";
                std::cin>>x;
                x -= 1;
                //
                if (board[0][x]==0) {
                    board[0][x]=this->token;
                    fall(board, 0, x, this->token);} 
                else {
                    std::cout << "FELD BESETZT" << std::endl;
                    player(board);}
            } 
            catch (...) {
                std::cout << "EINGABE NICHT KORREKT" << std::endl;
                player(board);
            }
        }

        std::vector<std::vector<int>> get_move(std::vector<std::vector<int>> board) {
            return player(board);
        }
};

//

class MinimaxPlayer {
    public:
        MinimaxPlayer(int token) : token(token) {}
        int token;
        int max_time=5;
        int starting_depth=1;
};

class MinimaxNode {
    public:
        MinimaxNode();
        int value;
        std::vector<MinimaxNode> children;
        std::vector<std::vector<int>> board;
        int player_am_zug;
        int token;
        int depth;
        bool expanded=false;

        std::vector<MinimaxNode> expand_node() {
            //reserve?
            std::list<std::vector<std::vector<int>>> list_of_positions = generate_children(this->board, this->player_am_zug);
            for (const std::vector<std::vector<int>>& board_position : list_of_positions) {
                MinimaxNode child;
                child.board=board_position;
                child.player_am_zug = -this->player_am_zug; 
                child.token=this->token;
                child.depth=this->depth+1;
                this->children.push_back(child);
            }
            return this->children;
        }

        int minimax(int alpha, int beta, bool max_player, int max_depth) {
            //
            if (this->depth==max_depth) {this->value=evaluate_position(this->board, this->token); return this->value;}
            else if (gewonnen(this->board,1)||gewonnen(this->board,-1)) {this->value=evaluate_position(this->board, this->token); return this->value;}
            else if (game_over(this->board)) {this->value=evaluate_position(this->board, this->token); return this->value;}
            //
            if (!this->expanded) {expand_node(); this->expanded=true;}
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
                int min_value=-1000000;
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



};

//


class VierGewinnt {
public:
    VierGewinnt(); 
private:
    std::vector<std::vector<int>> board;
    int turn=0;
};


//

int main() {}