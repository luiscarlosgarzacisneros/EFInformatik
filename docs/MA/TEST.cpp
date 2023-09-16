#include <iostream>
#include <vector>
#include <list>
#include <algorithm>
#include <cstdlib>
#include <cstdint>
#include <ctime>
#include <chrono>
#include <cmath>
#include <sstream>
#include <string>


void print_bitboard(const uint64_t bitboard) {
    for (int rank=7; rank>=0; --rank) {
        for (int file=0; file<8; ++file) {
            int square = rank*8+file;
            uint64_t m = 1ULL<<square;
            if (bitboard & m) {std::cout<<"1 ";}
            else {std::cout<<"0 ";}
        }
        std::cout << std::endl;
    }
}

//

bool is_one_at_this_index(const uint64_t bitboard, int index) {
    uint64_t m = 1ULL << index; //m=00000....001 1 wird um index rightshifted
    return (((bitboard & m) != 0));
    
}

int yx_zu_index(int y, int x) {
    return (y*8+x); //fangt unten rechts an!
}

bool is_in_board(int y, int x) {
    return ((x>-1 && x<8) && (y>-1 && y<8));
}

uint64_t shift_bit(uint64_t bitboard, int vy, int vx, int zy, int zx) {//wenn (vy, vx)==1
    //clear bit at (vy, vx)
    bitboard &= ~(1ULL << (vy * 8 + vx));
    //set bit at (zy, zx) to 1
    bitboard |= (1ULL << (zy * 8 + zx));
    return bitboard;
}

uint64_t clear_bit(uint64_t bitboard, int index) {
    //m with a 0 bit at index and 1s everywhere else
    uint64_t m = ~(1ULL << index);
    return bitboard & m;
}

uint64_t set_bit_to_one(uint64_t bitboard, int index) {
    uint64_t mask = 1ULL << index;
    return bitboard | mask;
}

//

std::vector<uint64_t> gcLl(const uint64_t knight_bitboard, const uint64_t this_players_pieces) {
    std::vector<uint64_t> childrenLl;
    //
    int dx[] = {1, 2, 2, 1, -1, -2, -2, -1};
    int dy[] = {2, 1, -1, -2, -2, -1, 1, 2};
    
    //get knights current position as (x, y) coord.
    std::vector<std::pair<int,int>> knight_positions;
    for (int y=0; y<8; ++y) {
        for (int x=0; x<8; ++x) {
            if (is_one_at_this_index(knight_bitboard, yx_zu_index(y, x))) {knight_positions.push_back({y, x});}
        }
    }
    //modify boards
    for (const auto& position : knight_positions) {
        int y_current = position.first;
        int x_current = position.second;
        //
        for (int i=0; i<8; ++i) {
            int y_new = y_current + dy[i];
            int x_new = x_current + dx[i];
            //
            if (is_in_board(y_new, x_new)) {
                if (!(is_one_at_this_index(this_players_pieces, yx_zu_index(y_new, x_new)))) {
                    uint64_t child=shift_bit(knight_bitboard, y_current, x_current, y_new, x_new);
                    childrenLl.push_back(child);
                }
            }
        }
    }
    //
    return childrenLl;
}

