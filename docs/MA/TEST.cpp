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

//

std::vector<uint64_t> gcLl(int player, const uint64_t knight_bitboard, const uint64_t this_players_pieces) {
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



class Board {
public:

    uint64_t w_pawn;
    uint64_t w_knight;
    uint64_t w_bishop;
    uint64_t w_rook;
    uint64_t w_queen;
    uint64_t w_king;
    uint64_t w_king_nm;
    uint64_t w_rook_nm;
    uint64_t w_pawn_ep;
    
    uint64_t b_pawn;
    uint64_t b_knight;
    uint64_t b_bishop;
    uint64_t b_rook;
    uint64_t b_queen;
    uint64_t b_king;
    uint64_t b_king_nm;
    uint64_t b_rook_nm;
    uint64_t b_pawn_ep;

    uint64_t white_pieces;
    uint64_t black_pieces;


    Board() {}

};



main() {
    Board root_node;
    root_node.w_pawn   = 0b0000000000000000000000000000000000000000000000001111111100000000ULL;
    root_node.w_knight = 0b0000000000000000000000000000000000000000000000000000000001000010ULL;
    root_node.w_bishop = 0b0000000000000000000000000000000000000000000000000000000000100100ULL;
    root_node.w_rook   = 0b0000000000000000000000000000000000000000000000000000000000000000ULL;
    root_node.w_queen  = 0b0000000000000000000000000000000000000000000000000000000000001000ULL;
    root_node.w_king   = 0b0000000000000000000000000000000000000000000000000000000000000000ULL;

    root_node.w_king_nm   = 0b0000000000000000000000000000000000000000000000000000000000010000ULL;
    root_node.w_rook_nm   = 0b0000000000000000000000000000000000000000000000000000000010000001ULL;
    root_node.w_pawn_ep   = 0b0000000000000000000000000000000000000000000000000000000000000000ULL;

    root_node.b_pawn   = 0b0000000011111111000000000000000000000000000000000000000000000000ULL;
    root_node.b_knight = 0b0100001000000000000000000000000000000000000000000000000000000000ULL;
    root_node.b_bishop = 0b0010010000000000000000000000000000000000000000000000000000000000ULL;
    root_node.b_rook   = 0b0000000000000000000000000000000000000000000000000000000000000000ULL;
    root_node.b_queen  = 0b0001000000000000000000000000000000000000000000000000000000000000ULL;
    root_node.b_king   = 0b0000000000000000000000000000000000000000000000000000000000000000ULL;

    root_node.b_king_nm   = 0b0000100000000000000000000000000000000000000000000000000000000000ULL;
    root_node.b_rook_nm   = 0b1000000100000000000000000000000000000000000000000000000000000000ULL;
    root_node.b_pawn_ep   = 0b0000000000000000000000000000000000000000000000000000000000000000ULL;

    root_node.white_pieces  = 0b0000000000000000000000000000000000000000000000001111111111111111ULL;
    root_node.black_pieces  = 0b1111111111111111000000000000000000000000000000000000000000000000ULL;

    print_bitboard(root_node.w_knight);
    std::cout<<"----"<<std::endl;
    for (const auto& child : gcLl(2, root_node.w_knight, root_node.white_pieces)) {
        print_bitboard(child);
        std::cout<<"----"<<std::endl;
        ;
    }
    print_bitboard(root_node.w_knight);
    

}

