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
    std::vector<int> bits;
    uint64_t m = 1ULL;
    //
    for (int i=0; i<64; ++i) {
        if (bitboard & m) {bits.push_back(1);}
        else {bits.push_back(0);}
        m <<= 1;
    }
    //
    std::reverse(bits.begin(), bits.end());
    //
    for (int i=0; i<bits.size(); ++i) {
        std::cout<<bits[i]<<" ";
        if ((i+1) % 8 == 0) {std::cout << std::endl;}
    }
}

std::vector<std::vector<int>> matrix_minus(std::vector<std::vector<int>> matrix) {
    for (int i=0; i<matrix.size(); ++i) {
        for (int j=0; j<matrix[i].size(); ++j) {
            matrix[i][j]=-matrix[i][j];
        }
    }
    return matrix;
}

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
    //if already 0: does nothing
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

//

std::vector<std::vector<int>> B_matrix = {
    { 0,  0,  0,  0,  0,  0,  0,  0},
    { 1,  1,  1,  1,  1,  1,  1,  1},
    { 2,  2,  2,  2,  2,  2,  2,  2},
    { 3,  3,  4,  4,  4,  4,  3,  3},
    { 3,  3,  4,  4,  4,  4,  3,  3},
    { 4,  4,  4,  4,  4,  4,  4,  4},
    { 5,  5,  5,  5,  5,  5,  5,  5},
    { 0,  0,  0,  0,  0,  0,  0,  0}
};

std::vector<std::vector<int>> b_matrix = {
    { 0,  0,  0,  0,  0,  0,  0,  0},
    { 5,  5,  5,  5,  5,  5,  5,  5},
    { 4,  4,  4,  4,  4,  4,  4,  4},
    { 3,  3,  4,  4,  4,  4,  3,  3},
    { 3,  3,  4,  4,  4,  4,  3,  3},
    { 2,  2,  2,  2,  2,  2,  2,  2},
    { 1,  1,  1,  1,  1,  1,  1,  1},
    { 0,  0,  0,  0,  0,  0,  0,  0}
};

std::vector<std::vector<int>> Ll_matrix = {
    {-1, -3, -2, -2, -2, -2, -3, -1},
    {-1,  0,  0,  0,  0,  0,  0, -1},
    {-1,  0,  1,  1,  1,  1,  0, -1},
    {-1,  0,  1,  2,  2,  1,  0, -1},
    {-1,  0,  1,  2,  2,  1,  0, -1},
    {-1,  0,  1,  1,  1,  1,  0, -1},
    {-1,  0,  0,  0,  0,  0,  0, -1},
    {-1, -3, -2, -2, -2, -2, -3, -1}
};

std::vector<std::vector<int>> Xx_matrix = {
    {-2, -1, -1, -1, -1, -1, -1, -2},
    {-1,  0,  0,  0,  0,  0,  0, -1},
    {-1,  0,  1,  1,  1,  1,  0, -1},
    {-1,  0,  1,  2,  2,  1,  0, -1},
    {-1,  0,  1,  2,  2,  1,  0, -1},
    {-1,  0,  1,  1,  1,  1,  0, -1},
    {-1,  0,  0,  0,  0,  0,  0, -1},
    {-2, -1, -1, -1, -1, -1, -1, -2}
};

std::vector<std::vector<int>> Tt_matrix = {
    { 0,  0,  0,  0,  0,  0,  0,  0},
    { 1,  1,  1,  1,  1,  1,  1,  1},
    { 1,  1,  1,  1,  1,  1,  1,  1},
    { 1,  1,  1,  1,  1,  1,  1,  1},
    { 1,  1,  1,  1,  1,  1,  1,  1},
    { 1,  1,  1,  1,  1,  1,  1,  1},
    { 1,  1,  1,  1,  1,  1,  1,  1},
    { 0,  0,  0,  0,  0,  0,  0,  0}
};

std::vector<std::vector<int>> Qq_matrix = {
    {-1, -1, -1, -1, -1, -1, -1, -1},
    {-1,  0,  0,  0,  0,  0,  0, -1},
    {-1,  0,  1,  1,  1,  1,  0, -1},
    {-1,  0,  1,  2,  2,  1,  0, -1},
    {-1,  0,  1,  2,  2,  1,  0, -1},
    {-1,  0,  1,  1,  1,  1,  0, -1},
    {-1,  0,  0,  0,  0,  0,  0, -1},
    {-1, -1, -1, -1, -1, -1, -1, -1}
};

