from tkinter import *
root=Tk()
root.geometry('1200x700')
root.title("Taj Mahal")
canvas=Canvas(root, height="700",width="1200",background="black")

canvas.create_rectangle(2,376,1197,456,fill="#bfbfbf")
canvas.create_rectangle(2,376,1197,388,fill="#bfbfbf",outline="#bfbfbf")
canvas.create_rectangle(2,444,1197,388,fill="#bfbfbf")
canvas.create_rectangle(27,414,45,443,fill="black")
canvas.create_polygon(27,414,36,402,44,413,)
canvas.create_rectangle(193,413,209,443,fill="black")
canvas.create_polygon(193,413,200,402,209,413,fill="black")
canvas.create_rectangle(378,413,394,443,fill="black")
canvas.create_polygon(378,413,385,402,394,413,fill="black")
canvas.create_rectangle(555,413,571,443,fill="black")
canvas.create_polygon(555,413,564,402,571,413)
canvas.create_rectangle(745,413,761,443,fill="black")
canvas.create_polygon(745,413,753,402,762,413)
canvas.create_rectangle(937,413,952,443,fill="black")
canvas.create_polygon(937,413,944,402,952,413)
canvas.create_rectangle(1107,413,1122,443,fill="black")
canvas.create_polygon(1107,413,1114,402,1122,413)
#center rectangle
canvas.create_rectangle(282,179,919,375,fill="#bfbfbf")
canvas.create_rectangle(282,179,919,190,fill="#bfbfbf")
canvas.create_rectangle(294,191,283,375,fill="#bfbfbf")
canvas.create_rectangle(906,191,919,375)
#center rectangle middle arch
canvas.create_rectangle(490,191,501,375)
canvas.create_rectangle(699,191,711,375)
canvas.create_rectangle(667,191,679,375)
canvas.create_rectangle(521,191,532,375)
#center rectangle left rectangle
canvas.create_rectangle(372,191,384,375)
#center rectangle right rectangle
canvas.create_rectangle(832,375,821,191)
#parallel lines
canvas.create_rectangle(384,277,490,289,)
canvas.create_rectangle(711,277,821,287)
canvas.create_polygon(372,276,372,288,294,305,294,295,outline="black",fill="#bfbfbf")
canvas.create_polygon(832,277,832,287,906,304,907,295,outline="black",fill="#bfbfbf")
#innerwindowsleft
canvas.create_rectangle(354,375,313,332,fill="black")
canvas.create_polygon(312,333,333,310,353,332)#lower
canvas.create_polygon(312,291,312,233,333,209,349,233,350,281)#upper
canvas.create_rectangle(419,323,455,375,fill="black")
canvas.create_polygon(419,323,435,301,455,323)
canvas.create_rectangle(416,224,453,277,fill="black")
canvas.create_polygon(416,224,435,201,453,224)
#innerwindowsright
canvas.create_rectangle(848,333,888,375,fill="black")
canvas.create_polygon(848,333,869,308,889,333)
canvas.create_rectangle(750,317,784,375,fill="black")
canvas.create_polygon(750,317,766,296,785,318)
canvas.create_rectangle(746,226,783,277,fill="black")#upper
canvas.create_polygon(746,226,764,199,783,225)
canvas.create_polygon(847,280,847,223,867,198,885,227,885,290)
#above rectangle , middle tomb
canvas.create_rectangle(509,141,692,179,fill="#bfbfbf")
canvas.create_rectangle(521,150,559,170,fill="black")
canvas.create_rectangle(580,150,620,170,fill="black")
canvas.create_rectangle(639,150,680,170,fill="black")
canvas.create_oval(587,12,616,95,fill="orange")
canvas.create_arc(490,58,709,221,fill="#bfbfbf",start=0,extent=180,outline="#bfbfbf")
#above rectangle , left tomb
canvas.create_oval(372,76,400,146,fill="orange")
canvas.create_rectangle(338,134,429,179,fill="#bfbfbf")
canvas.create_oval(339,120,428,146,fill="#bfbfbf",outline="#bfbfbf")
canvas.create_rectangle(367,141,399,158,fill="black")
#above rectangle , right tomb
canvas.create_oval(802,76,829,144,fill="orange")
canvas.create_rectangle(771,134,858,179,fill="#bfbfbf")#big rectangle
canvas.create_oval(772,120,857,147,fill="#bfbfbf",outline="#bfbfbf")
canvas.create_rectangle(797,142,831,159,fill="black")
#left bigger tower
canvas.create_oval(51,38,78,127,fill="yellow")
canvas.create_polygon(24,373,42,108,82,109,102,374,fill="#bfbfbf")
canvas.create_oval(27,82,97,121,fill="#bfbfbf",outline="#bfbfbf")
canvas.create_rectangle(47,283,80,373,fill="black")
canvas.create_polygon(47,283,62,260,80,283,fill="black")
canvas.create_rectangle(51,159,71,216,fill="black")
canvas.create_polygon(51,159,59,143,72,160,fill="black")

