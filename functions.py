#######################################################################################################################
# IMPORTS
#######################################################################################################################

import csv
import files
import game
import welcome

#######################################################################################################################
# VARIABLES
#######################################################################################################################

output_time = files.output_time
bool_backup = False
bool_backup_logfile = False
bool_nickname_duplicate = False
trenner = "#######################################################################################################################"

#######################################################################################################################
# FUNCTIONS
#######################################################################################################################


def check_nickname_duplicate():
    global bool_backup, bool_backup_logfile, bool_nickname_duplicate

    with open(files.csv_nicknames, mode='r', newline='') as file:
        reader = csv.reader(file)

        for row in reader:

            if row[1].lower() == welcome.nickname.lower():
                bool_nickname_duplicate = False
                break

            else:
                bool_nickname_duplicate = True


# function for username backup
def create_backup_nicknames():
    global bool_backup, bool_backup_logfile, nickname

    if bool_backup:

        with open(files.csv_nicknames_backup, mode='a', newline='') as file2:
            writer = csv.writer(file2)

            with open(files.csv_nicknames, mode='r', newline='') as file1:
                reader = csv.reader(file1)

                writer.writerow([trenner])
                writer.writerow([' ', ' ', ' ', files.backup_time])

                for row in reader:
                    writer.writerow(row)

        if bool_backup_logfile:

            with open(files.csv_logfile, mode='a', newline='') as logfile:
                writer_log = csv.writer(logfile)

                output_time.append(files.output_backup)
                output_time.append(files.backup_done)

                writer_log.writerow(output_time)
                output_time.clear()

        bool_backup = False
        bool_backup_logfile = False

    else:

        with open(files.csv_logfile, mode='a', newline='') as logfile:
            writer = csv.writer(logfile)

            output_time.append(files.output_backup)
            output_time.append(files.backup_fail)

            info2 = str(welcome.nickname.upper() + ' HAT DAS SPIEL GESTARTET!')

            output_time.append(info2)


            writer.writerow(output_time)
            output_time.clear()


# function for saving nicknames
def save_nickname():
    global output_time, bool_backup, bool_backup_logfile

    with open(files.csv_nicknames, mode='a', newline='') as file:
        writer = csv.writer(file)

        files.nickname_time.append(files.welcome.nickname)

        writer.writerow(files.nickname_time)

        bool_backup = True
        bool_backup_logfile = True

    with open(files.csv_logfile, mode='a', newline='') as file:
        writer = csv.writer(file)

        files.log_nickname.append(files.output_nickname)
        files.log_nickname.append(files.welcome.nickname)

        writer.writerow(files.log_nickname)


def insert_score():

    with open(files.csv_highscore, mode='a', newline='') as file:
        writer = csv.writer(file)

        files.highscore_time.append(welcome.nickname)
        files.highscore_time.append(game.punkte)

        writer.writerow(files.highscore_time)


def output_score():
    print(f'\nDu hast {game.punkte} erreicht!')
    print('\n')


def output_highscore():

    with open(files.csv_highscore, mode ='r', newline='') as file:
        reader = csv.reader(file)

        counter = 0

        while counter < 10 or row == '':

            for row in reader:
                print(row)

            counter += 1
