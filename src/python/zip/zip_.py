import zipfile
import tarfile

archive = zipfile.ZipFile('images.zip', 'r')
imgfile = archive.open('img_01.png')

fname = '.tar.gz'
if fname.endswith("tar.gz"):
    tar = tarfile.open(fname, "r:gz")
    tar.extractall()
    tar.close()
elif fname.endswith("tar"):
    tar = tarfile.open(fname, "r:")
    tar.extractall()
    tar.close()
