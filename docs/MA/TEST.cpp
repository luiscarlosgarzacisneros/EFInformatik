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

uint64_t remove_common_bits(uint64_t from_this_bitboard, uint64_t by_comparing_with_this_board) {
    //find common bits by AND operation
    uint64_t common_bits = from_this_bitboard & by_comparing_with_this_board;
    //remove common bits from bitboard1
    uint64_t result = from_this_bitboard & (~common_bits);
    return result;
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
    
    //get kings current position as (x, y) coord.
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

    std::vector<Board> generate_children(int playerk);

    std::vector<Board> gcYy(int player, const uint64_t this_players_pieces, const uint64_t all_pieces) {
        std::vector<Board> children;
        //
        uint64_t Yy_bitboard;
        uint64_t Kk_bitboard;
        uint64_t Zz_bitboard;
        uint64_t Tt_bitboard;
        if (player==6) {
            Yy_bitboard=this->y;
            Kk_bitboard=this->k;
            Zz_bitboard=this->z;
            Tt_bitboard=this->t;
        }
        else {
            Yy_bitboard=this->Y;
            Kk_bitboard=this->K;
            Zz_bitboard=this->Z;
            Tt_bitboard=this->T;
        }
        //
        //get Yy current positions as (x, y) coord.
        std::vector<std::pair<int,int>> Yy_positions;
        for (int y=0; y<8; ++y) {
            for (int x=0; x<8; ++x) {
                if (is_one_at_this_index(Yy_bitboard, yx_zu_index(y, x))) {Yy_positions.push_back({y, x});}
            }
        }
        //
        int dx[] = {0, 0, 1, -1, 1, -1, 1, -1};
        int dy[] = {1, -1, 0, 0, 1, 1, -1, -1};
        //
        //normal
        for (const auto& position : Yy_positions) {
            int y_current = position.first;
            int x_current = position.second;
            //
            for (int i=0; i<8; ++i) {
                int y_new = y_current + dy[i];
                int x_new = x_current + dx[i];
                //
                if (is_in_board(y_new, x_new)) {
                    if (!(is_one_at_this_index(this_players_pieces, yx_zu_index(y_new, x_new)))) {
                        uint64_t new_Kk=set_bit_to_one(Kk_bitboard, yx_zu_index(y_new, x_new));
                        uint64_t new_Yy=clear_bit(Yy_bitboard, yx_zu_index(y_new, x_new));
                        Board child;
                        if (player==6) {
                            child.b=this->b;
                            child.l=this->l;
                            child.x=this->x;
                            child.t=this->t;
                            child.q=this->q;
                            child.k=new_Kk;
                            child.y=new_Yy;
                            child.z=this->z;
                            child.f=this->f;
                            //
                            child.B=remove_common_bits(this->B, new_Kk);
                            child.L=remove_common_bits(this->L, new_Kk);
                            child.X=remove_common_bits(this->X, new_Kk);
                            child.T=remove_common_bits(this->T, new_Kk);
                            child.Q=remove_common_bits(this->Q, new_Kk);
                            child.K=remove_common_bits(this->K, new_Kk);
                            child.Y=remove_common_bits(this->Y, new_Kk);
                            child.Z=remove_common_bits(this->Z, new_Kk);
                            child.F=remove_common_bits(this->F, new_Kk);
                        }
                        else {
                            child.B=this->B;
                            child.L=this->L;
                            child.X=this->X;
                            child.T=this->T;
                            child.Q=this->Q;
                            child.K=new_Kk;
                            child.Y=new_Yy;
                            child.Z=this->Z;
                            child.F=this->F;
                            //
                            child.b=remove_common_bits(this->b, new_Kk);
                            child.l=remove_common_bits(this->l, new_Kk);
                            child.x=remove_common_bits(this->x, new_Kk);
                            child.t=remove_common_bits(this->t, new_Kk);
                            child.q=remove_common_bits(this->q, new_Kk);
                            child.k=remove_common_bits(this->k, new_Kk);
                            child.y=remove_common_bits(this->y, new_Kk);
                            child.z=remove_common_bits(this->z, new_Kk);
                            child.f=remove_common_bits(this->f, new_Kk);
                        }
                        //
                        children.push_back(child);
                    }
                }
            }
        }
        //rochade
        if (player==6) {
            if (is_one_at_this_index(Yy_bitboard, 3) && is_one_at_this_index(Zz_bitboard, 0) && !(is_one_at_this_index(all_pieces, 1)) && !(is_one_at_this_index(all_pieces, 2))) {
                uint64_t new_Kk=set_bit_to_one(Kk_bitboard, 1);
                uint64_t new_Yy=clear_bit(Yy_bitboard, 3);
                uint64_t new_Tt=set_bit_to_one(Tt_bitboard, 2);
                uint64_t new_Zz=clear_bit(Zz_bitboard, 0);
                //
                Board simulation;
                simulation.b=this->b;
                simulation.l=this->l;
                simulation.x=this->x;
                simulation.t=new_Tt;
                simulation.q=this->q;
                simulation.k=new_Kk;
                simulation.y=new_Yy;
                simulation.z=new_Zz;
                simulation.f=this->f;
                //
                simulation.B=remove_common_bits(this->B, new_Kk);
                simulation.L=remove_common_bits(this->L, new_Kk);
                simulation.X=remove_common_bits(this->X, new_Kk);
                simulation.T=remove_common_bits(this->T, new_Kk);
                simulation.Q=remove_common_bits(this->Q, new_Kk);
                simulation.K=remove_common_bits(this->K, new_Kk);
                simulation.Y=remove_common_bits(this->Y, new_Kk);
                simulation.Z=remove_common_bits(this->Z, new_Kk);
                simulation.F=remove_common_bits(this->F, new_Kk);
                //
                bool legal=true;
                for (Board child : simulation.generate_children(-6)) {
                    uint64_t other_players_pieces= child.B|child.L|child.X|child.T|child.Q|child.K|child.Y|child.Z|child.F;
                    if (is_one_at_this_index(other_players_pieces, 1) || is_one_at_this_index(other_players_pieces, 2) || is_one_at_this_index(other_players_pieces, 3)) {
                        legal=false;
                        break;
                    }
                }
                if (legal) {children.push_back(simulation);}
            }
            //
            if (is_one_at_this_index(Yy_bitboard, 3) && is_one_at_this_index(Zz_bitboard, 7) && !(is_one_at_this_index(all_pieces, 6)) && !(is_one_at_this_index(all_pieces, 5)) && !(is_one_at_this_index(all_pieces, 4))) {
                uint64_t new_Kk=set_bit_to_one(Kk_bitboard, 5);
                uint64_t new_Yy=clear_bit(Yy_bitboard, 3);
                uint64_t new_Tt=set_bit_to_one(Tt_bitboard, 4);
                uint64_t new_Zz=clear_bit(Zz_bitboard, 7);
                //
                Board simulation;
                simulation.b=this->b;
                simulation.l=this->l;
                simulation.x=this->x;
                simulation.t=new_Tt;
                simulation.q=this->q;
                simulation.k=new_Kk;
                simulation.y=new_Yy;
                simulation.z=new_Zz;
                simulation.f=this->f;
                //
                simulation.B=remove_common_bits(this->B, new_Kk);
                simulation.L=remove_common_bits(this->L, new_Kk);
                simulation.X=remove_common_bits(this->X, new_Kk);
                simulation.T=remove_common_bits(this->T, new_Kk);
                simulation.Q=remove_common_bits(this->Q, new_Kk);
                simulation.K=remove_common_bits(this->K, new_Kk);
                simulation.Y=remove_common_bits(this->Y, new_Kk);
                simulation.Z=remove_common_bits(this->Z, new_Kk);
                simulation.F=remove_common_bits(this->F, new_Kk);
                //
                bool legal=true;
                for (Board child : simulation.generate_children(-6)) {
                    uint64_t other_players_pieces= child.B|child.L|child.X|child.T|child.Q|child.K|child.Y|child.Z|child.F;
                    if (is_one_at_this_index(other_players_pieces, 3) || is_one_at_this_index(other_players_pieces, 4) || is_one_at_this_index(other_players_pieces, 5)) {
                        legal=false;
                        break;
                    }
                }
                if (legal) {children.push_back(simulation);}
            }
        }
        else {
            if (is_one_at_this_index(Yy_bitboard, 59) && is_one_at_this_index(Zz_bitboard, 56) && !(is_one_at_this_index(all_pieces, 57)) && !(is_one_at_this_index(all_pieces, 58))) {
                uint64_t new_Kk=set_bit_to_one(Kk_bitboard, 57);
                uint64_t new_Yy=clear_bit(Yy_bitboard, 59);
                uint64_t new_Tt=set_bit_to_one(Tt_bitboard, 58);
                uint64_t new_Zz=clear_bit(Zz_bitboard, 56);
                //
                Board simulation;
                simulation.B=this->B;
                simulation.L=this->L;
                simulation.X=this->X;
                simulation.T=new_Tt;
                simulation.Q=this->Q;
                simulation.K=new_Kk;
                simulation.Y=new_Yy;
                simulation.Z=new_Zz;
                simulation.F=this->F;
                //
                simulation.b=remove_common_bits(this->b, new_Kk);
                simulation.l=remove_common_bits(this->l, new_Kk);
                simulation.x=remove_common_bits(this->x, new_Kk);
                simulation.t=remove_common_bits(this->t, new_Kk);
                simulation.q=remove_common_bits(this->q, new_Kk);
                simulation.k=remove_common_bits(this->k, new_Kk);
                simulation.y=remove_common_bits(this->y, new_Kk);
                simulation.z=remove_common_bits(this->z, new_Kk);
                simulation.f=remove_common_bits(this->f, new_Kk);
                //
                bool legal=true;
                for (Board child : simulation.generate_children(6)) {
                    uint64_t other_players_pieces= child.b|child.l|child.x|child.t|child.q|child.k|child.y|child.z|child.f;
                    if (is_one_at_this_index(other_players_pieces, 59) || is_one_at_this_index(other_players_pieces, 58) || is_one_at_this_index(other_players_pieces, 57)) {
                        legal=false;
                        break;
                    }
                }
                if (legal) {children.push_back(simulation);}
            }
            //
            if (is_one_at_this_index(Yy_bitboard, 59) && is_one_at_this_index(Zz_bitboard, 63) && !(is_one_at_this_index(all_pieces, 62)) && !(is_one_at_this_index(all_pieces, 61)) && !(is_one_at_this_index(all_pieces, 60))) {
                uint64_t new_Kk=set_bit_to_one(Kk_bitboard, 61);
                uint64_t new_Yy=clear_bit(Yy_bitboard, 59);
                uint64_t new_Tt=set_bit_to_one(Tt_bitboard, 60);
                uint64_t new_Zz=clear_bit(Zz_bitboard, 63);
                //
                Board simulation;
                simulation.B=this->B;
                simulation.L=this->l;
                simulation.X=this->X;
                simulation.T=new_Tt;
                simulation.Q=this->Q;
                simulation.K=new_Kk;
                simulation.Y=new_Yy;
                simulation.Z=new_Zz;
                simulation.F=this->F;
                //
                simulation.b=remove_common_bits(this->b, new_Kk);
                simulation.l=remove_common_bits(this->l, new_Kk);
                simulation.x=remove_common_bits(this->x, new_Kk);
                simulation.t=remove_common_bits(this->t, new_Kk);
                simulation.q=remove_common_bits(this->q, new_Kk);
                simulation.k=remove_common_bits(this->k, new_Kk);
                simulation.y=remove_common_bits(this->y, new_Kk);
                simulation.z=remove_common_bits(this->z, new_Kk);
                simulation.f=remove_common_bits(this->f, new_Kk);
                //
                bool legal=true;
                for (Board child : simulation.generate_children(6)) {
                    uint64_t other_players_pieces= child.b|child.l|child.x|child.t|child.q|child.k|child.y|child.z|child.f;
                    if (is_one_at_this_index(other_players_pieces, 59) || is_one_at_this_index(other_players_pieces, 60) || is_one_at_this_index(other_players_pieces, 61)) {
                        legal=false;
                        break;
                    }
                }
                if (legal) {children.push_back(simulation);}
            }
        }
        //
        return children;
    }

    std::vector<Board> generate_children(int playerk) {
        std::vector<Board> children;
        //
        //Ff zu Bb
        std::vector<std::pair<int,int>> positions_Ff;
        if (playerk==6) {
            for (int y=0; y<8; ++y) {
                for (int x=0; x<8; ++x) {
                    if (is_one_at_this_index(this->f, yx_zu_index(y, x))) {positions_Ff.push_back({y, x});}
                }
            }
            for (const auto& position_Ff : positions_Ff) {
                int y=position_Ff.first;
                int x=position_Ff.second;
                uint64_t new_f=clear_bit(this->f, yx_zu_index(y, x));
                uint64_t new_b=set_bit_to_one(this->b, yx_zu_index(y, x));
                this->f=new_f;
                this->b=new_b;
            }
        }
        else {
            for (int y=0; y<8; ++y) {
                for (int x=0; x<8; ++x) {
                    if (is_one_at_this_index(this->F, yx_zu_index(y, x))) {positions_Ff.push_back({y, x});}
                }
            }
            for (const auto& position_Ff : positions_Ff) {
                int y=position_Ff.first;
                int x=position_Ff.second;
                uint64_t new_F=clear_bit(this->F, yx_zu_index(y, x));
                uint64_t new_B=set_bit_to_one(this->B, yx_zu_index(y, x));
                this->F=new_F;
                this->B=new_B;
            }
        }
        //
        uint64_t white_pieces = this->b|this->l|this->x|this->t|this->q|this->k|this->y|this->z|this->f;
        uint64_t black_pieces = this->B|this->L|this->X|this->T|this->Q|this->K|this->Y|this->Z|this->F;
        if (playerk==6) {
            if (this->b!=0) {
                for (const auto& board : gcBb(1, this->b, white_pieces, black_pieces, this->F)) {
                    Board child;
                    child.b=board.first;
                    child.l=this->l;
                    child.x=this->x;
                    child.t=this->t;
                    child.q=this->q;
                    child.k=this->k;
                    child.y=this->y;
                    child.z=this->z;
                    child.f=this->f;
                    //
                    child.B=remove_common_bits(this->B, board.first);
                    child.L=remove_common_bits(this->L, board.first);
                    child.X=remove_common_bits(this->X, board.first);
                    child.T=remove_common_bits(this->T, board.first);
                    child.Q=remove_common_bits(this->Q, board.first);
                    child.K=remove_common_bits(this->K, board.first);
                    child.Y=remove_common_bits(this->Y, board.first);
                    child.Z=remove_common_bits(this->Z, board.first);
                    child.F=remove_common_bits(board.second, board.first);
                    //
                    children.push_back(child);
                }
            }
            //
            if (this->l!=0) {
                for (const auto& board : gcLl(this->l, white_pieces)) {
                    Board child;
                    child.b=this->b;
                    child.l=board;
                    child.x=this->x;
                    child.t=this->t;
                    child.q=this->q;
                    child.k=this->k;
                    child.y=this->y;
                    child.z=this->z;
                    child.f=this->f;
                    //
                    child.B=remove_common_bits(this->B, board);
                    child.L=remove_common_bits(this->L, board);
                    child.X=remove_common_bits(this->X, board);
                    child.T=remove_common_bits(this->T, board);
                    child.Q=remove_common_bits(this->Q, board);
                    child.K=remove_common_bits(this->K, board);
                    child.Y=remove_common_bits(this->Y, board);
                    child.Z=remove_common_bits(this->Z, board);
                    child.F=remove_common_bits(this->F, board);
                    //
                    children.push_back(child);
                }
            }
            //
            if (this->t!=0) {
                for (const auto& board : gcTtXxQq(this->t, white_pieces, black_pieces, {{1, 0}, {-1, 0}, {0, 1}, {0, -1}})) {
                    Board child;
                    child.b=this->b;
                    child.l=this->l;
                    child.x=this->x;
                    child.t=board;
                    child.q=this->q;
                    child.k=this->k;
                    child.y=this->y;
                    child.z=this->z;
                    child.f=this->f;
                    //
                    child.B=remove_common_bits(this->B, board);
                    child.L=remove_common_bits(this->L, board);
                    child.X=remove_common_bits(this->X, board);
                    child.T=remove_common_bits(this->T, board);
                    child.Q=remove_common_bits(this->Q, board);
                    child.K=remove_common_bits(this->K, board);
                    child.Y=remove_common_bits(this->Y, board);
                    child.Z=remove_common_bits(this->Z, board);
                    child.F=remove_common_bits(this->F, board);
                    //
                    children.push_back(child);
                }
            }
            //
            if (this->x!=0) {
                for (const auto& board : gcTtXxQq(this->x, white_pieces, black_pieces, {{1, 1}, {-1, 1}, {1, -1}, {-1, -1}})) {
                    Board child;
                    child.b=this->b;
                    child.l=this->l;
                    child.x=board;
                    child.t=this->t;
                    child.q=this->q;
                    child.k=this->k;
                    child.y=this->y;
                    child.z=this->z;
                    child.f=this->f;
                    //
                    child.B=remove_common_bits(this->B, board);
                    child.L=remove_common_bits(this->L, board);
                    child.X=remove_common_bits(this->X, board);
                    child.T=remove_common_bits(this->T, board);
                    child.Q=remove_common_bits(this->Q, board);
                    child.K=remove_common_bits(this->K, board);
                    child.Y=remove_common_bits(this->Y, board);
                    child.Z=remove_common_bits(this->Z, board);
                    child.F=remove_common_bits(this->F, board);
                    //
                    children.push_back(child);
                }
            }
            //
            if (this->q!=0) {
                for (const auto& board : gcTtXxQq(this->q, white_pieces, black_pieces, {{1, 0}, {-1, 0}, {0, 1}, {0, -1}, {1, 1}, {-1, 1}, {1, -1}, {-1, -1}})) {
                    Board child;
                    child.b=this->b;
                    child.l=this->l;
                    child.x=this->x;
                    child.t=this->t;
                    child.q=board;
                    child.k=this->k;
                    child.y=this->y;
                    child.z=this->z;
                    child.f=this->f;
                    //
                    child.B=remove_common_bits(this->B, board);
                    child.L=remove_common_bits(this->L, board);
                    child.X=remove_common_bits(this->X, board);
                    child.T=remove_common_bits(this->T, board);
                    child.Q=remove_common_bits(this->Q, board);
                    child.K=remove_common_bits(this->K, board);
                    child.Y=remove_common_bits(this->Y, board);
                    child.Z=remove_common_bits(this->Z, board);
                    child.F=remove_common_bits(this->F, board);
                    //
                    children.push_back(child);
                }
            }
            //
            if (this->z!=0) {
                for (const auto& board : gcZz(this->z, this->t, white_pieces, black_pieces)) {
                    Board child;
                    child.b=this->b;
                    child.l=this->l;
                    child.x=this->x;
                    child.t=board.first;
                    child.q=this->q;
                    child.k=this->k;
                    child.y=this->y;
                    child.z=board.second;
                    child.f=this->f;
                    //
                    child.B=remove_common_bits(this->B, board.first);
                    child.L=remove_common_bits(this->L, board.first);
                    child.X=remove_common_bits(this->X, board.first);
                    child.T=remove_common_bits(this->T, board.first);
                    child.Q=remove_common_bits(this->Q, board.first);
                    child.K=remove_common_bits(this->K, board.first);
                    child.Y=remove_common_bits(this->Y, board.first);
                    child.Z=remove_common_bits(this->Z, board.first);
                    child.F=remove_common_bits(this->F, board.first);
                    //
                    children.push_back(child);
                }
            }
            //
            if (this->k!=0) {
                for (const auto& board : gcKk(this->k, white_pieces)) {
                    Board child;
                    child.b=this->b;
                    child.l=this->l;
                    child.x=this->x;
                    child.t=this->t;
                    child.q=this->q;
                    child.k=board;
                    child.y=this->y;
                    child.z=this->z;
                    child.f=this->f;
                    //
                    child.B=remove_common_bits(this->B, board);
                    child.L=remove_common_bits(this->L, board);
                    child.X=remove_common_bits(this->X, board);
                    child.T=remove_common_bits(this->T, board);
                    child.Q=remove_common_bits(this->Q, board);
                    child.K=remove_common_bits(this->K, board);
                    child.Y=remove_common_bits(this->Y, board);
                    child.Z=remove_common_bits(this->Z, board);
                    child.F=remove_common_bits(this->F, board);
                    //
                    children.push_back(child);
                }
            }
        }
        else {
            for (const auto& board : gcBb(-1, this->B, black_pieces, white_pieces, this->f)) {
                Board child;
                child.B=board.first;
                child.L=this->L;
                child.X=this->X;
                child.T=this->T;
                child.Q=this->Q;
                child.K=this->K;
                child.Y=this->Y;
                child.Z=this->Z;
                child.F=this->F;
                //
                child.b=remove_common_bits(this->b, board.first);
                child.l=remove_common_bits(this->l, board.first);
                child.x=remove_common_bits(this->x, board.first);
                child.t=remove_common_bits(this->t, board.first);
                child.q=remove_common_bits(this->q, board.first);
                child.k=remove_common_bits(this->k, board.first);
                child.y=remove_common_bits(this->y, board.first);
                child.z=remove_common_bits(this->z, board.first);
                child.f=remove_common_bits(board.second, board.first);
                //
                children.push_back(child);
            }
            for (const auto& board : gcLl(this->L, black_pieces)) {
                Board child;
                child.B=this->B;
                child.L=board;
                child.X=this->X;
                child.T=this->T;
                child.Q=this->Q;
                child.K=this->K;
                child.Y=this->Y;
                child.Z=this->Z;
                child.F=this->F;
                //
                child.b=remove_common_bits(this->b, board);
                child.l=remove_common_bits(this->l, board);
                child.x=remove_common_bits(this->x, board);
                child.t=remove_common_bits(this->t, board);
                child.q=remove_common_bits(this->q, board);
                child.k=remove_common_bits(this->k, board);
                child.y=remove_common_bits(this->y, board);
                child.z=remove_common_bits(this->z, board);
                child.f=remove_common_bits(this->f, board);
                //
                children.push_back(child);
            }
            for (const auto& board : gcTtXxQq(this->T, black_pieces, white_pieces, {{1, 0}, {-1, 0}, {0, 1}, {0, -1}})) {
                Board child;
                child.B=this->B;
                child.L=this->L;
                child.X=this->X;
                child.T=board;
                child.Q=this->Q;
                child.K=this->K;
                child.Y=this->Y;
                child.Z=this->Z;
                child.F=this->F;
                //
                child.b=remove_common_bits(this->b, board);
                child.l=remove_common_bits(this->l, board);
                child.x=remove_common_bits(this->x, board);
                child.t=remove_common_bits(this->t, board);
                child.q=remove_common_bits(this->q, board);
                child.k=remove_common_bits(this->k, board);
                child.y=remove_common_bits(this->y, board);
                child.z=remove_common_bits(this->z, board);
                child.f=remove_common_bits(this->f, board);
                //
                children.push_back(child);
            }
            for (const auto& board : gcTtXxQq(this->X, black_pieces, white_pieces, {{1, 1}, {-1, 1}, {1, -1}, {-1, -1}})) {
                Board child;
                child.B=this->B;
                child.L=this->L;
                child.X=board;
                child.T=this->T;
                child.Q=this->Q;
                child.K=this->K;
                child.Y=this->Y;
                child.Z=this->Z;
                child.F=this->F;
                //
                child.b=remove_common_bits(this->b, board);
                child.l=remove_common_bits(this->l, board);
                child.x=remove_common_bits(this->x, board);
                child.t=remove_common_bits(this->t, board);
                child.q=remove_common_bits(this->q, board);
                child.k=remove_common_bits(this->k, board);
                child.y=remove_common_bits(this->y, board);
                child.z=remove_common_bits(this->z, board);
                child.f=remove_common_bits(this->f, board);
                //
                children.push_back(child);
            }
            for (const auto& board : gcTtXxQq(this->Q, black_pieces, white_pieces, {{1, 0}, {-1, 0}, {0, 1}, {0, -1}, {1, 1}, {-1, 1}, {1, -1}, {-1, -1}})) {
                Board child;
                child.B=this->B;
                child.L=this->L;
                child.X=this->X;
                child.T=this->T;
                child.Q=board;
                child.K=this->K;
                child.Y=this->Y;
                child.Z=this->Z;
                child.F=this->F;
                //
                child.b=remove_common_bits(this->b, board);
                child.l=remove_common_bits(this->l, board);
                child.x=remove_common_bits(this->x, board);
                child.t=remove_common_bits(this->t, board);
                child.q=remove_common_bits(this->q, board);
                child.k=remove_common_bits(this->k, board);
                child.y=remove_common_bits(this->y, board);
                child.z=remove_common_bits(this->z, board);
                child.f=remove_common_bits(this->f, board);
                //
                children.push_back(child);
            }
            for (const auto& board : gcZz(this->Z, this->T, black_pieces, white_pieces)) {
                Board child;
                child.B=this->B;
                child.L=this->L;
                child.X=this->X;
                child.T=board.first;
                child.Q=this->Q;
                child.K=this->K;
                child.Y=this->Y;
                child.Z=board.second;
                child.F=this->F;
                //
                child.b=remove_common_bits(this->b, board.first);
                child.l=remove_common_bits(this->l, board.first);
                child.x=remove_common_bits(this->x, board.first);
                child.t=remove_common_bits(this->t, board.first);
                child.q=remove_common_bits(this->q, board.first);
                child.k=remove_common_bits(this->k, board.first);
                child.y=remove_common_bits(this->y, board.first);
                child.z=remove_common_bits(this->z, board.first);
                child.f=remove_common_bits(this->f, board.first);
                //
                children.push_back(child);
            }
            for (const auto& board : gcKk(this->K, black_pieces)) {
                Board child;
                child.B=this->B;
                child.L=this->L;
                child.X=this->X;
                child.T=this->T;
                child.Q=this->Q;
                child.K=board;
                child.Y=this->Y;
                child.Z=this->Z;
                child.F=this->F;
                //
                child.b=remove_common_bits(this->b, board);
                child.l=remove_common_bits(this->l, board);
                child.x=remove_common_bits(this->x, board);
                child.t=remove_common_bits(this->t, board);
                child.q=remove_common_bits(this->q, board);
                child.k=remove_common_bits(this->k, board);
                child.y=remove_common_bits(this->y, board);
                child.z=remove_common_bits(this->z, board);
                child.f=remove_common_bits(this->f, board);
                //
                children.push_back(child);
            }
        }
        return children;
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
    root_node.K   = 0b0000000000000000000000000000000000000000000000000000000000000000ULL;

    root_node.Y   = 0b0001000000000000000000000000000000000000000000000000000000000000ULL;
    root_node.Z   = 0b1000000100000000000000000000000000000000000000000000000000000000ULL;
    root_node.F   = 0b0000000000000000000000000000000000000000000000000000000000000000ULL;

    uint64_t white_pieces = root_node.b|root_node.l|root_node.x|root_node.t|root_node.q|root_node.k|root_node.y|root_node.z|root_node.f;
    uint64_t black_pieces = root_node.B|root_node.L|root_node.X|root_node.T|root_node.Q|root_node.K|root_node.Y|root_node.Z|root_node.F;

    root_node.print_board();
    std::cout<<"--------------"<<std::endl;
    for (Board child : root_node.generate_children(-6)) {
        child.print_board();
    }
    std::cout<<"--------------"<<std::endl;
    root_node.print_board();

}

