class PDController:
    def __init__(self, Kp, Kd):
        self.Kp = Kp  # Proportional gain
        self.Kd = Kd  # Derivative gain
        self.previous_error = 0  # To store the previous time step's error

    def compute(self, reference, current_depth, dt):
        # Calculate the error
        error = reference - current_depth
        
        # Proportional term
        proportional = self.Kp * error
        
        # Derivative term (change in error over time)
        derivative = self.Kd * (error - self.previous_error) / dt
        
        # Control action (PD formula)
        control_action = proportional + derivative
        
        # Store the current error for the next time step
        self.previous_error = error
        
        return control_action
