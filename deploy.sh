#!/bin/bash
lftp -c "
set ssl:verify-certificate no
open ftpupload.net
user if0_41386054 1UhaKvJpQS
mirror -R /app/dist/ htdocs/
bye
"
