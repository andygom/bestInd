import numpy as np
from numpy import random
import time
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

# INDIVIDUO CON experimento p100 g800 m0.5 / 4    -----      F I T N E S S  D E  53.56071662902832
# weightsIH = np.random.random((14, 14)) * 2 - 1

weightsIH = [-2.40636484e-01, -1.74263302e-03,  6.63366364e-02,  1.71395562e-03,
       -3.79531958e-01,  1.74477929e-02,  1.74407312e-05,  7.61316599e-01,
        7.42135552e-02,  1.60846417e-01,  5.72123812e-03, -1.84562686e+00,
       -3.21753742e+00, -1.41749162e+01] ,   [ 6.98014772e-01, -2.83888538e+00,  1.67825449e+00,  4.63126341e-02,
       -1.36242018e+00,  5.67582168e-02, -2.89842506e-01, -1.12568156e+00,
        1.33093078e-02, -3.59840539e+01,  9.62318588e-03, -3.93688661e-04,
        8.56223737e+00,  1.11539068e+00] ,   [ 1.15281959e-01, -6.94718192e+00, -1.32144976e+00, -1.13003153e-01,
       -8.44604712e-01,  5.64960506e-02, -3.71164548e-01, -2.01390255e+00,
       -1.29066404e+00,  5.77749679e-01, -4.93265718e-01, -3.39067610e-02,
       -4.63949614e-01, -3.78738183e-04] ,   [-5.87966787e-01, -2.72761035e-02,  1.41696481e-02,  6.98643844e-01,
        1.18089209e-01, -5.97753307e-02, -1.42164539e-02,  2.45629354e-01,
        1.71542015e-03,  2.01214573e-01,  1.44483369e-01, -5.11442077e+00,
        1.90948668e-01, -7.37845460e-01] ,   [  0.28040165,  -0.10124838,  -0.47262832,  -0.79993158,
       -24.10336793,   1.38505977,   0.20380902,   0.05137554,
        -0.52962208,   0.08429577,   0.06659999,  -0.37627264,
         0.0353511 ,   0.38192701] ,   [-0.28592337,  0.00487788, -2.84334406,  0.17383074,  0.01897699,
        1.49612303, -0.60429327,  0.24271228,  0.10499804,  0.22658934,
       -0.00799736, -0.05806773,  0.1304261 , -0.0811043 ], [ 3.01171286e+00, -1.90209212e-01,  1.89848773e+00, -1.39335345e+00,
        9.74865574e-05, -5.86786482e-02, -2.96998161e-01,  4.51995611e-02,
       -2.35345284e-03,  2.54526099e+01,  7.68659349e-02,  3.97811275e-02,
        2.08778935e-02,  2.12151935e-01] ,   [-1.70177915e+00, -1.34334158e-01, -2.40001311e-01,  5.45778036e-01,
        5.54986708e-01, -1.19547854e+01, -1.17225685e+01,  1.08444024e-03,
       -3.85776468e-03,  1.27996975e-02, -9.28629800e-03, -2.07893352e-01,
       -4.44812454e-02, -3.50234501e-01] ,   [ 2.17874409e-02,  4.17001725e-01, -4.36103105e-02, -3.79236706e-01,
        1.54411481e-03,  1.20218455e-02, -1.34475493e+01,  8.74134885e-01,
        1.41188375e-01,  6.97250750e-01,  1.90348497e-02, -2.49678025e-01,
       -5.46293231e-02,  3.24259829e-02] ,   [ 5.73304709e-01,  2.12033279e-01, -1.27368699e-01,  1.20640455e-02,
       -4.44835677e-03,  4.79485710e-01, -5.29822612e-05, -3.13648196e-03,
       -1.05578145e-01,  1.92018353e-01, -4.97100341e-02,  2.01855669e-02,
        9.20335680e-01, -2.96821590e-01] ,   [ 2.24959446e+00, -3.86541576e+00, -1.22085981e-05, -1.32206952e+00,
       -1.99292037e-01, -2.66417014e-02,  5.19817958e-02,  6.92978316e-01,
       -9.69499574e-02,  3.45542192e-01,  3.95717966e-01, -8.05041955e-02,
        1.50464778e-01, -1.63535532e+00] ,   [ 2.94079287e-03, -5.69424951e+00,  3.75801736e+00,  5.57055881e-01,
       -9.77317079e-01,  4.52456090e-02,  2.51470480e-02, -9.50077784e-01,
        2.08148676e-01, -3.18014264e+00,  7.05617966e-02, -3.34562021e-02,
        1.72169358e-02, -9.74818158e-01] ,   [ 0.62541125, -0.22046413, -0.24134438,  0.70725373,  0.01113252,
       -0.40591677, -1.15822132,  0.20612739, -0.22332458, -1.13610729,
        0.04399916, -1.33509242, -0.17688233,  0.13595855] ,   [ 0.00087978,  0.15115576, -0.01017319, -0.58052266,  0.04302093,
        0.75709556, -0.53776049,  0.00434497, -0.13632429, -0.04043214,
       -0.07206388, -0.00228137,  0.00248928, -0.27603436]

