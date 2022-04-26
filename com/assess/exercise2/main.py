import json


#########################################################################################
#########################################################################################
# Method: remove_element_from_json
# Arguments: 1.) json object, 2.) name of field to be removed from json
# Returns: Dict
# Testing:
#   1.) Single Elements - PASSED (Test Result: updated_test_payload_TEST1.json)
#   2.) Nested Elements - PASSED (Test Result: updated_test_payload_TEST2.json)
#########################################################################################
def remove_element_from_json(o, name):
    res = []

    #Searches for Element and Removes if found
    if isinstance(o, dict):
        for k in o:
            if k == name:
                res.append(o[k])
            r = remove_element_from_json(o[k], name)
            res.extend(r)
            if k == name:
                o.pop(k)
                break
    if isinstance(o, list):
        for k in o:
            r = remove_element_from_json(k, name)
            res.extend(r)
            if k == name:
                o.pop(k)
                break

    # Return Dict to calling method
    return payload_object


#########################################################################################
# Create and assign variables to be used for generating json object
#########################################################################################
json_file_name = "test_payload.json"
f = open(json_file_name)
payload_object = json.load(f)

#########################################################################################
#  Call to 'remove_element_from_json' method
#  Pass: 1.) json object, 2.) name of field to be removed from json
#########################################################################################
new_payload_object = remove_element_from_json(payload_object, 'retdt')

#########################################################################################
#  Write the json object to a new file
#########################################################################################
with open("updated_test_payload_TEST1.json", "w") as outfile:
    json.dump(new_payload_object, outfile, indent=2)

#########################################################################################
#  Close outfile
#########################################################################################
outfile.close()

#########################################################################################
#########################################################################################
