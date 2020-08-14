
FROM kalilinux/kali-rolling
RUN apt-get update && apt upgrade -y && apt-get install sudo

RUN apt-get install -y\
    coreutils \
    bash \
    nodejs \
    bzip2 \
    curl \
    figlet \
    gcc \
    g++ \
    git \
    aria2 \
    #util-linux \
    libevent-dev \
    libjpeg-dev \
    libffi-dev \
    libpq-dev \
    libwebp-dev \
    libxml2 \
    libxml2-dev \
    libxslt-dev \
    musl \
    neofetch \
    libcurl4-openssl-dev \
    postgresql \
    postgresql-client \
    postgresql-server-dev-all \
    #chromedriver \
    openssl \
    pv \
    jq \
    wget \
    python3 \
    python3-dev \
    python3-pip \
    libreadline-dev \
    #metasploit-framework \
    #apktool \
    #openjdk-13-jdk \
    #zipalign \
    sqlite \
    ffmpeg \
    libsqlite3-dev \
    chromium \
    zlib1g-dev \
    recoverjpeg \
    zip \
    megatools \
    libfreetype6-dev




RUN pip3 install --upgrade pip setuptools 
RUN pip3 install --upgrade pip install wheel 
RUN if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi 
RUN if [ ! -e /usr/bin/python ]; then ln -sf /usr/bin/python3 /usr/bin/python; fi 
RUN rm -r /root/.cache

RUN git clone https://github.com/rekcahkumar/javes /root/userbot
RUN mkdir /root/userbot/bin/
WORKDIR /root/userbot/
RUN mv userbot/javes_main/extra/apktool /usr/local/bin
RUN mv userbot/javes_main/extra/apktool.jar /usr/local/bin
#RUN mv userbot/javes_main/extra/apk.rb /usr/share/metasploit-framework/lib/msf/core/payload
RUN chmod +x /usr/local/bin/*
RUN pip3 install --ignore-installed -r requirements.txt
CMD ["python3","-m","userbot"]
