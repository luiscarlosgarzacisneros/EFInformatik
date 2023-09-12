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


    Board() : {}

    void print_bitboard(uint64_t bitboard) {
        for (int rank = 7; rank >= 0; --rank) {
            for (int file = 0; file < 8; ++file) {
                int square = rank * 8 + file;
                uint64_t mask = 1ULL << square;
                if (bitboard & mask) { std::cout << "1 "; }
                else { std::cout << "0 "; }
            }
            std::cout << std::endl;
        }
    }
};



main() {
    uint64_t w_pawn   = 0b0000000000000000000000000000000000000000000000001111111100000000ULL;
    uint64_t w_knight = 0b0000000000000000000000000000000000000000000000000000000001000010ULL;
    uint64_t w_bishop = 0b0000000000000000000000000000000000000000000000000000000000100100ULL;
    uint64_t w_rook   = 0b0000000000000000000000000000000000000000000000000000000000000000ULL;
    uint64_t w_queen  = 0b0000000000000000000000000000000000000000000000000000000000001000ULL;
    uint64_t w_king   = 0b0000000000000000000000000000000000000000000000000000000000000000ULL;

    uint64_t w_king_nm   = 0b0000000000000000000000000000000000000000000000000000000000010000ULL;
    uint64_t w_rook_nm   = 0b0000000000000000000000000000000000000000000000000000000010000001ULL;
    uint64_t w_pawn_ep   = 0b0000000000000000000000000000000000000000000000000000000000000000ULL;

    uint64_t b_pawn   = 0b0000000011111111000000000000000000000000000000000000000000000000ULL;
    uint64_t b_knight = 0b0100001000000000000000000000000000000000000000000000000000000000ULL;
    uint64_t b_bishop = 0b0010010000000000000000000000000000000000000000000000000000000000ULL;
    uint64_t b_rook   = 0b0000000000000000000000000000000000000000000000000000000000000000ULL;
    uint64_t b_queen  = 0b0001000000000000000000000000000000000000000000000000000000000000ULL;
    uint64_t b_king   = 0b0000000000000000000000000000000000000000000000000000000000000000ULL;

    uint64_t b_king_nm   = 0b0000100000000000000000000000000000000000000000000000000000000000ULL;
    uint64_t b_rook_nm   = 0b1000000100000000000000000000000000000000000000000000000000000000ULL;
    uint64_t b_pawn_ep   = 0b0000000000000000000000000000000000000000000000000000000000000000ULL;

    uint64_t white_pieces = w_pawn|w_knight|w_bishop|w_rook|w_queen|w_king|w_king_nm|w_rook_nm|w_pawn_ep;
    uint64_t black_pieces = b_pawn|b_knight|b_bishop|b_rook|b_queen|b_king|b_king_nm|b_rook_nm|b_pawn_ep;

    print_bitboard(white_pieces);
    print_bitboard(black_pieces);

}