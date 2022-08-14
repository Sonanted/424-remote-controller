import pyautogui
import pywinauto
import os
import shutil


def desktop_app_usage(dict_data):
    root_src_dir = r"D:\Lab_0104\osc\main\static\main"
    if os.path.exists(root_src_dir+'\\osc.png'):
        os.remove(root_src_dir+'\\osc.png')
    #try:
        #except Exception as e:
    #    app = pywinauto.Application().start("C:\Program Files\Gratten\GAScopeSetup_EN\GAScope.exe")
    #app.GaScope.move_window(0, 0, 1920, 1042, True)
    #app.GaScope.set_focus()
    #pyautogui.sleep(0.5)
    #pyautogui.click(x=219, y=44)
    #pyautogui.sleep(1.5)
    #if dict_data['channel'] == 'CH2':
    #    dlg_spec = app.window()
    #    dlg_spec.child_window(title="CH2", class_name="Button").click()
    app1 = pywinauto.application.Application().connect(best_match='UltraScope')
    app1.RIGOL_DS_Tools_UltraScope.set_focus()
    pyautogui.sleep(0.5)
    pyautogui.doubleClick(x=89, y=1002) #Y scale
    pyautogui.write(dict_data['ch_scale'])
    pyautogui.doubleClick(x=255, y=71) #X scale
    pyautogui.write(dict_data['time_base'])
    pyautogui.sleep(0.5)
    pyautogui.click(x=829, y=482) #center
    pywinauto.mouse.click(button="right", coords=(829,482))
    pyautogui.sleep(0.5)
    pyautogui.click(x=882, y=689) #Copy
    pyautogui.sleep(0.5)
    pyautogui.click(x=959, y=588) # close window
    pyautogui.sleep(1)
    app2 = pywinauto.application.Application().connect(best_match='mspaint')
    app2.mspaint.set_focus()
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.click(x=29, y=35) #menu
    pyautogui.sleep(2)
    pyautogui.click(x=86, y=192) #save
    pyautogui.sleep(2)
    pyautogui.write('osc.png')
    pyautogui.click(x=1427, y=771)  #ok
    pyautogui.sleep(4)
    # pyautogui.write("osc.jpg")
    #pyautogui.sleep(1)
    #pyautogui.click(x=1387, y=770)
    # delay for system to reidentify file, can't find a file to copy without delay
    #pyautogui.sleep(1)
    #if os.path.exists(root_src_dir + '\\osc.jpg'):
    #    if os.path.exists(root_dst_dir+'\\osc.jpg'):
    #        os.remove(root_dst_dir+'\\osc.jpg')
    #    shutil.copy2(root_src_dir+'\\osc.jpg', root_dst_dir)
