mkdir tmp
cp "$1" tmp/backup.ab
tail -c +25 tmp/backup.ab | python -c "import zlib,sys;sys.stdout.write(zlib.decompress(sys.stdin.read()))" > tmp/backup.tar
tar -xvf tmp/backup.tar --directory tmp
python db_extractor.py
rm -r tmp
