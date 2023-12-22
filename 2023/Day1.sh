#!/bin/bash

INPUT="./INPUT/Day1.txt"
SUMP1=0
SUMP2=0

# Start timestamp
START=$(date +%s.%N)

while read -r LINE
do
    DIGITS=$(echo "$LINE" | grep -o -P '[0-9]' | awk 'BEGIN{FS="";OFS=""} {if (NR==1) f=$0; l=$0} END{print f,l}')
#    NORMAL=$(echo "$LINE" | grep -o -m 1 -P '[0-9]|one|two|three|four|five|six|seven|eight|nine')
#    REVERSED=$(echo "$LINE" | rev |grep -o -m 1 -P '[0-9]|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin')
#    NORMALCONVERT=$(echo "$NORMAL" | sed 's/one/1/g; s/two/2/g; s/three/3/g; s/four/4/g; s/five/5/g; s/six/6/g; s/seven/7/g; s/eight/8/g; s/nine/9/g')
#    REVERSEDCONVERT=$(echo "$REVERSED" | sed 's/eno/1/g; s/owt/2/g; s/eerht/3/g; s/ruof/4/g; s/evif/5/g; s/xis/6/g; s/neves/7/g; s/thgie/8/g; s/enin/9/g' | rev)
#    WORDS="${NORMALCONVERT}${REVERSEDCONVERT}"
#    echo "$NORMALCONVERT $REVERSEDCONVERT"
    ((SUMP1+=DIGITS))
#    ((SUMP2+=WORDS))
done < "$INPUT"

# End timestamp
END=$(date +%s.%N)

# Calculate runtime in minutes, seconds, and milliseconds
DIFF=$(echo "$END - $START" | bc)
MIN=$(echo "$DIFF / 60" | bc)
SEC=$(echo "$DIFF % 60" | bc)

# Print the sum and runtime
echo "Part 1: $SUMP1"
#echo "Part 2: $SUMP2"
echo "Runtime: $MIN Minutes $SEC Seconds"