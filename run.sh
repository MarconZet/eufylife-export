tail -c +25 backup.ab | python -c "import zlib,sys;sys.stdout.write(zlib.decompress(sys.stdin.read()))" > backup.tar
tar -xvf backup.tar
python db_extractor.py
rm backup.tar