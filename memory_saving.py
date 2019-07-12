@profile
def read_rand_saving():
    with open("data_test/random_bytes", "rb") as source:
        content = source.read(1024 * 1000)
        content_to_write = memoryview(content)[1024:]
    print("Content length: %d, content to write length %d" % (len(content), len(content_to_write)))
    with open("data_test/random_write_saving", "wb") as target:
        target.write(content_to_write)
        
        
if __name__ == '__main__':
    read_rand_saving()
    
"""
read_rand_saving()
(tf_gpu) D:\Projects\Python_Learning>python -m memory_profiler memory_saving.py
Content length: 1024000, content to write length 1022976
Filename: memory_saving.py

Line #    Mem usage    Increment   Line Contents
================================================
     1   16.496 MiB   16.496 MiB   @profile
     2                             def read_rand_saving():
     3   16.496 MiB    0.000 MiB       with open("data_test/random_bytes", "rb") as source:
     4   17.477 MiB    0.980 MiB           content = source.read(1024 * 1000)
     5   17.492 MiB    0.016 MiB           content_to_write = memoryview(content)[1024:]
     6   17.496 MiB    0.004 MiB       print("Content length: %d, content to write length %d" % (len(content), len(content_to_write)))
     7   17.496 MiB    0.000 MiB       with open("data_test/random_write_saving", "wb") as target:
     8   17.496 MiB    0.000 MiB           target.write(content_to_write)

"""