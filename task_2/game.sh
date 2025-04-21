#!/bin/bash

IFS=$'\n'

FILE_NAME=$1
#создание массивов
questions=()
answers=()
user_answers=()

# Чтение CSV файла
while IFS=',' read -r question answer; do
  # Здесь IFS временно меняется на , только для команды read.
    questions+=("$question")
    answers+=("$answer")
done < <(tail -n +2 "$FILE_NAME")  # Пропускаем заголовок (первую строку)
# < <(...) — это Process Substitution, передаёт вывод команды tail как входные данные для цикла.

quantity=${#questions[@]}
# ${#questions[@]} - вычисляет количество элементов в массиве questions
# [@] — обращение ко всем элементам массива
# # перед массивом — подсчёт количества элементов

clear

# Задаём вопросы
for ((i=0; i<quantity; i++)); do
    current_question=$((i + 1))
    echo "$current_question из $quantity:"
    echo "${questions[$i]}"
    read -r -p "Ваш ответ: " user_answer
    if [[ -z "$user_answer" ]]; then
        user_answers+=("Нет ответа")
    else
        user_answers+=("$user_answer")
    fi
    clear
done

# Выводим результаты
echo "Результаты:"
echo "------------------------"

for ((i=0; i<quantity; i++)); do
    current_question=$((i + 1))
    echo "$current_question из $quantity:"
    echo "${questions[$i]}"
    echo "Ваш ответ: ${user_answers[$i]}"
    echo "Правильный ответ: ${answers[$i]}"
    echo "------------------------"
done