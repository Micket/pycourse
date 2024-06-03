# 2.A test:
np.set_printoptions(precision=2, floatmode='fixed', suppress=True, linewidth=1000)
for N_p in [2, 4, 6]:
    A = new_rotated_points(np.array([0.]), N_p=N_p, r=0.5)
    print(f'N_p = {N_p} : A = {A}')

# 2.B test:
print('{0}\n{1}'.format(*make_points(N_p=4, N_iter=2, r=0.5)))

