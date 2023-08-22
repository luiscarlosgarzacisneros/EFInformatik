#include <iostream>
#include <vector>
#include <list>
#include <algorithm>
#include <cstdlib>
#include <ctime>
#include <chrono>


void printboard(const std::vector<std::vector<int>>& board) {
    std::cout<<"  1   2   3   4   5   6   7"<<std::endl;
    std::cout<<"-----------------------------"<<std::endl;
    for (int i = 0; i <6; ++i) {
        std::cout<< "I ";
        for (int j = 0; j < 7; ++j) {
            if (board[i][j] == 1) {std::cout<<"X";}
            else if (board[i][j] == -1) {std::cout<<"O";}
            else {std::cout<<" ";}
            std::cout <<" I ";
        }
        std::cout<<std::endl;
        std::cout<<"-----------------------------"<<std::endl;
    }
}

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
    while (y<5 && board[y+1][x]==0) {
        board[y+1][x] = player;
        board[y][x] = 0;
        y+=1;
    }
}

std::list<std::vector<std::vector<int>>> generate_children(std::vector<std::vector<int>>& board, const int player) {
    std::list<std::vector<std::vector<int>>> children;
    for (int x = 0; x < 7; ++x) {
        std::vector<std::vector<int>> board_copy = deepcopy(board);
        if (board_copy[0][x] == 0) {
            board_copy[0][x] = player;
            fall(board_copy, 0, x, player);
            children.push_back(board_copy);
        }
    }
    return children;
}

std::vector<std::vector<int>> generate_one_random_child(std::vector<std::vector<int>>& board, const int player) {
    std::vector<std::vector<int>> board_copy=deepcopy(board);
    int x=generate_random_int(0, 6);
    while (true) {
        if (board_copy[0][x]==0) {break;}
        x=generate_random_int(0,6);
    }
    board_copy[0][x]=player;
    fall(board_copy, 0, x, player);
    return board_copy;
}

//

class HumanPlayer {
public:
    HumanPlayer(int token) : token(token) {}

    std::vector<std::vector<int>> player(std::vector<std::vector<int>>& board) {
        try {
            int x;
            std::cout<<"x: ";
            std::cin>>x;
            x -= 1;
            //
            if (board[0][x]==0) {
                board[0][x]=this->token;
                fall(board, 0, x, this->token);
                return board;
            }
            else {
                std::cout << "EINGABE NICHT KORREKT2" << std::endl;
                return player(board);
            }
        }
        catch (...) {
            std::cout << "EINGABE NICHT KORREKT1" << std::endl;
            return player(board);
        }
    }

    std::vector<std::vector<int>> get_move(std::vector<std::vector<int>>& board) {
        return player(board);
    }

private:
    int token;
};

//

int minimax_counter=0;

class MinimaxNode {
public:
    MinimaxNode() : value(), value_not_none(false),children(),board(),player_am_zug(),token(),depth(), expanded(false) {}

    int value;
    bool value_not_none;
    std::vector<MinimaxNode> children;
    std::vector<std::vector<int>> board;
    int player_am_zug;
    int token;
    int depth;
    bool expanded;

    std::vector<MinimaxNode> expand_node() {
        //reserve?
        std::list<std::vector<std::vector<int>>> list_of_positions = generate_children(this->board, this->player_am_zug);
        for (const std::vector<std::vector<int>>& board_position : list_of_positions) {
            MinimaxNode child;
            child.board=board_position;
            child.player_am_zug = -this->player_am_zug;
            child.token=this->token;
            child.depth=this->depth+1;
            child.value_not_none=false;
            child.value;
            child.children;
            this->children.push_back(child);
        }
        return this->children;
    }

    int minimax(int alpha, int beta, bool max_player, const int max_depth) {
        //
        std::cout<<"TEST1"<<std::endl;
        if (this->depth==max_depth) {
            this->value=evaluate_position(this->board, this->token);
            this->value_not_none=true;
            return this->value;
        }
        else if (gewonnen(this->board,1)||gewonnen(this->board,-1)) {
            this->value=evaluate_position(this->board, this->token);
            this->value_not_none=true;
            return this->value;
        }
        else {
            this->value=evaluate_position(this->board, this->token);
            this->value_not_none=true;
            return this->value;
        }
        //
        if (!this->expanded) {std::cout<<"TEST2"<<std::endl;expand_node(); this->expanded=true;}
        //
        if (max_player) {
            int max_value=-std::numeric_limits<int>::max();
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
            int min_value=std::numeric_limits<int>::max();
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
        //reserve?
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
            sorted_children.insert(sorted_children.end(), none_children.begin(), none_children.end());
            this->children=sorted_children;
            //
            for (MinimaxNode& child : not_none_children) {child.sort(false);}
        }
        else if (!max_player) {
            std::sort(not_none_children.begin(), not_none_children.end(),[](const MinimaxNode& a, const MinimaxNode& b) {return a.value < b.value;});
            //
            sorted_children.insert(sorted_children.end(), none_children.begin(), none_children.end());
            this->children=sorted_children;
            //
            for (MinimaxNode& child : not_none_children) {child.sort(true);}
        }
    }

};

