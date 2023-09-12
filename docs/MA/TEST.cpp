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


main() {
    std::vector<uint64_t> board;
    uint64_t w_pawn   = 0b0000000000000000000000000000000000000000000000001111111100000000ULL;
    uint64_t w_knight = 0b0000000000000000000000000000000000000000000000000000000001000010ULL;
    uint64_t w_bishop = 0b0000000000000000000000000000000000000000000000000000000000100100ULL;
    uint64_t w_rook   = 0b0000000000000000000000000000000000000000000000000000000010000001ULL;
    uint64_t w_queen  = 0b0000000000000000000000000000000000000000000000000000000000001000ULL;
    uint64_t w_king   = 0b0000000000000000000000000000000000000000000000000000000000010000ULL;

    uint64_t b_pawn   = 0b0000000011111111000000000000000000000000000000000000000000000000ULL;
    uint64_t b_knight = 0b0100001000000000000000000000000000000000000000000000000000000000ULL;
    uint64_t b_bishop = 0b0010010000000000000000000000000000000000000000000000000000000000ULL;
    uint64_t b_rook   = 0b1000000100000000000000000000000000000000000000000000000000000000ULL;
    uint64_t b_queen  = 0b0001000000000000000000000000000000000000000000000000000000000000ULL;
    uint64_t b_king   = 0b0000100000000000000000000000000000000000000000000000000000000000ULL;

    uint64_t white_pieces = w_pawn | w_knight | w_bishop | w_rook | w_queen | w_king;

    // Print the combined bitboard
    std::cout << "Combined bitboard for white pieces:" << std::endl;
    for (int rank = 7; rank >= 0; --rank) {
        for (int file = 0; file < 8; ++file) {
            int square = rank * 8 + file;
            uint64_t mask = 1ULL << square;
            char piece_char = (white_pieces & mask) ? '1' : '0';
            std::cout << piece_char << " ";
        }
        std::cout << std::endl;
    }

}