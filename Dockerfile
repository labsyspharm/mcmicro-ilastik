FROM python:3.6

RUN pip install scikit-image h5py pandas numpy pathlib tifffile pathlib scipy

COPY . /app/