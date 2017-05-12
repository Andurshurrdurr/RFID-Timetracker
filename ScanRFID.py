import serial
from struct import pack, unpack

prot = {
    'enquiry_module': '\x03\x12\x00\x15',
    'enquiry_module_return': '\x02\x12\x14',
    'active_buzzer': '\x02\x13\x15',
    'enquiry_card': pack('BBBB', 03, 02, 00, 05),
    'enquiry_cards_return': '\x03\x02\x01\x06', # got valid card
    'enquiry_no_card_found': '\x02\x01\x03', # no card reachable or invalid
    'enquiry_all_cards': '\x03\x02\x01\x05',
    'anticollision' : '\x02\x03\x05\x00',
    'select_card' : '\x02\x04\x06',
}



def getSerial():
    """ 
    Sends the serial commands to the RFID scanner
    and returns the Unique ID (UID) of the RFID card which is found.
    """
    
    ser = serial.Serial('/dev/ttyUSB0',9600,timeout=1)
    ser.write(prot['enquiry_card'])
    resp =  ser.read(4)

    UID = 0
    
    if resp == prot['enquiry_no_card_found']:
        print "no valid card reachable"
    elif resp == prot['enquiry_cards_return']:
        ser.write(prot['active_buzzer'])
        resp = ser.read(3)
        if resp == prot['active_buzzer']:
            print "found card, sending anticollision"
            ser.write(prot['anticollision'])
            resp = ser.read(7)
            header = resp.encode('hex')[:4]
            if header == "0603":
                UID = resp[-5:].encode('hex')
                print "Card Serial:" + UID

    ser.close()
    return UID
