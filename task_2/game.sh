#!/bin/bash

IFS=$'\n'

BD_PATH=$1
questions=(`csvtool col 1 $BD_PATH`)
answers=(`csvtool col 2 $BD_PATH`)
quantity=$((`csvtool height $BD_PATH`-1))

for question_number in ${!questions[@]}
do
	if [ $question_number -eq 0 ]; then echo "Всего будет $quantity вопросов";
	else
		echo $question_number ${questions[$question_number]}
		read user_answer
		user_answers+=($user_answer)
	fi
	clear
done

for question_number in ${!questions[@]}
do
	if [ $question_number -eq 0 ]; then echo "Результаты"
	else
		echo $question_number ${questions[$question_number]}
		echo "Ваш ответ: "${user_answers[$question_number]}
		echo "Правильный ответ: " ${answers[$question_number]}
	fi
	echo "---------"
done