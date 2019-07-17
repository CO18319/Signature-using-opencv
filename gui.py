from tkinter import *
import time
import pymysql
import cv2
import numpy as np
from collections import deque
from PIL import Image

url_sign = r"/home/deepinder/PycharmProjects/untitled/sign2.gif"
url_pic = r"/home/deepinder/PycharmProjects/untitled/car2.gif"


fread = open("count.txt", "r")
x = fread.read()
fread.close()
co = int(x, 9)

root = Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.config(bg='RoyalBlue4')
root.title("Registration")
#
Tops = Frame(root, width=w, height=5, relief=SUNKEN)
Tops.pack(side=TOP)
Tops.config(bg='RoyalBlue4')

f1 = Frame(root, width=w, height=1600)
f1.pack(side=LEFT)
f1.config(bg='RoyalBlue4')
#
localtime = time.asctime(time.localtime(time.time()))
lblinfo = Label(Tops, font=('Helvetica ', 30, 'bold'), bg='RoyalBlue4', text="Registration Form", fg="white", bd=10)
lblinfo.grid(row=0, column=0)
lblinfo = Label(Tops, font=('Helvetica ', 20), bg='RoyalBlue4', text=localtime, fg="white")
lblinfo.grid(row=1, column=0)
#
lblname = Label(f1, font=('Helvetica', 16, 'bold'), text="FIRST NAME", bg='RoyalBlue4', fg="White", bd=10, anchor='w')
lblname.grid(row=1, column=0)
txtname = Entry(f1, font=('Helvetica', 16), fg='Gray20', bd=6, insertwidth=4, bg="white", justify='left')
txtname.grid(row=1, column=3)

lbllname = Label(f1, font=('Helvetica', 16, 'bold'), text="LAST NAME", bg='RoyalBlue4', fg="White", bd=10, anchor='w')
lbllname.grid(row=2, column=0)
txtlname = Entry(f1, font=('Helvetica', 16), bd=6, fg='Gray20', insertwidth=4, bg="white", justify='left')
txtlname.grid(row=2, column=3)

lbld = Label(f1, font=('Helvetica', 16, 'bold'), text="DOB", bg='RoyalBlue4', fg="White", bd=10, anchor='w')
lbld.grid(row=3, column=0)
txtd = Entry(f1, font=('Helvetica', 16), fg='Gray20', bd=6, insertwidth=4, bg="white", justify='left')
txtd.grid(row=3, column=3)
txtd.insert(0, "dd/mm/yyyy")

lble = Label(f1, font=('Helvetica', 16, 'bold'), text="Email ID", bg='RoyalBlue4', fg="White", bd=10, anchor='w')
lble.grid(row=4, column=0)
txte = Entry(f1, font=('Helvetica', 16), fg='Gray20', bd=6, insertwidth=4, bg="white", justify='left')
txte.grid(row=4, column=3)

lblac = Label(f1, font=('Helvetica', 16, 'bold'), text="ADHAAR NUMBER", bg='RoyalBlue4', fg="White", bd=10, anchor='w')
lblac.grid(row=5, column=0)
txtac = Entry(f1, font=('Helvetica', 16), fg='Gray20', bd=6, insertwidth=4, bg="white", justify='left')
txtac.grid(row=5, column=3)
txtac.insert(0, "do not enter spaces")

#

def exw():
    root.destroy()


