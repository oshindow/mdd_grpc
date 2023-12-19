import grpc
import service_pb2
import service_pb2_grpc
import argparse

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--wavepath",
        type=str,
        help="""The path to wave file""",
    )
    parser.add_argument(
        "--text",
        type=str,
        help="The reference text ",
    )
    return parser.parse_args()

def run(args):
    channel = grpc.insecure_channel('host:port')
    stub = service_pb2_grpc.ServiceStub(channel)
    
    wavepath = args.wavepath
    with open(wavepath, 'rb') as wave_file:
        # Read all frames from the waveform
        bytes_data = wave_file.read()

    text = args.text
    print(text)
    
    request = service_pb2.Request(waveform=bytes_data, text=text)
    response = stub.Recognize(request)

    result = {'results': []}
    for char_info in response.scored_character:
        result['results'].append(
            { 
                "character": " ".join(char_info.reference_phone),
                "char_score": round((char_info.score_phone[0] + char_info.score_phone[1]) // 2, 1),
                "phone_list":[{
                    "onsite": char_info.xmin,
                    "offsite": char_info.xmax,
                    "pinyin": " ".join(char_info.recognized_phone),
                    }]
            }
        )
        
    print(result)

if __name__ == '__main__':
    args = get_args()
    run(args)
