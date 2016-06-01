#!/bin/env python3

import sys

from smartcard.System import readers

CALYPSO_CLA = [0x94]
SELECT_INS = [0xA4]
READ_RECORD_INS = [0xB2]
GET_RESPONSE_INS = [0xC0]
TICKETING_COUNTERS_FILE_ID = [0x20, 0x69]

def main():
    local_readers = readers()

    if local_readers:
        if len(local_readers) == 1:
            readerIndex = 0
        else:
            for i, reader in enumerate(local_readers):
                print("[{}]: {}".format(i, reader))
            readerIndex = int(input("Select a reader: "))
    else:
        print("No reader detected")
        sys.exit(1)

    calypso = local_readers[readerIndex].createConnection()
    calypso.connect()

    select_apdu = CALYPSO_CLA + SELECT_INS + [0x00, 0x00, 0x02] + TICKETING_COUNTERS_FILE_ID + [0x00]
    data, sw1, sw2 = calypso.transmit(select_apdu)
    if sw1 == 0x61:
        get_response_apdu = [0x00] + GET_RESPONSE_INS + [0x00, 0x00, sw2]
        data, sw1, sw2 = calypso.transmit(get_repsonse_apdu)

    read_record_apdu = CALYPSO_CLA + READ_RECORD_INS + [0x01, 0x04, 0x1D]
    data, sw1, sw2 = calypso.transmit(read_record_apdu)

    if sw1 == 0x90:
        # FIXME: each chunk of remaining trips stored on 3 bytes?
        #chunks = [data[x:x+3] for x in range(0, len(data), 3)]
        #total = 0
        #for chunk in chunks:
        #    total += chunk[2]
        #print("Number of remaining trips: {}".format(tot = chunks[i][2] for i in chunks))
        print("Number of remaining trips: {}".format(sum(data)))
    else:
        print("Error getting number of remaining trips")
        sys.exit(2)

if __name__ == '__main__':
    main()
