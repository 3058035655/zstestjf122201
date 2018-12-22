#或regsvr32 AutoitX.dll
import win32com.client
regsvr32 AutoItX3_x64.dll
autoit = win32com.client.Dispatch("AutoItX3.Control")
autoit.Run("NotePad.exe")