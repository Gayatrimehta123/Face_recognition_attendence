from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class Face_Recognition_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1280x720+0+0")
        self.root.title("face Recognition System")

         #firstimg
        img=Image.open(r"C:\Users\gayat\OneDrive\Desktop\pythonprojectimages\face_header_pc.jpg")
        img=img.resize((426,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=426,height=130)

        #secondimg
        img1=Image.open(r"C:\Users\gayat\OneDrive\Desktop\pythonprojectimages\face_header_pc.jpg")
        img1=img1.resize((426,130),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=426,y=0,width=426,height=130)


        #thirdimg
        img2=Image.open(r"C:\Users\gayat\OneDrive\Desktop\pythonprojectimages\face_header_pc.jpg")
        img2=img2.resize((426,130),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=852,y=0,width=426,height=130)


        img3=Image.open(r"C:\Users\gayat\OneDrive\Desktop\pythonprojectimages\face-recognition.jpg")
        img3=img3.resize((1280,590),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1280,height=590)

         
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM    ",font=("times new roman",35,"bold"),bg="blue",fg="white",anchor="center")
        title_lbl.place(x=0,y=0,width=1280,height=45)
        title_lbl.config(anchor="center")


        #button
        img4=Image.open(r"C:\Users\gayat\OneDrive\Desktop\pythonprojectimages\img1.webp")
        img4=img4.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,cursor="hand2")
        b1.place(x=80, y=100, width=220, height=220)

        b1=Button(bg_img,text="Student Details",cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white",anchor="center")
        b1.place(x=80, y=300, width=220, height=40)



        img5=Image.open(r"C:\Users\gayat\OneDrive\Desktop\pythonprojectimages\images (2).jpeg")
        img5=img5.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b2=Button(bg_img,image=self.photoimg5,cursor="hand2")
        b2.place(x=380, y=100, width=220, height=220)

        b2=Button(bg_img,text="Face Recognition",cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white",anchor="center")
        b2.place(x=380, y=300, width=220, height=40)


        #attendence 

        img6=Image.open(r"C:\Users\gayat\OneDrive\Desktop\pythonprojectimages\images.jpeg")
        img6=img6.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b3=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b3.place(x=680, y=100, width=220, height=220)
        b3=Button(bg_img,text="Student Details",cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white",anchor="center")
        b3.place(x=680, y=300, width=220, height=40)



        #chatbot
        img7=Image.open(r"C:\Users\gayat\OneDrive\Desktop\pythonprojectimages\images (3).jpeg")
        img7=img7.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b4=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b4.place(x=980, y=100, width=220, height=220)
        b4=Button(bg_img,text="Help Desk",cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white",anchor="center")
        b4.place(x=980, y=300, width=220, height=40)


        

        img8=Image.open(r"C:\Users\gayat\OneDrive\Desktop\pythonprojectimages\blog67.webp")
        img8=img8.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b5=Button(bg_img,image=self.photoimg8,cursor="hand2")
        b5.place(x=80, y=370, width=220, height=220)

        b5=Button(bg_img,text="Student Details",cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white",anchor="center")
        b5.place(x=80, y=570, width=220, height=40)



        img9=Image.open(r"C:\Users\gayat\OneDrive\Desktop\pythonprojectimages\images.png")
        img9=img9.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b6=Button(bg_img,image=self.photoimg9,cursor="hand2")
        b6.place(x=380, y=370, width=220, height=220)
        b6=Button(bg_img,text="Student Details",cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white",anchor="center")
        b6.place(x=380, y=570, width=220, height=40)





        img10=Image.open(r"C:\Users\gayat\OneDrive\Desktop\pythonprojectimages\images.jpeg")
        img10=img10.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b7=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b7.place(x=680, y=370, width=220, height=220)
        b7=Button(bg_img,text="Student Details",cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white",anchor="center")
        b7.place(x=680, y=570, width=220, height=40)

        


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_system(root)
    root.mainloop()     