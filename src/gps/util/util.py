import subprocess
import datetime
import math


def execute(cmd):
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    for stdout_line in iter(process.stdout.readline, ""):
        yield stdout_line
    process.stdout.close()
    return_code = process.wait()
    if return_code:
        raise subprocess.CalledProcessError(return_code, cmd)


def format_rinex_time(rinex_time):
    date = datetime.datetime.strptime(rinex_time, '%Y-%m-%d %H:%M:%S.%f')
    return date


def xyz2llh(x, y, z):
    """
    Function to convert xyz ECEF to llh
    convert cartesian coordinate into geographic coordinate
    ellipsoid definition: WGS84
      a= 6,378,137m
      f= 1/298.257

    Input
      x: coordinate X meters
      y: coordinate y meters
      z: coordinate z meters
    Output
      lat: latitude degrees
      lon: longitude degrees
      h: height meters
    """
    # --- WGS84 constants
    a = 6378137.0
    f = 1.0 / 298.257223563
    # --- derived constants
    b = a - f * a
    e = math.sqrt(math.pow(a, 2.0) - math.pow(b, 2.0)) / a
    clambda = math.atan2(y, x)
    p = math.sqrt(pow(x, 2.0) + pow(y, 2))
    h_old = 0.0
    # first guess with h=0 meters
    theta = math.atan2(z, p * (1.0 - math.pow(e, 2.0)))
    cs = math.cos(theta)
    sn = math.sin(theta)
    N = math.pow(a, 2.0) / math.sqrt(math.pow(a * cs, 2.0) + math.pow(b * sn, 2.0))
    h = p / cs - N
    while abs(h - h_old) > 1.0e-6:
        h_old = h
        theta = math.atan2(z, p * (1.0 - math.pow(e, 2.0) * N / (N + h)))
        cs = math.cos(theta)
        sn = math.sin(theta)
        N = math.pow(a, 2.0) / math.sqrt(math.pow(a * cs, 2.0) + math.pow(b * sn, 2.0))
        h = p / cs - N
    llh = {'lon': (clambda * 180 / math.pi), 'lat': (theta * 180 / math.pi), 'height': h}
    return llh
