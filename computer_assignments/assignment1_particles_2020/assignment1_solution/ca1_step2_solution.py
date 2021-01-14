""" NB! This file only contains the helper functions from step2 that
are imported and used in step3. """

# -- Solution

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

def plot_statistical_analysis(R, V, time_step, filename):
    """Perform all statistical analysis in ca1 step2 and plot
    result in a single figure. """

    bins = 100
    bins_fine = 400
    N_time_steps_in_pdf = 10

    Nt = R.shape[0]
    N = R.shape[-1]

    t = np.arange(Nt) * time_step

    r_tin = R
    v_tin = V

    x_tn = R[:, 0]
    y_tn = R[:, 1]

    vx_tn = V[:, 0]
    vy_tn = V[:, 1]

    norm_v2_tn = np.sum(v_tin ** 2, axis=1)
    E_t = np.sum(norm_v2_tn, axis=-1)
    Vtot_t = np.linalg.norm(np.sum(v_tin, axis=-1), axis=-1)

    # -- Pair distribution function
    N_steps = 5
    dr = np.linalg.norm(R[-N_steps:-1, :, :, None] - R[-N_steps:-1, :, None, :], axis=1)
    dr += -np.eye(N)[None, :, :]

    subp = [4, 2, 1]
    v_variance = 0.1
    v_range = (-4 * v_variance, 4 * v_variance)
    norm_v_range = (0., 4 * v_variance)
    r_range = (-1., 1.)

    fig = plt.figure(figsize=(6, 6))

    ax = plt.subplot(*subp);
    subp[-1] += 1
    plt.plot(t, Vtot_t)
    plt.xlabel('time')
    plt.ylabel('Average speed')

    ax = plt.subplot(*subp);
    subp[-1] += 1
    plt.plot(t, E_t)
    E_mean = np.mean(E_t)
    plt.ylim([0.99 * E_mean, 1.01 * E_mean])
    plt.xlabel('time')
    plt.ylabel('Kinetic Energy')

    ax = plt.subplot(*subp);
    subp[-1] += 1
    plt.hist(dr.flatten(), range=(0., 3.), bins=200, density=True)
    plt.xlabel('distance')
    plt.ylabel('Pair distribution\nprobability')

    ax = plt.subplot(*subp);
    subp[-1] += 1
    plt.hist(np.sqrt(norm_v2_tn.flatten()), range=norm_v_range, bins=bins, density=True)
    x = np.linspace(norm_v_range[0], norm_v_range[1], num=500)
    plt.plot(x, stats.chi.pdf(x / v_variance, 2) / v_variance, '-', alpha=0.74)
    plt.xlabel('speed')
    plt.ylabel('Velocity norm\nprobability')

    ax = plt.subplot(*subp);
    subp[-1] += 1
    plt.hist(x_tn.flatten(), range=r_range, bins=bins, density=True)
    plt.ylim([0, 1])
    plt.xlabel('x position')
    plt.ylabel('probability')

    ax = plt.subplot(*subp);
    subp[-1] += 1
    plt.hist(y_tn.flatten(), range=r_range, bins=bins, density=True)
    plt.ylim([0, 1])
    plt.xlabel('y position')
    plt.ylabel('probability')

    ax = plt.subplot(*subp);
    subp[-1] += 1
    plt.hist(vx_tn.flatten(), range=v_range, bins=bins, density=True)
    x = np.linspace(v_range[0], v_range[1], num=500)
    plt.plot(x, stats.norm.pdf(x, 0., v_variance), '-', alpha=0.74)
    plt.xlabel('x velocity')
    plt.ylabel('probability')

    ax = plt.subplot(*subp);
    subp[-1] += 1
    plt.hist(vy_tn.flatten(), range=v_range, bins=bins, density=True)
    x = np.linspace(v_range[0], v_range[1], num=500)
    plt.plot(x, stats.norm.pdf(x, 0., v_variance), '-', alpha=0.74)
    plt.xlabel('y velocity')
    plt.ylabel('probability')

    plt.tight_layout()
    plt.savefig(filename)

import os
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate_particles(R, time_step, filename='movie.mp4'):
    """Generates an mp4 movie with the particle trajectories
    using MatPlotLib. """

    if os.path.isfile(filename):
        print('WARNING (animate_particles): The output file', filename, 'exists. Skipping animation.')
        return

    frames = R.shape[0]
    frames_per_second = 1. / time_step

    fig = plt.figure(figsize=(6, 6))
    ax = plt.subplot()

    plt.xlabel('x')
    plt.ylabel('y')
    plt.axis('image')
    plt.xlim([-1.0, 1.0])
    plt.ylim([-1.0, 1.0])

    markers = ax.scatter([], [], s=200, alpha=0.5)
    text = plt.text(-0.9, 0.9, 'frame =', ha='left')

    def update(frame, markers, text):
        print('frame =', frame)
        r = R[frame]
        markers.set_offsets(r.T)
        text.set_text('frame = {}'.format(frame))

    anim = animation.FuncAnimation(
        fig, update,
        frames=frames, interval=50,
        fargs=(markers, text),
        blit=False, repeat=False,
    )

    writer = animation.writers['ffmpeg'](fps=frames_per_second)
    anim.save(filename, writer=writer, dpi=100)
    plt.close()
