import random


class Player:
    """Represents a player object. Used for the Connectfour class create_player method so that it could easily access
    the data members this class provides."""

    def __init__(self):
        pass


class Connectfour:
    """Class that represents the Connectfour game, played by 2 players. Uses Player class so each player's data members can
    be accessed. End result of class determines who won the game or if there was a tie. Also provides information on the
    current state of the game, taking into account its rules."""

    def __init__(self):
        self._connect_player_dict = {}
        self._whos_turn = 1
        self._num_turns = 1
        self._end = False
        self._board_checkers_list_1 = [None, None, None, None, None, None, None,
                                       None, None, None, None, None, None, None,
                                       None, None, None, None, None, None, None,
                                       None, None, None, None, None, None, None,
                                       None, None, None, None, None, None, None,
                                       None, None, None, None, None, None, None,
                                       None, None, None, None, None, None, None]
        self._board_checkers_list_2 = [None, None, None, None, None, None, None,
                                       None, None, None, None, None, None, None,
                                       None, None, None, None, None, None, None,
                                       None, None, None, None, None, None, None,
                                       None, None, None, None, None, None, None,
                                       None, None, None, None, None, None, None,
                                       None, None, None, None, None, None, None]

    def create_player(self, player_name):
        """Adds a player's name and its object to the player dictionary"""
        if player_name not in self._connect_player_dict:
            if len(self._connect_player_dict) < 3:
                self._connect_player_dict[player_name] = Player()
        return self._connect_player_dict[player_name]

    def play_game(self):
        """Uses helper methods for playing games for either player to play game"""
        if self._num_turns > 42:
            print("Game board has been filled.")
            print()
            return
        if self._end is True:
            print("Game is over.")
            print()
            return
        if self._rolls == 1:
            self.first_turn()
        # otherwise, play rest of game as normal, alternating turns
        else:
            if self._turn == 1:
                self.play_player_1()
            else:
                self.play_player_2()
        self._num_turns += 1

    def first_turn(self):
        """Handles the first turn at random, then plays the game as normal"""
        val = random.randint(1, 2)
        if val == 1:
            self.play_player_1()
        else:
            self.play_player_2()

    def play_player_1(self):
        """Uses a variety of helper methods to help the user pick the correct location and determine victory"""
        # gives an idea of where user should place checker
        self.print_board_1()
        self.print_positions_1()
        # makes sure that user chose a correct checker location
        position_1 = self.validate_position_1()
        # places player one's checker in that spot
        self._board_checkers_list_1[position_1] = True
        # places the same checker using player two's version of the board
        position_2 = self.find_other_player_position(position_1)
        self._board_checkers_list_2[position_2] = True
        # determines if player one has won either vertically, horizontally, or diagonally after each checker placed
        self._end = self.check_horiz(position_1)
        if self._end is True:
            return ""
        self._end = self.check_vert(position_1)
        if self._end is True:
            return ""
        self._end = self.check_diag(position_1)
        if self._end is True:
            return ""
        # if user has not won yet
        print("Continue playing.")
        print()
        print()
        print()
        # change turns
        self._whos_turn = 2

    def play_player_2(self):
        """Uses a variety of helper methods to help the user pick the correct location and determine victory.
        Uses same process as player 1 method."""
        self.print_board_2()
        self.print_positions_2()
        position_2 = self.validate_position_2()
        self._board_checkers_list_2[position_2] = False
        position_1 = self.find_other_player_position(position_2)
        self._board_checkers_list_1[position_1] = False
        self._end = self.check_horiz(position_1)
        if self._end is True:
            return ""
        self._end = self.check_vert(position_1)
        if self._end is True:
            return ""
        self._end = self.check_diag(position_1)
        if self._end is True:
            return ""
        print("Continue playing.")
        print()
        print()
        print()
        self._whos_turn = 1

    def print_board_1(self):
        """Prints the board as it would appear by slicing to look like a Connect 4 board to help player 1 choose."""
        print("Here is player 1's view of the board:")
        print(self._board_checkers_list_1[0:7])
        print(self._board_checkers_list_1[7:14])
        print(self._board_checkers_list_1[14:21])
        print(self._board_checkers_list_1[21:28])
        print(self._board_checkers_list_1[28:35])
        print(self._board_checkers_list_1[35:42])
        print()

    def print_board_2(self):
        """Prints the board as it would appear by slicing to look like a Connect 4 board to help player 2 choose."""
        print("Here is player 2's view of the board:")
        print(self._board_checkers_list_2[0:7])
        print(self._board_checkers_list_2[7:14])
        print(self._board_checkers_list_2[14:21])
        print(self._board_checkers_list_2[21:28])
        print(self._board_checkers_list_2[28:35])
        print(self._board_checkers_list_2[35:42])
        print()

    def print_positions_1(self):
        """Helps player 1 choose what number position to place their checker. Slices to create connect four board."""
        board_postions_list_1 = [" 0", " 1", " 2", " 3", " 4", " 5", " 6",
                                 " 7", " 8", " 9", "10", "11", "12", "13",
                                 "14", "15", "16", "17", "18", "19", "20",
                                 "21", "22", "23", "24", "25", "26", "27",
                                 "28", "29", "30", "31", "32", "33", "34",
                                 "35", "36", "37", "38", "39", "40", "41"]
        print("Here is player 1's positions of the board:")
        print(board_postions_list_1[0:7])
        print(board_postions_list_1[7:14])
        print(board_postions_list_1[14:21])
        print(board_postions_list_1[21:28])
        print(board_postions_list_1[28:35])
        print(board_postions_list_1[35:42])
        print()

    def print_positions_2(self):
        """Helps player 2 choose what number position to place their checker. Slices to create connect four board."""
        board_postions_list_2 = [" 6", " 5", " 4", " 3", " 2", " 1", " 0",
                                 "13", "12", "11", "10", " 9", " 8", " 7",
                                 "20", "19", "18", "17", "16", "15", "14",
                                 "27", "26", "25", "24", "23", "22", "21",
                                 "34", "33", "32", "31", "30", "29", "28",
                                 "41", "40", "39", "38", "37", "36", "35"]
        print("Here is player 2's positions of the board:")
        print(board_postions_list_2[0:7])
        print(board_postions_list_2[7:14])
        print(board_postions_list_2[14:21])
        print(board_postions_list_2[21:28])
        print(board_postions_list_2[28:35])
        print(board_postions_list_2[35:42])
        print()

    def validate_position_1(self):
        """Determines if the position player 1 choice was valid, checking multiple possible inputs."""
        print("Choose your position to place your checker. Type just the number and choose a None spot either above another checker or on the bottom row if available.")
        valid_position = False
        while valid_position is False:
            try:
                position = int(input(
                    "What position would you like to place your checker? (True respesents your checkers) "))
            except ValueError:
                print("Please enter an integer number for your position")
                print("")
            else:
                if position < 0 or position > 41:
                    print("Please choose a checker within the range of positions.")
                    print()
                elif self._board_checkers_list_1[position] != None:
                    print("Please choose an empty position.")
                    print()
                elif self._board_checkers_list_1[position + 7] == None and position + 7 < 42:
                    print("Please choose a position above a checker or on the bottom row.")
                    print()
                # valid entry
                else:
                    valid_position = True
        return position

    def validate_position_2(self):
        """Determines if the position player 2 choice was valid, checking multiple possible inputs."""
        print("Choose your position to place your checker. Type just the number and choose a None spot either above another checker or on the bottom row if available.")
        valid_position = False
        while valid_position is False:
            try:
                position = int(input(
                    "What position would you like to place your checker? (False respesents your checkers) "))
            except ValueError:
                print("Please enter an integer number for your position")
                print("")
            else:
                position = self.find_other_player_position(position)
                if position < 0 or position > 41:
                    print("Please choose a checker within the range of positions.")
                    print()
                elif self._board_checkers_list_2[position] != None:
                    print("Please choose an empty position.")
                    print()
                elif self._board_checkers_list_2[position + 7] == None and position + 7 < 42:
                    print("Please choose a position above a checker or on the bottom row.")
                    print()
                # valid entry
                else:
                    valid_position = True
        return position

    def find_other_player_position(self, position):
        """Finds the opposite player's position to place checker on that player's board"""
        # provides a mirror image of the board positions
        if position % 7 == 0:
            position += 6
        elif position % 7 == 1:
            position += 4
        elif position % 7 == 2:
            position += 2
        elif position % 7 == 4:
            position -= 2
        elif position % 7 == 5:
            position -= 4
        elif position % 7 == 6:
            position -= 6
        else:
            return position
        return position

    def check_horiz(self, position):
        """Determines if the player won horizontally"""
        # start with the original checkeras the first count
        horiz_count = 1
        # check left
        horiz_position = position - 1
        if self._whos_turn == 1:
            if horiz_position >= 0:
                while self._board_checkers_list_1[horiz_position] is True:
                    horiz_count += 1
                    horiz_position -= 1
                    if horiz_count == 4:
                        print("Congratulations Player 1! You have won horizontally!")
                        # print final board
                        print(self.print_board_1())
                        return True
                    # avoids wrap around to higher row
                    if horiz_position % 7 == 6:
                        break
            # check right
            horiz_position = position + 1
            if horiz_position <= 41:
                while self._board_checkers_list_1[horiz_position] is True:
                    horiz_count += 1
                    horiz_position += 1
                    if horiz_count == 4:
                        print("Congratulations Player 1! You have won horizontally!")
                        print(self.print_board_1())
                        return True
                    # avoid wrap around
                    if horiz_position % 7 == 0:
                        break
        # check for player two if its thier turn
        else:
            if horiz_position >= 0:
                while self._board_checkers_list_1[horiz_position] is False:
                    horiz_count += 1
                    horiz_position -= 1
                    if horiz_count == 4:
                        print("Congratulations Player 2! You have won horizontally!")
                        print(self.print_board_2())
                        return True
                    if horiz_position % 7 == 6:
                        break
            horiz_position = position + 1
            if horiz_position <= 41:
                while self._board_checkers_list_1[horiz_position] is False:
                    horiz_count += 1
                    horiz_position += 1
                    if horiz_count == 4:
                        print("Congratulations Player 2! You have won horizontally!")
                        print(self.print_board_2())
                        return True
                    if horiz_position % 7 == 0:
                        break
        return False

    def check_vert(self, position):
        """Determines if the player won vertically"""
        vert_count = 1
        vert_position = position - 7
        if self._whos_turn == 1:
            if vert_position >= 0:
                # check up
                while self._board_checkers_list_1[vert_position] is True:
                    vert_count += 1
                    vert_position -= 7
                    if vert_count == 4:
                        print("Congratulations Player 1! You have won vertically!")
                        print(self.print_board_1())
                        return True
                    if vert_position < 0:
                        break
            vert_position = position + 7
            if vert_position <= 41:
                # check down
                while self._board_checkers_list_1[vert_position] is True:
                    vert_count += 1
                    vert_position += 7
                    if vert_count == 4:
                        print("Congratulations Player 1! You have won vertically!")
                        print(self.print_board_1())
                        return True
                    if vert_position > 41:
                        break
        else:
            if vert_position >= 0:
                while self._board_checkers_list_1[vert_position] is False:
                    vert_count += 1
                    vert_position -= 7
                    if vert_count == 4:
                        print("Congratulations Player 2! You have won vertically!")
                        print(self.print_board_2())
                        return True
                    if vert_position < 0:
                        break
            vert_position = position + 7
            if vert_position <= 41:
                while self._board_checkers_list_1[vert_position] is False:
                    vert_count += 1
                    vert_position += 7
                    if vert_count == 4:
                        print("Congratulations Player 2! You have won vertically!")
                        print(self.print_board_2())
                        return True
                    if vert_position > 41:
                        break
        return False

    def check_diag(self, position):
        """Determines if the player won diagonally"""
        diag_count = 1
        diag_position = position - 8
        # checks both types of diagonals, which require two sets of two while loops for each player
        if self._whos_turn == 1:
            if diag_position >= 0:
                while self._board_checkers_list_1[diag_position] is True:
                    diag_count += 1
                    diag_position -= 8
                    if diag_count == 4:
                        print("Congratulations Player 1! You have won diagonally!")
                        print(self.print_board_1())
                        return True
                    if diag_position < 0:
                        break
            diag_position = position + 8
            if diag_position <= 41:
                while self._board_checkers_list_1[diag_position] is True:
                    diag_count += 1
                    diag_position += 8
                    if diag_count == 4:
                        print("Congratulations Player 1! You have won diagonally!")
                        print(self.print_board_1())
                        return True
                    if diag_position > 41:
                        break
            diag_count = 1
            diag_position = position + 6
            if diag_position <= 41:
                while self._board_checkers_list_1[diag_position] is True:
                    diag_count += 1
                    diag_position += 6
                    if diag_count == 4:
                        print("Congratulations Player 1! You have won diagonally!")
                        print(self.print_board_1())
                        return True
                    if diag_position > 41:
                        break
            diag_position = position - 6
            if diag_position >= 0:
                while self._board_checkers_list_1[diag_position] is True:
                    diag_count += 1
                    diag_position -= 6
                    if diag_count == 4:
                        print("Congratulations Player 1! You have won diagonally!")
                        print(self.print_board_1())
                        return True
                    if diag_position < 0:
                        break
        else:
            if diag_position >= 0:
                while self._board_checkers_list_1[diag_position] is False:
                    diag_count += 1
                    diag_position -= 8
                    if diag_count == 4:
                        print("Congratulations Player 2! You have won diagonally!")
                        print(self.print_board_2())
                        return True
                    if diag_position < 0:
                        break
            diag_position = position + 8
            if diag_position <= 41:
                while self._board_checkers_list_1[diag_position] is False:
                    diag_count += 1
                    diag_position += 8
                    if diag_count == 4:
                        print("Congratulations Player 2! You have won diagonally!")
                        print(self.print_board_2())
                        return True
                    if diag_position > 41:
                        break
            diag_count = 1
            diag_position = position + 6
            if diag_position <= 41:
                while self._board_checkers_list_1[diag_position] is False:
                    diag_count += 1
                    diag_position += 6
                    if diag_count == 4:
                        print("Congratulations Player 2! You have won diagonally!")
                        print(self.print_board_2())
                        return True
                    if diag_position > 41:
                        break
            diag_position = position - 6
            if diag_position >= 0:
                while self._board_checkers_list_1[diag_position] is False:
                    diag_count += 1
                    diag_position -= 6
                    if diag_count == 4:
                        print("Congratulations Player 2! You have won diagonally!")
                        print(self.print_board_2())
                        return True
                    if diag_position < 0:
                        break
        return False

# the max nmber of turns that can be played
Game = Connectfour()
Game.play_game()
Game.play_game()
Game.play_game()
Game.play_game()
Game.play_game()
Game.play_game()
Game.play_game()
Game.play_game()
Game.play_game()
Game.play_game()
Game.play_game()
Game.play_game()
Game.play_game()
Game.play_game()
Game.play_game()
Game.play_game()
Game.play_game()
Game.play_game()
Game.play_game()
Game.play_game()
Game.play_game()
Game.play_game()
Game.play_game()
Game.play_game()
Game.play_game()
Game.play_game()
Game.play_game()
Game.play_game()
Game.play_game()
Game.play_game()
Game.play_game()
Game.play_game()
Game.play_game()
Game.play_game()
Game.play_game()
Game.play_game()
Game.play_game()
Game.play_game()
Game.play_game()
Game.play_game()
Game.play_game()
Game.play_game()
