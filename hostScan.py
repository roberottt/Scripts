import subprocess as sp

def main():
    i = 2
    while(i < 254):
        try:
            sp.run(["ping", "-c", "1", "192.168.1.{}".format(i)], timeout=1)
            i += 1
        except:
            pass
main()