### Requirement
``` shell
git clone https://github.com/oshindow/mdd_grpc.git
cd mdd_grpc_client
pip install grpcio
```

Input audio: 

- sample rate: 16kHz
- bit depth: 16
- channel: 1

convert tool: sox 
```shell
sox youraudio.wav -r 16000 -b 16 -c 1 youraudio_16k_16b_1c.wav
```

Output:
- pinyin sequence: ['le2', 'le2', 'le4', 'qv1', 'xiang4', 'xiang4', 'tian1', 'ke1', 'bai2', 'mao2', 'fu2', 'li4', 'shui3', 'hong2', 'zhang3', 'bo1', 'qing1', 'bo1']

### Run

``` shell
python3 client_clean.py --wavepath /path/to/wavefile --text reference_text

usage: client.py [-h] [--wavepath WAVEPATH] [--text TEXT]

options:
  -h, --help           show this help message and exit
  --wavepath WAVEPATH  The path to wave file
  --text TEXT          The reference text
```
