


void generate_children_schlagen_WM(int y, int x, std::vector<std::vector<int>> board, int player, bool new_b) {
    if (new_b) {children_schlagen_WM.clear();}
    //
    std::vector<std::vector<int>> board_copy = board;
    //
    if (player==-2) {
        //
        for (int o=0; o<7; ++o) {
            if (y + 2 + o > 7 || x + 2 + o > 7) {break;}
            if (board_copy[y + 1 + o][x + 1 + o] < 0) {break;}
            if (board_copy[y + 1 + o][x + 1 + o] > 0) {
                if (board_copy[y + 2 + o][x + 2 + o] == 0) {
                    board_copy[y + 2 + o][x + 2 + o] = -2;
                    board_copy[y + 1 + o][x + 1 + o] = 0;
                    board_copy[y][x] = 0;
                    children_schlagen_WM.push_back(board_copy);
                    generate_children_schlagen_WM(y + 2 + o, x + 2 + o, board_copy, -2, false);
                    board_copy = board;
                    break;
                }
                else {break;}
            }
        }
        //
        for (int o=0; o<7; ++o) {
            if (y - 2 - o < 0 || x + 2 + o > 7) {break;}
            if (board_copy[y - 1 - o][x + 1 + o] < 0) {break;}
            if (board_copy[y - 1 - o][x + 1 + o] > 0) {
                if (board_copy[y - 2 - o][x + 2 + o] == 0) {
                    board_copy[y - 2 - o][x + 2 + o] = -2;
                    board_copy[y - 1 - o][x + 1 + o] = 0;
                    board_copy[y][x] = 0;
                    children_schlagen_WM.push_back(board_copy);
                    generate_children_schlagen_WM(y - 2 - o, x + 2 + o, board_copy, -2, false);
                    board_copy = board;
                    break;
                }
                else {break;}
            }
        }
        //
        for (int o=0; o<7; ++o) {
            if (y - 2 - o < 0 || x - 2 - o < 0) {break;}
            if (board_copy[y - 1 - o][x - 1 - o] < 0) {break;}
            if (board_copy[y - 1 - o][x - 1 - o] > 0) {
                if (board_copy[y - 2 - o][x - 2 - o] == 0) {
                    board_copy[y - 2 - o][x - 2 - o] = -2;
                    board_copy[y - 1 - o][x - 1 - o] = 0;
                    board_copy[y][x] = 0;
                    children_schlagen_WM.push_back(board_copy);
                    generate_children_schlagen_WM(y - 2 - o, x - 2 - o, board_copy, -2, false);
                    board_copy = board;
                    break;
                }
                else {break;}
            }
        }
        //
        for (int o=0; o<7; ++o) {
            if (y + 2 + o > 7 || x - 2 - o < 0) {break;}
            if (board_copy[y + 1 + o][x - 1 - o] < 0) {break;}
            if (board_copy[y + 1 + o][x - 1 - o] > 0) {
                if (board_copy[y + 2 + o][x - 2 - o] == 0) {
                    board_copy[y + 2 + o][x - 2 - o] = -2;
                    board_copy[y + 1 + o][x - 1 - o] = 0;
                    board_copy[y][x] = 0;
                    children_schlagen_WM.push_back(board_copy);
                    generate_children_schlagen_WM(y + 2 + o, x - 2 - o, board_copy, -2, false);
                    board_copy = board;
                    break;
                }
                else {break;}
            }
        }

    }
    //
    else if (player == 2) {
        //
        for (int o=0; o<7; ++o) {
            if (y + 2 + o > 7 || x + 2 + o > 7) {break;}
            if (board_copy[y + 1 + o][x + 1 + o] > 0) {break;}
            if (board_copy[y + 1 + o][x + 1 + o] < 0) {
                if (board_copy[y + 2 + o][x + 2 + o] == 0) {
                    board_copy[y + 2 + o][x + 2 + o] = 2;
                    board_copy[y + 1 + o][x + 1 + o] = 0;
                    board_copy[y][x] = 0;
                    children_schlagen_WM.push_back(board_copy);
                    generate_children_schlagen_WM(y + 2 + o, x + 2 + o, board_copy, 2, false);
                    board_copy = board;
                    break;
                }
                else {break;}
            }
        }
        //
        for (int o=0; o<7; ++o) {
            if (y - 2 - o < 0 || x + 2 + o > 7) {break;}
            if (board_copy[y - 1 - o][x + 1 + o] > 0) {break;}
            if (board_copy[y - 1 - o][x + 1 + o] < 0) {
                if (board_copy[y - 2 - o][x + 2 + o] == 0) {
                    board_copy[y - 2 - o][x + 2 + o] = 2;
                    board_copy[y - 1 - o][x + 1 + o] = 0;
                    board_copy[y][x] = 0;
                    children_schlagen_WM.push_back(board_copy);
                    generate_children_schlagen_WM(y - 2 - o, x + 2 + o, board_copy, 2, false);
                    board_copy = board;
                    break;
                }
                else {break;}
            }
        }
        //
        for (int o = 0; o < 7; ++o) {
            if (y - 2 - o < 0 || x - 2 - o < 0) {break;}
            if (board_copy[y - 1 - o][x - 1 - o] > 0) {break;}
            if (board_copy[y - 1 - o][x - 1 - o] < 0) {
                if (board_copy[y - 2 - o][x - 2 - o] == 0) {
                    board_copy[y - 2 - o][x - 2 - o] = 2;
                    board_copy[y - 1 - o][x - 1 - o] = 0;
                    board_copy[y][x] = 0;
                    children_schlagen_WM.push_back(board_copy);
                    generate_children_schlagen_WM(y - 2 - o, x - 2 - o, board_copy, 2, false);
                    board_copy = board;
                    break;
                }
                else {break;}
            }
        }
        //
        for (int o=0; o<7; ++o) {
            if (y + 2 + o > 7 || x - 2 - o < 0) {break;}
            if (board_copy[y + 1 + o][x - 1 - o] > 0) {break;}
            if (board_copy[y + 1 + o][x - 1 - o] < 0) {
                if (board_copy[y + 2 + o][x - 2 - o] == 0) {
                    board_copy[y + 2 + o][x - 2 - o] = 2;
                    board_copy[y + 1 + o][x - 1 - o] = 0;
                    board_copy[y][x] = 0;
                    children_schlagen_WM.push_back(board_copy);
                    generate_children_schlagen_WM(y + 2 + o, x - 2 - o, board_copy, 2, false);
                    board_copy = board;
                    break;
                }
                else {break;}
            }
        }
    }
    //
    std::reverse(children_schlagen_WM.begin(), children_schlagen_WM.end());
}

