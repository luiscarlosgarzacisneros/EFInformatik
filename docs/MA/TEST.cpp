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

//Xx: {{1, 1}, {-1, 1}, {1, -1}, {-1, -1}}
//Qq: {{1, 0}, {-1, 0}, {0, 1}, {0, -1}, {1, 1}, {-1, 1}, {1, -1}, {-1, -1}}
std::vector<uint64_t> gcXxQq(const uint64_t bitboard, const uint64_t this_players_pieces, const uint64_t other_players_pieces, std::vector<std::pair<int,int>> directions) {
    std::vector<uint64_t> children;
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
                        children.push_back(child);
                        break;
                    }
                    else if (is_one_at_this_index(this_players_pieces, yx_zu_index(y_new, x_new))) {break;}
                    else {
                        uint64_t child=shift_bit(bitboard, y_current, x_current, y_new, x_new);
                        children.push_back(child);
                    }
                }
                else {break;}
            }
        }
    }
    //
    return children;//für Zz:
}

//Tt: {{1, 0}, {-1, 0}, {0, 1}, {0, -1}}

//

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

    print_bitboard(root_node.b_queen);
    std::cout<<"----"<<std::endl;
    for (const auto& child : gcXxQq(root_node.b_queen, root_node.black_pieces, root_node.white_pieces, {{1, 0}, {-1, 0}, {0, 1}, {0, -1}, {1, 1}, {-1, 1}, {1, -1}, {-1, -1}})) {
        print_bitboard(child);
        std::cout<<"----"<<std::endl;
    }
    print_bitboard(root_node.b_queen);
    

}

