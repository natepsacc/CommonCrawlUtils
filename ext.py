import warc
f = warc.open("TEST-000001.extracted.warc.gz")
for record in f:
  print (record.payload.read())
