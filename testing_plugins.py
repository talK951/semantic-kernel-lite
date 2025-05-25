from SemanticKernel.KernelFunctions import kernel_function
from SemanticKernel.Kernel import Kernel

class Plugin:
    @kernel_function(name="print_msg")
    def print_msg(self):
        print("Testing code")

kernel = Kernel()
kernel.add_plugin(Plugin(), "test_plugin")

print(kernel.plugins["test_plugin"].print_msg.kernel_name)