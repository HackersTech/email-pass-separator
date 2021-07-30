clear
bash m.sh |lolcat

echo -e "\e[4;32m for password separator press 1"
echo 'for updating press 2 '
read -p "enter option" k
if [ "$k"==1 ]
python password.py

elif [ "$k"==2 ]
bash u.sh
