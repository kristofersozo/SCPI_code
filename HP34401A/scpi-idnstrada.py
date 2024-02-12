import serial	# pakete priekš komunikācijas ar virknes interfeisu
import time	# pakete priekš ar laiku saistītām operācijām

ser = serial.Serial('COM4', 9600)	# atver COM portu
ser.write(b'\n')	# izveido jaunu rindu, lai pārliecinātos, ka visi neapstiprinātie dati ir notīrīti
ser.flush()	# iztīra autputa buferi, lai pārliecinātos, ka dati ir nosūtīti
time.sleep(1)	# nogaida 1 sekundi
ser.read_all()	# nolasa visus pieejamos datus no bufera
ser.write(b'*RST\n')	# nosūta "reset" komandu
ser.flush()	# iztīra autputa buferi, lai pārliecinātos, ka dati ir nosūtīti
print('Resetting the device...')
time.sleep(1)	# nogaida 1 sekundi
ser.write(b'*CLS\n')	# nosūta komandu, kas iztīra ierīci
ser.flush()	# iztīra autputa buferi, lai pārliecinātos, ka dati ir nosūtīti
print('Clearing the device...')
time.sleep(1)	# nogaida 1 sekundi
#ser.timeout = 5000	# virknes interfeisa komunikācijas taimauts milisekundēs

#ser.write(b'*RST;*CLS\n')	# vienlaicīgu nosūta "reset" un komandu, kas iztīra ierīci
while True:	# izveido atkārtojošos cilpu
	 # nosūta "*IDN?" komandu, lai noteiktu ierīces identifikāciju
	ser.write(b'*IDN?\n')
	ser.flush()	# iztīra autputa buferi, lai pārliecinātos, ka dati ir nosūtīti

	print('Sending the "*IDN?" command...')

	response = ser.readline()	# nolasa atbildi

	print(response)

	time.sleep(1)	# nogaida 1 sekundi

ser.timeout = 1000	# taimauts virknes komunikācijai
while 1:	# izveido atkārtojošos cilpu
	time.sleep(3)	# nogaida 3 sekundes
	print('lol')
	ser.read_all()	# nolasa visus pieejamos datus no bufera
	time.sleep(1)	# nogaida 1 sekundi
	print('writing')
	ser.write(b'*IDN?\n')	# nosūta "*IDN?" komandu, lai noteiktu ierīces identifikāciju

ser.close()	# aizver COM portu