std::vector<std::vector<int>> K_matrix = {
    { 2,  3,  1,  0,  0,  1,  3,  2},
    { 2,  2,  0,  0,  0,  0,  2,  2},
    {-1, -2, -2, -2, -2, -2, -2, -1},
    {-2, -3, -3, -4, -4, -3, -3, -2},
    {-3, -4, -4, -5, -5, -4, -4, -3},
    {-3, -4, -4, -5, -5, -4, -4, -3},
    {-4, -5, -5, -6, -6, -5, -5, -4},
    {-4, -5, -5, -6, -6, -5, -5, -4}
};

std::vector<std::vector<int>> k_matrix = {
    { -4,  -5,  -5,  -6,  -6,  -5,  -5,  -4},
    { -4,  -5,  -5,  -6,  -6,  -5,  -5,  -4},
    { -3,  -4,  -4,  -5,  -5,  -4,  -4,  -3},
    { -3,  -4,  -4,  -5,  -5,  -4,  -4,  -3},
    { -2,  -3,  -3,  -4,  -4,  -3,  -3,  -2},
    { -1,  -2,  -2,  -2,  -2,  -2,  -2,  -1},
    {  2,   2,   0,   0,   0,   0,   2,   2},
    {  2,   3,   1,   0,   0,   1,   3,   2}
};

std::vector<std::vector<int>> other_B_matrix = matrix_minus(B_matrix);
std::vector<std::vector<int>> other_b_matrix = matrix_minus(b_matrix);
std::vector<std::vector<int>> other_Ll_matrix = matrix_minus(Ll_matrix);
std::vector<std::vector<int>> other_Xx_matrix = matrix_minus(Xx_matrix);
std::vector<std::vector<int>> other_Tt_matrix = matrix_minus(Tt_matrix);
std::vector<std::vector<int>> other_Qq_matrix = matrix_minus(Qq_matrix);
std::vector<std::vector<int>> other_K_matrix = matrix_minus(K_matrix);
std::vector<std::vector<int>> other_k_matrix = matrix_minus(k_matrix);

//

