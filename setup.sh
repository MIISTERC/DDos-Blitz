echo "PACKAGES ARE BEING INSTALLED PLEASE WAIT.."
pack=$(pip3 install colorama)

echo "do you want to exectue ddos  from any where from your system?  [y/n] : "
read usr
echo "Are you using termux ? [y/n]"
read usr2
if [ "$usr2" == "y" ] && [ "$usr" == "y" ]; then
	python=$(command -v python3)
	sed -i "1i \#!$python" ddos.py
	mv ddos.py ddos
	mv ddos /data/data/com.termux/files/usr/bin
	echo "setup successfully done, now ypu can execute the script by typing ddos"
elif [ "$usr" == "y" ] && [ "$usr2" == "n" ]; then
	linux=$(command -v python3)
        sed -i "1i \#!$linux" ddos.py
	mv ddos.py ddos
	mv ddos /usr/bin
	echo "setup successfully donw , now you can execute the scriptby typing ddos"
else
	./ddos.py
fi
