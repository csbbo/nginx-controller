#!/bin/bash

if [ $# -ne 1 ] && [ $# -ne 2 ] && [ $# -ne 3 ]
then
    echo "Invalid parameter!!!"
    echo "Userge:"$0" FunctioninID ReplacedString [NginxFilePath]"
    exit 0
fi

if [ $3 ]
then
	nginxpath=$3
else
	nginxpath="/etc/nginx/nginx.conf"
fi

funtls(){
	tlsstr="ssl_protocols "$*";"
	$(sed -i "s/ssl_protocols.*/$tlsstr/g" $nginxpath)
    $(systemctl reload nginx.service)
	# echo "TLS change success!"
}

funalm(){
	almstr="ssl_ciphers "$1";"
	sed -i "s/ssl_ciphers.*/$almstr/g" $nginxpath
    $(systemctl reload nginx.service)
	# echo "TLS change success!"
}

funtlsstat(){
    sslstr=$(echo `grep -m 1 ssl_protocols $nginxpath`)
    if [[ $sslstr == 'ssl_protocols TLSv1 TLSv1.1 TLSv1.2 TLSv1.3;' ]]
    then
        echo auto
    elif [[ $sslstr == 'ssl_protocols TLSv1;' ]]
    then
        echo v0
    elif [[ $sslstr == 'ssl_protocols TLSv1.1;' ]]
    then
        echo v1
    elif [[ $sslstr == 'ssl_protocols TLSv1.2;' ]]
    then
        echo v2
    elif [[ $sslstr == 'ssl_protocols TLSv1.3;' ]]
    then
        echo v3
    fi
}

funalmstat(){
    almstr=""
    if $(grep -q -m 1 3DES $nginxpath)
    then
        almstr=$almstr"1"
    fi

    if $(grep -q -m 1 AES $nginxpath)
    then
        almstr=$almstr"2"
    fi

    if $(grep -q -m 1 AESGCM $nginxpath)
    then
        almstr=$almstr"3"
    fi

    if $(grep -q -m 1 Camellia $nginxpath)
    then
        almstr=$almstr"4"
    fi

    if $(grep -q -m 1 IDEA $nginxpath)
    then
        almstr=$almstr"5"
    fi

    if $(grep -q -m 1 RC4 $nginxpath)
    then
        almstr=$almstr"6"
    fi

    if $(grep -q -m 1 SEED $nginxpath)
    then
        almstr=$almstr"7"
    fi
    echo $almstr
}

if [ $1 -eq 0 ]
then
	funtls $2
elif [ $1 -eq 1 ]
then
	funalm $2
elif [ $1 == 3 ]
then
    funtlsstat
elif [ $1 == 4 ]
then
    funalmstat
else
	echo "There is no such option!"
	echo "Please enter a valid option."
fi
