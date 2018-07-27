#Install all dependencies 

PASSWORD= ""
[ "$UID" -eq 0 ] || exec sudo bash "$0" "$@"

	echo $PASSWORD | sudo -S apt-get update && apt-get upgrade
	echo 'y'

	echo $PASSWORD | sudo -S apt-get install git
	echo 'y'

	echo $PASSWORD | sudo -S apt-get install python-dev
	echo 'y'

	echo $PASSWORD | sudo -S apt-get install g++
	echo 'y'

	echo $PASSWORD | sudo apt-get install build essential
	echo 'y'

	echo $PASSWORD | sudo apt-get install libevent-dev
	echo 'y'

	echo $PASSWORD | sudo apt get install libssl-dev
	echo 'y'

	echo $PASSWORD | sudo apt-get install openssl
	echo 'y'

	echo $PASSWORD | sudo apt-get install python-tk
	echo 'y'

#build the VOLTTRON platform
'git clone https://github.com/VOLTTRON/volttron volttron'

'cd ~/volttron'
'python bootstrap.py'




