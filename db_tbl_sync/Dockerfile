FROM perl:5.20
RUN apt-get install libdbi-perl
RUN apt-get install libdbd-mysql-perl

COPY . /usr/src/myapp
WORKDIR /usr/src/myapp
CMD [ "perl", "./your-daemon-or-script.pl" ]
