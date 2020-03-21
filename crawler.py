#-*- coding:utf8 -*-
import os, time
from multiprocessing import Pool, current_process
import requests

def doubler(number, parent_proc_id, parent_proc_name):
    result = number * 2
    proc_id = os.getpid()
    proc_name = current_process().name
    # 设置等待时间，可以验证apply和apply_async的阻塞和非阻塞
    time.sleep(2)
    print('parent_proc_id:{0} parent_proc_name:{1} proc_id:{2} proc_name:{3} number:{4} result:{5}'.format(parent_proc_id, parent_proc_name, proc_id, proc_name, number, result))


if __name__ == '__main__':

    polyps_num = {
        "Hyperplasic": [x for x in range(0, 22)],
        "Serrated": [x for x in range(0, 15)],
        "Adenomanum": [x for x in range(0, 40)]
    }

    parent_proc_id = os.getpid()
    parent_proc_name = current_process().name
    pool = Pool(processes=3)
    for num in numbers:

        for polyp_type in {"Hyperplasic", "Serrated", "Adenoma"}:
            for i in polyps_num[polyp_type]:
                link = "http://www.depeca.uah.es/colonoscopy_dataset/%s/%s_%s/videos/WL.mp4" % (
                polyp_type, str.lower(polyp_type), i)
                r = requests.get(link, stream=True)
        # 非阻塞
        pool.apply_async(doubler, (num, parent_proc_id, parent_proc_name))
        # 阻塞其它进程
        # pool.apply_async(doubler, (num, parent_proc_id, parent_proc_name))

    # 关闭pool使其不再接受新的任务
    pool.close()

    # 关闭pool，结束工作进程，不在处理未完成的任务
    # pool.terminate()

    # 主进程阻塞，结束工作进程，不再处理未完成的任务，join方法要在close或terminate之后使用
    pool.join()

    print('Done')