class MinimaxPlayer {
public:
    MinimaxPlayer(int token, std::vector<std::vector<int>> board) : token(token), board(board) {
        root_node.board = board;
        root_node.player_am_zug = token;
        root_node.value_not_none = false;
        root_node.value = 0;
        root_node.depth = 0;
        root_node.children = root_node.expand_node();
    }
    MinimaxNode root_node;
    int token;
    std::vector<std::vector<int>> board;
    int max_time=1;
    int starting_depth=1;

    std::vector<std::vector<int>> minimaxer(int depth, std::chrono::duration<double> vergangene_zeit) {
        auto start = std::chrono::high_resolution_clock::now();
        //
        for (MinimaxNode child : root_node.children){
            child.minimax(-std::numeric_limits<int>::max(),std::numeric_limits<int>::max(),false, depth);
            std::cout<<"a";//child wurde fertig berechnet
            //
            auto now = std::chrono::high_resolution_clock::now();
            std::chrono::duration<double> vergangene_zeit2 =(now+vergangene_zeit)-start;
            if (vergangene_zeit2.count() >= max_time) {break;}
        }
        //
        std::list<int> values;
        for (MinimaxNode child : root_node.children) {values.push_back(child.value);}
        //
        std::vector<MinimaxNode> best_moves;
        int best_value = -std::numeric_limits<int>::max();
        for (int v : values) {
            if (v > best_value) {
                best_value = v;
            }
        }
        for (MinimaxNode child : root_node.children) {
            if (child.value==best_value) {
                best_moves.push_back(child);
            }
        }
        //
        //output---------
        std::cout << std::endl;
        for (int value : values) {
            std::cout<<value;
        }
        std::cout << std::endl;
        std::cout << best_value << std::endl;
        //---------------
        MinimaxNode best_move=best_moves[generate_random_int(0, best_moves.size()-1)];
        return best_move.board;

    }

    std::vector<std::vector<int>> minimaxerer(std::vector<std::vector<int>> board_0) {
        auto start = std::chrono::high_resolution_clock::now();
        int minimax_counter=0;
        //
        int depth=this->starting_depth;
        std::vector<std::vector<int>> move;
        while (true) {
            //break
            auto now = std::chrono::high_resolution_clock::now();
            std::chrono::duration<double> vergangene_zeit = now - start;
            if (vergangene_zeit.count() >= max_time) {break;}
            //calculate move
            move=minimaxer(depth,vergangene_zeit);
            //sort+output
            if (vergangene_zeit.count() >= max_time) {std::cout<<"NICHT FERTIG";}
            else {root_node.sort(true); depth+=1;}
            std::cout<<"---";
            std::cout<<minimax_counter<<std::endl;
        }
        return move;
    }

    std::vector<std::vector<int>> get_move(std::vector<std::vector<int>> board) {
        return minimaxerer(board);
    }
};

//

class VierGewinnt {
public:
    VierGewinnt() : board({
            {0,0,0,0,0,0,0},
            {0,0,0,0,0,0,0},
            {0,0,0,0,0,0,0},
            {0,0,0,0,0,0,0},
            {0,0,0,0,0,0,0},
            {0,0,0,0,0,0,0},
            {0,0,0,0,0,0,0}
        }), turn(1) {}

    int play() {
    int current = 1;

    while (true) {
        //-----------------------------------------
        HumanPlayer player_1(1);
        MinimaxPlayer player_2(-1, this->board);
        //-----------------------------------------
        std::cout<<this->turn<<std::endl;
        printboard(this->board);

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
        if (game_over(board)) {printboard(this->board); std::cout<<"UNENTSCHIEDEN"<<std::endl; return 0;}
        else if (gewonnen(this->board, 1)) {printboard(this->board); std::cout<<"X HAT GEWONNEN"<<std::endl; return 1;}
        else if (gewonnen(this->board, -1)) {printboard(this->board); std::cout<<"O HAT GEWONNEN"<<std::endl; return -1;}
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
    VierGewinnt game;
    int x_wins=0;
    int o_wins=0;
    int unentschieden=0;
    //
    for (int i=0; i<z; ++i) {
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
    spielen(3);

}

//MCTS +reserve?
//eingabe Human
