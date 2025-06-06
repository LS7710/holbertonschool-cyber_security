#!/bin/bash

tail -n 1000 auth.log | grep "Failed password" | awk '{for(i=1;i<=NF;i++){if($i=="for"){print $(i+1)}}}' | sort | uniq -c | sort -nr > .failed_users.txt
tail -n 1000 auth.log | grep "Accepted password" | awk '{for(i=1;i<=NF;i++){if($i=="for"){print $(i+1)}}}' | sort | uniq -c | sort -nr > .successful_users.txt

cat .successful_users.txt | while read count user
do
  grep " $user$" .failed_users.txt > /dev/null
  result=$?
  if test $result -eq 0
  then
    echo $user
    break
  fi
done

rm -f .failed_users.txt .successful_users.txt
