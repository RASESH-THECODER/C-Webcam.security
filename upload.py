import cv2
import dropbox
import time
import random

start_time=time.time()
def take_snapshot():

    number=random.randint(0,100)
    videocaptureobject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videocaptureobject.read()
        img_name="img"+str(number)+".png_"
        cv2.imwrite(img_name,frame)
        result=False
    return img_name
    print("snapshot taken")    
    videocaptureobject.release()
    cv2.destroyAllWindows()

def upload_files(img_name):
    access_token='sl.AjqSR-rBp4AosepHjBh5Xuzr3C2uDxIhdkat8BzCnk0_Xp2nBrFU_lA9TEUv7uusBjO5WW3ODCozsXaLgg_GO3a5yKr6AsQ1ZOQW6MXxk1lfJ1YZcA9HyxiLfwEKFhVWr_hAQ6A'
    file=img_name
    file_from=file
    file_to="/newfolder1/"+(img_name)
    dbx=dropbox.Dropbox(access_token)

    with open(file_from,'rb')as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")

def main():
    while(True):
        if((time.time()-start_time)>=5):
            name=take_snapshot()
            upload_files(name)

main()
