from datetime import datetime
from math import ceil
import numpy as np
import cv2

def distance(a,b):
  return abs(b-a)

def label(numbers, sep):
  numbers.sort()
  label = {}
  index = 0
  last = numbers[0]
  label[last] = 1
  for n in numbers:
    if (distance(n,last) > sep):
      index += 1
    label[n] = index
    last = n
  return label

def mk_histogram(numbers):
  histogram = {}
  for x in numbers:
    if x in histogram:
      histogram[x] += 1
    else:
      histogram[x] = 1
  return histogram

# keys must be integers
def draw_histogram(freq, colors, width=1024, height=64, bgcolor=(255,255,255)):
  window_width_max = 86400
  x_min = min(list(freq))
  span = max(list(freq)) - x_min
  max_count = max(freq.values())
  number_lines = ceil(span/window_width_max)

  window_height = number_lines * max_count
  window_width = min([span, window_width_max])

  img = np.zeros((window_height,window_width,3), np.uint8)
  img = cv2.rectangle(img, 
    (0,0), (window_width,window_height), bgcolor, -1)

  # draw grid
#  w = 3600
  h = 7*max_count
#  for i in range(24*60*6):
#    if i%6==0: color=(255,1,1)
#    if i%60==0: color=(255,255,255)
#    else: color=(55,55,255)
#    img = cv2.line(img, (i*600, 0), (i*600, window_height), color, thickness=10)
#  for j in range(int(window_height/h)):
#    img = cv2.line(img, (0, j*h), (window_width,j*h), (255,255,255))


#  for x in sorted(freq):
#    img = cv2.rectangle(img
#      , ( (x - x_min)%window_width_max , int((x - x_min)/window_width_max)*max_count )
#      , ( (x - x_min)%window_width_max + 1, int((x - x_min)/window_width_max)*max_count + freq[x] )
#      , colors[x], -1)
  for x in sorted(freq):
    img = cv2.rectangle(img
      , ( x%window_width_max , int(x/window_width_max)*max_count )
      , ( x%window_width_max + 1, int(x/window_width_max)*max_count + freq[x] )
      , colors[x], -1)

  cv2.imshow('main',img)
  filename = 'results/' + datetime.now().isoformat() + '.png'
  cv2.waitKey(0) 
  cv2.imwrite('b.png', img)
  cv2.destroyAllWindows()


# Testing
# data is N uniformly random integers from 0 to 100
from random import uniform
N = 300
l = 3
data = [int(uniform(400,3*3600)) for i in range(N)]





data = []
with open('data/seconds.csv') as f:
  for line in f:
    data.append(int(line))



color_map = [(0,255,255),(255,0,255),(255,255,0)]
group_label = label(data.copy(), 60)
colors = {n: color_map[group_label[n] % len(color_map)] for n in data}

print(group_label)


hist = mk_histogram(data)
draw_histogram(hist, width = 32000, colors=colors, bgcolor=(0,0,0))
