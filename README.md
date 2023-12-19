# mdd_grpc_client
``` shell
git clone https://github.com/oshindow/mdd_grpc.git
cd mdd_grpc_client
pip install grpcio
```

**Modify the server address and port in `client.py`**

``` shell
python3 client.py --wavepath /path/to/wavefile --text reference_text

usage: client.py [-h] [--wavepath WAVEPATH] [--text TEXT]

options:
  -h, --help           show this help message and exit
  --wavepath WAVEPATH  The path to wave file
  --text TEXT          The reference text
```