std::vector<std::pair<uint64_t, uint64_t>> gcBb(int player, const uint64_t pawn_bitboard, const uint64_t this_players_pieces, const uint64_t other_players_pieces, const uint64_t o_p_p_en) {
    std::vector<std::pair<uint64_t, uint64_t>> childrenBb;
    //get pawns current positions as (x, y) coord.
    std::vector<std::pair<int,int>> pawn_positions;
    for (int y=0; y<8; ++y) {
        for (int x=0; x<8; ++x) {
            if (is_one_at_this_index(pawn_bitboard, yx_zu_index(y, x))) {pawn_positions.push_back({y, x});}
        }
    }
    //
    uint64_t all_pieces=this_players_pieces|other_players_pieces;
    //modify boards
    for (const auto& position : pawn_positions) {
        int vy = position.first;
        int vx = position.second;
        //
        if (player==1) {
            //2 nach vorne
            if (vy==1 && !(is_one_at_this_index(all_pieces, yx_zu_index(vy+1, vx))) && !(is_one_at_this_index(all_pieces, yx_zu_index(vy+2, vx)))) {
                uint64_t child=shift_bit(pawn_bitboard, vy, vx, vy+2, vx);
                childrenBb.push_back({child, o_p_p_en});
            }
            //normal 1 nach vorne
            if (vy+1<8 && !(is_one_at_this_index(all_pieces, yx_zu_index(vy+1, vx)))) {
                uint64_t child=shift_bit(pawn_bitboard, vy, vx, vy+1, vx);
                childrenBb.push_back({child, o_p_p_en});
            }
            //schlagen
            if (vy+1<8 && vx-1>-1 && is_one_at_this_index(other_players_pieces, yx_zu_index(vy+1, vx-1))) {
                uint64_t child=shift_bit(pawn_bitboard, vy, vx, vy+1, vx-1);
                childrenBb.push_back({child, o_p_p_en});
            }
            if (vy+1<8 && vx+1<8 && is_one_at_this_index(other_players_pieces, yx_zu_index(vy+1, vx+1))) {
                uint64_t child=shift_bit(pawn_bitboard, vy, vx, vy+1, vx+1);
                childrenBb.push_back({child, o_p_p_en});
            }
            //en passant
            if (vy+1<8 && vx-1>-1 && !(is_one_at_this_index(all_pieces, yx_zu_index(vy+1, vx-1))) && is_one_at_this_index(o_p_p_en, yx_zu_index(vy, vx-1))) {
                uint64_t child=shift_bit(pawn_bitboard, vy, vx, vy+1, vx-1);
                uint64_t new_o_p_p_en=clear_bit(o_p_p_en, yx_zu_index(vy, vx-1));
                childrenBb.push_back({child, new_o_p_p_en});
            }
            if (vy+1<8 && vx+1<8 && !(is_one_at_this_index(all_pieces, yx_zu_index(vy+1, vx+1))) && is_one_at_this_index(o_p_p_en, yx_zu_index(vy, vx+1))) {
                uint64_t child=shift_bit(pawn_bitboard, vy, vx, vy+1, vx+1);
                uint64_t new_o_p_p_en=clear_bit(o_p_p_en, yx_zu_index(vy, vx+1));
                childrenBb.push_back({child, new_o_p_p_en});
            }
        }
        //
        else {
            //2 nach vorne
            if (vy==6 && !(is_one_at_this_index(all_pieces, yx_zu_index(vy-1, vx))) && !(is_one_at_this_index(all_pieces, yx_zu_index(vy-2, vx)))) {
                uint64_t child=shift_bit(pawn_bitboard, vy, vx, vy-2, vx);
                childrenBb.push_back({child, o_p_p_en});
            }
            //normal 1 nach vorne
            if (vy+1<8 && !(is_one_at_this_index(all_pieces, yx_zu_index(vy-1, vx)))) {
                uint64_t child=shift_bit(pawn_bitboard, vy, vx, vy-1, vx);
                childrenBb.push_back({child, o_p_p_en});
            }
            //schlagen
            if (vy-1>-1 && vx-1>-1 && is_one_at_this_index(other_players_pieces, yx_zu_index(vy-1, vx-1))) {
                uint64_t child=shift_bit(pawn_bitboard, vy, vx, vy-1, vx-1);
                childrenBb.push_back({child, o_p_p_en});
            }
            if (vy-1>-1 && vx+1<8 && is_one_at_this_index(other_players_pieces, yx_zu_index(vy-1, vx+1))) {
                uint64_t child=shift_bit(pawn_bitboard, vy, vx, vy-1, vx+1);
                childrenBb.push_back({child, o_p_p_en});
            }
            //en passant
            if (vy-1>-1 && vx-1>-1 && !(is_one_at_this_index(all_pieces, yx_zu_index(vy-1, vx-1))) && is_one_at_this_index(o_p_p_en, yx_zu_index(vy, vx-1))) {
                uint64_t child=shift_bit(pawn_bitboard, vy, vx, vy-1, vx-1);
                uint64_t new_o_p_p_en=clear_bit(o_p_p_en, yx_zu_index(vy, vx-1));
                childrenBb.push_back({child, new_o_p_p_en});
            }
            if (vy-1>.1 && vx+1<8 && !(is_one_at_this_index(all_pieces, yx_zu_index(vy-1, vx+1))) && is_one_at_this_index(o_p_p_en, yx_zu_index(vy, vx+1))) {
                uint64_t child=shift_bit(pawn_bitboard, vy, vx, vy-1, vx+1);
                uint64_t new_o_p_p_en=clear_bit(o_p_p_en, yx_zu_index(vy, vx+1));
                childrenBb.push_back({child, new_o_p_p_en});
            }
        }
    }
    //
    return childrenBb; //return a pair with child_pawn_this_player and new_o_p_p_en_other_player_of_this_child: in generate_children it can be implemented.
}

