#!/bin/bash

# this is for ubuntu 20.04.4

# instructions for running -
# give execution permission to the script
# '$ chmod +x install_20.04.4.sh'
# run it as the user with sudo;
# for eg : '$ sudo -u ubuntu ./install_20.04.4.sh'
# Power off the vm and restart the VM again to use Driverbeat or Driverdar
# cd /path/to/ShadeWatcher/parse
# ./driverdar -trace /path/to/file or ./driverbeat -trace /path/to/file

sudo apt update &&
sudo apt install -y git curl python python3 pkg-config make gcc g++ &&
sudo apt-get install --reinstall ca-certificates &&

git clone https://github.com/jun-zeng/ShadeWatcher.git &&
cd ShadeWatcher/lib &&
LIB_INSTALL_PATH=$PWD &&

sudo apt-get install -y libssl-dev neo4j-client libneo4j-client-dev &&

sudo apt install -y libpq-dev &&
wget --no-check-certificate https://github.com/jtv/libpqxx/archive/refs/tags/6.4.5.tar.gz &&
tar xvzf 6.4.5.tar.gz &&
cd libpqxx-6.4.5 &&
./configure --disable-documentation --prefix=$LIB_INSTALL_PATH &&
make -j8 &&
make install &&
cd .. &&

wget https://hyperrealm.github.io/libconfig/dist/libconfig-1.7.2.tar.gz &&
tar xvzf libconfig-1.7.2.tar.gz &&
cd libconfig-1.7.2 &&
./configure --prefix=$LIB_INSTALL_PATH &&
make -j8 &&
make install &&
cd .. &&

sudo apt-get install -y libjsoncpp-dev &&
cd $LIB_INSTALL_PATH/include &&
wget https://raw.githubusercontent.com/nlohmann/json/develop/single_include/nlohmann/json.hpp &&
cd .. &&

git clone https://github.com/edenhill/librdkafka.git &&
cd librdkafka/ &&
./configure --prefix=$LIB_INSTALL_PATH &&
make -j8 &&
make install &&
cd .. &&

echo export CPLUS_INCLUDE_PATH=$LIB_INSTALL_PATH/include:$CPLUS_INCLUDE_PATH >> ~/.bashrc &&
echo export PATH=$LIB_INSTALL_PATH/bin:$PATH >> ~/.bashrc &&
echo export LD_LIBRARY_PATH=$LIB_INSTALL_PATH/lib:$LIB_INSTALL_PATH/lib64:$LD_LIBRARY_PATH >> ~/.bashrc &&
source ~/.bashrc &&

sudo apt install -y postgresql postgresql-contrib &&
sudo service postgresql start &&
sudo apt install -y default-jre default-jre-headless &&

sudo apt install -y apt-transport-https ca-certificates curl software-properties-common &&
sudo curl -fsSL https://debian.neo4j.com/neotechnology.gpg.key | sudo apt-key add - &&
echo 'deb https://debian.neo4j.com stable 4.1' | sudo tee /etc/apt/sources.list.d/neo4j.list &&
sudo apt-get update &&
sudo apt-get install -y neo4j &&

cd ../parse &&
sudo make
# Now you should have driverbeat inside /ShadeWatcher/parse
