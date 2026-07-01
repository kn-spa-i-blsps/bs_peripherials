FROM ros:humble-ros-base

# Zainstaluj zależności systemowe
RUN apt update && apt install -y \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Zainstaluj zależności Python
RUN pip install --upgrade pip setuptools
RUN pip install lgpio \
    adafruit-circuitpython-pca9685 \
    adafruit-blinka \
    adafruit-circuitpython-motor \
    numpy

# Skopiuj i zainstaluj bibliotekę
WORKDIR /workspace/bs_peripherials
COPY . .
RUN pip install -e .

# Domyślna komenda
CMD ["bash"]
