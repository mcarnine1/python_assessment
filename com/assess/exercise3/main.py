import csv
import datetime
import pytz

#########################################################################################
# Parses jmeter log files in CSV format
#########################################################################################

res_file_name = "Jmeter_log1.jtl"
line_count = 0


def convertDateTimeStampToPST(jmeter_date_timestamp):
    date_time = datetime.datetime.fromtimestamp(int(jmeter_date_timestamp) / 1000.0, tz=datetime.timezone.utc)
    pacific_tzinfo = pytz.timezone("US/Pacific")
    pacific_time = date_time.astimezone(pacific_tzinfo)

    return pacific_time


with open(res_file_name) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    #########################################################################################
    #  Begin looping through the jmeter log file
    #########################################################################################
    for row in csv_reader:
        if line_count >= 1:
            #########################################################################################
            #  Assign values to variables used for printing to stdout
            #########################################################################################
            time_stamp = row[0]
            label = row[2]
            response_code = row[3]
            response_message = row[4]
            failure_message = row[8]

            #########################################################################################
            #  if there are any non-successful endpoint responses recorded in the log
            #  print out the label, responseCode, responseMessage, failureMessage, timeStamp
            #########################################################################################
            if int(response_code) >= 400:
                pacific_time = convertDateTimeStampToPST(time_stamp)
                print("label: " + label)
                print("responseCode: " + response_code)
                print("responseMessage: " + response_message)
                print("failureMessage: " + failure_message)
                print("timeStamp: " + str(pacific_time))
                print("----------------------------------------------------------------------------------------")
            else:
                pass

        line_count += 1


#########################################################################################
#  Converts timeStamp to Date/Time in PST Time Zone
#########################################################################################
