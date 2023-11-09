import time
import multiprocessing.pool


def time_and_memory_consuming_function(n):
    # Consume memory by creating a large list
    memory_hog = [0] * (n * 1024 * 1024)  # n megabytes of memory

    # Consume CPU time with a nested loop
    for i in range(n):
        for j in range(n):
            _ = i * j

    return memory_hog


' also cupy is interesting: https://docs.cupy.dev/en/stable/user_guide/interoperability.html --> especially because of the Interoperability'
' https://www.youtube.com/watch?v=wa0EmEq5Otw '

' speed up algorithms: https://towardsdatascience.com/speed-up-your-algorithms-part-2-numba-293e554c5cc1'

import numba
import numpy as np
from numba import cuda

# Define a function and specify the target as 'cuda'
# @numba.jit(target='cuda')
# numba.cuda.cudadrv.error.NvvmSupportError: libNVVM cannot be found. Do `conda install cudatoolkit`:
# @cuda.jit('void(int32[:], int32[:], int32[:])')
# @cuda.jit
# def add_arrays(a, b, result):
#    for i in range(len(a)):
#        result[i] = a[i] + b[i]
#

#### numba -> take operations that work primarly with numbers and compile it to assembler code -> thus they run with high speed!
#######            -_> also possible to deploy this combiled code to the gpu with cuda!!!
#########                 --> also possible to check if cuda is available, otherwise dont use it

#from numba import jit
from numba import cuda
from numba import cuda, jit

@jit  # takes python code and takes it into machine code
#@jit(target_backend='cpu')
def A(X):
    X ** X ** X

def B(X):
    X ** X ** X


@cuda.jit
#@jit(_target='cuda')
def C(X):
    X ** X ** X


if __name__ == "__main__":
    try:
        time_start = time.time()  # in seconds
        A(10000)
        print(f"Time elapsed: {time.time() - time_start:.2} sec --> max: 10000^10000^10000")
    except:
        print("A failed")

    try:
        time_start = time.time()  # in seconds
        B(8)
        print(f"Time elapsed: {time.time() - time_start:.2} sec --> max about (time limit): 8^8^8")
    except:
        print("B failed")

    try:
        # Get the current GPU device
        device = cuda.get_current_device()

        # Determine the number of blocks and threads based on device capabilities
        max_threads_per_block = device.WARP_SIZE
        max_blocks_per_grid = device.MAX_GRID_DIM_X  # subdivisions which we are using for this job

        # Your computation or problem-specific configuration
        X = 10000000000000000000
        problem_size = X

        # Calculate the number of blocks and threads per block
        threads_per_block = min(max_threads_per_block, problem_size)
        blocks_per_grid = min(max_blocks_per_grid, (problem_size + threads_per_block - 1) // threads_per_block)

        C[max_blocks_per_grid, max_threads_per_block](X)
        # C(8)
        print(
            f"Time elapsed: {time.time() - time_start:.2} sec --> max: 10000000000000000000^10000000000000000000^10000000000000000000")
    except:
        print("C failed")


    from numba import cuda

    print(cuda.gpus)

    # time_start = time.time()  # in seconds
    # result = time_and_memory_consuming_function(1000)
    # print(f"Time elapsed: {time.time() - time_start:.2} sec")

    # time_start = time.time()  # in seconds
    # number_cores = multiprocessing.cpu_count()
    # pool = multiprocessing.pool.Pool(processes=number_cores)
    # result = pool.apply_async(time_and_memory_consuming_function, (1000,))
    # pool.close()
    # pool.join()
    # final_result = result.get()
    # print(f"Time elapsed: {time.time() - time_start:.2} sec")

    # time_start = time.time()  # in seconds
    # with pool:
    #    result = time_and_memory_consuming_function(1000)

    # print(f"Time elapsed: {time.time() - time_start:.2} sec")

    # Create NumPy arrays and call the GPU-accelerated function
    # a = np.array([1, 2, 3])
    # b = np.array([4, 5, 6])
    # result = np.empty_like(a)
    # add_arrays(a, b, result)

