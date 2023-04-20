import time
import pprint
import pyshark

def capture_to_file():
    timestr = time.strftime("%Y%m%d-%H%M%S")
    capture_file = 'capture_' + timestr + '.cap'

    capture = pyshark.LiveCapture(interface='wlp2s0', output_file=capture_file)

    for packet in capture.sniff_continuously(packet_count=10):
        pass

if __name__ == '__main__':
    capture_to_file()
