import tkinter as tk
import serial
num = int(input("Enter the number of the port: "))
ser = serial.Serial(f"/dev/ttyACM{num}", 115200, timeout=1)
print("connected to: ", ser.portstr)
def foo():
    print("On!")
    
    ser.write(b'gpio mode PA7 1\n\r')
    ser.write(b'gpio set PA7 1 1\n\r')

def bar():
    print("Off!")
    ser.write(b'gpio mode PA7 1\n\r')
    ser.write(b'gpio set PA7 0\n\r')

# Create the main window
window = tk.Tk()
window.title("Led Control")
window.geometry("300x200")

# Create buttons
button_foo = tk.Button(window, text="On", command=foo)
button_foo.pack(pady=10)

button_bar = tk.Button(window, text="Off", command=bar)
button_bar.pack(pady=10)

# Start the Tkinter event loop
window.mainloop()
