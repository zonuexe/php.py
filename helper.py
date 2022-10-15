# -*- coding: utf-8 -*-
import subprocess
def run(input):print(subprocess.run(["php"],input=str(input,'utf-8'),capture_output=True, text=True).stdout)
