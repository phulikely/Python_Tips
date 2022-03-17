image_file_listttttttt = ['ce48c536b7254cd0add327fb5710f741_16032022122417.jpg',
                          'a9f4db38af66479f94b2eeddc2fbb56b_16032022122417.jpg',
                          '1c7cb964c3d24fa69add077af144ee7d_16032022121335.jpg']

image_file_listttttttt = str(image_file_listttttttt)
image_file_listttttttt = image_file_listttttttt.replace('[', '').replace(']', '').replace("'", "").replace(' ', '')
image_file_listttttttt = image_file_listttttttt.split(',')
print(image_file_listttttttt[0])
print(image_file_listttttttt[1])
print(image_file_listttttttt[2])
print(len(image_file_listttttttt))
print(image_file_listttttttt[3])
