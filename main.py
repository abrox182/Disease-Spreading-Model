import math
def simulate(prob, t0, t1, t2, alpha, gamma, rho, epsilon, T):
    state = [1, 0, 0, 0, 0, 0, 0]
    beta = prob[1][2] + prob[1][3]
    global EI
    EI = beta
    for t in range(1,T+1):
        state_1 = []
        for i in range(7):
            state_1.append(state[i])
        state[0] = state_1[0] - prob[0][1]*state_1[0] - prob[0][5]*state_1[0] + prob[5][0]*state_1[5]
        state[1] = state_1[1] + prob[0][1]*state_1[0] - EI*state_1[1]
        state[2] = state_1[2] + rho*EI*state_1[1] - prob[2][4]*state_1[2] - prob[2][6]*state_1[2]
        state[3] = state_1[3] + (1-rho)*EI*state_1[1] - prob[3][4]*state_1[3] - prob[3][6]*state_1[3]
        state[4] = state_1[4] + prob[2][4]*state_1[2] + prob[3][4]*state_1[3]
        state[5] = state_1[5] + prob[0][5]*state_1[0] - prob[5][0]*state_1[5]
        state[6] = state_1[6] + prob[3][6]*state_1[3] + prob[2][6]*state_1[2]

        if(t < t0):
            prob[0][5] = 0
        elif(t >= t0):
            prob[0][5] = alpha*(t - t0)
        SS = prob[0][0]
        prob[0][0] = ((1 - prob[0][5])*(prob[0][0]))/(prob[0][1] + prob[0][0])
        prob[0][1] = ((1-prob[0][5])*prob[0][1])/(prob[0][1] + SS)
        if(t < t1 or t > t2):
            EI = beta
        elif(t >= t1 and t <= t2):
            EI = gamma*beta
        prob[0][1] = prob[0][1] + epsilon*math.sin((2*math.pi/365)*(t))
        prob[0][0] = prob[0][0] - epsilon*math.sin((2*math.pi/365)*(t))
    return state