//forward declarartions
class Board;
std::vector<Board> generate_children(int playerk);

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

    void print_board() const {
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
        for (int i=0; i<8; i++) {std::reverse(board[i].begin(), board[i].end());}
        //
        //print the board
        std::cout <<"    8   7   6   5   4   3   2   1\n";
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

    bool verloren(int playerk) const {
        if (playerk==6) {
            if (this->k==0 && this->y==0) {return true;}
            else {return false;}
        }
        else {
            if (this->K==0 && this->Y==0) {return true;}
            else {return false;}
        }
    }

    int evaluate_position(int playerk) const {
        int val = 0;
        if (playerk==6) {
            for (int p=0; p<8; ++p) {
                for (int o=0; o<8; ++o) {
                    if (is_one_at_this_index(this->B, yx_zu_index(p, o)) || is_one_at_this_index(this->F, yx_zu_index(p, o))) {
                        val += -100;
                        val += other_B_matrix[p][o];
                        // Pawn structure
                        if (p+1<=7 && o+1<=7) {
                            if (is_one_at_this_index(this->B, yx_zu_index(p+1, o+1)) || is_one_at_this_index(this->F, yx_zu_index(p+1, o+1))) {val += -1;}
                        }
                        if (p-1>=0 && o-1>=0) {
                            if (is_one_at_this_index(this->B, yx_zu_index(p-1, o-1)) || is_one_at_this_index(this->F, yx_zu_index(p-1, o-1))) {val += -1;}
                        }
                        if (p+1<=7 && o-1>=0) {
                            if (is_one_at_this_index(this->B, yx_zu_index(p+1, o-1)) || is_one_at_this_index(this->F, yx_zu_index(p+1, o-1))) {val += -1;}
                        }
                        if (p-1>=0 && o+1<=7) {
                            if (is_one_at_this_index(this->B, yx_zu_index(p-1, o+1)) || is_one_at_this_index(this->F, yx_zu_index(p-1, o+1))) {val += -1;}
                        }
                    }//
                    else if (is_one_at_this_index(this->b, yx_zu_index(p, o)) || is_one_at_this_index(this->f, yx_zu_index(p, o))) {
                        val += 100;
                        val += b_matrix[p][o];
                        // Pawn structure
                        if (p+1<=7 && o+1<=7) {
                            if (is_one_at_this_index(this->b, yx_zu_index(p+1, o+1)) || is_one_at_this_index(this->f, yx_zu_index(p+1, o+1))) {val += 1;}
                        }
                        if (p-1>=0 && o-1>=0) {
                            if (is_one_at_this_index(this->b, yx_zu_index(p-1, o-1)) || is_one_at_this_index(this->f, yx_zu_index(p-1, o-1))) {val += 1;}
                        }
                        if (p+1<=7 && o-1>=0) {
                            if (is_one_at_this_index(this->b, yx_zu_index(p+1, o-1)) || is_one_at_this_index(this->f, yx_zu_index(p+1, o-1))) {val += 1;}
                        }
                        if (p-1>=0 && o+1<=7) {
                            if (is_one_at_this_index(this->b, yx_zu_index(p-1, o+1)) || is_one_at_this_index(this->f, yx_zu_index(p-1, o+1))) {val += 1;}
                        }
                    }
                    else if (is_one_at_this_index(this->L, yx_zu_index(p, o))) {
                        val += -300;
                        val += other_Ll_matrix[p][o];
                    }
                    else if (is_one_at_this_index(this->X, yx_zu_index(p, o))) {
                        val += -300;
                        val += other_Xx_matrix[o][p];
                    }
                    else if (is_one_at_this_index(this->T, yx_zu_index(p, o)) || is_one_at_this_index(this->Z, yx_zu_index(p, o))) {
                        val += -500;
                        val += other_Tt_matrix[p][o];
                    }
                    else if (is_one_at_this_index(this->l, yx_zu_index(p, o))) {
                        val += 300;
                        val += Ll_matrix[p][o];
                    }
                    else if (is_one_at_this_index(this->x, yx_zu_index(p, o))) {
                        val += 300;
                        val += Xx_matrix[o][p];
                    }
                    else if (is_one_at_this_index(this->t, yx_zu_index(p, o)) || is_one_at_this_index(this->z, yx_zu_index(p, o))) {
                        val += 500;
                        val += Tt_matrix[p][o];
                    }
                    else if (is_one_at_this_index(this->Q, yx_zu_index(p, o))) {
                        val += -900;
                        val += other_Qq_matrix[p][o];
                    }
                    else if (is_one_at_this_index(this->K, yx_zu_index(p, o)) || is_one_at_this_index(this->Y, yx_zu_index(p, o))) {
                        val += -100000;
                        val += other_K_matrix[p][o];
                    }
                    else if (is_one_at_this_index(this->q, yx_zu_index(p, o))) {
                        val += 900;
                        val += Qq_matrix[p][o];
                    }
                    else if (is_one_at_this_index(this->k, yx_zu_index(p, o)) || is_one_at_this_index(this->y, yx_zu_index(p, o))) {
                        val += 100000;
                        val += k_matrix[p][o];
                    }
                }
            }
        }
        else if (playerk==-6) {
            for (int p=0; p<8; ++p) {
                for (int o=0; o<8; ++o) {
                    if (is_one_at_this_index(this->B, yx_zu_index(p, o)) || is_one_at_this_index(this->F, yx_zu_index(p, o))) {
                        val += 100;
                        val += B_matrix[p][o];
                        // Pawn structure
                        if (p+1<=7 && o+1<=7) {
                            if (is_one_at_this_index(this->B, yx_zu_index(p+1, o+1)) || is_one_at_this_index(this->F, yx_zu_index(p+1, o+1))) {val += 1;}
                        }
                        if (p-1>=0 && o-1>=0) {
                            if (is_one_at_this_index(this->B, yx_zu_index(p-1, o-1)) || is_one_at_this_index(this->F, yx_zu_index(p-1, o-1))) {val += 1;}
                        }
                        if (p+1<=7 && o-1>=0) {
                            if (is_one_at_this_index(this->B, yx_zu_index(p+1, o-1)) || is_one_at_this_index(this->F, yx_zu_index(p+1, o-1))) {val += 1;}
                        }
                        if (p-1>=0 && o+1<=7) {
                            if (is_one_at_this_index(this->B, yx_zu_index(p-1, o+1)) || is_one_at_this_index(this->F, yx_zu_index(p-1, o+1))) {val += 1;}
                        }
                    }
                    else if (is_one_at_this_index(this->b, yx_zu_index(p, o)) || is_one_at_this_index(this->f, yx_zu_index(p, o))) {
                        val += -100;
                        val += other_b_matrix[p][o];
                        // Pawn structure
                        if (p+1<=7 && o+1<=7) {
                            if (is_one_at_this_index(this->b, yx_zu_index(p+1, o+1)) || is_one_at_this_index(this->f, yx_zu_index(p+1, o+1))) {val += -1;}
                        }
                        if (p-1>=0 && o-1>=0) {
                            if (is_one_at_this_index(this->b, yx_zu_index(p-1, o-1)) || is_one_at_this_index(this->f, yx_zu_index(p-1, o-1))) {val += -1;}
                        }
                        if (p+1<=7 && o-1>=0) {
                            if (is_one_at_this_index(this->b, yx_zu_index(p+1, o-1)) || is_one_at_this_index(this->f, yx_zu_index(p+1, o-1))) {val += -1;}
                        }
                        if (p-1>=0 && o+1<=7) {
                            if (is_one_at_this_index(this->b, yx_zu_index(p-1, o+1)) || is_one_at_this_index(this->f, yx_zu_index(p-1, o+1))) {val += -1;}
                        }
                    }
                    else if (is_one_at_this_index(this->L, yx_zu_index(p, o))) {
                        val += 300;
                        val += Ll_matrix[p][o];
                    }
                    else if (is_one_at_this_index(this->X, yx_zu_index(p, o))) {
                        val += 300;
                        val += Xx_matrix[p][o];
                    }
                    else if (is_one_at_this_index(this->T, yx_zu_index(p, o)) || is_one_at_this_index(this->Z, yx_zu_index(p, o))) {
                        val += 500;
                        val += Tt_matrix[p][o];
                    }
                    else if (is_one_at_this_index(this->l, yx_zu_index(p, o))) {
                        val += -300;
                        val += other_Ll_matrix[p][o];
                    }
                    else if (is_one_at_this_index(this->x, yx_zu_index(p, o))) {
                        val += -300;
                        val += other_Xx_matrix[p][o];
                    }
                    else if (is_one_at_this_index(this->t, yx_zu_index(p, o)) || is_one_at_this_index(this->z, yx_zu_index(p, o))) {
                        val += -500;
                        val += other_Tt_matrix[p][o];
                    }
                    else if (is_one_at_this_index(this->Q, yx_zu_index(p, o))) {
                        val += 900;
                        val += other_Qq_matrix[p][o];
                    }
                    else if (is_one_at_this_index(this->K, yx_zu_index(p, o)) || is_one_at_this_index(this->Y, yx_zu_index(p, o))) {
                        val += 100000;
                        val += other_K_matrix[p][o];
                    }
                    else if (is_one_at_this_index(this->q, yx_zu_index(p, o))) {
                        val += -900;
                        val += Qq_matrix[p][o];
                    }
                    else if (is_one_at_this_index(this->k, yx_zu_index(p, o)) || is_one_at_this_index(this->y, yx_zu_index(p, o))) {
                        val += -100000;
                        val += other_k_matrix[p][o];
                    }
                }
            }
        }
        return val;
    }

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
                        uint64_t new_Yy=clear_bit(Yy_bitboard, yx_zu_index(y_current, x_current));
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
        //
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
        uint64_t all_pieces = white_pieces|black_pieces;
        //
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
            //
            if (this->y!=0) {
                for (Board child_Yy : gcYy(6, white_pieces, all_pieces)) {children.push_back(child_Yy);}
            }
        }
        else {
            if (this->B!=0) {
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
            }
            //
            if (this->L!=0) {
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
            }
            //
            if (this->T!=0) {
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
            }
            //
            if (this->X!=0) {
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
            }
            //
            if (this->Q!=0) {
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
            }
            //
            if (this->Z!=0) {
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
            }
            //
            if (this->K!=0) {
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
            //
            if (this->Y!=0) {
                for (Board child_Yy : gcYy(-6, black_pieces, all_pieces)) {children.push_back(child_Yy);}
            }
        }
        return children;
    }

};

