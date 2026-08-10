"""
Demonstrating Jupyter/IPython debugging and profiling magics for issue #51.
Run interactively in IPython to see the magic commands work.
"""
import time

def slow_function():
    total = 0
    for i in range(1000000):
        total += i
    return total

def buggy_function(data):
    return data["focus_minutes"] / data["goal_minutes"]

# Deliberately buggy call: missing "goal_minutes" key, to demo post-mortem debugging
sample = {"focus_minutes": 45}
