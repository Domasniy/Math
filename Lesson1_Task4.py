#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt


# In[9]:


x = np.linspace(-10, 10, 201)
plt.plot(x, np.cos(5*x))
plt.plot(x, np.cos(x))
plt.xlabel('x')
plt.ylabel('y')
plt.axis('tight')
plt.show()


# In[ ]:




