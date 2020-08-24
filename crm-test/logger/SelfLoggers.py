#coding:utf-8
import logging,time,os

class SelfLoggers(object):
    def __init__(self,level=logging.INFO,className="Loggers"):
        self.logger=logging.getLogger(className)
        self.logger.setLevel(level)
        fileTimeName=time.strftime("%Y-%m-%d",time.localtime())
        genpath=os.path.abspath("..")
        logpath=os.path.join(genpath,"log")
        if os.path.exists(logpath):
            pass
        else:
            os.makedirs(logpath)
        logFileName=logpath+"/"+fileTimeName+".log"
        fh=logging.FileHandler(logFileName,mode="a",encoding="utf-8")
        formatter=logging.Formatter(
            "%(asctime)s - %(filename)s[line:%(lineno)d] %(name)s - %(levelname)s: %(message)s"
        )
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)
        stream_hander=logging.StreamHandler()
        stream_hander.setFormatter(formatter)
        self.logger.addHandler(stream_hander)

if __name__ == '__main__':
    log=SelfLoggers(level=logging.INFO)
    result=6
    log.logger.error("错误日志：%s"%result)
