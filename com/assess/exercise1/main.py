import xml.etree.ElementTree as XMLDoc
from datetime import datetime, timedelta

#########################################################################################
#  Variables used to hold XML Doc
#########################################################################################
payload_mkup = XMLDoc.parse('test_payload1.xml')
payload_mkup_root = payload_mkup.getroot()

#########################################################################################
#  Variables used to store dates for creating future date calculations
#########################################################################################
today = datetime.now()
depart_date = today
updated_doc_name = "updated_payload1.xml"

#########################################################################################
#  Loop through XML Document (test_payload1.xml) updating the 'DEPART'
#  tag with today's date
#########################################################################################
for departs in payload_mkup_root.iter('DEPART'):
    depart_date = datetime.strptime(departs.text, '%Y%m%d')

    # Perform the update to the 'DEPART' tag in memory
    departs.text = today.strftime('%Y%m%d')

#########################################################################################
#  Loop through XML Document (test_payload1.xml) updating the 'RETURN'
#  tag with today's date in addition to number of days departed
#########################################################################################
for returns in payload_mkup_root.iter('RETURN'):
    returns_date = datetime.strptime(returns.text, '%Y%m%d')
    diff = (returns_date - depart_date).days
    new_return_date = (today + timedelta(days=diff)).strftime('%Y%m%d')

    # Perform the update to the 'RETURN' tag in memory
    returns.text = new_return_date

#########################################################################################
#  Write the updated XML Document to a new file
#########################################################################################
payload_mkup.write(updated_doc_name)
