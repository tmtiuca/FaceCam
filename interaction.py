import lua
lg = lua.globals()

lua.execute("onForegroundWindowChange")
lua.execute("onPeriodic")
lua.execute("onPoseEdge")

average_short = 0
average_long = 0

def vibration_short (moving_average_short):
	if len(moving_average_short) == 0:
		return 0
	average_short = moving_average_short / len(moving_average_short)
	if abs(average_short - 0.4) > 0.05:
		return True
	return False

def vibration_long (moving_average_long):
	if len(moving_average_long) == 0:
		return 0
	average_long = moving_average_long / len(moving_average_long)
	if abs(average_long - 0.9) > 0.05 
		return True
	return False
