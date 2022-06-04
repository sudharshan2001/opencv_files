import cv2, os, glob
import numpy as np
import pandas as pd

 
def yolo_to_csv(width=width,height=height,annotation_files=annotation_file_path,classes=classes):
    '''
        width: width of the image
        height: height of the image
        annotation_files: path to annotation files
        classes: classes files in list
    '''
    myFiles = glob.glob(annotation_files)
    classes=classes

    width=width
    height=height
    image_id=0
    
    final_df=[]
    for item in myFiles:

        image_id+=1
        with open(item, 'rt') as fd:
            for line in fd.readlines():
                row = []
                bbox_temp = []
                splited = line.split()
                try:
                    row.append(classes[int(splited[0])])

                    row.append(float(splited[1]))
                    row.append(float(splited[2]))
                    row.append(float(splited[3]))
                    row.append(float(splited[4]))
                    row.append(item[:-4]+".jpg")
                    row.append(width)
                    row.append(height)
                    row.append(width*float(splited[1]))
                    row.append(height*float(splited[2]))
                    row.append((width*float(splited[3]))+(width*float(splited[1])))
                    row.append((height*float(splited[4]))+(height*float(splited[2])))
                    final_df.append(row)

                except:
                    pass
    df = pd.DataFrame(final_df, columns=['label','x','y','w','h','path','img_width','img_height','xmin','ymin', 'xmax','ymax'])
    return df

df = yolo_to_csv()
df.to_csv('converted_csv_file.csv')
