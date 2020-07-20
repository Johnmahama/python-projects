import os
import sys
import argparse


def shutdown(mins=0):
    os.system(f"shutdown -s -t {mins * 60}")
    return f"shutdown in {mins} min"

def restart(mins=0):
    os.system(f"Shutdown -r -t {mins * 60} ")
    return f"Restart in {mins} min"

if __name__=="__main__":
    restart(5)