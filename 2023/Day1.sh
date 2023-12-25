#!/bin/bash

INPUT="./INPUT/Day1.txt"
SUMP1=0
SUMP2=0

# Start timestamp
START=$(date +%s.%N)

while read -r LINE
do
    DIGITS=$(echo "$LINE" | grep -o -P '[0-9]' | awk 'BEGIN{FS="";OFS=""} {if (NR==1) f=$0; l=$0} END{print f,l}')
    ((SUMP1+=DIGITS))
done < "$INPUT"

while read -r LINE
do
    FIRST=$(echo "$LINE" | grep -o -m 1 -P '[0-9]|one|two|three|four|five|six|seven|eight|nine' | head -n 1)
    LAST=$(echo "$LINE" | sed 's/oneight/oneeight/g' | grep -o -P '[0-9]|nine|eight|seven|six|five|four|three|two|one' | tac | head -n 1)
    FIRSTCONVERT=$(echo "$FIRST" | sed 's/one/1/g; s/two/2/g; s/three/3/g; s/four/4/g; s/five/5/g; s/six/6/g; s/seven/7/g; s/eight/8/g; s/nine/9/g')
    LASTCONVERT=$(echo "$LAST" | sed 's/one/1/g; s/two/2/g; s/three/3/g; s/four/4/g; s/five/5/g; s/six/6/g; s/seven/7/g; s/eight/8/g; s/nine/9/g')
    WORDS="${FIRSTCONVERT}${LASTCONVERT}"
    ((SUMP2+=WORDS))
done  < "$INPUT"

# End timestamp
END=$(date +%s.%N)

# Calculate runtime in minutes, seconds, and milliseconds
DIFF=$(echo "$END - $START" | bc)
MIN=$(echo "$DIFF / 60" | bc)
SEC=$(echo "$DIFF % 60" | bc)

# Print the sum and runtime
echo "Part 1: $SUMP1"
echo "Part 2: $SUMP2"
echo "Runtime: $MIN Minutes $SEC Seconds"