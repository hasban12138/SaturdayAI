import os
import subprocess  # 导入子进程模块
from pathlib import Path
import soundfile as sf
from transformers import AutoModel, AutoTokenizer
from flask import Flask, request, make_response
from paddlespeech.t2s.exps.syn_utils import get_am_output
from paddlespeech.t2s.exps.syn_utils import get_frontend
from paddlespeech.t2s.exps.syn_utils import get_predictor
from paddlespeech.t2s.exps.syn_utils import get_voc_output

app = Flask(__name__)

history = []

tokenizer = AutoTokenizer.from_pretrained("./module", trust_remote_code=True)
model = AutoModel.from_pretrained("./module", trust_remote_code=True)

am_inference_dir = "./voice"
voc_inference_dir = "./pwgan"
output_voice_dir = "./output/voice/"
device = "gpu"

# frontend
frontend = get_frontend(
    lang="mix",
    phones_dict=os.path.join(am_inference_dir, "phone_id_map.txt"),
    tones_dict=None,
)

# am_predictor
am_predictor = get_predictor(
    model_dir=am_inference_dir,
    model_file="fastspeech2_mix" + ".pdmodel",
    params_file="fastspeech2_mix" + ".pdiparams",
    device=device,
)

# voc_predictor
voc_predictor = get_predictor(
    model_dir=voc_inference_dir,
    model_file="pwgan_aishell3" + ".pdmodel",
    params_file="pwgan_aishell3" + ".pdiparams",
    device=device,
)


def prepare_model():
    global model
    model = model.half().quantize(4).cuda()
    model = model.eval()


prepare_model()


def predict(query, max_length, top_p, temperature):
    global history
    output, history = model.chat(
        tokenizer,
        query=query,
        history=history,
        max_length=max_length,
        top_p=top_p,
        temperature=temperature,
    )
    return output


@app.route("/chat", methods=["GET"])
def chat():
    # 接收文本
    text = request.args.get("Text", "")
    print(f"输入: {text}")

    if text == "清除":
        global history
        history.clear()
        outText = "已清除"
    else:
        # AI返回
        outText = predict(text, 2048, 0.7, 0.95)
    print(f"AI: {outText}")

    # 音频产生
    am_output_data = get_am_output(
        input=outText,
        am_predictor=am_predictor,
        am="fastspeech2_mix",
        frontend=frontend,
        lang="mix",
        merge_sentences=True,
        speaker_dict=os.path.join(am_inference_dir, "phone_id_map.txt"),
        spk_id=0,
    )
    wav = get_voc_output(voc_predictor=voc_predictor, input=am_output_data)
    sf.write(f"{output_voice_dir}output.wav", wav, samplerate=24000)

    # 微软的音频服务
    # command = f'edge-tts --voice zh-CN-XiaoyiNeural --text "{outText}" --write-media {output_voice_dir}output.wav'
    # subprocess.run(command, shell=True)
    # command = 'ffmpeg -y -i ./output.wav -ar 44100 ./out.wav'
    # os.system(command)

    # 返回数据
    rsp = make_response()
    rsp.headers.add_header("Text", outText.encode("utf-8"))
    # 响应body中写入音频数据
    with open(f"{output_voice_dir}output.wav", "rb") as f:
        rsp.set_data(f.read())
    return rsp


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8180)