//

class HumanPlayer {
public:
    HumanPlayer(int token, Board board) : token(token), board(board) {}
    int token=token;
    Board board;

    bool do_these_two_vectors_have_the_same_elements(const std::vector<std::vector<int>>& vector1, const std::vector<std::vector<int>>& vector2) {
        for (size_t i=0; i<vector1.size(); ++i) {
            for (size_t j=0; j<vector1[i].size(); ++j) {
                if (vector1[i][j] != vector2[i][j]) {return false;}
            }
        }
        return true;
    }

    std::vector<int> eingabe() {
        try {
            int vx, vy, zx, zy;
            std::cout <<"von x: ";
            std::cin>> vx;
            std::cout <<"von y: ";
            std::cin>> vy;
            std::cout <<"zu x: ";
            std::cin>> zx;
            std::cout <<"zu y: ";
            std::cin >> zy;
            //
            vx -= 1;
            vy -= 1;
            zx -= 1;
            zy -= 1;
            //
            if (vy < 8 && vy > -1 && vx < 8 && vx > -1 && zy < 8 && zy > -1 && zx < 8 && zx > -1 && is_int(vx) && is_int(vy)&& is_int(zx)&& is_int(zy)) {
                    return {vy, vx, zy, zx};
            }
            else {
                std::cin.clear();
                std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
                std::cout << "EINGABE NICHT KORREKT1" << std::endl;
                return eingabe();
            }
        }
        catch (...) {
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            std::cout << "EINGABE NICHT KORREKT1" << std::endl;
            return eingabe();
        }
    }

