#!/bin/bash
set -euo pipefail
curl -sL https://s3.amazonaws.com/ds2002-resources/labs/lab3-bundle.tar.gz -o lab3-bundle.tar.gaz
tar -xzvf lab3-bundle.tar.gz
awk '!/^[[:space:]]*$/' lab3_data.tsv > cleaned.tsv
tr '\t' ',' < cleaned.tsv > cleaned.csv
ROWCOUNT=$(wc -l < cleaned.csv)
echo "Remaining data rows: $ROWCOUNT"
tar -czvf cleaned-bundle.tar.gz cleaned.csv
#this is how you clean a dataset --> csv