"""GPU implementation of the mandelbrot algorithm.

    This script calculates and plots the mandelbrot set with the help of a GPU.
"""
from timeit import default_timer as timer
import matplotlib.pyplot as plt
import numpy as np
import pyopencl as cl


def plot_gpu(height: int, width: int, device: int,
             MAX_ITER: np.uint16 = np.uint16(80)) -> None:
    """
        Plots the mandelbrot set calculated with an opencl kernel.

        ### Parameters
        height: int
            Height component of the resolution. Determines the number of rows in the 2D mandelbrot set.
        width: int
            Width component of the resolution. Determines the number of columns in the 2D mandelbrot set.
        device: int
            Compute device.
        MAX_ITER: int
            Maximum number of iterations.

        ### Returns
        None.
    """

    start = timer()

    # Create the host side data and a empty array to hold the result.
    a = np.linspace(-2, 1, height)
    b = np.linspace(-1.5, 1.5, width)*1j
    C_host = np.ravel(a + b[:, np.newaxis]).astype(np.complex64)
    n_host = np.zeros((height, width), dtype=np.uint16)

    # Create the context (containing platform and device information) and command queue.
    context = cl.create_some_context(answers=[device])
    cmd_queue = cl.CommandQueue(context)

    # Create a device side read-only memory buffer and copy the data from "hostbuf" into it.
    mf = cl.mem_flags
    C_device = cl.Buffer(context, mf.READ_ONLY |
                         mf.COPY_HOST_PTR, hostbuf=C_host)
    n_device = cl.Buffer(context, mf.WRITE_ONLY, n_host.nbytes)

    kernel = """
    #include <pyopencl-complex.h>
    __kernel void mandelbrot(
        __global const cfloat_t *C,
        __global       ushort *n,
                 const ushort MAX_ITER)
    {
        int gid = get_global_id(0);
        cfloat_t Z;
        Z.real = 0;
        Z.imag = 0;
        n[gid] = 0;

        while(Z.real*Z.real + Z.imag*Z.imag <= 4 && n[gid] < MAX_ITER)
        {
            cfloat_t Z_mul = cfloat_mul(Z,Z);
            Z = cfloat_add(Z_mul, C[gid]);
            n[gid]++;
        }
    }
    """

    prog = cl.Program(context, kernel).build()

    prog.mandelbrot(cmd_queue, C_host.shape, None,
                    C_device, n_device, MAX_ITER)

    cl.enqueue_copy(cmd_queue, n_host, n_device)

    end = timer()
    plt.figtext(0.5, 0.01, "Time to run: {:.2f} seconds".format(end-start),
                ha="center", fontsize=14, bbox={"facecolor": "white",
                "alpha": 0.5, "pad": 4})
    plt.imshow(n_host, cmap='magma')
    plt.show()


if __name__ == "__main__":
    plot_gpu(1500, 1500, 1)
