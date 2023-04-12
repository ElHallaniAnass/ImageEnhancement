import cv2
import numpy as np
from numpy.fft import fft2, ifft2, fftshift, ifftshift
from matplotlib import pyplot as plt
from skimage import io


class Tf:
    def __init__(self):
        pass    

    def FFT(self,img):
        f = fft2(img)
        fshift = fftshift(f)
        return fshift

    def inversFFT(self,fftImg):
        return ifft2(ifftshift(fftImg))



    def Spectrum(self,fftImg):
        return 20*np.log(np.abs(fftImg))


class Filtre:

    def __init__(self) -> None:
        pass

    # Filter: Low pass filter
    def idealLowPass(self,img, cut_of_frequency):
        L,C = img.shape
        Low = np.zeros((L,C), dtype=np.float32)
        for u in range(L):
            for v in range(C):
                D = np.sqrt((u-L/2)**2 + (v-C/2)**2)
                if D <= cut_of_frequency :
                    Low[u,v] = 1
                else:
                    Low[u,v] = 0
        return Low

    #/////////////////////////////////////////////////////////
    # Filter: Low pass filter
    def idealHighPass(self,img,cut_of_frequency):
        Low = Filtre().idealLowPass(img,cut_of_frequency)
        High = 1 - Low
        return High

    #/////////////////////////////////////////////////////////
    def ButterwortLow(self,img,cut_of_frequency,order):
        M,N = img.shape
        H = np.zeros((M,N), dtype=np.float32)
        # print(H)
        D0 = cut_of_frequency 
        n = order 
        for u in range(M):
            for v in range(N):
                D = np.sqrt((u-M/2)**2 + (v-N/2)**2)
                H[u,v] = 1 / (1 + (D/D0)**(2*n))
        return H

    #/////////////////////////////////////////////////////////
    def ButterwortHigh(self, img,cut_of_frequency,order):
        M,N = img.shape
        H = np.zeros((M,N), dtype=np.float32)
        # print(H)
        D0 = cut_of_frequency 
        n = order 
        for u in range(M):
            for v in range(N):
                D = np.sqrt((u-M/2)**2 + (v-N/2)**2)
                H[u,v] = 1 / (1 + (D0/D)**(2*n))
        return H
    #/////////////////////////////////////////////////////////


    def GaussianLow(self, img, cut_of_frequency):
        L,C = img.shape
        GaussianLow = np.zeros((L,C), dtype=np.float32)
        D0 = cut_of_frequency
        for u in range(L):
            for v in range(C):
                D = np.sqrt((u-L/2)**2 + (v-C/2)**2)
                GaussianLow[u,v] = np.exp(-D**2/(2*D0*D0))
        return GaussianLow
    # /////////////////////////////////////////////////
    def GaussianHigh(self, img, cut_of_frequency):
        GaussianLow = Filtre().GaussianLow(img, cut_of_frequency)
        GaussianHigh = 1 - GaussianLow
        return GaussianHigh
    # /////////////////////////////////////////////////


    def LaplacianFilter(self, img):
        f = img
        f = f / 255
        F = Tf().FFT(f)

        L,C = F.shape
        H = np.zeros((L,C), dtype=np.float32)
        for u in range(L):
            for v in range(C):
                D = ((u-L/2)**2 + (v-C/2)**2)
                H[u,v] = -4*np.pi*np.pi*D
            
        Lap = H * F
        Lap = Tf().inversFFT(Lap)
        Lap = np.real(Lap)

        OldRange = np.max(Lap) - np.min(Lap)
        NewRange = 1 - -1
        LapScaled = (((Lap - np.min(Lap)) * NewRange) / OldRange) + -1

        # image ehancement
        c = -1
        g = f + c*LapScaled
        g = np.clip(g, 0, 1)

        return LapScaled, H ,g



