std::list<std::vector<std::vector<int>>> generate_children_WM(int y, int x, std::vector<std::vector<int>> board, int player) {
    std::list<std::vector<std::vector<int>>> childrenWM1;
    std::list<std::vector<std::vector<int>>> childrenWM2;
    std::vector<std::vector<int>> board_copy = board;
    bool schlagen = false;

    if (player == -2) {
        for (int o=0; o<7; ++o) {
            schlagen = false;
            if (y + 1 + o > 7 || x + 1 + o > 7) {break;}
            if (board_copy[y + 1 + o][x+ 1 + o] < 0) {break;}
            if (board_copy[y + 1 + o][x + 1 + o] > 0) {
                if (!(y + 2 + o > 7) && !(x + 2 + o > 7)) {schlagen = true;}
            }
            if (board_copy[y + 1 + o][x + 1 + o]==0) {
                board_copy[y + 1 + o][x + 1 + o]=-2;
                board_copy[y][x] = 0;
                childrenWM2.push_back(board_copy);
                board_copy = board;
            }
            if (schlagen) {
                if (board_copy[y + 2 + o][x + 2 + o]==0) {
                    board_copy[y + 2 + o][x + 2 + o]=-2;
                    board_copy[y][x] = 0;
                    board_copy[y + 1 + o][x + 1 + o]=0;
                    childrenWM1.push_back(board_copy);
                    //
                    children_schlagen_WM.clear();
                    generate_children_schlagen_WM(y + 2 + o, x + 2 + o, board_copy, -2, true);
                    std::list<std::vector<std::vector<int>>> r_children = children_schlagen_WM;
                    childrenWM1.insert(childrenWM1.end(), r_children.begin(), r_children.end());
                    board_copy = board;
                    schlagen = false;
                    break;
                }
                else {break;}
            }
        }
        //
        for (int o=0; o<7; ++o) {
            schlagen = false;
            if (y + 1 + o > 7 || x - 1 - o < 0) {break;}
            if (board_copy[y + 1 + o][x - 1 - o] < 0) {break;}
            if (board_copy[y + 1 + o][x - 1 - o] > 0) {
                if (!(y + 2 + o > 7) && !(x - 2 - o < 0)) {schlagen = true;}
            }
            if (board_copy[y + 1 + o][x - 1 - o]==0) {
                board_copy[y + 1 + o][x - 1 - o]=-2;
                board_copy[y][x] = 0;
                childrenWM2.push_back(board_copy);
                board_copy = board;
            }
            if (schlagen) {
                if (board_copy[y + 2 + o][x - 2 - o]==0) {
                    board_copy[y + 2 + o][x - 2 - o]=-2;
                    board_copy[y][x] = 0;
                    board_copy[y + 1 + o][x - 1 - o]=0;
                    childrenWM1.push_back(board_copy);
                    //
                    children_schlagen_WM.clear();
                    generate_children_schlagen_WM(y + 2 + o, x - 2 - o, board_copy, -2, true);
                    std::list<std::vector<std::vector<int>>> r_children = children_schlagen_WM;
                    childrenWM1.insert(childrenWM1.end(), r_children.begin(), r_children.end());
                    board_copy = board;
                    schlagen = false;
                    break;
                }
                else {break;}
            }
        }
        //
        for (int o=0; o<7; ++o) {
            schlagen = false;
            if (y - 1 - o < 0 || x - 1 - o < 0) {break;}
            if (board_copy[y - 1 - o][x - 1 - o] < 0) {break;}
            if (board_copy[y - 1 - o][x - 1 - o] > 0) {
                if (!(y - 2 - o < 0) && !(x - 2 - o < 0)) {schlagen = true;}
            }
            if (board_copy[y - 1 - o][x - 1 - o]==0) {
                board_copy[y - 1 - o][x - 1 - o]=-2;
                board_copy[y][x] = 0;
                childrenWM2.push_back(board_copy);
                board_copy = board;
            }
            if (schlagen) {
                if (board_copy[y - 2 - o][x - 2 - o]==0) {
                    board_copy[y - 2 - o][x - 2 - o]=-2;
                    board_copy[y][x] = 0;
                    board_copy[y - 1 - o][x - 1 - o]=0;
                    childrenWM1.push_back(board_copy);
                    //
                    children_schlagen_WM.clear();
                    generate_children_schlagen_WM(y - 2 - o, x - 2 - o, board_copy, -2, true);
                    std::list<std::vector<std::vector<int>>> r_children = children_schlagen_WM;
                    childrenWM1.insert(childrenWM1.end(), r_children.begin(), r_children.end());
                    board_copy = board;
                    schlagen = false;
                    break;
                }
                else {break;}
            }
        }
        //
        for (int o=0; o<7; ++o) {
            schlagen = false;
            if (y - 1 - o < 0 || x + 1 + o > 7) {break;}
            if (board_copy[y - 1 - o][x + 1 + o] < 0) {break;}
            if (board_copy[y - 1 - o][x + 1 + o] > 0) {
                if (!(y - 2 - o < 0) && !(x + 2 + o > 7)) {schlagen = true;}
            }
            if (board_copy[y - 1 - o][x + 1 + o]==0) {
                board_copy[y - 1 - o][x + 1 + o]=-2;
                board_copy[y][x] = 0;
                childrenWM2.push_back(board_copy);
                board_copy = board;
            }
            if (schlagen) {
                if (board_copy[y - 2 - o][x + 2 + o]==0) {
                    board_copy[y - 2 - o][x + 2 + o]=-2;
                    board_copy[y][x] = 0;
                    board_copy[y - 1 - o][x + 1 + o]=0;
                    childrenWM1.push_back(board_copy);
                    //
                    children_schlagen_WM.clear();
                    generate_children_schlagen_WM(y - 2 - o, x + 2 + o, board_copy,-2, true);
                    std::list<std::vector<std::vector<int>>> r_children = children_schlagen_WM;
                    childrenWM1.insert(childrenWM1.end(), r_children.begin(), r_children.end());
                    board_copy = board;
                    schlagen = false;
                    break;
                }
                else {break;}
            }
        }
    }
    //
    else if (player == 2) {
        //
        for (int o = 0; o < 7; ++o) {
            schlagen = false;
            if (y + 1 + o > 7 || x + 1 + o > 7) {break;}
            if (board_copy[y + 1 + o][x + 1 + o] > 0) {break;}
            if (board_copy[y + 1 + o][x + 1 + o] < 0) {
                if (!(y + 2 + o > 7) && !(x + 2 + o > 7)) {schlagen = true;}
            }
            if (board_copy[y + 1 + o][x + 1 + o] == 0) {
                board_copy[y + 1 + o][x + 1 + o] = 2;
                board_copy[y][x] = 0;
                childrenWM2.push_back(board_copy);
                board_copy = board;
            }
            if (schlagen) {
                if (board_copy[y + 2 + o][x + 2 + o] == 0) {
                    board_copy[y + 2 + o][x + 2 + o] = 2;
                    board_copy[y][x] = 0;
                    board_copy[y + 1 + o][x + 1 + o] = 0;
                    childrenWM1.push_back(board_copy);
                    //
                    children_schlagen_WM.clear();
                    generate_children_schlagen_WM(y + 2 + o, x + 2 + o, board_copy, 2, true);
                    std::list<std::vector<std::vector<int>>> r_children = children_schlagen_WM;
                    childrenWM1.insert(childrenWM1.end(), r_children.begin(), r_children.end());
                    board_copy = board;
                    schlagen = false;
                    break;
                }
                else {break;}
            }
        }
        //
        for (int o = 0; o < 7; ++o) {
            schlagen = false;
            if (y + 1 + o > 7 || x - 1 - o < 0) {break;}
            if (board_copy[y + 1 + o][x - 1 - o] > 0) {break;}
            if (board_copy[y + 1 + o][x - 1 - o] < 0) {
                if (!(y + 2 + o > 7) && !(x - 2 - o < 0)) {schlagen = true;}
            }
            if (board_copy[y + 1 + o][x - 1 - o] == 0) {
                board_copy[y + 1 + o][x - 1 - o] = 2;
                board_copy[y][x] = 0;
                childrenWM2.push_back(board_copy);
                board_copy = board;
            }
            if (schlagen) {
                if (board_copy[y + 2 + o][x - 2 - o] == 0) {
                    board_copy[y + 2 + o][x - 2 - o] = 2;
                    board_copy[y][x] = 0;
                    board_copy[y + 1 + o][x - 1 - o] = 0;
                    childrenWM1.push_back(board_copy);
                    //
                    children_schlagen_WM.clear();
                    generate_children_schlagen_WM(y + 2 + o, x - 2 - o, board_copy, 2, true);
                    std::list<std::vector<std::vector<int>>> r_children = children_schlagen_WM;
                    childrenWM1.insert(childrenWM1.end(), r_children.begin(), r_children.end());
                    board_copy = board;
                    schlagen = false;
                    break;
                }
                else {break;}
            }
        }
        //
        for (int o = 0; o < 7; ++o) {
            schlagen = false;
            if (y - 1 - o < 0 || x - 1 - o < 0) {break;}
            if (board_copy[y - 1 - o][x - 1 - o] > 0) {break;}
            if (board_copy[y - 1 - o][x - 1 - o] < 0) {
                if (!(y - 2 - o < 0) && !(x - 2 - o < 0)) {schlagen = true;}
            }
            if (board_copy[y - 1 - o][x - 1 - o] == 0) {
                board_copy[y - 1 - o][x - 1 - o] = 2;
                board_copy[y][x] = 0;
                childrenWM2.push_back(board_copy);
                board_copy = board;
            }
            if (schlagen) {
                if (board_copy[y - 2 - o][x - 2 - o] == 0) {
                    board_copy[y - 2 - o][x - 2 - o] = 2;
                    board_copy[y][x] = 0;
                    board_copy[y - 1 - o][x - 1 - o] = 0;
                    childrenWM1.push_back(board_copy);
                    //
                    children_schlagen_WM.clear();
                    generate_children_schlagen_WM(y - 2 - o, x - 2 - o, board_copy, 2, true);
                    std::list<std::vector<std::vector<int>>> r_children = children_schlagen_WM;
                    childrenWM1.insert(childrenWM1.end(), r_children.begin(), r_children.end());
                    board_copy = board;
                    schlagen = false;
                    break;
                }
                else {break;}
            }
        }
        //
        for (int o = 0; o < 7; ++o) {
            schlagen = false;
            if (y - 1 - o < 0 || x + 1 + o > 7) {break;}
            if (board_copy[y - 1 - o][x + 1 + o] > 0) {break;}
            if (board_copy[y - 1 - o][x + 1 + o] < 0) {
                if (!(y - 2 - o < 0) && !(x + 2 + o > 7)) {schlagen = true;}
            }
            if (board_copy[y - 1 - o][x + 1 + o] == 0) {
                board_copy[y - 1 - o][x + 1 + o] = 2;
                board_copy[y][x] = 0;
                childrenWM2.push_back(board_copy);
                board_copy = board;
            }
            if (schlagen) {
                if (board_copy[y - 2 - o][x + 2 + o] == 0) {
                    board_copy[y - 2 - o][x + 2 + o] = 2;
                    board_copy[y][x] = 0;
                    board_copy[y - 1 - o][x + 1 + o] = 0;
                    childrenWM1.push_back(board_copy);
                    //
                    children_schlagen_WM.clear();
                    generate_children_schlagen_WM(y - 2 - o, x + 2 + o, board_copy, 2, true);
                    std::list<std::vector<std::vector<int>>> r_children = children_schlagen_WM;
                    childrenWM1.insert(childrenWM1.end(), r_children.begin(), r_children.end());
                    board_copy = board;
                    schlagen = false;
                    break;
                }
                else {break;}
            }
        }
    }
    //
    childrenWM1.insert(childrenWM1.end(), childrenWM2.begin(), childrenWM2.end());
    return childrenWM1;
}
