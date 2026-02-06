from rembg import remove

input_path ="Squirrel.jpg"
output_path ="output.png"

with open (input_path,"rb") as i:
    with open (output_path,"wb") as o:
        input = i.read()
        output_file = remove(input)
        o.write(output_file)




