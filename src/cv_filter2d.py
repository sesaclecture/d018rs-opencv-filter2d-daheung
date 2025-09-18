import cv2
import sys
import numpy as np

KERNEL_SIZE = 3

def identity_kernel() -> np.array:
    # TODO: 아이덴티티 커널을 정의하세요.
    arr = np.identity(KERNEL_SIZE, np.float32)
    kernel = np.array(arr, dtype=np.float32)
    return kernel

def ones_kernel() -> np.array:
    # TODO: 모든 값이 1인 커널을 정의 하세요.
    arr = np.ones((KERNEL_SIZE, KERNEL_SIZE), np.float32)
    kernel = np.array(arr, dtype=np.float32)
    return kernel

def original_kernel() -> np.array:
    # TODO: 원본을 그대로 반환하는 커널을 작성 하세요.
    arr = np.zeros((KERNEL_SIZE, KERNEL_SIZE), dtype=np.float32)
    arr[1][1] = 1

    kernel = np.array(arr, dtype=np.float32)
    return kernel

def doubling_kernel() -> np.array:
    # TODO: 원본을 2배로 반환 하는 커널을 작성하세요.
    arr = np.zeros((KERNEL_SIZE, KERNEL_SIZE), dtype=np.float32)
    arr[1][1] = 2

    kernel = np.array(arr, dtype=np.float32)
    return kernel