    Board* player(Board& pos) {
        int other_player = (this->token == 6) ? -6 : 6;
        std::vector<Board> legal_moves;
        bool legal_move_exists = false;
        std::vector<Board> all_moves = pos.generate_children(this->token);
        uint64_t all_pieces=pos.b|pos.l|pos.x|pos.t|pos.q|pos.k|pos.f|pos.z|pos.y|pos.B|pos.L|pos.X|pos.T|pos.Q|pos.K|pos.F|pos.Z|pos.Y;
        //
        for (Board& child_of_root : all_moves) {
            bool king_is_killed = false;
            for (const auto& child_of_child : child_of_root.generate_children(other_player)) {
                if (child_of_child.verloren(this->token)) {
                    king_is_killed = true;
                    break;
                }
            }
            if (!king_is_killed) {
                legal_move_exists = true;
                legal_moves.push_back(child_of_root);
            }
        }
        //
        if (!legal_move_exists) {return nullptr;}
        //
        while (true) {
            Board boardcopy = pos;
            std::vector<int> input_move = this->eingabe();
            int vy = input_move[0];
            int vx = input_move[1];
            int zy = input_move[2];
            int zx = input_move[3];

            //update boardcopy
            //1 & -1 to 5 & -5
            for (int x=0; x<8; ++x) {
                if (is_one_at_this_index(boardcopy.b, 56+x)) {clear_bit(boardcopy.b, 56+x); set_bit_to_one(boardcopy.q, 56+x);}
            }
            for (int x=0; x<8; ++x) {
                if (is_one_at_this_index(boardcopy.B, 0+x)) {clear_bit(boardcopy.B, 0+x); set_bit_to_one(boardcopy.Q, 0+x);}
            }
            //9 & -9weg man konete nur die korrekten y suchen
            if (this->token==6) {
                for (int y=0; y<8; ++y) {
                    for (int x=0; x<8; ++x) {
                        if (is_one_at_this_index(boardcopy.f, yx_zu_index(y,x))) {clear_bit(boardcopy.f, yx_zu_index(y,x)); set_bit_to_one(boardcopy.b, yx_zu_index(y,x));}
                    }
                }
            }
            else if (this->token==-6) {
                for (int y=0; y<8; ++y) {
                    for (int x=0; x<8; ++x) {
                        if (is_one_at_this_index(boardcopy.F, yx_zu_index(y,x))) {clear_bit(boardcopy.F, yx_zu_index(y,x)); set_bit_to_one(boardcopy.B, yx_zu_index(y,x));}
                    }
                }
            }
            //special moves
            bool special = false;
            //rochade
            if (vy==0 && vx==4 && zy==0 && zx==6 && this->token==6 && is_one_at_this_index(boardcopy.y, yx_zu_index(vy,vx))) {
                special = true;
                set_bit_to_one(boardcopy.k, 1);
                set_bit_to_one(boardcopy.t, 2);
                clear_bit(boardcopy.y, 3);
                clear_bit(boardcopy.z, 0);
            }
            if (vy==0 && vx==4 && zy==0 && zx==2 && this->token==6 && is_one_at_this_index(boardcopy.y, yx_zu_index(vy,vx))) {
                special = true;
                set_bit_to_one(boardcopy.k, 5);
                set_bit_to_one(boardcopy.t, 4);
                clear_bit(boardcopy.y, 3);
                clear_bit(boardcopy.z, 7);
            }
            if (vy==7 && vx==4 && zy==7 && zx==6 && this->token==-6 && is_one_at_this_index(boardcopy.Y, yx_zu_index(vy,vx))) {
                special = true;
                set_bit_to_one(boardcopy.k, 57);
                set_bit_to_one(boardcopy.t, 58);
                clear_bit(boardcopy.y, 59);
                clear_bit(boardcopy.z, 56);
            }
            if (vy==7 && vx==4 && zy==7 && zx==2 && this->token==-6 && is_one_at_this_index(boardcopy.Y, yx_zu_index(vy,vx))) {
                special = true;
                set_bit_to_one(boardcopy.k, 61);
                set_bit_to_one(boardcopy.t, 60);
                clear_bit(boardcopy.y, 59);
                clear_bit(boardcopy.z, 63);
            }
            // Bb 2 nach vorne
            if (is_one_at_this_index(boardcopy.b, yx_zu_index(vy,vx)) && vy==6 && !(is_one_at_this_index(all_pieces, yx_zu_index(zy,zx))) && !(is_one_at_this_index(all_pieces, yx_zu_index(vy+1,vx))) && vx==zx && zy==vy+2) {
                special = true;
                set_bit_to_one(boardcopy.f, yx_zu_index(zy,zx));
                clear_bit(boardcopy.b, yx_zu_index(vy,vx));
            }
            if (is_one_at_this_index(boardcopy.B, yx_zu_index(vy,vx)) && vy==1 && !(is_one_at_this_index(all_pieces, yx_zu_index(zy,zx))) && !(is_one_at_this_index(all_pieces, yx_zu_index(vy-1,vx))) && vx==zx && zy==vy-2) {
                special = true;
                set_bit_to_one(boardcopy.F, yx_zu_index(zy,zx));
                clear_bit(boardcopy.B, yx_zu_index(vy,vx));
            }
            // En passant
            if (is_one_at_this_index(boardcopy.b, yx_zu_index(vy,vx)) && zy==vy+1 && zx==vx-1 && !(is_one_at_this_index(all_pieces, yx_zu_index(zy,zx)))) {
                special = true;
                clear_bit(boardcopy.b, yx_zu_index(vy,vx));
                set_bit_to_one(boardcopy.b, yx_zu_index(zy,zx));
                clear_bit(boardcopy.F, yx_zu_index(vy,zx));
            }
            if (is_one_at_this_index(boardcopy.b, yx_zu_index(vy,vx)) && zy==vy+1 && zx==vx+1 && !(is_one_at_this_index(all_pieces, yx_zu_index(zy,zx)))) {
                special = true;
                clear_bit(boardcopy.b, yx_zu_index(vy,vx));
                set_bit_to_one(boardcopy.b, yx_zu_index(zy,zx));
                clear_bit(boardcopy.F, yx_zu_index(vy,zx));
            }
            if (is_one_at_this_index(boardcopy.B, yx_zu_index(vy,vx)) && zy==vy-1 && zx==vx-1 && !(is_one_at_this_index(all_pieces, yx_zu_index(zy,zx)))) {
                special = true;
                clear_bit(boardcopy.B, yx_zu_index(vy,vx));
                set_bit_to_one(boardcopy.B, yx_zu_index(zy,zx));
                clear_bit(boardcopy.f, yx_zu_index(vy,zx));
            }
            if (is_one_at_this_index(boardcopy.B, yx_zu_index(vy,vx)) && zy==vy-1 && zx==vx+1 && !(is_one_at_this_index(all_pieces, yx_zu_index(zy,zx)))) {
                special = true;
                clear_bit(boardcopy.B, yx_zu_index(vy,vx));
                set_bit_to_one(boardcopy.B, yx_zu_index(zy,zx));
                clear_bit(boardcopy.f, yx_zu_index(vy,zx));
            }
            //normal muss geändert werden!!!
            if (!special) {
                if (boardcopy[vy][vx]==7) {boardcopy[zy][zx] = 4;}
                else if (boardcopy[vy][vx]==-7) {boardcopy[zy][zx] = -4;}
                else if (boardcopy[vy][vx]==8) {boardcopy[zy][zx] = 6;}
                else if (boardcopy[vy][vx]==-8) {boardcopy[zy][zx] = -6;}
                else {boardcopy[zy][zx] = boardcopy[vy][vx];}
                boardcopy[vy][vx] = 0;
            }
            //
            bool move_legal = false;
            for (const auto& legal_move : legal_moves) {
                if (do_these_two_vectors_have_the_same_elements(boardcopy, legal_move)) {
                    move_legal = true;
                    break;
                }
            }
            if (move_legal) {return &boardcopy;}
            else {
                boardcopy.print_board();
                std::cout << "legal_children" << std::endl;
                for (Board& s : legal_moves) {s.print_board();}
                std::cout << "---------------------------------" << std::endl;
                pos.print_board();
                std::cout << "EINGABE NICHT KORREKT2" << std::endl;
            }
        }
    }

