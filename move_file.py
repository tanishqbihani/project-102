import shutil
import os


from_dir ="F:\project white hat\Test_for_file_separation"
to_dir="F:\project white hat\Destination_for_test"
list_of_files=os.listdir(from_dir)

#moving all images and text in separate folders
for file_name in list_of_files:

    name,extension = os.splitext(file_name)

    if extension == " ":
        continue
    if extension in ['.png','.jpg','.jpeg']:
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/image_files/'
        path3 = to_dir + '/image_files/' + file_name

        print(path1)
        print(path3)

        if os.path.exists(path2):
            print("moving file" + file_name)
            shutil.move(path1,path3)

        else:
            os.makedirs(path2)
            print("moving file" + file_name)
            shutil.move(path1,path3)
        