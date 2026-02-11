# 星期六

[中文](../../README.md) | English

## About

Author: [此号已封12138](https://space.bilibili.com/40358750)

Demo: [花费时间两周半 ChatGLM(清华源)+语音生成+L2D 的对话AI【此号已封】](https://www.bilibili.com/video/BV1SV4y1D7fG)

References:

[【保姆级教程】教你使用群友语音快速得到一个AI群友 | 基于paddlespeech项目训练AI语音合成模型](https://www.bilibili.com/video/BV15e4y1c7ci)

[【AI虚拟主播】B站第一个开源的自主学习的虚拟主播！](https://www.bilibili.com/video/BV1WP411Z7qu) 

[AI-Vtuber](https://github.com/XzaiCloud/AI-Vtuber)

[【ChatGLM】本地版ChatGPT？6G显存可用！ChatGLM-6B 清华开源模型一键包发布 可更新](https://www.bilibili.com/video/BV1E24y1u7Go) 

 [ChatGLM-webui](https://github.com/Akegarasu/ChatGLM-webui)

[【有手就行】使用你自己的声音做语音合成](https://aistudio.baidu.com/aistudio/projectdetail/5003396)

[【有手就行】使用自己的声音做语音合成（二）本地部署](https://zhuanlan.zhihu.com/p/587765776)

[Live2DMascot](https://github.com/Arkueid/Live2DMascot)

[(vits+ChatGLM)采用清华开源模型ChatGLM的本地化语音聊天](https://www.bilibili.com/video/BV14X4y1f7rt)

[vits_with_chatgpt-gpt3](https://github.com/Paraworks/vits_with_chatgpt-gpt3)

## Start

### Install python

```
python -m pip install paddlepaddle-gpu==2.4.2.post117 -f https://www.paddlepaddle.org.cn/whl/windows/mkl/avx/stable.html -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

Download[nltk_data](https://gitee.com/link?target=https%3A%2F%2Fpaddlespeech.bj.bcebos.com%2FParakeet%2Ftools%2Fnltk_data.tar.gz) and put it in your python file

<font color=red>Note:</font> 

<font color=red>1.Install paddlepaddle according to your cuda version you can find more paddlepaddle in https://www.paddlepaddle.org.cn/</font> 

<font color=red>2.python version need 3.9</font> 

<font color=Red>3.Module and voice are too big .So I would't upload it. You can find it in[【ChatGLM】本地版ChatGPT？6G显存可用！ChatGLM-6B 清华开源模型一键包发布 可更新](https://www.bilibili.com/video/BV1E24y1u7Go) My module is from that. Copy all the content in chatglm-6b to the module. Voice is here: https://pan.baidu.com/s/1pv0BubXrMaGq0trw8J8cFw?pwd=6666</font> 

### Insatll L2D

Dwonload [Live2DMascot](https://github.com/Arkueid/Live2DMascot)

Configure as below. Satrt l2d

![ladsconfig](../../resources/markdown/ladsconfig.png)

### Run

```python
python server.py
```

Double-click the right button to open the input box for communication

## License

[MIT](https://github.com/hasban12138/SaturdayAI/blob/main/LICENSE)

