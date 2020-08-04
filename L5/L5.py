##1
import numpy as np
def gauss(pm_A,pm_B):
    print(pm_A)
    print(pm_B)
    s_N = np.size(pm_A, 0)
    m_Au = np.concatenate((pm_A, pm_B), 1)
    for i in range(0, s_N):
        s_MaxPiv = np.abs(m_Au[i, i])
        s_MaxPivInd = i
        for k in range(i + 1, s_N):
            if np.abs(m_Au[k, i]) <= s_MaxPiv:
                continue
            s_MaxPiv = np.abs(m_Au[k, i])
            s_MaxPivInd = k
        if s_MaxPivInd != i:
            v_Aux = 1.0 * m_Au[s_MaxPivInd, :]
            m_Au[s_MaxPivInd, :] = 1.0 * m_Au[i, :]
            m_Au[i, :] = 1.0 * v_Aux
            
        s_IndIni = i + 1
        for j in range(s_IndIni, s_N):
            if i == j:
                continue
            v_Aux = 1.0 * m_Au[i, :]
            v_Aux = (1.0 / m_Au[i, i]) * m_Au[i, :]
            v_Aux = (-1.0 * m_Au[j, i]) * v_Aux
            m_Au[j, :] = m_Au[j, :] + v_Aux
    m_X = np.zeros((s_N, np.size(pm_B, 1)))
    for k in range(np.size(pm_B, 1) - 1, -1, -1):
        for i in range(s_N - 1, -1, -1):
            s_SumAux = 0
            for j in range(i + 1, s_N):
                s_SumAux = s_SumAux + m_Au[i, j] * m_X[j, k]
            m_X[i, k] = (1.0 / m_Au[i, i]) * (m_Au[i, s_N + k] - s_SumAux)
    return m_X

N=3
pm_A=np.random.rand(N,N)
pm_B=np.random.rand(N,1)
print("Solución de la función:")
print(gauss(pm_A,pm_B))
print("Solución de NumPy")
print(np.linalg.solve(pm_A,pm_B))
##2 Gauss Jordan
import numpy as np
def gaussJordan(pm_A,pm_B):
    print(pm_A)
    print(pm_B)
    s_N = np.size(pm_A, 0)
    m_Au = np.concatenate((pm_A, pm_B), 1)
    for i in range(0, s_N):
        s_MaxPiv = np.abs(m_Au[i, i])
        s_MaxPivInd = i
        for k in range(i + 1, s_N):
            if np.abs(m_Au[k, i]) <= s_MaxPiv:
                continue
            s_MaxPiv = np.abs(m_Au[k, i])
            s_MaxPivInd = k
        if s_MaxPivInd != i:
            v_Aux = 1.0 * m_Au[s_MaxPivInd, :]
            m_Au[s_MaxPivInd, :] = 1.0 * m_Au[i, :]
            m_Au[i, :] = 1.0 * v_Aux

        s_IndIni = 0
        v_Aux = (1.0 / m_Au[i, i]) * m_Au[i, :]
        m_Au[i, :] = 1.0 * v_Aux

        for j in range(s_IndIni, s_N):
            if i == j:
                continue

            v_Aux = 1.0 * m_Au[i, :]
            v_Aux = (-1.0 * m_Au[j, i]) * v_Aux

            m_Au[j, :] = m_Au[j, :] + v_Aux
        m_X = 1.0 * m_Au[:, s_N:]
    return m_X

print("GAUSS JORDAN")
pm_A=np.random.rand(N,N)
pm_B=np.random.rand(N,1)
print("Solución de la función:")
print(gaussJordan(pm_A,pm_B))
print("Solución de NumPy")
print(np.linalg.solve(pm_A,pm_B))
print("Inversa de la matriz:")
print(np.linalg.inv(pm_A))

##3

'Un sistema matricial de la forma Ax=b puede ser:'
'Consistente o compatible si tiene una(de la forma 1 0 0 = x con x!=0) o infinitas soluciones (de la forma 0 0 0 = 0)'
'Inconsistente o incompatible si no tiene solucion, da algo de la forma 0 0 0 = x con x!=0'
##4
import numpy as np
def gaussJordan(pm_A,pm_B):
    print(pm_A)
    print(pm_B)
    s_N = np.size(pm_A, 0)
    m_Au = np.concatenate((pm_A, pm_B), 1)
    for i in range(0, s_N):
        s_MaxPiv = np.abs(m_Au[i, i])
        s_MaxPivInd = i
        for k in range(i + 1, s_N):
            if np.abs(m_Au[k, i]) <= s_MaxPiv:
                continue
            s_MaxPiv = np.abs(m_Au[k, i])
            s_MaxPivInd = k
        if s_MaxPivInd != i:
            v_Aux = 1.0 * m_Au[s_MaxPivInd, :]
            m_Au[s_MaxPivInd, :] = 1.0 * m_Au[i, :]
            m_Au[i, :] = 1.0 * v_Aux
        s_IndIni = 0
        v_Aux = (1.0 / m_Au[i, i]) * m_Au[i, :]
        m_Au[i, :] = 1.0 * v_Aux
        for j in range(s_IndIni, s_N):
            if i == j:
                continue
            v_Aux = 1.0 * m_Au[i, :]
            v_Aux = (-1.0 * m_Au[j, i]) * v_Aux
            m_Au[j, :] = m_Au[j, :] + v_Aux
        m_X = 1.0 * m_Au[:, s_N:]
    return m_X
pm_A=np.asmatrix(np.array([[-2,0,1],[-7,1,1],[5,-1,1]]))
pm_B=np.array([-4,-50,-26])
pm_B=pm_B.reshape(-1,1)
print("Solución de la función:")
print(gaussJordan(pm_A,pm_B))
print("Solución de NumPy")
print(np.linalg.solve(pm_A,pm_B))
