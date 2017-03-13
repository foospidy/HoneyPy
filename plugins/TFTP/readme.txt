TFTP HoneyPy plugin!

Basic functionality:
- When the client sends the get command, no matter what path/file the specify it will always return
  file.txt or file.bin, depending on the mode, e.g. netascii or octet.
- When the client sends the put command, the file will not be written to disk but will end up in logs,
  also there is a max file size allowed set by the MAX_UPLOAD_SIZE variable.
  
References to tftp related stuff:

- https://www.akamai.com/uk/en/multimedia/documents/state-of-the-internet/trivial-file-transfer-protocol-reflection-ddos-threat-advisory.pdf
