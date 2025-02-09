#!/bin/sh

if [ ! -d "../.venv" ]
then
    python3 -m venv ../.venv
fi

aoc() {
    case "${1}" in
        's' | 'start')

            find . -name '*.html' -exec rm -f {} \;
            cpus=$(sysctl -a | grep core_count | cut -d\  -f2)
            for i in $(seq 1 25)
            do
                mkdir -p $i
                printf "%s" "<script> \
                    window.location.replace(\"https://adventofcode.com/2024/day/$i\") \
                </script>" | tr -d ' ' | sed 's/ /\n/g' > $i/$i.html
            done


        ;;
        'a' | 'again')
            dttm=$(date -Iseconds | sed 's/\+.*//;s/:/-/g')
            file="history_${dttm}.tar.gz"

            dir="../bkp/aoc/"
            if [ ! -d $dir ]
            then
                mkdir -p $dir
            fi

            tar -cf $file ./*
            echo "$file -> $dir"
            cp -r $file $dir && rm $file
            find . -type d -not -name '.' -exec rm -r {} \; 2> /dev/null

            aoc start
        ;;
  esac
}