    Board* get_move() {
        return player(this->board);
    }

};


//

int minimax_counter=0;

class MinimaxNode {
public:
    MinimaxNode() : value(0), value_not_none(false), children(), board(), player_am_zug(0), token(0), depth(0), expanded(false) {}

    int value;
    bool value_not_none;
    std::vector<MinimaxNode> children;
    Board board;
    int player_am_zug;
    int token;
    int depth;
    bool expanded;

    std::vector<MinimaxNode> expand_node() {
        std::vector<MinimaxNode> new_children;
        std::vector<Board> list_of_positions = this->board.generate_children(this->player_am_zug);
        for (const Board& board_position : list_of_positions) {
            MinimaxNode child;
            child.board = board_position;
            child.player_am_zug = -this->player_am_zug;
            child.token = this->token;
            child.depth = this->depth + 1;
            child.value_not_none = false;
            child.value=0;
            child.children;
            new_children.push_back(child);
        }
        return new_children;
    }

    int minimax(int alpha, int beta, bool max_player, const int max_depth) {
        //
        minimax_counter+=1;
        //
        if (this->depth>=max_depth || this->board.verloren(6) || this->board.verloren(-6)) {
            this->value = this->board.evaluate_position(this->token);
            this->value_not_none=true;
            return this->value;
        }
        //
        if (!this->expanded) {this->children=this->expand_node(); this->expanded = true;}
        if (this->children.empty()) {
            this->value = this->board.evaluate_position(this->token);
            this->value_not_none=true;
            return this->value;
        }
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
            int min_value=1000000;
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
        if (this->expanded) {
            //
            std::vector<MinimaxNode> not_none_children;
            std::list<MinimaxNode> none_children;
            std::vector<MinimaxNode> sorted_children;
            //
            for (const MinimaxNode& child : this->children) {
                if (!child.value_not_none) {none_children.push_back(child);}
                else {not_none_children.push_back(child);}
            }
            //
            if (max_player) {
                std::sort(not_none_children.begin(), not_none_children.end(),[](const MinimaxNode& a, const MinimaxNode& b) {return a.value > b.value;});
                //
                sorted_children.insert(sorted_children.end(), not_none_children.begin(), not_none_children.end());
                sorted_children.insert(sorted_children.end(), none_children.begin(), none_children.end());
                this->children=sorted_children;
                //
                for (MinimaxNode& child : not_none_children) {child.sort(false);}
            }
            else {
                std::sort(not_none_children.begin(), not_none_children.end(),[](const MinimaxNode& a, const MinimaxNode& b) {return a.value < b.value;});
                //
                sorted_children.insert(sorted_children.end(), not_none_children.begin(), not_none_children.end());
                sorted_children.insert(sorted_children.end(), none_children.begin(), none_children.end());
                this->children=sorted_children;
                //
                for (MinimaxNode& child : not_none_children) {child.sort(true);}
            }
        }
    }

};