def ttnw():
    ###########################################################################################################################################################
    roo = Toplevel(bg='Moccasin')
    roo.title("Photo & Signature")
    w1, h1 = roo.winfo_screenwidth(), roo.winfo_screenheight()
    roo.geometry("%dx%d+0+0" % (w1, h1))

    pic = 1

    def exitw():
        roo.destroy()

    def signw():
        fread = open("count.txt", "r")
        x = fread.read()
        fread.close()
        co = int(x, 9)
        start = 1
        count = 0
        done = 0
        found = 0
        plot = 0

        if __name__ == '__main__':

            img = np.zeros((512, 512, 3), np.uint8)
            cap = cv2.VideoCapture(0)
            points = deque(maxlen=1024)
            # points2 = deque(maxlen=512)

            kernel = np.ones((5, 5), np.uint8)
            while True:
                ret, frame = cap.read()
                frame = cv2.flip(frame, 1)

                if done != 1:
                    roi = frame[100:470]
                    # roi2 = frame[100:350, 60:600]

                colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 255, 255)]
                frame = cv2.rectangle(frame, (1, 160), (65, 255), colors[2], -1)
                frame = cv2.rectangle(frame, (570, 160), (635, 255), colors[2], -1)
                frame = cv2.rectangle(frame, (65, 100), (570, 350), colors[2], 3)
                frame = cv2.rectangle(frame, (250, 410), (380, 470), colors[2], -1)

                cv2.putText(frame, "START", (10, 185), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
                cv2.putText(frame, "DONE", (580, 185), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
                cv2.putText(frame, "RETAKE", (270, 440), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

                hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

                if not ret:
                    break

                '''
                lower_green = np.array([65,60,60])
                upper_green = np.array([80,255,255])
                '''

                lower_green = np.array([110, 153, 69])
                upper_green = np.array([179, 255, 255])

                '''lower_blue = np.array([69, 94, 196])
                upper_blue = np.array([179, 255, 255])
                '''

                lower_blue = np.array([62, 45, 5])
                upper_blue = np.array([97, 255, 66])

                # a threshold for the hsv image to get only green colours
                mask_green = cv2.inRange(hsv, lower_green, upper_green)
                mask_green = cv2.erode(mask_green, kernel, iterations=2)
                mask_green = cv2.morphologyEx(mask_green, cv2.MORPH_OPEN, kernel)
                mask_green = cv2.dilate(mask_green, kernel, iterations=1)

                # bue mask
                mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
                mask_blue = cv2.erode(mask_blue, kernel, iterations=2)
                mask_blue = cv2.morphologyEx(mask_blue, cv2.MORPH_OPEN, kernel)
                mask_blue = cv2.dilate(mask_blue, kernel, iterations=1)

                # green contour
                contours, hier = cv2.findContours(mask_green, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

                # blue contour
                contours_blue, hier2 = cv2.findContours(mask_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

                center = None
                center_blue = None

                if len(contours) > 0:
                    # Sort the contours and find the largest one -- we
                    # will assume this contour correspondes to the area of the bottle cap
                    cnt = sorted(contours, key=cv2.contourArea, reverse=True)[0]
                    # Get the radius of the enclosing circle around the found contour
                    # find the circumcircle of an object using the function cv2.minEnclosingCircle().It is a circle which completely covers the object with minimum area.
                    ((x, y), radius) = cv2.minEnclosingCircle(cnt)
                    # Draw the circle around the contour
                    cv2.circle(roi, (int(x), int(y)), int(radius), (0, 255, 255), 2)
                    # Get the moments to calculate the center of the contour (in this case Circle)
                    # function cv2.moments() gives a dictionary of all moment values calculated
                    M = cv2.moments(cnt)
                    #cx = int(M['m10'] / M['m00'])
                    #cy = int(M['m01'] / M['m00'])
                    center = (int(M['m10'] / M['m00']), int(M['m01'] / M['m00']))
                    points.appendleft(center)

                if count == 1:
                    if start == 1:
                        while len(points) > 1:
                            points.pop()
                            points.popleft()
                            start = 0

                    else:
                        for i in range(1, len(points)):
                            if points[i - 1] is None or points[i] is None:
                                continue
                            elif (points[i - 1][0] <= 170 and points[i][0] <= 170) or (
                                    points[i - 1][0] >= 500 and points[i][0] >= 500):
                                continue
                            else:
                                cv2.line(roi, points[i - 1], points[i], (0, 0, 255), 6)
                                cv2.line(img, points[i - 1], points[i], (0, 0, 255), 6)
                                plot = 1

                if len(contours_blue) > 0:
                    cnt2 = sorted(contours_blue, key=cv2.contourArea, reverse=True)[0]
                    ((x_b, y_b), radius_b) = cv2.minEnclosingCircle(cnt2)
                    cv2.circle(roi, (int(x_b), int(y_b)), int(radius_b), (0, 255, 255), 2)
                    found = 1
                    M_b = cv2.moments(cnt2)
                    cx_b = int(M_b['m10'] / M_b['m00'])
                    cy_b = int(M_b['m01'] / M_b['m00'])
                    center = (int(M_b['m10'] / M_b['m00']), int(M_b['m01'] / M_b['m00']))

                    if cx_b >= 260 and cx_b <= 410 and cy_b >= 300 and cy_b <= 350:
                        if start != 1:
                            '''while len(points)>0:
                                points.pop()
                                points.popleft()
                            '''
                            # cap.release()
                            # cv2.destroyAllWindows()
                            start = 1
                            img = np.zeros((512, 512, 3), np.uint8)
                            frame = cv2.resize(frame, (640, 480))
                            img = cv2.resize(img, (640, 480))
                            Signature = np.concatenate((frame, img), axis=1)
                            cv2.imshow("Signature", Signature)

                    if cx_b >= 0 and cx_b <= 100 and cy_b >= 70 and cy_b <= 150:
                        if start == 1:
                            count = 1

                    elif cx_b >= 570 and cx_b <= 635 and cy_b >= 160 and cy_b <= 255:
                        if start != 1:
                            done = 1
                            cv2.imwrite("Sign{}.png".format(co), img)
                            co = co + 1
                            cap.release()
                            cv2.destroyAllWindows()

                if found == 1 and start == 0 and plot == 1:
                    while len(points) > 1:
                        points.pop()
                        points.popleft()
                        found = 0

                frame = cv2.resize(frame, (640, 480))
                img = cv2.resize(img, (640, 480))
                Signature = np.concatenate((frame, img), axis=1)
                cv2.imshow("Signature", Signature)
                key = cv2.waitKey(1)
                if key == 27:
                    break
            x = str(co)
            fwrite = open("count.txt", "w")
            fwrite.write(x)
            fwrite.close()
            cap.release()
            cv2.destroyAllWindows()


            image2 = Image.open('white.jpg')
            image2.save('white.gif')
            photo2 = PhotoImage(file="sign2.gif")
            wr2 = Label(ff2, image=photo2, width=600, height=450)
            wr2.grid(row=1, column=2)
            ff2.update_idletasks()
            return

    def picw():
        video_capture = cv2.VideoCapture(0)
        cv2.namedWindow("Smile!")
        while True:
            # Captures video_capture frame by frame
            ret, frame = video_capture.read()
            frame=cv2.flip(frame,1)
            cv2.imshow("Smile!", frame)
            if not ret:
                break
            # The control breaks once q key is pressed
            k = cv2.waitKey(1)
            if k % 256 == 32:
                # SPACE pressed
                cv2.imwrite("DP{}.png".format(co), frame)
                break

        # Release the capture once all the processing is done.
        video_capture.release()
        cv2.destroyAllWindows()


        if pic==0:
            image = Image.open('DP1.png')
            image.save('DP1.gif')
            photo3 = PhotoImage(file="DP1.gif")
            wr = Label(ff1,image=photo3,width=600, height=450)
            #wr.config(image=photo3)
            wr.grid(row=1, column=1)
            ff1.update_idletasks()
            #return

    def nxtw():
        ###########################################################################################################################################################
        db = pymysql.connect("localhost", "root", "", "ccet")
        cursor = db.cursor()
        sql = "INSERT INTO STUDENT VALUES('%s','%s','%s','%s','%s','%s','%s')" % (
        txtname.get(), txtlname.get(), txtd.get(), txtac.get(), txte.get(), url_pic + x,
        url_sign + x)
        cursor.execute(sql)
        db.commit()
        db.close()
        #third window
        las = Toplevel(bg='RoyalBlue4')
        las.title("Details")
        w2, h2 = las.winfo_screenwidth(), roo.winfo_screenheight()
        las.geometry("%dx%d+0+0" % (w2, h2))

        def submitw():
            #
            url_sign1 = "/home/deepinder/PycharmProjects/untitled/sign2.gif"
            url_pic1 = "/home/deepinder/PycharmProjects/untitled/car2.gif"

            '''ff4 = Frame(las, width=w, height=1600)
            ff4.pack(side=LEFT)
            ff4.config(bg='RoyalBlue4')
            '''
            lblname1 = Label(las, font=('Helvetica', 16, 'bold'), text="FIRST NAME", bg='RoyalBlue4', fg="White", bd=10,
                             anchor='w')
            lblname1.grid(row=1, column=0)
            txtname1 = Label(las, font=('Helvetica', 16), fg='Gray20', bd=6, text=txtname.get(), bg="white")
            txtname1.grid(row=1, column=3)

            lbllname1 = Label(las, font=('Helvetica', 16, 'bold'), text="LAST NAME", bg='RoyalBlue4', fg="White", bd=10,
                              anchor='w')
            lbllname1.grid(row=2, column=0)
            txtname2 = Label(las, font=('Helvetica', 16), fg='Gray20', bd=6, text=txtlname.get(), bg="white")
            txtname2.grid(row=2, column=3)

            lbld1 = Label(las, font=('Helvetica', 16, 'bold'), text="DOB", bg='RoyalBlue4', fg="White", bd=10,
                          anchor='w')
            lbld1.grid(row=3, column=0)
            txtd1 = Label(las, font=('Helvetica', 16), fg='Gray20', bd=6, text=txtd.get(), bg="white")
            txtd1.grid(row=3, column=3)

            lble1 = Label(las, font=('Helvetica', 16, 'bold'), text="Email ID", bg='RoyalBlue4', fg="White", bd=10,
                          anchor='w')
            lble1.grid(row=4, column=0)
            txte1 = Label(las, font=('Helvetica', 16), fg='Gray20', bd=6, text=txte.get(), bg="white")
            txte1.grid(row=4, column=3)

            lblac1 = Label(las, font=('Helvetica', 16, 'bold'), text="AADHAAR NUMBER", bg='RoyalBlue4', fg="White",
                           bd=10, anchor='w')
            lblac1.grid(row=5, column=0)
            txtac1 = Label(las, font=('Helvetica', 16), fg='Gray20', bd=6, text=txtac.get(), bg="white")
            txtac1.grid(row=5, column=3)

            '''image = Image.open(url_pic1 + x + ".png")
            image.save("DP" + x + ".gif")
            '''
            image = Image.open(url_pic1)
            image.save("DP" + x + ".gif")

            '''image2 = Image.open(url_sign1 + x + ".png")
            image2.save("Sign" + x + ".gif")
            '''
            image2 = Image.open(url_sign1)
            image2.save("Sign" + x + ".gif")

            #ff5 = Frame(las, width=w, height=1600)
            #ff5.pack(side=RIGHT)
            #ff5.config(bg='RoyalBlue4')

            piclbl = PhotoImage(file="sign2.gif")
            p1 = Label(las, image=piclbl)
            p1.grid(row=0, column=1)
            piclb2 = PhotoImage(file="car2.gif")
            p2 = Label(las, image=piclb2)
            p2.grid(row=0, column=2)
            #

        btnsub = Button(las, padx=20, pady=16, bd=10, fg="RED4", font=(50), width=10, text="Submit", bg="Snow",
                        command=submitw)
        btnsub.grid(row=0, column=0)
        las.mainloop()

    ff = Frame(roo, width=w, height=10)
    ff.pack(side=TOP)
    ff.config(bg='Moccasin')

    ff1 = Frame(roo, width=w, height=1600)
    ff1.pack(side=LEFT)
    ff1.config(bg='Moccasin')

    ff2 = Frame(roo, width=w, height=1600)
    ff2.pack(side=RIGHT)
    ff2.config(bg='Moccasin')

    ff3 = Frame(roo, width=w, height=1600)
    ff3.pack(side=BOTTOM)
    ff3.config(bg='Moccasin')

    lblinfo2 = Label(ff, font=('Helvetica ', 30, 'bold'), bg='Moccasin', text="Photo and Signature", fg="white",
                     bd=10)
    lblinfo2.grid(row=0, column=1)


    lblinfo2w = Label(ff3, font=('Helvetica ', 30, 'bold'), bg='Moccasin', text="", fg="white",
                     bd=10)
    lblinfo2w.grid(row=1, column=1)

    if pic==1:
        image = Image.open('white.jpg')
        image.save('white.gif')
        photo1 = PhotoImage(file="white.gif")
        wr = Label(ff1, image=photo1, width=600, height=450)
        wr.image = photo1
        wr.grid(row=1, column=1)

        image2 = Image.open('white.jpg')
        image2.save('white.gif')
        photo2 = PhotoImage(file="white.gif")
        wr2 = Label(ff2, image=photo2, width=600, height=450)
        wr2.grid(row=1, column=2)

        pic = 0



    btnph = Button(roo, padx=20, pady=16, bd=10, fg="Green", font=(50), width=10, text="Take Photo", bg="Snow",
                   command=picw)
    #btnph.grid(row=2, column=0)
    btnph.place(x=150,y=170)
    btnsi = Button(roo, padx=20, pady=16, bd=10, fg="Green", font=(50), width=10, text="Put Signature", bg="Snow",
                   command=signw)
    #btnsi.grid(row=2, column=2)
    btnsi.place(x=1480, y=170)
    btnsub = Button(ff3, padx=20, pady=16, bd=10, fg="Green", font=(50), width=10, text="Submit", bg="Snow",
                    command=nxtw)
    btnsub.grid(row=0, column=1)
    btnexit = Button(ff3, padx=20, pady=16, bd=10, fg="RED4", font=(50), width=10, text="Exit", bg="Snow",
                     command=exitw)
    btnexit.grid(row=0,column=0)
    roo.mainloop()


###########################################################################################################################################################

btnex = Button(f1, padx=20, pady=16, bd=10, fg="Green", font=(50), width=10, text="Next", bg="Snow", command=ttnw)
btnex.grid(row=7, column=8)
btnexit = Button(f1, padx=20, pady=16, bd=10, fg="RED4", font=(50), width=10, text="Exit", bg="Snow", command=exw)
btnexit.grid(row=7, column=7)

root.mainloop()
###########################################################################################################################################################