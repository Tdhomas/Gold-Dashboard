#!/bin/bash

export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

# Create a CSV file with headers if it doesn't exist
FILE="/home/ec2-user/dashboard_project/gold.csv"
if [ ! -f "$FILE" ]; then
    echo "timestamp,price" > "$FILE"
fi

# Find the full path of the curl command
CURL_PATH=$(which curl)

# Get the current timestamp
timestamp=$(/usr/bin/date +"%Y-%m-%d %H:%M:%S")

# Fetch the HTML content from the website
html_content=$($CURL_PATH -s "https://goldrate.com")

# Extract the price from the HTML content
price=$(echo "$html_content" | grep -oP '<em class="price-value">\K[\d,]+(\.\d{2})')
# Remove commas from the price
price=${price//,/}

# Append the timestamp and price to the CSV file
echo "$timestamp,$price" >> "$FILE"
