import time
from selenium import webdriver
import subprocess
import pyshark
from scapy.all import sniff
from scapy.all import wrpcap
import csv


def web_crawler(category, address, iterations):

    for i in range(iterations):
        driver = webdriver.Chrome('driver/chromedriver')  # Optional argument, if not specified will search path.
        driver.get(address)
        time.sleep(2) # Let the user actually see something!
        capture = pyshark.LiveCapture(interface='ens33', bpf_filter= 'ip host 10.63.7.188 || tcp',
                                      output_file='csv/' + category + '_' + str(i) +'_Chrome.pcap')
        capture.sniff(timeout=60)

        driver.quit()


if __name__ == '__main__':
    c_name = []
    address = []
    iteration = 10
    with open('list.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            c_name.append(row['category'])
            address.append(row['address'])
    for idx, name in enumerate(c_name):
        web_crawler(name, address[idx], iteration)