weightsHO = [-6.61792637e-04,  5.45384097e-02,  3.05729649e+00,  1.99870563e-01,
       -9.98696510e-02, -2.56839258e-01,  4.52895935e-02,  1.55559388e+00] ,   [-0.00546253,  0.59764858, -2.48451052,  0.04439166,  0.01438323,
        0.19373463,  1.27478644, -0.14179556] ,   [ 0.32465259,  0.96442731,  0.83101835, -0.18693782,  0.83474105,
       -0.02870707, -0.2990088 , -0.38790254] ,   [ 6.24995814e+00, -1.18306834e+00,  1.78949124e-03, -5.22480445e-01,
       -2.00937531e-01,  7.50988789e-02,  2.10385405e-03,  2.12510647e-02] ,   [-2.01464119, -0.16837862,  0.15169155,  0.8866197 , -0.00485403,
       -0.01407076,  0.15240077,  0.49295674] ,   [ 7.32433467e-01,  1.79549347e-01,  3.41162924e-01,  1.90813351e+00,
       -5.36749101e-02, -7.51113532e-02,  4.42014227e-01,  3.03928189e-04] ,   [ 0.43325769,  1.01802065, -1.11165036,  0.11426402,  0.26157178,
       -0.16547849, -0.23303562, -0.21234458] ,   [-5.70202765e-01,  2.93959510e-01, -5.85295811e+01,  1.67847725e-03,
        3.04004732e-01, -1.03037614e+00,  7.96979547e-03, -7.94198882e-03] ,   [ 0.0548202 , -0.07456757, -1.71422561,  0.08054637, -0.26739852,
       -1.9817484 ,  0.44962631, -0.49272979] ,   [ 0.70413375,  0.03326465, -0.9528597 ,  0.5934409 , -0.18879535,
       -0.00687019,  0.52132268,  0.37277299] ,   [ 0.5424941 , -0.53916267, -0.2968379 ,  0.71871201, -0.08216665,
        1.37469506, -2.42895439, -0.00461364] ,   [ 0.17794029, -2.08002468,  0.44658162,  0.0043167 , -0.00668033,
       -0.06464207, -0.0022729 , -0.03603184] ,   [ 0.00100032, -0.0028427 ,  0.27995187,  0.0118586 , -0.15083475,
       -0.5849592 , -0.0011323 ,  0.00486807] ,   [ 0.71663974,  0.21336921,  0.83248701, -0.7478093 ,  0.66477269,
        1.48651684,  0.03682249,  0.01129099]


neuronH = [0 for c in range(14)]

neuronO = [0 for c in range(8)]

motor = [0 for c in range(8)]

ultsensor = [0 for c in range(6)]


COUNT = 0


# normalización de los motores
def motorNorm(motorArray):

        print(motorArray)
        for i in range(0, len(motorArray)):

            motor[i] = ((motorArray[i] + 1) * 180) / 2
            
        print(motor)

            # if abs(motorArray[i] * 180) == 0:

            #     # -1 - 1
            #     180    0

            #     motor[i] = 90
            # else:
            #     motor[i] = abs(motorArray[i] * 180)
        # print(motor)

        kit.servo[0].angle = motor[0]
        kit.servo[1].angle = motor[1]
        kit.servo[2].angle = motor[2]
        kit.servo[3].angle = motor[3]
        kit.servo[4].angle = motor[4]
        kit.servo[5].angle = motor[5]
        kit.servo[6].angle = motor[6]
        kit.servo[7].angle = motor[7]
                
        # implementar mandar motor a los motores reales


# normalizacion de los sensotres ultrasonicos
def usNorm(usArray):
        for i in range(0, len(usArray)):

            ultsensor[i] = abs(usArray[i] * 20)


# entradas de los sensores 
def input():
    print('new inputs')

    sensorInput = np.random.random((3)) * 2 - 1


def network():

    sensorInput = np.random.random((14)) * 2 - 1
    

    print(COUNT)
    if COUNT == 0:
        sensorInput = np.random.random((14)) * 2 - 1
    else:
        for i in range(0, 6):
            sensorInput[i] = neuronO[i - 6]

        # for i in range(6, 14):
        #     sensorInput[i] = neuronO[i - 6]
        # print(sensorInput)
        
    # print(motor)

    # print(sensorInput)

    # print(weightsIH)

    for j in range(0, 14):
        for i in range(0, 14):

            anh = []

            anh.append(sensorInput[j] * weightsIH[j][i])

        # print(sum(anh))

        # print(anh)


        neuronH[j] = np.tanh(sum(anh))

        # dotN = np.dot(sensorInput, weightsIH[i])
        # neuronH[i] = np.tanh(dotN)

    # print(neuronH)

    for j in range(0, 8):
        for i in range(0, 14):

            anOP = []

            anOP.append(neuronH[j] * weightsIH[j][i])

        neuronO[j] = np.tanh(sum(anOP))
 
    # print(neuronO)

    # print(neuronO)

    motorNorm(neuronO)
    input()
    # sensorInput = np.random.random((14)) * 2 - 1

    # print(neuronH)
    # print(neuronO)

try:

    while True:
        # if COUNT == 0:

            # kit.servo[0].angle = 90
            # kit.servo[1].angle = 90
            # kit.servo[2].angle = 90
            # kit.servo[3].angle = 90
            # kit.servo[4].angle = 90
            # kit.servo[5].angle = 90
            # kit.servo[6].angle = 90
            # kit.servo[7].angle = 90

        network()
        COUNT = COUNT + 1
        
        # intentar no utilizar sleep y que sean intervalos iguales a los del simulador 
        time.sleep(2)

except KeyboardInterrupt:

    print("Press Ctrl-C to terminate while statement")

    pass
