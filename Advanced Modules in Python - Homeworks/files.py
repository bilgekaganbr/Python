#program that writes all .mp3, .pdf, and .txt files with their paths in C:/ directory to separate mp3_files, pdf_files,
#and txt_files respectively

#os module
import os

#open a file for mp3 files for just writing
with open("mp3_files.txt", "w", encoding="utf-8") as mp3_file:

    #loop for all the content in the C:/
    for folder_road, folder_name, file_name in os.walk("C:/"):

        #loop for all individual files
        for file in file_name:

            if file.endswith(".mp3"):

                #if the file is a mp3 file then write it to the mp3_files.txt
                mp3_file.write("Road: {} ------------------> File Name: {}\n".format(folder_road, file))

#same process for pdf files
with open("pdf_files.txt", "w", encoding="utf-8") as pdf_file:

    for folder_road, folder_name, file_name in os.walk("C:/"):

        for file in file_name:

            if file.endswith(".pdf"):

                pdf_file.write("Road: {} ------------------> File Name: {}\n".format(folder_road, file))

#same process for txt files
with open("txt_files.txt", "w", encoding="utf-8") as txt_file:

    for folder_road, folder_name, file_name in os.walk("C:/"):

        for file in file_name:

            if file.endswith(".txt"):

                txt_file.write("Road: {} ------------------> File Name: {}\n".format(folder_road, file))







