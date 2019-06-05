# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  config.vm.box = "bento/ubuntu-18.04"
  config.vm.network "private_network", ip: "44.44.44.4"

  config.vm.provision "shell", inline: <<-SHELL
    echo "xxxXXXxxx Starting instalation! xxxXXXxxx"

    sudo apt-get update
    
    # nodejs installation
    curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
    sudo apt-get install -y nodejs
    sudo npm i -g serve
  	sudo npm i -g pm2

  	# python and virtualenv installation
    sudo apt install -y python3-pip python3-dev build-essential libssl-dev libpq-dev
    sudo pip3 install pipenv
    export PIPENV_VENV_IN_PROJECT=1
    export VIRTUALENV_ALWAYS_COPY=1
    cd /vagrant/api && pipenv install -r requirements.txt

    # postgresql installation
    sudo apt install -y postgresql 
    sudo apt install -y postgresql-contrib
    sudo apt-get install python-psycopg2
		sudo apt-get install libpq-dev
    sudo -u postgres createdb users_prod
    sudo -u postgres createdb users_dev
    sudo -u postgres createdb users_tests

    echo "xxxXXXxxx Done installing your virtual machine! xxxXXXxxx"
  SHELL
end

# next steps:

# psql - setting user password
# sudo -u postgres psql
# in psql shell: 
# ALTER USER postgres WITH ENCRYPTED PASSWORD 'postgres';
# \q - to quit postfres console