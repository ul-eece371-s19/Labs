'''this code copies image array for progmem format


'''



import pandas as pd
import numpy

pmdata = open("progmemdata.txt","w");

image1 = pd.read_csv("Image4.csv", index_col=None, header=None);
img = numpy.array(image1);
pmdata.write('{')
d1,d2 = img.shape
for i in range(d1):
    pmdata.write('{')
    for j in range(d2):
        pmdata.write(str(img[i][j]))
        if j!= d2-1:
            pmdata.write(',')
    pmdata.write('}')
    if i!=d1-1:
        pmdata.write(',')
pmdata.write('}')

