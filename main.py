#######################################################################################################################
# IMPORTS
#######################################################################################################################

import welcome
import functions
import game

#######################################################################################################################
# PROGRAM
#######################################################################################################################

welcome.welcome_dialog()
functions.check_nickname_duplicate()
if functions.bool_nickname_duplicate:
    functions.save_nickname()
functions.create_backup_nicknames()
game.game_loop()
functions.output_score()
functions.insert_score()
functions.output_highscore()

exit()
