import time
import serial
import numpy as np
 
N = 10
data = np.zeros((N, 2))
# Abrimos la conexion con Arduino
arduino = serial.Serial('/dev/ttyS3', baudrate=9600, timeout=1.0)
with arduino:
    ii = 0
    while ii < N:
        try:
            line = arduino.readline()
            if not line:
                # HACK: Descartamos líneas vacías porque fromstring produce
                # resultados erróneos, ver
                # https://github.com/numpy/numpy/issues/1714
                continue
            data[ii] = np.fromstring(line.decode('ascii', errors='replace'), sep=' ')
            ii += 1
        except KeyboardInterrupt:
            print("Exiting")
            break
        print(data)