class MinimaxPlayer {
public:
    MinimaxPlayer(int token, Board board) : token(token), board(board) {
        root_node.board = board;
        root_node.player_am_zug = token;
        root_node.token=token;
        root_node.value_not_none = false;
        root_node.value = 0;
        root_node.depth = 0;
        root_node.children = root_node.expand_node();
        root_node.expanded=true;
        //
        minimax_counter=0;
    }

    MinimaxNode root_node;
    int token;
    Board board;
    int max_time=5;
    int max_depth=10;
    int starting_depth=2;

    Board* minimaxer(const int depth, const std::chrono::duration<double> vergangene_zeit) {
        auto start = std::chrono::high_resolution_clock::now();
        //
        std::vector<int> values;
        std::vector<MinimaxNode> best_moves;
        MinimaxNode best_move;
        int best_value = -1000000;
        std::vector<MinimaxNode>& root_node_children=root_node.children;
        Board return_board;
        //
        for (MinimaxNode& child : root_node_children){
            int eval;
            if (child.value>-90000) {
                eval=child.minimax(-1000000,1000000,false, depth);
                child.value=eval;
                std::cout<<"a ";//child wurde fertig berechnet
            }
            //
            auto now = std::chrono::high_resolution_clock::now();
            std::chrono::duration<double> vergangene_zeit2 =(now+vergangene_zeit)-start;
            if (vergangene_zeit2.count() >= max_time) {std::cout<<" NICHT FERTIG"; break;}
        }
        //
        for (MinimaxNode& child : root_node_children) {
            if (child.value>-90000) {
                values.push_back(child.value);
            }
        }
        if (values.empty()) {return nullptr;}
        for (int v : values) {if (v > best_value) {best_value = v;}}
        for (MinimaxNode& child : root_node_children) {if (child.value==best_value) {best_moves.push_back(child);}}
        //
        //output---------
        std::cout << std::endl;
        std::cout << best_value << std::endl;
        std::cout<<"COUNTER: "; std::cout<<minimax_counter<<std::endl;
        //---------------
        best_move=best_moves[generate_random_int(0, best_moves.size()-1)];
        return_board=best_move.board;
        //
        Board* ret=&return_board;
        return ret;

    }

    Board* get_move() {
        auto start = std::chrono::high_resolution_clock::now();
        //
        int depth=this->starting_depth;
        Board* move = new Board();
        while (true) {
            //break
            auto now = std::chrono::high_resolution_clock::now();
            std::chrono::duration<double> vergangene_zeit = now - start;
            if (vergangene_zeit.count() >= max_time) {break;}
            else if (depth>max_depth) {break;}
            //calculate move
            std::cout<<"---DEPTH: ";
            std::cout<<depth<<std::endl;
            //
            Board* new_move=minimaxer(depth,vergangene_zeit);
            *move=*new_move;
            if (new_move==nullptr) {return nullptr;}
            //
            for (const MinimaxNode& child : root_node.children) {std::cout<<child.value;  std::cout<<", ";}
            std::cout<<std::endl;
            //sort+depth
            //this->root_node.sort(true);
            //
            for (MinimaxNode& child : root_node.children) {std::cout<<child.value;  std::cout<<", ";}
            std::cout<<std::endl;
            if (depth>max_depth) {break;}
            depth+=1;
        }
        return move;
    }

};

//

