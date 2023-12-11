#für images

import tkinter as tk

def handle_click(event):
    # Handle mouse click on a square
    clicked_square = event.widget
    # Update game state and visuals

# Create the main window
root = tk.Tk()
root.title("Board Game")

# Create a canvas for the game board
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Create game board squares and bind click events
for row in range(8):
    for col in range(8):
        color = "white" if (row + col) % 2 == 0 else "black"
        square = canvas.create_rectangle(col * 50, row * 50, (col + 1) * 50, (row + 1) * 50, fill=color)
        canvas.tag_bind(square, '<Button-1>', handle_click)

# Load the original image


# Display the resized image using canvas.create_image
# Example: Displaying a black king at position (0, 4)
white_king_sprite = canvas.create_image(4 * 50, 0 * 50, image="docs/MA/white_king.png")

# Display sprites using canvas.create_image
# Example: Displaying a white pawn at position (1, 2)


# Start the Tkinter event loop
root.mainloop()

#





