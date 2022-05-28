from math import pi, cos, asin, sin

n2_pi = 1.493
n2_sigma = 1.490

I_0pi = 2550
I_0sigma = 1340

a = 0.29
theta_brewster = 56.8

def R_pi(x):
  theta1 = x / 180 * pi
  theta2 = asin(1 / n2_pi * sin(theta1))

  r_pi = (1 * cos(theta2) - n2_pi * cos(theta1)) / (1 * cos(theta2) + n2_pi * cos(theta1))
  return I_0pi * (r_pi ** 2)

def R_sigma(x):
  theta1 = x / 180 * pi
  theta2 = asin(1 / n2_pi * sin(theta1))

  r_sigma = (1 * cos(theta1) - n2_sigma * cos(theta2)) / (1 * cos(theta1) + n2_sigma * cos(theta2))
  return I_0sigma * (r_sigma ** 2)

def D(func, x):
  return (func(x+0.0000001) - func(x-0.0000001)) / 0.0000002

def parabola(x):
  return a*((x - theta_brewster)**2)

def calc_chisquare(xs, ys, delta_xs, delta_ys, func):
  delta_y1s = [delta_xs * D(func, x) for x, delta_xs in zip(xs, delta_xs)]
  delta_ys_corrected = [dy + dy1 for dy, dy1 in zip(delta_ys, delta_y1s)]
  os = [func(x) for x in xs]
  chi_square = sum([((e - o) / dyc)**2 for e, o, dyc in zip(ys, os, delta_ys_corrected)])
  return chi_square


datasets = ["./data/pi/run3-adjusted.csv", "./data/sigma/run1-adjusted.csv", "./data/pi/run3-parabola.csv"]
funcs = [R_pi, R_sigma, parabola]
constraints = [2, 2, 2]
for dataset, func, constraints in zip(datasets, funcs, constraints):
  xs = []
  ys = []
  delta_xs = []
  delta_ys = []
  with open(dataset) as file:
    for line in file:
      x, y, dx, dy = line.split()
      xs.append(float(x))
      ys.append(float(y))
      delta_xs.append(0) # float(dx)) we don't want to recalculate this.
      delta_ys.append(float(dy))
  print(dataset, calc_chisquare(xs, ys, delta_xs, delta_ys, func) / (len(xs) - constraints))
