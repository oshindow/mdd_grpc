import grpc
import service_pb2
import service_pb2_grpc
import argparse

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--wavepath",
        type=str,
        default="test.wav",
        help="""The path to wave file""",
    )
    parser.add_argument(
        "--text",
        type=str,
        default="鹅鹅鹅曲项向天歌白毛浮绿水红掌拨清波",
        help="The reference text ",
    )
    return parser.parse_args()

def run(args):
    channel = grpc.insecure_channel('smc-gpu1.d2.comp.nus.edu.sg:8889')
    stub = service_pb2_grpc.ServiceStub(channel)
    
    wavepath = args.wavepath
    with open(wavepath, 'rb') as wave_file:
        # Read all frames from the waveform
        bytes_data = wave_file.read()

    text = args.text
    print(wave_file)
    
    request = service_pb2.Request(waveform=bytes_data, text='')
    response = stub.Recognize(request)
        
    recognized_pinyins = [res.recognized_pinyin for res in response.scored_character]
    print(recognized_pinyins)

if __name__ == '__main__':
    args = get_args()
    run(args)

