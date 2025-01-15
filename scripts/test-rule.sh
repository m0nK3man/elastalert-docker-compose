#!/bin/bash

# Ensure the script exits on errors
set -e

# Check if a rule file name was provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <rule_file_name>"
    exit 1
fi

# Set variables
RULES_DIR="rules"             # Directory where your rule files are stored
CONFIG_FILE="config.yaml"     # Path to your ElastAlert configuration file
RULE_FILE="$1"                # Rule file passed as an argument

# Full path to the rule file
FULL_RULE_PATH="$RULES_DIR/$RULE_FILE"

# Verify the rule file exists
if [ ! -f "$FULL_RULE_PATH" ]; then
    echo "Error: Rule file '$FULL_RULE_PATH' not found!"
    exit 1
fi

# Run the test command in the ElastAlert container
docker exec -it elastalert /usr/local/bin/elastalert-test-rule --config "$CONFIG_FILE" "$FULL_RULE_PATH"
