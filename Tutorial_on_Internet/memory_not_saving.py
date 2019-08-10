@profile
def read_rand():
    with open("data_test/random_bytes", "rb") as source:
        content = source.read(1024 * 1000)
        content_to_write = content[1024:]
    print("Content length: %d, content to write length %d" % (len(content), len(content_to_write)))
    with open("data_test/random_write", "wb") as target:
        target.write(content_to_write)
       
if __name__ == '__main__':
    read_rand()
    
        
        
        
"""
read_rand()
(tf_gpu) D:\Projects\Python_Learning>python -m memory_profiler memmory_saving.py
Content length: 1024000, content to write length 1022976
Filename: memmory_saving.py

Line #    Mem usage    Increment   Line Contents
================================================
     1   16.559 MiB   16.559 MiB   @profile
     2                             def read_rand():
     3   16.559 MiB    0.000 MiB       with open("data_test/random_bytes", "rb") as source:
     4   17.512 MiB    0.953 MiB           content = source.read(1024 * 1000)
     5   18.492 MiB    0.980 MiB           content_to_write = content[1024:]
     6   18.496 MiB    0.004 MiB       print("Content length: %d, content to write length %d" % (len(content), len(content_to_write)))
     7   18.496 MiB    0.000 MiB       with open("data_test/random_write", "wb") as target:
     8   18.496 MiB    0.000 MiB           target.write(content_to_write)

"""