# kernel-extension-demo

This repository demonstrates how to extend the IPython kernel.

This kernel extension starts a server listening on a random port on the local machine. The server will interpret any data sent to it as a string and execute that string inside the IPython kernel.

# Install and Run

```
git clone https://github.com/stevenstetzler/kernel-extension-demo.git
cd kernel-extension-demo
cat config.py >> $(ipython profile locate default)/ipython_kernel_config.py
jupyter notebook
```

When you launch the Jupyter notebook `Kernel Test.ipynb`, the kernel extension should be loaded and you should be able to walk through the notebook.
