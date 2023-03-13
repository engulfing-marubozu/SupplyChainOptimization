import pandas as pd
import matplotlib.pyplot as plt
filename = 'data.xlsx'

sheets_dict = pd.read_excel(filename, sheet_name=None)

Sheet1 = sheets_dict.get("Sheet1").to_dict()
Sheet2 = sheets_dict.get("Sheet2").to_dict()
Sheet3 = sheets_dict.get("Sheet3").to_dict()

Sheet1dict = {}
toBeDeleted = []
length = len(Sheet1['Timestamp'])
for index in range(length):
    if Sheet1['Scan the roll cage QR code (1)'][index] in Sheet1dict.keys():
        toBeDeleted.append(Sheet1['Scan the roll cage QR code (1)'][index])
    else:
        Sheet1dict[Sheet1['Scan the roll cage QR code (1)'][index]]=Sheet1['Timestamp'][index]

shootOperatorTimestamp = []
for index in range(length):
    shootOperatorTimestamp.append(Sheet1['Timestamp'][index])

shootOperatorTimestampdiff = []
for index in range(len(shootOperatorTimestamp)-1):
    shootOperatorTimestampdiff.append( round(((shootOperatorTimestamp[index+1] - shootOperatorTimestamp[index]).total_seconds()/60),2))


shootOperatorTimestampdiff = list(filter(lambda x: 0 <= x <= 100, shootOperatorTimestampdiff))
         
plt.scatter(range(len(shootOperatorTimestampdiff)), shootOperatorTimestampdiff)
plt.xlabel('index')
plt.ylabel('Time')
plt.title('Time taken by shootOprator to process each Roll cage')
averagee = sum(shootOperatorTimestampdiff) / len(shootOperatorTimestampdiff)
print(averagee)  

Sheet2dict = {}
toBeDeleted.clear()
length = len(Sheet2['Timestamp'])
for index in range(length):
    if Sheet2['Scan the roll cage QR code (2)'][index] in Sheet2dict.keys():
        toBeDeleted.append(Sheet2['Scan the roll cage QR code (2)'][index])
    else:
        Sheet2dict[Sheet2['Scan the roll cage QR code (2)'][index]]=Sheet2['Timestamp'][index]
             

Sheet3dict = {}
toBeDeleted.clear()
length = len(Sheet3['Timestamp'])
for index in range(length):
    if Sheet3['Scan the roll cage QR code (3)'][index] in Sheet3dict.keys():
        toBeDeleted.append(Sheet3['Scan the roll cage QR code (3)'][index])
    else:
        Sheet3dict[Sheet3['Scan the roll cage QR code (3)'][index]]=Sheet3['Timestamp'][index]

TrackingDict = {}

for key in Sheet1dict:
    TrackingDict[key]= []

for key in TrackingDict:
    if key in Sheet2dict.keys() and round(((Sheet2dict[key] - Sheet1dict[key]).total_seconds()/60),2) < 300:
        TrackingDict[key].append(round(((Sheet2dict[key] - Sheet1dict[key]).total_seconds()/60),2))
    else:
        TrackingDict[key].append(None)

for key in TrackingDict:
    if key in Sheet2dict.keys() and  key in Sheet3dict.keys() and round(((Sheet3dict[key] - Sheet2dict[key]).total_seconds()/60),2)<300:
        TrackingDict[key].append(round(((Sheet3dict[key] - Sheet2dict[key]).total_seconds()/60),2))
    else:
        TrackingDict[key].append(None)

x_list = {}

for key in TrackingDict:
    if TrackingDict[key][0] is not None:
        x_list[key]= TrackingDict[key][0]
x_axis = list(x_list.keys())
for index in range(len(x_axis)):
    x_axis[index]= x_axis[index][-4:]
y_axis =  list(x_list.values())
average = sum(y_axis) / len(y_axis)
print(average)      
print(x_axis)

# plt.plot(x_axis,y_axis)

# plt.title("Time taken from Non con zon to drop zone")
# plt.xlabel("Roll Cage")
# plt.ylabel("Time in minutes")
# plt.text(5, 34, average, fontsize=12, color="red")
plt.text(5, 34, averagee, fontsize=12, color="red")
plt.show()