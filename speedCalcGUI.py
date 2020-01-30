from tkinter import *
import numpy as np


def main_screen():
    screen = Tk()
    # screen.geometry("300x250")
    screen.title("Speed Calculator")

    # Label(text="Speed Calc 1.0", width="100",
    #       height="2", font=("Calibri", 13)).grid(row=1, column=1)

    speed = Label(text="Speedtest")
    mlab = Label(text="MLab Test")
    jperf = Label(text="Jperf Test")

    Label(text="test 1").grid(row=0, column=1)
    Label(text="test 2").grid(row=0, column=2)
    Label(text="test 3").grid(row=0, column=3)

    speed.grid(row=1, column=0)
    mlab.grid(row=2, column=0)
    jperf.grid(row=3, column=0)

    s1 = Entry(screen)
    s1.grid(row=1, column=1)
    s2 = Entry(screen)
    s2.grid(row=1, column=2)
    s3 = Entry(screen)
    s3.grid(row=1, column=3)

    m1 = Entry(screen)
    m1.grid(row=2, column=1)
    m2 = Entry(screen)
    m2.grid(row=2, column=2)
    m3 = Entry(screen)
    m3.grid(row=2, column=3)

    j1 = Entry(screen)
    j1.grid(row=3, column=1)
    j2 = Entry(screen)
    j2.grid(row=3, column=2)
    j3 = Entry(screen)
    j3.grid(row=3, column=3)

    def answer():
        speedtest = []
        mlab = []
        jperf = []

        speedone = float(s1.get())
        speedtwo = float(s2.get())
        speedthree = float(s3.get())
        speedtest.append(speedone)
        speedtest.append(speedtwo)
        speedtest.append(speedthree)

        mOne = float(m1.get())
        mTwo = float(m2.get())
        mThree = float(m3.get())

        mlab.append(mOne)
        mlab.append(mTwo)
        mlab.append(mThree)

        jpOne = float(j1.get())
        jpTwo = float(j2.get())
        jpThree = float(j3.get())

        jperf.append(jpOne)
        jperf.append(jpTwo)
        jperf.append(jpThree)

        average_speed = np.average(speedtest)
        average_mlab = np.average(mlab)
        average_jperf = np.average(jperf)
        answer = f"\n Speedtest average:{average_speed} \n "
        mlab_answer = f"MLab average:{average_mlab}"
        official_data = str(
            f"{answer}{mlab_answer} \n Jperf average:{average_jperf}")
        result.insert(INSERT, official_data)

    Button(text="Calculate", command=answer,bg="#39A2C9",fg="white").grid(row=4, column=2)

    result = Text(screen)
    result.grid(row=5, columnspan=4)

    screen.mainloop()


main_screen()
