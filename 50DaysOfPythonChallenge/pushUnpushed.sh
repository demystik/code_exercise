#!/usr/bin/bash

# My commit message
COMMIT_MESSAGE="File updated"

# Go to current working directory
cd "($pwd)"

# Loop through each unpushed file
for file in $(git status -s | awk '{print $2}'); do
	# Add the file to the staging area
	git add "$file"

	# Commit the changes with the same commit message
	git commit -m "$COMMIT_MESSAGE"

	# Push the changes to the repository
	git push
dones
