
```shell
pip install -r requirements.txt
python ./rapper_lyrics_from_qq.py
```

nltk 字典包的安装如果报出`连接远程服务器失败的错误`是因为被墙了，给终端设置代理即可


```shell

# cmd 设置代理
> set HTTP_PROXY=http://127.0.0.1:1080
> set HTTPS_PROXY=http://127.0.0.1:1080

# 进入 python
> python

>>> import nltk
>>> nltk.download()
```
弹出一个用`tkinter`实现的GUI界面，点击 `all-corpora`，点击 `Download` 即可。