#######################################################################################################################
# IMPORTS
#######################################################################################################################

import datetime
import welcome

#######################################################################################################################
# VARIABLES
#######################################################################################################################

system_date = datetime.date.today()
system_time = datetime.datetime.now()
time = system_time.strftime("%H:%M")

output_time = ['[TIME: ' + str(system_date) + ' | ' + str(time) + ']']

nickname_time = ['[TIME: ' + str(system_date) + ' | ' + str(time) + ']']
log_nickname = ['[TIME: ' + str(system_date) + ' | ' + str(time) + ']']

backup_time = ['[TIME: ' + str(system_date) + ' | ' + str(time) + ']']

highscore_time = ['[TIME: ' + str(system_date) + ' | ' + str(time) + ']']

output_backup = '[BACKUP]'
output_nickname = '[NEW NICKNAME]'

bool_backup = False

backup_done = 'SUCCESS'
backup_fail = 'NO NEED'

nickname = welcome.nickname

#######################################################################################################################
# CSV-DATA
#######################################################################################################################

csv_nicknames = "nicknames.csv"
csv_highscore = "highscore.csv"
csv_logfile = "logfile.csv"
csv_nicknames_backup = "nicknames_backup.csv"
