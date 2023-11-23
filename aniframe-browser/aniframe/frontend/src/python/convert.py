# accepts file then generates new file/overwrites file
import os
import subprocess
print(os.listdir('/mount_dir'))

def convertAnf(str):
    
    with open('/mount_dir/sample.js', 'w') as f:
        f.write(str);
    
    f = open("/mount_dir/sample.js", "r")
    print(f.read())

    f.close()

    print("hello world")
    # subprocess.run(["echo", "hello"])

    # return str


    