int max_turns=10;

class Schach {
public:
Board board;
int turn;
    Schach() : turn(1) {
        board.b   = 0b0000000000000000000000000000000000000000000000001111111100000000ULL;
        board.l = 0b0000000000000000000000000000000000000000000000000000000001000010ULL;
        board.x = 0b0000000000000000000000000000000000000000000000000000000000100100ULL;
        board.t   = 0b0000000000000000000000000000000000000000000000000000000000000000ULL;
        board.q  = 0b0000000000000000000000000000000000000000000000000000000000010000ULL;
        board.k   = 0b0000000000000000000000000000000000000000000000000000000000000000ULL;

        board.y   = 0b0000000000000000000000000000000000000000000000000000000000001000ULL;
        board.z   = 0b0000000000000000000000000000000000000000000000000000000010000001ULL;
        board.f   = 0b0000000000000000000000000000000000000000000000000000000000000000ULL;

        board.B   = 0b0000000011111111000000000000000000000000000000000000000000000000ULL;
        board.L = 0b0100001000000000000000000000000000000000000000000000000000000000ULL;
        board.X = 0b0010010000000000000000000000000000000000000000000000000000000000ULL;
        board.T   = 0b0000000000000000000000000000000000000000000000000000000000000000ULL;
        board.Q  = 0b0001000000000000000000000000000000000000000000000000000000000000ULL;
        board.K   = 0b0000000000000000000000000000000000000000000000000000000000000000ULL;

        board.Y   = 0b0000100000000000000000000000000000000000000000000000000000000000ULL;
        board.Z   = 0b1000000100000000000000000000000000000000000000000000000000000000ULL;
        board.F   = 0b0000000000000000000000000000000000000000000000000000000000000000ULL;
    }

    int play() {
        int current = 1;
        while (true) {
            //-----------------------------------------
            MinimaxPlayer player_1(6, this->board);
            MinimaxPlayer player_2(-6, this->board);
            //-----------------------------------------
            std::cout<<this->turn<<std::endl;
            this->board.print_board();
            //
            Board new_move;
            Board* new_board;
            if (current==1) {
                std::cout <<"k ist am Zug"<<std::endl;
                new_board = player_1.get_move();
            }
            else if (current==2) {
                std::cout<<"K ist am Zug"<<std::endl;
                new_board = player_2.get_move();
            }
            //
            if (new_board != nullptr) {new_move = *new_board;}
            else {std::cout<<"NULLPOINTER2"<<std::endl;}
            //
            if (!(new_board==nullptr)) {this->board = new_move;}
            else {
                bool king_captured = false;
                int other;
                int this_players_token;
                //
                if(current == 1) {other = -6;}
                else {other = 6;}
                if (current == 1) {this_players_token = 6;}
                else {this_players_token = -6;}
                //
                std::vector<Board> children = this->board.generate_children(other);
                for (const Board& child : children) {
                    if (child.verloren(this_players_token)) {
                        king_captured = true;
                    }
                }
                if (!king_captured) {
                    this->board.print_board();
                    std::cout << "UNENTSCHIEDEN" << std::endl;
                    return 0;
                }
                else {
                    if (this_players_token == 6) {
                        this->board.print_board();
                        std::cout << "K HAT GEWONNEN" << std::endl;
                        return -1;
                    }
                    else {
                        this->board.print_board();
                        std::cout << "k HAT GEWONNEN" << std::endl;
                        return 1;
                    }
                }
            }
            //
            if (this->turn==max_turns) {this->board.print_board();; std::cout<<"UNENTSCHIEDEN"<<std::endl; return 0;}
            //
            if (current==1) {current = 2;}
            else {current = 1;}
            this->turn += 1;
        }
    }

private:
    
};

//

void spielen(int z) {
    std::cout<<"NEUES SPIEL"<<std::endl;
    int k_wins=0;
    int K_wins=0;
    int unentschieden=0;
    //
    for (int i=0; i<z; ++i) {
        Schach game;
        int r = game.play();
        if (r==1) {k_wins+=1;}
        else if (r==-1) {K_wins+=1;}
        else if (r==0) {unentschieden+=1;}
        std::cout<<"k: "<<k_wins<<std::endl;
        std::cout<<"K: "<<K_wins<<std::endl;
        std::cout<<"-: "<<unentschieden<<std::endl;
    }
    std::cout<<"FERTIG"<<std::endl;
}

//

int main() {
    srand(time(0)); //seed
    spielen(1);
    //test-------------------
    //Schach game;
    //game.board.print_board();
    //for (const Board& child : game.board.generate_children(-6)) {
        //child.print_board();
    //}
    //test-----------------
}

//


//MCTS bitboard
//nur schlagen ab einer gewissen tiefe
//remove_common_bits_rochade nicht nötig