#board zeichnen

import tkinter as tk

root = tk.Tk()
root.title("Schach Luis")

# Create a canvas for the game board
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Create game board squares and bind click events
for row in range(8):
    for col in range(8):
        color = "white" if (row + col) % 2 == 0 else "black"
        square = canvas.create_rectangle(col * 50, row * 50, (col + 1) * 50, (row + 1) * 50, fill=color)

# Start the Tkinter event loop
root.mainloop()

#to close window
#root.destroy()
