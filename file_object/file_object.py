
#file objects

f = open('test.txt', 'r')

print(f.name)
print(f.mode)
f.close()

with open('test.txt', 'r') as g:
    g_contents = g.read()
    print(g_contents)
    #Doesn't work with read and readlines at the same time.
    g_contents = g.readlines()
    print(g_contents)


with open('test.txt','r') as a:
    a_contents = a.readline()
    print(a_contents,end='')
    a_contents = a.readline()
    print(a_contents,end='')

    for line in a:
        print(line,end='')


with open('test.txt','r') as b:

    size_to_read = 100

    b_contents = b.read(size_to_read)
    print(b.tell())
    b.seek(0)
    while len(b_contents) > 0:
        print(b_contents,end='')
        b_contents = b.read(size_to_read)


print(g.closed)


with open('test2.txt','r') as rf:
    with open('test2_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

with open('mine.jpg','rb') as rf:
    with open('Ours.jpg', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)



