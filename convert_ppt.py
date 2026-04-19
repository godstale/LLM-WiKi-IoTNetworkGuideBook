import win32com.client
import os
import sys

def convert_ppt_to_pptx(ppt_path):
    ppt_path = os.path.abspath(ppt_path)
    if not os.path.exists(ppt_path):
        print(f"File not found: {ppt_path}")
        return False
    
    pptx_path = os.path.splitext(ppt_path)[0] + ".pptx"
    
    try:
        powerpoint = win32com.client.Dispatch("PowerPoint.Application")
        # ppSaveAsOpenXMLPresentation = 24
        presentation = powerpoint.Presentations.Open(ppt_path, WithWindow=False)
        presentation.SaveAs(pptx_path, 24)
        presentation.Close()
        print(f"Successfully converted {ppt_path} to {pptx_path}")
        return True
    except Exception as e:
        print(f"Error converting {ppt_path}: {e}")
        return False
    finally:
        try:
            powerpoint.Quit()
        except:
            pass

if __name__ == "__main__":
    files = [
        "raw/chap4-wifi.ppt",
        "raw/chap5-sensor-server-mobile.ppt",
        "raw/chap7-home-automation.ppt"
    ]
    
    # Also handle chap1 if it's not already converted or just for consistency
    # But chap1 seems to have a backup md, so maybe skip for now or include if needed.
    # The user asked for "others too".
    
    for f in files:
        convert_ppt_to_pptx(f)
