# dict.py

def iterate_json_string(myDictionary):
    for k, v in myDictionary.items():
        print("key is " + str(type(k)) + ", value is " + str(type(v)))
        if isinstance(v, dict):
            iterate_json_string(v)
        else:
            print("{key} : {value}".format(k, v))
            if (isinstance(v, list)):
                for vv in v:
                    if (isinstance(vv, dict)):
                        iterate_json_string(vv)
