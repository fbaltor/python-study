import sys
import tarfile


def main(argv):

    input = argv[1]
    if tarfile.is_tarfile(input):
        tar = tarfile.open(input)

        members = tar.getmembers()
        names = tar.getnames()

        print(tar.name)
        parts = tar.name.split('/')

        firm_filename = parts[-1]
        print(firm_filename)

        firm_name = firm_filename.split('.')[0]
        print(firm_name)

        firmware = tar.name.split('/')[-1].split('.')[0]
        print(firmware)



if __name__ == '__main__':
    main(sys.argv)
