#!/usr/bin/python3
import os
import sys
#-----------------------------------------------------
# give the searched word here in lowercase(!):
if len(sys.argv) > 0:
    searchfor = sys.argv[1]
else:
    searchfor = "real_time"
# give the aimed directory here:
searchdir = "/media/maxime/Data/framework/newTest"
#-----------------------------------------------------
wordsize = len(searchfor)
unreadable = []
print("\nFound matches:")
for root, dirs, files in os.walk(searchdir, topdown=True):
    for name in files:
        file_subject = root+"/"+name
        if not name.endswith("~") and not "migrations" in root:  
            try:
                with open(file_subject) as check_file:
                    words = check_file.read()
                    words_lower = words.lower()
                    found_matches_list = [i for i in range(len(words_lower)) if words_lower.startswith(searchfor, i)]
                    found_matches = [words[index:index+wordsize] for index in found_matches_list]
                    if len(found_matches) != 0:
                        print(file_subject, found_matches)
                    else:
                        pass
            except Exception:
                unreadable.append(file_subject)
if len(unreadable) != 0:
    print("\ncould not read the following files:", len(unreadable))
    #for item in unreadable:
        #print("unreadable:", item)
