clear
bash m.sh |lolcat
chmod +x k.sh 

echo -e "\e[5;32m 1) for password separator press 1"
echo '2)for updating press 2 '
read -p "enter option-:" k
if [ "$k" == 1 ]
then
python password.py

elif [ "$k" == 2 ]
then
bash u.sh
else 
echo 'error occurred'
fi
