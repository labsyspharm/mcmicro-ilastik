FROM python:3.6

RUN pip install scikit-image h5py pandas numpy pathlib tifffile pathlib scipy

ARG ilastik_binary=ilastik-1.3.3post2-Linux.tar.bz2

ADD http://files.ilastik.org/$ilastik_binary /

RUN mkdir ilastik-release && \
    tar xjvf $ilastik_binary -C ilastik-release --strip-components=1 && \
    rm $ilastik_binary

COPY . /app/