//Tt: {{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
//Xx: {{1, 1}, {-1, 1}, {1, -1}, {-1, -1}}
//Qq: {{1, 0}, {-1, 0}, {0, 1}, {0, -1}, {1, 1}, {-1, 1}, {1, -1}, {-1, -1}}
std::vector<uint64_t> gcTtXxQq(const uint64_t bitboard, const uint64_t this_players_pieces, const uint64_t other_players_pieces, std::vector<std::pair<int,int>> directions) {
    std::vector<uint64_t> children_Tt_Xx_Qq;
    //get current positions as (x, y) coord.
    std::vector<std::pair<int,int>> positions;
    for (int y=0; y<8; ++y) {
        for (int x=0; x<8; ++x) {
            if (is_one_at_this_index(bitboard, yx_zu_index(y, x))) {positions.push_back({y, x});}
        }
    }
    //
    //modify board
    for (const auto& position : positions) {
        int y_current = position.first;
        int x_current = position.second;
        //
        for (const auto& direction : directions) {
            int direction_y=direction.first;
            int direction_x=direction.second;
            //
            for (int i=1; i<8; ++i) {
                int y_new = y_current + i*direction_y;
                int x_new = x_current + i*direction_x;
                //
                if (is_in_board(y_new, x_new)) {
                    if (is_one_at_this_index(other_players_pieces, yx_zu_index(y_new, x_new))) {
                        uint64_t child=shift_bit(bitboard, y_current, x_current, y_new, x_new);
                        children_Tt_Xx_Qq.push_back(child);
                        break;
                    }
                    else if (is_one_at_this_index(this_players_pieces, yx_zu_index(y_new, x_new))) {break;}
                    else {
                        uint64_t child=shift_bit(bitboard, y_current, x_current, y_new, x_new);
                        children_Tt_Xx_Qq.push_back(child);
                    }
                }
                else {break;}
            }
        }
    }
    //
    return children_Tt_Xx_Qq;
}