#right bigger tower
canvas.create_oval(1124,43,1149,110,fill="yellow")
canvas.create_polygon(1098,375,1117,111,1155,113,1177,375,fill="#bfbfbf")
canvas.create_oval(1100,83,1170,121,fill="#bfbfbf",outline="#bfbfbf")
canvas.create_rectangle(1124,279,1155,375,fill="black")#lower door
canvas.create_polygon(1123,279,1138,259,1156,279)
canvas.create_rectangle(1128,149,1148,207,fill="black")
canvas.create_polygon(1128,149,1137,134,1149,149)
canvas.create_rectangle(53,95,70,110,fill="black")
canvas.create_rectangle(1127,93,1145,110,fill="black")
#left small tower
canvas.create_oval(178,112,195,173,fill="yellow")
canvas.create_polygon(165,375,218,374,200,177,175,176,fill="#bfbfbf")
canvas.create_oval(169,149,205,182,fill="#bfbfbf",outline="#bfbfbf")
canvas.create_rectangle(182,161,192,169,fill="black")
canvas.create_rectangle(180,298,202,375,fill="black")
canvas.create_polygon(180,298,191,283,203,299,fill="black")
canvas.create_rectangle(181,216,196,254,fill="black")
canvas.create_polygon(181,216,189,205,197,216,fill="black")
#right samall tower
canvas.create_oval(1000,112,1017,165,fill="yellow")
canvas.create_polygon(1044,374,986,375,1000,178,1022,174,fill="#bfbfbf")
canvas.create_oval(992,147,1027,180,fill="#bfbfbf",outline="#bfbfbf")
canvas.create_rectangle(1003,158,1013,166,fill="black")
canvas.create_rectangle(1003,293,1024,374,fill="black")
canvas.create_polygon(1003,293,1012,278,1024,293)
canvas.create_rectangle(1005,211,1020,251,fill="black")#upper window
canvas.create_polygon(1005,211,1012,200,1021,211)
#main door and arch
canvas.create_rectangle(532,191,667,245,fill="orange")
canvas.create_oval(532,230,667,260,outline="#bfbfbf",fill="#bfbfbf")
canvas.create_rectangle(567,293,635,375,fill="black")
canvas.create_oval(567,272,635,308,fill="black")
#below green part
canvas.create_rectangle(1,457,1200,700,fill="#4CBB17")
canvas.create_polygon(505,456,688,457,768,700,420,699,fill="#4169E1")
canvas.create_polygon(688,457,766,457,860,700,770,701,fill="#bfbfbf")#right walk
canvas.create_polygon(430,456,504,457,419,701,332,700,fill="#bfbfbf")
canvas.create_oval(770,482,817,560,fill="green")#right first plant
canvas.create_rectangle(788,559,798,574,fill="brown")
canvas.create_oval(810,609,856,688,fill="green")#right second plant
canvas.create_rectangle(828,687,839,698,fill="brown")
canvas.create_oval(366,482,415,565,fill="green")#lft first plant
canvas.create_rectangle(386,563,396,581,fill="brown")
canvas.create_oval(325,602,371,685,fill="green")#lft second plant
canvas.create_rectangle(343,684,353,698,fill="brown")
def pos(e):
    print(e.x, e.y)
root.bind('<Button-1>', pos)
canvas.pack()
mainloop()
