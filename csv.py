import csv

f = open('wordlist.csv','at',newline='')
csv_writer = csv.writer(f)
csv_writer.writerow(["name","surname"])

csv_writer.writerow(["david","jones"])