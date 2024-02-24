#######################################################################################################################
# IMPORTS
#######################################################################################################################

import csv
import files

#######################################################################################################################
# VARIABLES
#######################################################################################################################

output_time = files.output_time
bool_backup = False
bool_backup_logfile = False
trenner = "#######################################################################################################################"

#######################################################################################################################
# FUNCTIONS
#######################################################################################################################


def create_backup():
    global bool_backup, bool_backup_logfile

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

            writer.writerow(output_time)
            output_time.clear()


def save_nickname():
    global output_time, bool_backup

    with open(files.csv_nicknames, mode='a', newline='') as file:
        writer = csv.writer(file)

        files.nickname_time.append(files.welcome.nickname)

        writer.writerow(files.nickname_time)

        bool_backup = True

    with open(files.csv_logfile, mode='a', newline='') as file:
        writer = csv.writer(file)

        files.log_nickname.append(files.output_nickname)
        files.log_nickname.append(files.welcome.nickname)

        writer.writerow(files.log_nickname)
        
