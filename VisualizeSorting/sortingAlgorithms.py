from tkinter import *
from tkinter import ttk
import random
from bubblesort import bubble_Sort
from quicksort import quick_sort

root = Tk()
root.title("Visualizing Sorting Algorithm")
root.maxsize(1200, 600)
root.config(bg='black')

# variables
selected_alg = StringVar()
data = []

def drawData(data, colorArray):
    canvas.delete("all")
    c_height = 380
    c_width = 1000 # 600
    x_width = c_width / (len(data) + 1)
    offset = 30
    spacing = 10
    constantData = [i / max(data) for i in data]
    for i, height in enumerate(constantData):
        # Top Left Corner
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        # Bottom Left Corner
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        # Test
        # print("x0 is: " + str(x0))
        # print("y0 is: " + str(y0))
        # print("x1 is: " + str(x1))

        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))

    root.update_idletasks()

def Generate():
    global data

    minVal = int(minEntry.get())
    maxVal = int(maxEntry.get())
    size = int(sizeEntry.get())

    data = []
    for _ in range(size):
        data.append(random.randrange(minVal, maxVal+1))

    drawData(data, ['red' for x in range(len(data))])

def StartAlgorithm():
    global data
    if not data: return

    if(algMenu.get() == 'Quick Sort'):
        quick_sort(data, 0, len(data)-1, drawData, speedScale.get())
        drawData(data, ['green' for x in range(len(data))])

    elif algMenu.get() == 'Bubble Sort':
        bubble_Sort(data, drawData, speedScale.get())


UI_frame = Frame(root, width=1000, height=200, bg='black')
UI_frame.grid(row=0, column=0, padx=5, pady=5)

canvas = Canvas(root, width=1000, height=300, bg='black')
canvas.grid(row=1, column=0, padx=10, pady=5)

# User Interface


# Row[0] First row in Menu
Label(UI_frame, text="Set Bounds: ", bg='gray').grid(row=0, column=0, padx=5, pady=5, sticky=W)

sizeEntry = Scale(UI_frame, from_=3, to=25, resolution=1, orient=HORIZONTAL, label="Data Size" )
sizeEntry.grid(row=0, column=1, padx=5, pady=5)

minEntry = Scale(UI_frame, from_=0, to=10, resolution=1, orient=HORIZONTAL, label="Min Value" )
minEntry.grid(row=0, column=2, padx=5, pady=5)

maxEntry = Scale(UI_frame, from_=10, to=100, resolution=1, orient=HORIZONTAL, label="Max Value" )
maxEntry.grid(row=0, column=3, padx=5, pady=5)

speedScale = Scale(UI_frame, from_=0.1, to=2.0, length=200, digits=2, resolution=0.2, orient=HORIZONTAL, label="Select Speed [s]" )
speedScale.grid(row=0, column=4, padx=5, pady=5)

Button(UI_frame, text="   Generate   ", command=Generate, bg='white').grid(row=0, column=5, padx=5, pady=5)

# Row[1] Second row in Menu
Label(UI_frame, text="Algorithm: ", bg='gray').grid(row=1, column=0, padx=5, pady=5, sticky=W)
algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=['Bubble Sort', 'Quick Sort', 'Merge Sort'])
algMenu.grid(row=1, column=1, padx=5, pady=5)
algMenu.current(0)

Button(UI_frame, text="     Start       ", command=StartAlgorithm, bg='green').grid(row=1, column=2, padx=5, pady=5)


root.mainloop()
