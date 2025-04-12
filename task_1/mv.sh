#!/bin/bash

script_name="$0"
extension="${script_name##*.}"

for file in `ls -p | grep -v / | grep -o '\..*$' | sort -uf`
do
	#echo "${file##*.}"
	echo "${file:1}"

	#mv *$file $file/
	if [ ! -d "${file:1}" ] 
	then
		mkdir "${file:1}"

		shopt -s nocaseglob  
		mv *."${file:1}" "${file:1}"
		shopt -u nocaseglob
	fi
done

mv $extension/$0 .
