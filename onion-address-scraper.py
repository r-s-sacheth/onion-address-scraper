import re
import os
import requests

DISPLAY_ADDRESS = 10

def get_address(user_inp):
    if " " in user_inp:
        user_inp=user_inp.replace(" ","_")
    filename=f"{user_inp}.txt"
    if "_" in user_inp:
        user_inp=user_inp.replace("_","+")

    # Make a request to the Ahmia search engine
    site=requests.get(f"https://ahmia.fi/search/?q={user_inp}")
    webpage=site.text
    

    # Use regex to find Onion addresses in the webpage
    onion_address=re.findall("\w+\.onion",webpage)

    # Remove duplicates from the list of onion addresses
    onion_address=list(dict.fromkeys(onion_address))

    # Check if the file already exists
    if not os.path.exists(filename):
        with open(filename,'w') as file:
            for idx,address in enumerate(onion_address,1):
                if idx<=DISPLAY_ADDRESS:
                    print(f"{idx}) {address}\n")
                file.write(f"{idx}) {address}\n")
            print(f"\nSaved to {filename}\n")
    
    
    # If the file exists, inform the user and create a new file
    else:
        print(f"{filename} already exits, creating new file....")
        user_inp=f"{user_inp} "
        get_address(user_inp)


user_inp=input("Enter a Keyword: ")
get_address(user_inp)
