#!/usr/bin/env python
# coding: utf-8

# In[50]:


from pynput.mouse import Button, Controller
from pynput import keyboard


# In[51]:


mouse = Controller()


# In[53]:


with keyboard.Events() as events:
    # Block at most one second
    y = 1
    while y != 0:
        event = events.get(1.0)
        if event is None:
            #print('Pressing Button')
            mouse.press(Button.left)
            mouse.release(Button.left)
        else:
            y = 0


# In[ ]:




