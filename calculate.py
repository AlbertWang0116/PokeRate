import json
import sys
import math

def get_max_current_cp(current_cp,
                       max_cp):
  eps = 1e-6
  if current_cp == 10 and 10.0-max_cp > eps:
    return max_cp
  else:
    current_cp = float(current_cp)
    if current_cp-max_cp > eps:
      return -1.0
    else:
      return min(current_cp+1.0-eps, max_cp)

def get_min_current_cp(current_cp,
                       min_cp):
  eps = 1e-6
  if current_cp == 10 and 10.0-min_cp > eps:
    return min_cp
  else:
    current_cp = float(current_cp)
    if min_cp-1.0-current_cp > -eps:
      return -1.0
    else:
      return max(current_cp, min_cp)

def get_rate(current_cp,
             min_cp,
             max_cp):
  return (current_cp-min_cp)/(max_cp-min_cp)

eps = 1e-6
file_path = sys.argv[1]
stardust = int(sys.argv[2])
current_cp = int(sys.argv[3])
content = open(file_path).read()
levels = json.loads(content)
possible_wild_levels = []
possible_other_levels = []
for level in levels:
  if level['Stardust'] == stardust and get_max_current_cp(current_cp, level['maxcp']) > 0.0 and get_min_current_cp(current_cp, level['mincp']) > 0.0:
    if int(level['level']) == int(level['level']+0.5+eps):
      possible_wild_levels += [level]
    else:
      possible_other_levels += [level]
print "Possible data for wild pokemon:"
for level in possible_wild_levels:
  print "level:{0} min_level_cp:{1} max_level_cp:{2} worst:{3:.6f} best:{4:.6f}".format(level['level'],
                                                                                level['mincp'],
                                                                                level['maxcp'],
                                                                                get_rate(get_min_current_cp(current_cp, level['mincp']), level['mincp'], level['maxcp']),
                                                                                get_rate(get_max_current_cp(current_cp, level['maxcp']), level['mincp'], level['maxcp']))
print "Possible data for non-wild pokemon:"
for level in possible_other_levels:
  print "level:{0} min_level_cp:{1} max_level_cp:{2} worst:{3:.6f} best:{4:.6f}".format(level['level'],
                                                                                level['mincp'],
                                                                                level['maxcp'],
                                                                                get_rate(get_min_current_cp(current_cp, level['mincp']), level['mincp'], level['maxcp']),
                                                                                get_rate(get_max_current_cp(current_cp, level['maxcp']), level['mincp'], level['maxcp']))
