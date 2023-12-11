import tkinter as tk

def save_canvas_as_image(canvas, filename):
    canvas.postscript(file=filename, colormode='color')

def display_snapshot():
    image_label = tk.Label(root)
    image_label.image = tk.PhotoImage(file='canvas_image.png')
    image_label.config(image=image_label.image)
    image_label.grid(row=0, column=0)  # Adjust row and column as needed

def exit_program():
    save_canvas_as_image(canvas, 'canvas_image.png')
    display_snapshot()
    root.quit()

root = tk.Tk()
root.title("Canvas Snapshot Example")

canvas = tk.Canvas(root, width=400, height=400)
canvas.grid(row=1, column=0, padx=10, pady=10)

# Draw on the canvas as needed
canvas.create_rectangle(50, 50, 200, 200, fill="blue")
canvas.create_text(100, 100, text="Hello, Canvas!")

exit_button = tk.Button(root, text="Exit", command=exit_program)
exit_button.grid(row=50, column=50)  # Adjust row and column as needed

root.mainloop()