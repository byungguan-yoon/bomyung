from threading import Thread
import os
import datetime 

from comm.py_image_buffer_save import create_device, start_stream, destroy_device
from comm.connect_light import lightConnector
from comm.melsec_connector import MelsecConnector

# config
plc_add = "192.168.10.7"
plc_port = 2001
light_port = ['/dev/ttyUSB0', '/dev/ttyUSB1']
light_baud = 9600
is_save = True


def chk_comm_plc():
    pass

def chk_comm_light():
    pass

def chk_comm_camera():
    pass

def inspection(is_inspection, is_blue, is_back):
    connector = MelsecConnector(plc_add, plc_port)
    light_connector = lightConnector(light_port[0], light_baud)
    light_connector2 = lightConnector(light_port[1], light_baud)

    path_tmp = f"./static/{datetime.date.today()}"
    path = path_tmp + f"/{datetime.datetime.now().strftime('%H_%M_%S')}"
    os.makedirs(path, exist_ok=True)

    if is_blue:
        light_connector.change_state('2','2ON')
        light_connector.change_state('2','040')

        loop(connector, path, is_inspection, is_save, True)
        print("End Loop")
        light_connector.initialize_light()

    if is_back:
        for i in range(1,5):
            light_connector2.change_state(f'{i}',f'{i}'+'ON')
            light_connector2.change_state(f'{i}','130')

        loop(connector, path, is_inspection, is_save, False)
        print("End Loop")
        light_connector2.initialize_light()


# is_blue는 블루인지 백라이트인지 체크용
def loop(connector, path, is_inspection, is_save, is_blue):
    for i in range(1,56 + 1):
                        while True:
                            print(connector.plc2pc_get_val(headdevice="D10001")[0])
                            if i == connector.plc2pc_get_val(headdevice="D10001")[0]:
                                device = create_device()
                                with device.start_stream(1):
                                    print(f"START: {i} Shot")
                                    i_str = str(i)
                                    i_str = i_str.zfill(2)
                                    if is_blue:
                                        connector.process_snapshot(device, path + f"/1_{i_str}", is_inspection, is_save)
                                    else:
                                        connector.process_snapshot(device, path + f"/2_{i_str}", is_inspection, is_save)                                        
                                    print(f"END: {i} Shot")
                                destroy_device()
                                break