### Requirements
Clone this repository and install the required dependencies:
``` shell
git clone https://github.com/oshindow/mdd_grpc.git
cd mdd_grpc_client
pip install grpcio
```

Ensure your input audio is in the correct format. If necessary, convert it using `sox`:

Required Audio Format:

- sample rate: 16kHz
- bit depth: 16
- channel: 1

Convert Audio Using `sox`:
```shell
sox youraudio.wav -r 16000 -b 16 -c 1 youraudio_16k_16b_1c.wav
```

### API Response Format
The API returns a list of instances containing phonetic/pinyin recognition details. The response structure follows the format defined in the proto file:
```python
class Character_info():
    def __init__(self, reference=[], recognized=[], score_phone=[], reference_pinyin=[], recognized_pinyin=[], summary='', xmin=0, xmax=0):
        self.reference_phone = reference
        self.recognized_phone = recognized
        self.score_phone = score_phone 
        self.xmin = xmin
        self.xmax = xmax
        self.reference_pinyin = reference_pinyin
        self.recognized_pinyin = recognized_pinyin
        self.summary = summary
```
e.g.
- pinyin sequence: ['le2', 'le2', 'le4', 'qv1', 'xiang4', 'xiang4', 'tian1', 'ke1', 'bai2', 'mao2', 'fu2', 'li4', 'shui3', 'hong2', 'zhang3', 'bo1', 'qing1', 'bo1']

### Server Address & Ports
Server Address:
- smc-gpu1.d2.comp.nus.edu.sg

Ports & Services:
- 8888 for whisper-pinyin (Will **NOT** process with groundtruth text; random text is ok. e.g. text="啊啊啊")

- 8889 for Pitch-Aware RNN-T (Will **NOT** process with groundtruth text; random text is ok. e.g. text="啊啊啊")

- 8800 for Pitch-Aware RNN-T with score (Process with groundtruth text; requires exact groundtruth text)
### Running the Client

``` shell
python3 client_clean.py --wavepath /path/to/wavefile --text reference_text
```
### Usage
```
usage: client_clean.py [-h] [--wavepath WAVEPATH] [--text TEXT]

options:
  -h, --help           show this help message and exit
  --wavepath WAVEPATH  The path to wave file
  --text TEXT          The reference text
```
