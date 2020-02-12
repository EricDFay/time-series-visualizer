from datetime import datetime

with open('../data/timestamps.csv') as filein:
  with open('../data/seconds.csv','w') as fileout:
    first_timestamp = filein.readline().strip()
    dt = datetime.strptime(first_timestamp, '%Y%m%dT%H%M%S')
    dt0 = dt.replace(hour=0,minute=0,second=0,microsecond=0)
    fileout.write(str(int((dt-dt0).total_seconds())) + '\n')
    for line in filein:
      line = line.strip()
      dt1 = datetime.strptime(line, '%Y%m%dT%H%M%S')
      seconds = int((dt1 - dt0).total_seconds())
      fileout.write(str(seconds) + '\n')
