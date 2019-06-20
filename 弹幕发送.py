import requests
import time
url = 'https://api.live.bilibili.com/msg/send'
def dm(dm,rnd,room):
    data={
        'color': '16777215',
        'fontsize': '25',
        'mode': '1',
        'msg': dm,
        'rnd': rnd,
        'roomid': room,
        'bubble': '0',
        'csrf_token': '7d81238b61b679b0eb2536495013eb8c',
        'csrf': '7d81238b61b679b0eb2536495013eb8c'
    }
    return data
header = {
    "cookie":"_uuid=2584A8B7-75A3-D63A-A47A-74FFE76FE27460274infoc; buvid3=F7048B06-44DC-4053-82F7-04597C74E2EE110239infoc; LIVE_BUVID=AUTO5315610329613379; CURRENT_FNVAL=16; sid=55gy8620; stardustvideo=1; rpdid=|(u)~Rm~YY|)0J'ulYu|JJul~; DedeUserID=339873772; DedeUserID__ckMd5=d787a72c8b602d41; SESSDATA=e725fa57%2C1563628201%2C54679161; bili_jct=7d81238b61b679b0eb2536495013eb8c; _dfcaptcha=4158d1cee32047060581071a3f72b0db; finger=b3372c5f; im_notify_type_339873772=0; LIVE_PLAYER_TYPE=2"
}
#请求
datalist=['233']
rnd='1561036415'
roomid='7049047'
for datas in datalist:
    data = dm(datas,rnd,roomid)
    requests.post(url,data=data,headers=header)
    time.sleep(2)
