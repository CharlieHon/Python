from distutils.core import setup

setup(name="ch_message",    # 包名
    version="1.0",          # 版本
    description="Charlie's 发送和接收消息模块",  # 描述信息
    long_description="完整的发送和接收消息模块",    # 完整的描述信息
    author="CharlieHon",     # 作者
    author_email="CharlieHon@charlie.com",
    url="https://github.com/CharlieHon/Python",   # 主页
    py_modules=["ch_message.send_message",
                "ch_message.receive_message"]     # 以列表形式指定压缩包中包含的模块的名称
    )