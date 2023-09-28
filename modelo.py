import matplotlib.pyplot as plt
import numpy as np
import cvxpy as cp
np.random.seed(0)

TOTAL_BUDGET = 100_000

# Alpha and beta constants
alphas = np.array([-3300, -1233, -2633])
betas = np.array([4533, 5833, 3333])

# Linearly spaced numbers
x = np.linspace(1, TOTAL_BUDGET, TOTAL_BUDGET)

# Variables
google   = cp.Variable(pos=True)
facebook = cp.Variable(pos=True)
twitter  = cp.Variable(pos=True)

# Constraint
constraint = [google + facebook + twitter <= TOTAL_BUDGET]

# Objective
obj = cp.Maximize(alphas[0] + betas[0] * cp.log(google)
                + alphas[1] + betas[1] * cp.log(facebook)
                + alphas[2] + betas[2] * cp.log(twitter))

# Solve
prob = cp.Problem(obj, constraint)
prob.solve(solver='ECOS', verbose=False)

# Print solution
print('='*59 + '\n' + ' '*24 + 'Solution' + ' '*24 + '\n' + '='*59)
print(f'Status = {prob.status}')
print(f'Returns = ${round(prob.value):,}\n')
print('Hamburguesería Marketing allocation:')
print(f' - Anuncios de Hamburguesa   = ${round(google.value):,}')
print(f' - Anuncios de Patatas = ${round(facebook.value):,}')
print(f' - Anuncios de Croissants  = ${round(twitter.value):,}')

# Plot the functions and the results
fig = plt.figure(figsize=(10, 5), dpi=300)
plt.plot(x, alphas[0] + betas[0] * np.log(x), color='red', label='Google Ads')
plt.plot(x, alphas[1] + betas[1] * np.log(x), color='blue', label='Facebook Ads')
plt.plot(x, alphas[2] + betas[2] * np.log(x), color='green', label='Twitter Ads')

# Plot optimal points
plt.scatter([google.value, facebook.value, twitter.value],
            [alphas[0] + betas[0] * np.log(google.value),
             alphas[1] + betas[1] * np.log(facebook.value),
             alphas[2] + betas[2] * np.log(twitter.value)],
             marker="+", color='black', zorder=10)

plt.xlabel('Budget ($)')
plt.ylabel('Returns ($)')
plt.legend()
plt.show()