std::vector<std::pair<uint64_t, uint64_t>> gcZz(const uint64_t Zz_bitboard, const uint64_t Tt_bitboard, const uint64_t this_players_pieces, const uint64_t other_players_pieces) {
    std::vector<std::pair<int,int>> directions={{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    std::vector<std::pair<uint64_t, uint64_t>> children_Tt_Zz;
    //
    //position von Zz mit yx finden
    std::vector<std::pair<int,int>> positions;
    for (int y=0; y<8; ++y) {
        for (int x=0; x<8; ++x) {
            if (is_one_at_this_index(Zz_bitboard, yx_zu_index(y, x))) {positions.push_back({y, x});}
        }
    }
    //
    //modify board
    for (const auto& position : positions) {
        int y_current = position.first;
        int x_current = position.second;
        //
        for (const auto& direction : directions) {
            int direction_y=direction.first;
            int direction_x=direction.second;
            //
            for (int i=1; i<8; ++i) {
                int y_new = y_current + i*direction_y;
                int x_new = x_current + i*direction_x;
                //
                if (is_in_board(y_new, x_new)) {
                    if (is_one_at_this_index(other_players_pieces, yx_zu_index(y_new, x_new))) {
                        uint64_t child_Tt=set_bit_to_one(Tt_bitboard, yx_zu_index(y_new, x_new));
                        uint64_t child_Zz=clear_bit(Zz_bitboard, yx_zu_index(y_current, x_current));
                        children_Tt_Zz.push_back({child_Tt, child_Zz});
                        break;
                    }
                    else if (is_one_at_this_index(this_players_pieces, yx_zu_index(y_new, x_new))) {break;}
                    else {
                        uint64_t child_Tt=set_bit_to_one(Tt_bitboard, yx_zu_index(y_new, x_new));
                        uint64_t child_Zz=clear_bit(Zz_bitboard, yx_zu_index(y_current, x_current));
                        children_Tt_Zz.push_back({child_Tt, child_Zz});
                    }
                }
                else {break;}
            }
        }
    }
    //
    return children_Tt_Zz;//{child_Tt, child_Zz}
}

std::vector<uint64_t> gcKk(const uint64_t king_bitboard, const uint64_t this_players_pieces) {
    std::vector<uint64_t> childrenKk;
    //
    int dx[] = {0, 0, 1, -1, 1, -1, 1, -1};
    int dy[] = {1, -1, 0, 0, 1, 1, -1, -1};
    
    //get knights current position as (x, y) coord.
    std::vector<std::pair<int,int>> knight_positions;
    for (int y=0; y<8; ++y) {
        for (int x=0; x<8; ++x) {
            if (is_one_at_this_index(king_bitboard, yx_zu_index(y, x))) {knight_positions.push_back({y, x});}
        }
    }
    //modify boards
    for (const auto& position : knight_positions) {
        int y_current = position.first;
        int x_current = position.second;
        //
        for (int i=0; i<8; ++i) {
            int y_new = y_current + dy[i];
            int x_new = x_current + dx[i];
            //
            if (is_in_board(y_new, x_new)) {
                if (!(is_one_at_this_index(this_players_pieces, yx_zu_index(y_new, x_new)))) {
                    uint64_t child=shift_bit(king_bitboard, y_current, x_current, y_new, x_new);
                    childrenKk.push_back(child);
                }
            }
        }
    }
    //
    return childrenKk;
}

//bei gcYy: return bitbKk und bitbTt und bitbZz

//

class Board {
public:

    uint64_t b;
    uint64_t l;
    uint64_t x;
    uint64_t t;
    uint64_t q;
    uint64_t k;
    uint64_t y;
    uint64_t z;
    uint64_t f;
    
    uint64_t B;
    uint64_t L;
    uint64_t X;
    uint64_t T;
    uint64_t Q;
    uint64_t K;
    uint64_t Y;
    uint64_t Z;
    uint64_t F;

    Board() {}

    void print_board() {
        std::vector<std::vector<std::string>> board;
        //initialize board with spaces
        for (int i = 0; i < 8; i++) {
            std::vector<std::string> empty_string_vector(8, " ");
            board.push_back(empty_string_vector);
        }
        //place symbols on board based on bitboards
        for (int i=0; i<8; i++) {
            for (int j=0; j<8; j++) {
                uint64_t mask = 1ULL << (i*8+j);
                if (this->b & mask) board[i][j] = 'b';
                if (this->B & mask) board[i][j] = 'B';
                if (this->f & mask) board[i][j] = 'f';
                if (this->F & mask) board[i][j] = 'F';
                if (this->l & mask) board[i][j] = 'l';
                if (this->L & mask) board[i][j] = 'L';
                if (this->x & mask) board[i][j] = 'x';
                if (this->X & mask) board[i][j] = 'X';
                if (this->t & mask) board[i][j] = 't';
                if (this->T & mask) board[i][j] = 'T';
                if (this->z & mask) board[i][j] = 'z';
                if (this->Z & mask) board[i][j] = 'Z';
                if (this->q & mask) board[i][j] = 'q';
                if (this->Q & mask) board[i][j] = 'Q';
                if (this->k & mask) board[i][j] = 'k';
                if (this->K & mask) board[i][j] = 'K';
                if (this->y & mask) board[i][j] = 'y';
                if (this->Y & mask) board[i][j] = 'Y';
                
            }
        }
        //
        std::reverse(board.begin(), board.end());
        //
        //print the board
        std::cout <<"    1   2   3   4   5   6   7   8\n";
        std::cout <<"  ---------------------------------\n";
        for (int i=0; i<8; i++) {
            std::cout << i+1 <<" I";
            for (int j=0; j<8; j++) {
                std::cout << " ";
                std::cout << board[i][j];
                std::cout << " ";
                std::cout << "I";
            }
            std::cout <<'\n';
            std::cout <<"  ---------------------------------\n";
        }
    }

    bool verloren(int playerk) {
        if (playerk==6) {
            if (this->k==0 && this->y==0) {return true;}
            else {return false;}
        }
        else {
            if (this->K==0 && this->Y==0) {return true;}
            else {return false;}
        }
    }

};

//

main() {
    Board root_node;
    root_node.b   = 0b0000000000000000000000000000000000000000000000001111111100000000ULL;
    root_node.l = 0b0000000000000000000000000000000000000000000000000000000001000010ULL;
    root_node.x = 0b0000000000000000000000000000000000000000000000000000000000100100ULL;
    root_node.t   = 0b0000000000000000000000000000000000000000000000000000000000000000ULL;
    root_node.q  = 0b0000000000000000000000000000000000000000000000000000000000001000ULL;
    root_node.k   = 0b0000000000000000000000000000000000000000000000000000000000000000ULL;

    root_node.y   = 0b0000000000000000000000000000000000000000000000000000000000010000ULL;
    root_node.z   = 0b0000000000000000000000000000000000000000000000000000000010000001ULL;
    root_node.f   = 0b0000000000000000000000000000000000000000000000000000000000000000ULL;

    root_node.B   = 0b0000000011111111000000000000000000000000000000000000000000000000ULL;
    root_node.L = 0b0100001000000000000000000000000000000000000000000000000000000000ULL;
    root_node.X = 0b0010010000000000000000000000000000000000000000000000000000000000ULL;
    root_node.T   = 0b0000000000000000000000000000000000000000000000000000000000000000ULL;
    root_node.Q  = 0b0000100000000000000000000000000000000000000000000000000000000000ULL;
    root_node.K   = 0b0000000000000000100000000000000000000000000000000000000000000000ULL;

    root_node.Y   = 0b0001000000000000000000000000000000000000000000000000000000000000ULL;
    root_node.Z   = 0b1000000100000000000000000000000000000000000000000000000000000000ULL;
    root_node.F   = 0b0000000000000000000000000000000000000000000000000000000000000000ULL;

    uint64_t white_pieces = root_node.b|root_node.l|root_node.x|root_node.t|root_node.q|root_node.k|root_node.y|root_node.z|root_node.f;
    uint64_t black_pieces = root_node.B|root_node.L|root_node.X|root_node.T|root_node.Q|root_node.K|root_node.Y|root_node.Z|root_node.F;

    print_bitboard(root_node.K);
    std::cout<<"----"<<std::endl;
    for (const auto& child : gcKk(root_node.K, black_pieces)) {
        print_bitboard(child);
        std::cout<<"----"<<std::endl;
    }
    print_bitboard(root_node.K);
    std::cout<<"----"<<std::endl;
    print_bitboard(root_node.Y);
    std::cout<<"----"<<std::endl;
    print_bitboard(root_node.y);
    
    root_node.print_board();

}

