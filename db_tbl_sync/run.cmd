sudo apt-get install libdbi-perl
sudo apt-get install libdbd-mysql-perl

git clone https://github.com/percona/percona-toolkit.git

perl Makefile.PL
make
make test
make install

pt-table-sync --databases=twee --tables=twees h=127.0.0.1,P=10000,u=root,p=passwd h=127.0.0.1,P=9999,u=root,p=passwd --print
pt-table-sync --databases=twee --tables=twees h=127.0.0.1,P=10000,u=root,p=passwd h=127.0.0.1,P=9999,u=root,p=passwd --execute
